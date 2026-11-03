import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import vm from 'node:vm';

const source=readFileSync(new URL('../fold_app/static/app.js',import.meta.url),'utf8');
const sandbox={document:{querySelector:()=>({content:'test',addEventListener:()=>{}}),addEventListener:()=>{}},sessionStorage:{getItem:()=>null},window:{addEventListener:()=>{}},Intl,Date,setTimeout,clearTimeout};
vm.createContext(sandbox);
// Run the production helpers and handlers without starting an HTTP load.
vm.runInContext(source.slice(0,source.lastIndexOf('(async()=>{')),sandbox);
const run=code=>vm.runInContext(code,sandbox);
run(`
const defs={document_number:{},pod:{},amount_due:{},due_date:{}};
function fixture(id,amount,due,payment='unknown',origin='document') {
  const current={document_number:{value:id,origin},pod:{value:'IT001E12345678',origin},amount_due:{value:{amount,currency:'EUR'},origin}};
  if(due)current.due_date={value:due,origin};
  if(payment!=='unknown')current.payment_status={value:payment,origin:'human_declaration'};
  return {id,title:id+'.pdf',created_at:'2026-11-03',current,field_definitions:defs,situation:{reference_date:'2026-11-03'}};
}
subjects=[fixture('BILL-1','84.72','2026-11-03'),fixture('BILL-2','120.00','2026-10-30','paid'),fixture('BILL-3','9.00',null),fixture('BILL-4','20.00','2026-12-03'),fixture('BILL-5','30.00','2026-12-04')];
`);
run(`view={q:'bill-1 84,72',filter:'all',sort:'number'}`);
assert.equal(run('orderedDocuments().length'),1,'combined number/amount search');
run(`view={q:'',filter:'soon',sort:'due'}`);
assert.equal(run('orderedDocuments().map(x=>x.id).join(",")'),'BILL-1,BILL-4','today and day 30 included, day 31 and ambiguity excluded');
run(`view.filter='overdue'`);
assert.equal(run('orderedDocuments()[0].current.payment_status.value'),'paid','elapsed date does not imply unpaid');
run(`view.filter='unpaid'`);
assert.equal(run('orderedDocuments().length'),0,'no invented unpaid declarations');
run(`view.filter='review'`);
assert.equal(run('orderedDocuments().map(x=>x.id).join(",")'),'BILL-3','complete machine readings need no forced confirmation');
run(`view={q:'',filter:'all',sort:'amount'}`);
assert.equal(run('orderedDocuments().map(x=>x.id).join(",")'),'BILL-2,BILL-1,BILL-5,BILL-4,BILL-3');
assert.equal(run(`dataLabel(fixture('verified','0','2026-11-10','unknown','human_confirmation'))`),'Dati verificati da te');
assert.equal(run(`dataLabel(fixture('read','0','2026-11-10'))`),'Dati letti dal PDF');
assert.equal(run(`escape('<img src=x onerror="x">')`),'&lt;img src=x onerror=&quot;x&quot;&gt;');
assert(!source.includes('importDocument();'),'real UI does not insert a demo');
sandbox.history={replaceState:(state,_,url)=>{sandbox.lastUrl=url},pushState:()=>{}};
sandbox.window.scrollTo=()=>{};
run(`render=()=>{}; document.querySelector=()=>({focus:()=>{}}); active=subjects[0]; enterDetail(subjects[1]);`);
assert.equal(sandbox.lastUrl,'#bolletta-BILL-2','upload while a detail is open updates the document address');
console.log('10 gruppi di controlli UI superati: ricerca, date limite, pagamento, ambiguità, ordine, provenienza, escaping, assenza di demo e continuità del dettaglio.');
