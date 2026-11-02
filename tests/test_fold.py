import hashlib
import io
import json
import sqlite3
import tempfile
import threading
import unittest
import urllib.error
import urllib.request
import zipfile
from datetime import date
from pathlib import Path
from unittest.mock import patch

from pypdf import PdfWriter

from fold_app import electricity
from fold_app.core import ConflictError, Store
from fold_app.demo import example_pdf
from fold_app.extraction import extract_pdf
from fold_app.server import FoldServer, present


class DomainTests(unittest.TestCase):
    def test_labels_keep_amount_due_separate_from_other_totals(self):
        text = "Totale bolletta: 200,00 EUR\nTotale da pagare: 84,72 EUR\nScadenza: 20/11/2026"
        result = electricity.interpret([text])
        self.assertEqual([r['value']['amount'] for r in result if r['predicate']=='amount_due'], ['84.72'])
        self.assertTrue(all(r['excerpt'] in text and r['page']==1 for r in result))

    def test_italian_money_and_precision(self):
        self.assertEqual(electricity.normalize('amount_due','1.234,56')['amount'], '1234.56')
        for value in ('1.2.3,45','-2,50','12.3456','nan',''):
            with self.subTest(value=value), self.assertRaises(ValueError):
                electricity.normalize('amount_due',value)

    def test_invalid_date_is_not_invented(self):
        self.assertEqual(electricity.interpret(['Scadenza: 31/02/2026']), [])

    def test_payment_not_inferred_from_elapsed_time_or_payment_method(self):
        fields = {'due_date':{'value':'2026-10-30'}}
        state = electricity.situation(fields,'unknown',date(2026,11,2))
        self.assertEqual(state['key'],'overdue')
        self.assertIn('non verificato',state['label'])
        self.assertNotEqual(state['key'],'unpaid')
        self.assertFalse(any(x['predicate']=='payment_status' for x in electricity.interpret(['Modalita di pagamento: bonifico'])))

    def test_declared_payment_and_reference_time(self):
        fields = {'due_date':{'value':'2026-11-03'}}
        self.assertEqual(electricity.situation(fields,'unknown',date(2026,11,2))['key'],'upcoming')
        self.assertEqual(electricity.situation(fields,'paid',date(2026,11,4))['key'],'paid')
        self.assertEqual(electricity.situation({},'unknown',date(2026,11,2))['key'],'unknown')


class PDFTests(unittest.TestCase):
    def test_example_uses_real_extractor(self):
        pages = extract_pdf(example_pdf())
        self.assertEqual(len(pages),1)
        self.assertEqual(len(electricity.interpret(pages)),4)

    def test_scanned_or_blank_document_keeps_empty_reading(self):
        writer = PdfWriter(); writer.add_blank_page(width=100,height=100)
        stream = io.BytesIO(); writer.write(stream)
        self.assertEqual(extract_pdf(stream.getvalue()), [''])

    def test_invalid_and_encrypted_pdf(self):
        for data in (b'not a pdf',b'%PDF-1.4\nnot valid'):
            with self.subTest(data=data), self.assertRaises(ValueError): extract_pdf(data)
        writer = PdfWriter(); writer.add_blank_page(width=100,height=100); writer.encrypt('secret')
        stream = io.BytesIO(); writer.write(stream)
        with self.assertRaisesRegex(ValueError,'cifrato'): extract_pdf(stream.getvalue())


class StoreTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='fold-test-')
        self.store = Store(self.tmp.name)
        self.content = example_pdf()
        self.pages = ['Bolletta n. DEMO-001\nPOD: IT001E12345678\nTotale da pagare: 84,72 EUR\nScadenza: 30/10/2026']
        self.subject, _ = self.store.import_document(self.content,'esempio.pdf',self.pages,electricity.interpret(self.pages),'electricity_bill')

    def tearDown(self): self.tmp.cleanup()

    def test_duplicate_preserves_original_and_receives_again(self):
        same, duplicate = self.store.import_document(self.content,'altro-nome.pdf',[],[],'electricity_bill')
        data = self.store.subject(self.subject)
        self.assertTrue(duplicate); self.assertEqual(same,self.subject)
        self.assertEqual(len(self.store.list_subjects()),1)
        self.assertEqual(len(data['assertions']),4)
        self.assertEqual(data['sources'][0]['receptions'],2)
        self.assertEqual(self.store.source(data['sources'][0]['id'])[1],self.content)

    def test_correction_keeps_original_and_human_basis_distinct(self):
        before = self.store.subject(self.subject)['current']['amount_due']
        self.store.revise(self.subject,'amount_due',{'amount':'34.72','currency':'EUR'},0,
                          {'value_entered':'34,72','note':'Ho corretto la lettura confrontando il PDF.'})
        after = self.store.subject(self.subject)
        self.assertEqual(len(after['assertions']),5)
        new = after['current']['amount_due']
        self.assertEqual(new['supersedes_id'],before['id'])
        self.assertIsNone(new['observation_id'])
        self.assertEqual(new['received']['value_entered'],'34,72')
        self.assertEqual(next(a for a in after['assertions'] if a['id']==before['id'])['value']['amount'],'84.72')

    def test_conflicting_dates_are_not_arbitrarily_selected(self):
        pages = ['Scadenza: 01/11/2026\nScadenza: 20/11/2026']
        subject, _ = self.store.import_document(self.content+b'\n%second', 'ambigua.pdf',pages,electricity.interpret(pages),'electricity_bill')
        data = self.store.subject(subject)
        self.assertNotIn('due_date',data['current'])
        self.assertEqual(len(data['assertions']),2)
        self.assertEqual(present(self.store,subject)['situation']['key'],'unknown')

    def test_same_value_twice_is_not_two_votes(self):
        pages = ['Scadenza: 20/11/2026\nScadenza: 20/11/2026']
        subject, _ = self.store.import_document(self.content+b'\n%repeat','ripetuta.pdf',pages,electricity.interpret(pages),'electricity_bill')
        self.assertEqual(self.store.subject(subject)['current']['due_date']['value'],'2026-11-20')

    def test_stale_window_cannot_change_new_revision(self):
        self.store.revise(self.subject,'payment_status','paid',0,{'note':'Pagata il 2 novembre.'},'human_declaration')
        with self.assertRaises(ConflictError):
            self.store.revise(self.subject,'payment_status','unpaid',0,{'note':'Risposta alla vecchia scheda.'},'human_declaration')
        self.assertEqual(self.store.subject(self.subject)['current']['payment_status']['value'],'paid')
        self.assertEqual(len(self.store.subject(self.subject)['assertions']),5)

    def test_reopen_and_backup_restore_include_links_and_original(self):
        self.store.revise(self.subject,'payment_status','paid',0,{'note':'Dichiarazione di esempio.'},'human_declaration')
        self.assertEqual(Store(self.tmp.name).subject(self.subject)['revision'],1)
        archive = zipfile.ZipFile(io.BytesIO(self.store.backup()))
        with tempfile.TemporaryDirectory(prefix='fold-restore-') as folder:
            (Path(folder)/'fold.sqlite3').write_bytes(archive.read('fold.sqlite3'))
            restored = Store(folder)
            data = restored.subject(self.subject)
            self.assertEqual(data['current']['payment_status']['value'],'paid')
            self.assertEqual(restored.source(data['sources'][0]['id'])[1],self.content)
            with restored.connection() as db:
                self.assertEqual(db.execute('PRAGMA integrity_check').fetchone()[0],'ok')
                self.assertEqual(db.execute('PRAGMA foreign_key_check').fetchall(),[])
        self.assertIn('manifest.json',archive.namelist())
        self.assertIn('originals/'+hashlib.sha256(self.content).hexdigest()+'.pdf',archive.namelist())

    def test_failed_revision_is_atomic(self):
        with self.assertRaises(ValueError):
            self.store.revise(self.subject,'due_date','2026-11-20',0,{'note':'Errore'},selected_id='f'*32)
        self.assertEqual(self.store.subject(self.subject)['revision'],0)


class HTTPTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='fold-http-')
        self.server = FoldServer(('127.0.0.1',0),Store(self.tmp.name))
        self.thread = threading.Thread(target=self.server.serve_forever,daemon=True); self.thread.start()
        self.base = f'http://127.0.0.1:{self.server.server_port}'

    def tearDown(self):
        self.server.shutdown(); self.server.server_close(); self.thread.join(); self.tmp.cleanup()

    def request(self,path,body=None,headers=None):
        request = urllib.request.Request(self.base+path,data=body,headers=headers or {})
        try:
            with urllib.request.urlopen(request,timeout=30) as response:
                return response.status,response.read(),response.headers
        except urllib.error.HTTPError as exc: return exc.code,exc.read(),exc.headers

    def headers(self):
        return {'Origin':self.base,'X-Fold-Token':self.server.token,'Content-Type':'application/json'}

    def test_complete_http_flow_and_original_download(self):
        status, html, _ = self.request('/')
        self.assertEqual(status,200); self.assertIn(self.server.token.encode(),html)
        status, body, _ = self.request('/api/demo',b'',self.headers())
        self.assertEqual(status,201)
        data = json.loads(body)['subject']
        payload = {'predicate':'payment_status','value':'paid','revision':data['revision'],'note':'Ho verificato il pagamento.'}
        status, body, _ = self.request('/api/subjects/'+data['id']+'/revise',json.dumps(payload).encode(),self.headers())
        self.assertEqual(status,200); self.assertEqual(json.loads(body)['situation']['key'],'paid')
        status, _, _ = self.request('/api/subjects/'+data['id']+'/revise',json.dumps(payload).encode(),self.headers())
        self.assertEqual(status,409)
        status, original, _ = self.request('/api/sources/'+data['sources'][0]['id'])
        self.assertEqual(status,200); self.assertEqual(hashlib.sha256(original).hexdigest(),data['sources'][0]['sha256'])
        status, backup, _ = self.request('/api/backup'); self.assertEqual(status,200)
        self.assertTrue(zipfile.is_zipfile(io.BytesIO(backup)))

    def test_cross_origin_or_missing_token_writes_are_rejected(self):
        for headers in ({}, {'Origin':'http://evil.example','X-Fold-Token':self.server.token}, {'Origin':self.base,'X-Fold-Token':'wrong'}):
            with self.subTest(headers=headers): self.assertEqual(self.request('/api/demo',b'',headers)[0],403)
        self.assertEqual(self.server.store.list_subjects(),[])

    def test_rebinding_host_rejected_and_paths_not_served(self):
        self.assertEqual(self.request('/',headers={'Host':'evil.example'})[0],403)
        self.assertEqual(self.request('/../core.py')[0],404)

    def test_invalid_upload_does_not_create_partial_case(self):
        self.assertEqual(self.request('/api/import',b'not pdf',self.headers())[0],422)
        self.assertEqual(self.server.store.list_subjects(),[])


if __name__ == '__main__': unittest.main()
