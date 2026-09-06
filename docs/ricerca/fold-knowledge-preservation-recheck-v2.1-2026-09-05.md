# Fold — Knowledge Preservation re-check mirato della candidata v2.1

Questo re-check autorizza esclusivamente il passaggio da Knowledge Preservation a FOL-40 / Model Preservation se tutti i controlli passano. Non autorizza il freeze della v2.1, l’implementazione, la chiusura di FOL-36 o la risoluzione delle questioni aperte.

**Data:** 2026-09-05  
**Issue di riferimento:** FOL-36  
**Stato del documento:** Research — rapporto di verifica  
**Candidata verificata:** `fold-anatomia-v2.1-candidate-2026-09-04.md`  
**Gate precedente:** `fold-knowledge-preservation-gate-v2.1-2026-09-04.md`  

## 1. Perimetro e metodo

Il controllo è limitato alla patch di Knowledge Preservation applicata dopo il primo Gate non superato. Per ciascuno dei 24 finding verifica separatamente che la conoscenza richiesta:

- sia presente nella candidata;
- sia completa rispetto al Knowledge / Decision Ledger;
- non sia stata rafforzata oltre il suo stato genealogico;
- non sia stata indebolita;
- non risolva una questione che deve restare aperta;
- non introduca una nuova teoria, primitiva o responsabilità.

Le autorità usate sono, in quest’ordine: Knowledge / Decision Ledger, delta v2→v2.1 e Coverage Ledger v2. Lo snapshot v2 localizza la base precedente; il Gate non superato identifica i finding da ricontrollare. Il Patch Record della candidata è una traccia dell’intervento, non un’autorità genealogica.

La classificazione impiegata è:

- **PASS** — tutti i controlli richiesti sono soddisfatti;
- **FAIL** — almeno un requisito è assente o contraddetto;
- **AMBIGUO** — il testo non consente una conclusione determinata senza nuova interpretazione.

Il re-check non valuta ancora la conservazione complessiva del modello, che appartiene a FOL-40 / Model Preservation.

## 2. Stato Git iniziale

Branch e relazione remota iniziali: `main...origin/main`.  
HEAD iniziale: `ef3b24f450e21173c07563aee02c96ef39babcf7`.

Modifiche presenti prima della creazione di questo rapporto:

```text
?? docs/ricerca/fold-anatomia-v2.1-candidate-2026-09-04.md
?? docs/ricerca/fold-knowledge-preservation-gate-v2.1-2026-09-04.md
```

Non risultavano modifiche tracciate. L’hash SHA-256 iniziale della candidata era `98ef21e3128b217afaa863c616fc3c12eb579507103b495ffcc9c7f90e8de754`.

## 3. Re-check dei finding B01–B09

| Finding | K-ID | Evidenza e verifica mirata | Protezioni genealogiche e progettuali | Esito |
|---|---|---|---|---|
| **B01** | K-043 | In F, G e H5 i risultati utili dei singoli tentativi restano recuperabili; un retry non seleziona o sostituisce in blocco tutto ciò che lo precede e ogni tentativo mantiene Provenance e limiti propri. | Conservata la distinzione tra retry e nuova valutazione; non introdotti `Result`/`Attempt` Core, merge automatico o selettore globale. | **PASS** |
| **B02** | K-068 | H10 e la sezione I sul tempo mantengono l’ignoto come ignoto, non trasformano un dato impreciso in preciso, non riempiono ruoli temporali incompatibili e richiedono condizioni dichiarate per la comparabilità. | Nessuna `Validity` universale, nessun timestamp obbligatorio e nessuna data inferita automaticamente. | **PASS** |
| **B03** | K-078 | H10 e I distinguono tempo/cadenza di produzione o emissione, periodo o fenomeno descritto e tempo/cadenza di disponibilità a Fold. Distinguono inoltre pattern osservato, previsione, dichiarazione, obbligo e raccomandazione. | La formulazione è generale e non contiene esempi domestici hardcoded; C02 resta esplicitamente aperta e non compare una `Expectation` universale. | **PASS** |
| **B04** | K-117 | La sezione E sulla correzione e H9 fondano una rettifica sulla relazione pertinente fra bersaglio, supporto e contesto. Numero, recenza o autorevolezza globale delle fonti non bastano. | Nessun ranking generico, voto di maggioranza o `truth score`; la forza resta relativa alla proposizione e al caso. | **PASS** |
| **B05** | K-132 | La sezione I e la grammatica J rendono distinguibili relazioni Referent→Referent, Referent→Value e qualificazioni epistemiche su contenuti o supporti. | La distinzione non viene tradotta in una `Relation` tecnica universale né in una nuova primitiva Core. | **PASS** |
| **B06** | K-150 | G e H11 rendono recuperabili base d’inclusione, membri considerati, periodo/scope e metodo delle aggregazioni derivate. | L’aggregazione resta Derivation e H18 resta Projection; nessun oggetto `Aggregate` universale è stato introdotto. | **PASS** |
| **B07** | K-151 | H7, H9 e H16 vietano l’ammissione congiunta, nello stesso scope, di alternative mutuamente esclusive; eliminare un’alternativa non fornisce nuovo supporto positivo a quella rimasta. | Nessun `Candidate` universale, solver, stato o controller centrale; restano possibili restringimento, sospensione e verifica motivati. | **PASS** |
| **B08** | K-169 | H5 e I distinguono lettura nativa, OCR e rappresentazione visuale; metodo, Provenance, Quality e divergenze restano recuperabili e il grezzo non è sostituito silenziosamente. | Non è scelto alcun algoritmo visuale e nessuna lettura è promossa automaticamente a verità. | **PASS** |
| **B09** | K-171 | H6, H7 e I vietano di trasferire automaticamente alle parti il tipo attribuito al contenitore; la classificazione delle parti richiede basi proprie. | K-142 e i criteri documentali specifici restano aperti; nessuna tassonomia o regola tecnica è stata imposta. | **PASS** |

## 4. Re-check dei finding m01–m15

| Finding | K-ID | Evidenza e verifica mirata | Protezioni genealogiche e progettuali | Esito |
|---|---|---|---|---|
| **m01** | K-002 | C, F, H5 e H7 distinguono ciò che il produttore rende disponibile con i suoi limiti, ciò che il consumatore richiede e considera sufficiente e ciò che il Work decide di proseguire. | Non compare un orchestratore centrale né un contratto universale di pipeline. | **PASS** |
| **m02** | K-006 | C distingue produrre un risultato, renderlo osservabile come accadimento/segnale, reagire a esso ed esserne vincolati come dipendenza. | K-006 e il vocabolario restano CANDIDATI; l’eventuale `EMITS` non è canonizzata né resa relazione obbligatoria. | **PASS** |
| **m03** | K-013 | F distingue retry con presupposti equivalenti da nuova valutazione dovuta a un cambiamento materiale; il nuovo esito non riscrive la storia del precedente. | Nessuna nuova primitiva `Attempt`; restano Provenance, Lineage e storicità a sostenere la distinzione. | **PASS** |
| **m04** | K-031 | I ammette porzioni sovrapposte, incomplete o incerte senza richiedere una segmentazione preventiva totale. | Raggruppamento e locator non provano ordine, completezza o identità documentale. | **PASS** |
| **m05** | K-042 | C, F, H5 e H7 separano limiti dichiarati dal produttore, sufficienza valutata dal consumatore e scelta operativa del Work di continuare, attendere o fermarsi. | Non è introdotto un `Result Validator` universale. | **PASS** |
| **m06** | K-063 | F qualifica un output vuoto come successo con zero risultati, incompletezza oppure non processabilità e conserva copertura e tentativo. | L’assenza di output non viene trasformata in assenza nel mondo. | **PASS** |
| **m07** | K-074 | H12 e I distinguono ciò che Fold poteva sostenere al tempo storico dalla ricostruzione odierna di quel passato, conservando reference context e basi. | Nessuna retrodatazione di conoscenza acquisita successivamente. | **PASS** |
| **m08** | K-095 | E separa correttezza procedurale della Decision da correttezza fattuale del contenuto impiegato. | Nessuna delle due viene usata come prova automatica dell’altra. | **PASS** |
| **m09** | K-100 | I separa origine, integrità/fedeltà, competenza o autorità relativa alla proposizione, indipendenza e corroborazione. | Nessuna affidabilità intrinseca della fonte, score globale o algoritmo di ranking. | **PASS** |
| **m10** | K-107 | G richiede la granularità minima necessaria a distinguere effetti differenti sui contenuti. | Non deriva una segmentazione tecnica universale o preventiva. | **PASS** |
| **m11** | K-181 | G distingue audit delle decisioni, osservabilità operativa, Provenance/Lineage e storia epistemica. | Nessuno stack di monitoring o logging è assunto come modello concettuale. | **PASS** |
| **m12** | K-073 | La sezione I esplicita due assi non equivalenti: stato genealogico nel Ledger e forza/forma locale nell’anatomia. La responsabilità della Reconstruction resta STABILE; soltanto la forma concreta del risultato resta CANDIDATA. | Nessun indebolimento genealogico della Reconstruction e nessuna promozione della forma locale. | **PASS** |
| **m13** | K-143 | I conserva come forte la necessità referenziale e come CANDIDATA la specifica definizione K-143 del Referent. | La necessità non viene indebolita; la definizione candidata non viene promossa a stabile. | **PASS** |
| **m14** | K-049, K-050, K-148 | I conserva STABILI le definizioni di Source e Observation e CANDIDATA la loro collocazione concreta descritta da K-148. | Né le definizioni vengono indebolite né la collocazione viene promossa. | **PASS** |
| **m15** | K-006, K-090, K-096 | O rende esplicito F2d: il cambiamento di versione può diventare osservabile, ma la sua origine non è ancora assegnata. I diversi stati genealogici restano visibili. | Nessun C08, produttore universale, manager, event bus, polling o scheduler; F2d resta aperto. | **PASS** |

## 5. Controlli speciali

### 5.1 B03 — generalità della distinzione temporale

| Controllo | Risultato |
|---|---|
| Produzione/emissione distinta dal fenomeno descritto | **PASS** |
| Fenomeno descritto distinto dalla disponibilità a Fold | **PASS** |
| Pattern osservato distinto da previsione | **PASS** |
| Previsione distinta da dichiarazione, obbligo e raccomandazione | **PASS** |
| Nessun concetto domestico hardcoded o nuova primitiva temporale | **PASS** |
| C02 ancora esplicitamente aperta | **PASS** |

La correzione ripristina K-078 in forma generale. Non decide come produrre o confrontare una particolare attesa e non risolve il rapporto fra base predittiva e successivo riscontro negativo.

### 5.2 m02 — direzioni non equivalenti

| Controllo | Risultato |
|---|---|
| Risultato distinto da segnalazione osservabile | **PASS** |
| Segnalazione distinta dalla reazione di un’altra responsabilità | **PASS** |
| Reazione distinta dal vincolo di dipendenza | **PASS** |
| K-006 e il vocabolario conservati come CANDIDATI | **PASS** |
| `EMITS` non canonizzata | **PASS** |

### 5.3 m12–m14 — stato genealogico e forza locale

La candidata dichiara esplicitamente che i due assi non sono equivalenti. Il controllo puntuale conferma:

- K-073: responsabilità della Reconstruction STABILE; forma concreta CANDIDATA — **PASS**;
- K-143: necessità referenziale forte; definizione del Referent CANDIDATA — **PASS**;
- K-049/K-050: definizioni di Source e Observation STABILI; K-148, relativa alla collocazione, CANDIDATA — **PASS**.

Non risultano promozioni o degradazioni ottenute per trasposizione impropria fra i due assi.

### 5.4 F2d — origine del cambiamento di versione

F2d è ora visibile come questione aperta: la candidata non inventa un produttore dell’accadimento, non crea C08 e non seleziona manager, event bus, polling, scheduler o fase backend. La formulazione ripristina il problema senza risolverlo — **PASS**.

## 6. Anti-regressione mirata

| Controllo | Evidenza sintetica | Esito |
|---|---|---|
| Δ01–Δ09 intatti | Le nove destinazioni del delta restano presenti senza nuove primitive o universalizzazioni. | **PASS** |
| C01–C07 ancora aperti | Tutti e sette gli aperti sono mantenuti come tali; nessuno è convertito in decisione. | **PASS** |
| F2d ancora aperto | È esplicitato in O come assegnazione mancante, senza soluzione adottata. | **PASS** |
| R01–R10 ancora respinti | Le dieci tesi respinte restano escluse; nessuna è reintrodotta dalla patch. | **PASS** |
| D06 ancora aperto | L’ownership Decision/Disposition non-Policy non viene risolta. | **PASS** |
| K-080 ancora CANDIDATA | La forma della temporal attention non è promossa a universale. | **PASS** |
| K-023 ancora CANDIDATA | Il test di parallelizzabilità non viene trasformato in regola dell’anatomia. | **PASS** |
| Inventario H invariato | Sono presenti esattamente 22 responsabilità H; non esiste H23. | **PASS** |
| Nessuna nuova primitiva o responsabilità | Le correzioni operano su contratti, distinzioni e guardrail esistenti. | **PASS** |
| Nessuna scelta software | Non sono decisi servizi, classi, database, API, code, scheduler, event bus, polling o algoritmi. | **PASS** |
| Nessuna operazionalizzazione del Ledger | Il Ledger resta autorità genealogica e non diventa runtime, registry o policy engine. | **PASS** |

## 7. Verifica del Knowledge Preservation Patch Record

Il Patch Record contiene esattamente **24 righe di finding**:

- **9** righe B, da B01 a B09;
- **15** righe m, da m01 a m15;
- **24 identificativi univoci**, senza omissioni o duplicazioni.

Le localizzazioni dichiarate sono coerenti con il corpo della candidata e ogni riga rende visibili sia l’intervento sia il guardrail preservato. Il Record non viene usato per auto-convalidare la patch: i suoi riferimenti sono stati confrontati con il testo della candidata e con le fonti genealogiche — **PASS**.

## 8. FAIL e AMBIGUI

Non sono stati rilevati finding in stato **FAIL** o **AMBIGUO**.

| Stato | Conteggio |
|---|---:|
| PASS | 24 |
| FAIL | 0 |
| AMBIGUO | 0 |

I controlli speciali, l’anti-regressione mirata e il Patch Record risultano a loro volta superati. Non emergono problemi residui appartenenti al perimetro di questo re-check. Restano aperte, senza essere risolte qui, le questioni che il delta e la candidata demandano al test domestico o a una decisione successiva.

## 9. Verdetto finale

# KNOWLEDGE PRESERVATION RE-CHECK SUPERATO

Tutti i 24 finding hanno esito PASS; non vi sono FAIL o AMBIGUI. È quindi autorizzato esclusivamente il passaggio da Knowledge Preservation a **FOL-40 / Model Preservation**.

Questo verdetto non dichiara la candidata v2.1 approvata, finale o congelata; non autorizza l’implementazione; non chiude FOL-36; non risolve C01–C07, F2d o D06; non sostituisce il successivo controllo di Model Preservation.

## 10. Stato Git finale

Alla chiusura del re-check il branch resta `main`, HEAD resta `ef3b24f450e21173c07563aee02c96ef39babcf7` e non risultano modifiche tracciate. Sono presenti soltanto i due artefatti già non versionati e questo nuovo rapporto:

```text
?? docs/ricerca/fold-anatomia-v2.1-candidate-2026-09-04.md
?? docs/ricerca/fold-knowledge-preservation-gate-v2.1-2026-09-04.md
?? docs/ricerca/fold-knowledge-preservation-recheck-v2.1-2026-09-05.md
```

L’hash SHA-256 finale della candidata è `98ef21e3128b217afaa863c616fc3c12eb579507103b495ffcc9c7f90e8de754`, identico a quello iniziale del re-check: la candidata non è stata modificata.
