# Fold — Model Preservation Source Readiness Check

**Status:** Research  
**Data:** 2026-09-05  
**Issue:** FOL-40, nel percorso di FOL-36  
**Oggetto:** disponibilità e sufficienza delle fonti per le genealogie componenti/responsabilità e Core/primitive.

## 1. Scopo

Verificare se le due genealogie possano essere costruite a partire da documenti e ragionamenti effettivamente recuperabili. Questo rapporto identifica le fonti, controlla la presenza delle catene documentali e segnala i limiti della conservazione attuale. Non contiene le due genealogie definitive.

Il Knowledge Preservation re-check SUPERATO è assunto come antecedente dichiarato dall’utente e documentato nel relativo rapporto. Non è stato rieseguito e non sono state rivalutate le singole K-ID. La candidata v2.1 resta Draft.

Nel rapporto si distinguono:

- **documentazione del repository:** conserva stati, conclusioni distillate, copertura e formulazioni successive;
- **conversazione originale recuperata:** conserva i testi nei quali sono state formulate ipotesi, stress, correzioni e disposizioni;
- **valutazione di questo controllo:** riguarda la sufficienza delle fonti identificate, non introduce conclusioni teoriche sul modello.

Il Ledger resta autorità genealogica sulle conoscenze già consolidate nel percorso. Questo ruolo non lo rende una fonte primaria del ragionamento originario: la natura della fonte e l’autorità progettuale sono due dimensioni differenti. Una divergenza sostanziale fra fonti andrebbe segnalata, non risolta per recenza o preferenza di formulazione.

## 2. Cosa autorizza e cosa non autorizza

L’esito di questo controllo autorizza la costruzione delle due genealogie soltanto nella misura in cui sono disponibili le fonti necessarie. Non equivale al Model Preservation Gate e non valuta già la fedeltà completa della futura ricostruzione.

Non autorizza freeze della v2.1, implementazione, chiusura di FOL-36, nuove primitive, nuove responsabilità o risoluzione di questioni aperte. In questa attività è creato soltanto il presente documento.

## 3. Stato iniziale e fonti disponibili

### 3.1 Stato Git e contesto operativo

Lo stato iniziale coincideva esattamente con quello atteso:

```text
?? docs/ricerca/fold-anatomia-v2.1-candidate-2026-09-04.md
?? docs/ricerca/fold-knowledge-preservation-gate-v2.1-2026-09-04.md
?? docs/ricerca/fold-knowledge-preservation-recheck-v2.1-2026-09-05.md
```

Branch: `main`. HEAD: `ef3b24f450e21173c07563aee02c96ef39babcf7`. Nessun’altra modifica materialmente rilevante.

Consultati `README.md`, `docs/README.md`, `docs/metodo-di-lavoro.md`, il working model Core/Domain e la decisione 0001 sul perimetro di validazione fondazionale. Questi documenti definiscono contesto e disciplina; non sostituiscono gli esiti dei Round.

Consultata in sola lettura [FOL-40](https://linear.app/folderapp/issue/FOL-40/preservare-e-verificare-levoluzione-strutturale-del-modello-di-fold): stato `In Progress`, parent FOL-36, relazione con FOL-37. Descrizione e risultati attesi concordano con il mandato corrente. La lettura dei commenti non ha restituito checkpoint aggiuntivi. La descrizione dell’issue è fonte del contratto operativo, non prova dei conteggi o delle conclusioni storiche.

### 3.2 Archivio primario effettivamente recuperato

Il registro del Ledger indica la sessione `01a05d0a-e483-7793-a648-e46306e04177`. Il relativo archivio locale esiste ed è stato letto direttamente:

```text
C:\Users\giuseppe\.codex\sessions\2026\09\01\rollout-2026-09-01T14-56-30-01a05d0a-e483-7793-a648-e46306e04177.jsonl
```

I testi elencati sotto sono messaggi `response_item`, con `payload.type = message`, `role = assistant` e `phase = final_answer`. Gli **ordinal sono identificativi nel JSONL, non numeri di riga**. Il corpo è il testo degli elementi `payload.content`, nella sequenza originale. Gli hash SHA-256 sono calcolati sul corpo UTF-8, senza wrapper JSON e senza normalizzazione editoriale.

I dieci hash R1–REG già registrati nel Ledger coincidono con quelli ricalcolati dai messaggi originali. Per V1 e i due assemblaggi sono state calcolate anche le impronte qui riportate. L’hash di ASM2 coincide con quello del corpo originale dichiarato nello snapshot v2.

| Sigla | Messaggio e data UTC | Ordinal | SHA-256 del corpo |
|---|---|---:|---|
| V1 | Anatomia concettuale completa; 2026-09-01 14:54:04.659 | 210 | `58cf78872ea5e96890a65ecb4fc131561d5698e2bc1d32448421fc9f267902e1` |
| R1 | Round 1; 2026-09-03 15:43:17.415 | 287 | `5fb8ce0254c4f05eab269401dfa6a6047a0b8573423e3962d0ee73b068031921` |
| R2 | Round 2; 2026-09-03 16:18:55.599 | 346 | `ecec0a90a41adea38c0cf2279e82d3531924d7e0fc39f5660e0ce01cde57098e` |
| R2C | Chiarimento/delta strutturale Round 2; 2026-09-03 16:48:33.734 | 428 | `1da70e3482e80224ce5680b2b6aec5805ec5fa887c64729dd34519d470874ca6` |
| R3 | Round 3; 2026-09-03 17:17:26.933 | 491 | `79ad61ee3422d868164cf361977cc634fd204504abf219a5dc1419a0fba6dec7` |
| R4 | Round 4; 2026-09-03 17:53:00.474 | 561 | `e8fba153785d436c414839f6a4eb162ecaf3755e0695564a0bbbfdb4ac68783e` |
| R5 | Round 5; 2026-09-03 18:09:20.674 | 618 | `68c1bc51f8627545407b2a5dfafc3c38f4b0b0ce2c8fa937e7a271c42cbdd2a3` |
| R6 | Self-audit e Readiness Gate; 2026-09-03 18:26:24.962 | 661 | `1246773134d196608c00c55053dd108b11dd92cafb9d5d94f3bb05746a53e088` |
| GATE | Controllo finale dei tre problemi; 2026-09-03 18:33:11.566 | 692 | `1892741375aab1c342751afd852507423604754ae49c975962246df3e81babf2` |
| AUDIT | Audit dei 34 e Coverage Gate; 2026-09-03 18:56:39.427 | 822 | `504d4177ea8997f8c4b1b4cd1bc5e941cf3c0bd305356f7d918b12e2fb726be4` |
| ASM1 | Primo assemblaggio candidata v2; 2026-09-03 20:46:13.519 | 888 | `af3e3c24939537a1a4b9fb68b69edd3576e68ac7fd086478e10c5ce086102d99` |
| REG | Regression & Change-Justification Audit; 2026-09-03 21:09:51.828 | 1070 | `f756ac83259a7d1b99aba157d93a0aa3a0d3766d84eb2a066fa33f9ead3600d1` |
| ASM2 | Candidata v2 integrata; 2026-09-03 21:24:49.034 | 1105 | `fad314962da4e44968824c213d44fcd0ac4eef8c02856cfd386d5f2d8dbc2567` |

### 3.3 Classificazione per natura e uso consentito

| Fonte | Classificazione | Che cosa dimostra e limite d’uso |
|---|---|---|
| V1 | **1 — FONTE PRIMARIA DEL RAGIONAMENTO** | Formulazione originale dell’anatomia: problemi, operazioni e confini dei componenti; elenco delle forme Core allora candidate. Prova il punto di partenza, non il suo successivo mantenimento. |
| R1, R2, R2C, R3, R4, R5 | **1 — FONTE PRIMARIA DEL RAGIONAMENTO** | Diagnosi, alternative, casi di stress, conclusioni e aperture prodotte nei singoli passaggi. R2C è indispensabile per distinguere il Round 2 iniziale dalla sua correzione. |
| R6 e GATE | **1 — FONTE PRIMARIA DEL RAGIONAMENTO** | Self-audit, contraddizioni cross-round e soluzioni minime adottate in quei controlli. I riepiloghi delle fasi precedenti vanno confrontati con i rispettivi Round. |
| AUDIT | **1 — FONTE PRIMARIA DEL RAGIONAMENTO dell’audit** | Matrice dei 34, 34 schede, audit 25a–25i, contabilità e inventario dei 24 prodotti in quella fase. È retrospettivo rispetto ai Round: non è la fonte primaria dei ragionamenti che attribuisce ai Round. |
| ASM1 e ASM2 | **2 — PRESERVAZIONE SUCCESSIVA** del percorso Round | Conservano assemblaggio ed esito. Sono testimonianza diretta delle scelte di assemblaggio effettuate in quel momento, ma non provano retroattivamente lo stress originario. |
| REG | **1 — FONTE PRIMARIA DEL RAGIONAMENTO del Regression Audit** | Confronto fra assemblaggio e materiale precedente; motivazione D07 per la ricezione tracciata, residuo D06 e dieci trasformazioni L01–L10. Le genealogie che riepiloga richiedono comunque riscontro nei Round. |
| `fold-knowledge-decision-ledger-2026-09-04.md` | **2 — PRESERVAZIONE SUCCESSIVA** | Autorità genealogica su conclusioni e stati distillati; registro verificabile dei messaggi originali. Non è il verbale integrale dei Round. |
| `fold-coverage-ledger-v2-2026-09-04.md` | **2 — PRESERVAZIONE SUCCESSIVA** | Confronto Ledger/v2 e reverse coverage; non coincide con AUDIT e non contiene al suo posto le 34 schede originarie. |
| `fold-anatomia-v2-snapshot-2026-09-04.md` | **2 — PRESERVAZIONE SUCCESSIVA** | Corpo integrale di ASM2, utile per il punto d’arrivo v2 e la sezione K. Non sostituisce V1, R2C o AUDIT. |
| `fold-delta-v2-v2.1-2026-09-04.md` | **2 — PRESERVAZIONE SUCCESSIVA** | Mandato controllato dei ripristini, aperture e tesi respinte; non prova come siano state ottenute le conclusioni nei Round. |
| `fold-anatomia-v2.1-candidate-2026-09-04.md` | **2 — PRESERVAZIONE SUCCESSIVA** | Destinazioni attuali, sezioni H/I/J/K e aperture. Si usa alla fine della catena, non per ricostruire l’inizio. |
| Gate Knowledge Preservation e re-check del 2026-09-05 | **2 — PRESERVAZIONE SUCCESSIVA** | Evidenza dei controlli già svolti sulla conservazione delle conoscenze. Non sono Model Preservation e non sono rieseguiti. |
| `fold-fol34-coverage-ledger-2026-09-04.md` | **2 — PRESERVAZIONE SUCCESSIVA** | Copertura successiva della ricerca FOL-34; non sostituisce né inventario né stress dei Round. |
| `docs/architecture/core-domain-working-model.md` | **3 — CONTESTO SECONDARIO** per le due genealogie correnti | Working model del 2026-08-30: ipotesi iniziali più ampie e domande aperte. È documento della propria fase, non prova degli esiti Round 1–6. |
| README, indice docs, metodo e decisione 0001 | **3 — CONTESTO SECONDARIO** rispetto alla genealogia | Autorità sul metodo e sui perimetri, non sui risultati strutturali specifici dei Round. |
| Descrizione FOL-40 e mandato corrente | **3 — CONTESTO SECONDARIO** rispetto alla genealogia | Contratto operativo esplicito; i numeri e risultati storici riportati richiedono verifica indipendente nelle fonti. |
| Titoli degli allegati e soli prompt storici | **4 — INSUFFICIENTE**, se usati al posto delle risposte | Provano che fu richiesta una revisione, non quale conclusione fu raggiunta. Non sono stati usati come sostituti dei testi finali. |
| Memoria implicita del modello o conversazioni non recuperate | **4 — INSUFFICIENTE / NON DISPONIBILE** | Nessuna conclusione necessaria è basata su un ricordo non riscontrabile. |

La numerazione delle categorie riguarda la natura documentale, non una scala che permetta a ogni fonte primaria di modificare il Ledger. In particolare una critica è fonte primaria della critica, non per questo una nuova decisione di Fold.

## 4. Readiness del percorso componenti

**Esito: ricostruibile combinando più fonti effettivamente disponibili.** L’inventario, le disposizioni e la contabilità sono direttamente documentati in AUDIT; la catena completa richiede V1, Round, AUDIT e fonti dell’assemblaggio.

### 4.1 Inventario originale e problemi recuperabili

V1 contiene 40 schede principali nelle aree 1–5. Il perimetro dei 34 selezionato dall’audit esclude sei risorse/memorie: Mapping Definitions, Domain Model, Core Model, Quality Model, Application Decision Policies e Knowledge Repository. Le trasversali dell’area 6 e i meccanismi interni del Core Engine hanno un trattamento distinto. Quindi “34” non va ottenuto contando indiscriminatamente tutti i titoli della v1.

Gli elementi recuperati sono quelli nominati in AUDIT §A. Le varianti lessicali sono localizzabili nella v1, per esempio “Referent Candidate Generation”/“Generator”, “Extraction Provenance”/“Recorder” e “Source Preservation e Source Registry”/“Source Preservation”. Queste corrispondenze di denominazione non provano da sole una trasformazione: quella è documentata nelle schede dell’audit.

| Porzione dell’inventario AUDIT | Elementi originali recuperabili | Fonte v1 |
|---|---|---|
| 1–6 | Channel Adapter; Acquisition Controller; Technical Validation; Fingerprinting / Technical Deduplication; Staging / Technical Lifecycle; Source Preservation | §§1.1–1.6 |
| 7–15 | Format Decoder; Text Extraction; OCR; Layout Analyzer; Structure Detector; Lexical Parser; Observation Builder; Extraction Quality Assessment; Extraction Provenance Recorder | §§2.1–2.9 |
| 16–22 | Source Classifier; Mapping Executor; Existing Knowledge Reader; Referent Candidate Generator; Evidence Construction; Interpretation Coordinator; Semantic Quality Assessment | §§3.1, 3.3, 3.6–3.10 |
| 23–28 | Candidate Validator; Quality Assessment; Core Engine; Policy Evaluation; Verification Workflow; Knowledge Admission & State Management | §§4.1, 4.3, 4.4, 4.6–4.8 |
| 29–34 | Query & Retrieval; Projection Builder; Application Functions; Explanation Composer; Presentation Layer; Feedback Handler | §§5.1–5.6 |

AUDIT contiene **34 righe di matrice e 34 schede analitiche**. Per tutte e 34 sono presenti i campi: problema originario, responsabilità v1, cosa hanno mostrato i Round, permanenza del problema, destinazione candidata, collocazione della responsabilità, perdita da eliminazione impropria e verdetto. Non sono stati trovati campi mancanti in questo controllo di disponibilità.

### 4.2 Contabilità verificata sulle disposizioni

I conteggi sono stati ricalcolati dalle 34 righe di AUDIT §A e confrontati con AUDIT §C. Non sono assunti dal prompt o dalla candidata v2.1.

| Disposizione storica | Numero verificato | Numeri dei componenti AUDIT |
|---|---:|---|
| Mantenuti autonomi | 7 | 1, 3, 4, 17, 30, 32, 33 |
| Mantenuti ma ridefiniti | 9 | 2, 6, 21, 26, 27, 28, 29, 31, 34 |
| Accorpati | 7 | 7, 10, 11, 12, 13, 16, 18 |
| Distribuiti | 7 | 14, 15, 19, 20, 22, 23, 24 |
| Specializzazioni | 2 | 8, 9 |
| Riclassificati | 2 | 5, 25 |
| Eliminati puramente | 0 | Nessuno |
| **Totale** | **34** | Tutti i 34, una disposizione principale per elemento |

Le nove voci 25a–25i sono auditate separatamente in AUDIT §B e non si sommano ai 34. In particolare document identity, conflict detection, correction/supersession e traversal non devono scomparire perché cambia la collocazione del Core Engine.

### 4.3 Catena delle fonti e collegamento ai 24

| Passaggio da dimostrare | Disponibilità delle fonti | Valutazione |
|---|---|---|
| Inventario iniziale | V1 e matrice AUDIT §A | Direttamente documentato, con perimetro esplicito. |
| Problema/responsabilità di ciascuno | Schede V1 e 34 schede AUDIT | Recuperabile per 34/34. |
| Ragionamento che modifica natura/confine | R1; R2 e R2C §8; R3 “Componenti dopo Round 3”; R4 audit dei componenti; R5 audit e delta; R6 self-audit e GATE | Ricostruibile combinando le sezioni pertinenti. Non si deve attribuire a ogni componente uno stress originale in ogni Round. |
| Disposizione di ciascuno | AUDIT §A, schede e §C | Direttamente documentata per 34/34. |
| Destinazione nei 24 gruppi | AUDIT §F, 24 righe con problema, componenti assorbiti/riallocati e autonomia candidata | Direttamente documentata; per gli obblighi distribuiti occorrono anche le schede e §G. |
| Passaggio 24 gruppi → esposizione v2 | ASM1 §K; REG §B1/D07; ASM2 §K | Documentato prima della v2.1. |
| Collocazione v2.1 | Candidata §K, schede H e viste F/G | Localizzabile come punto d’arrivo; la valutazione completa della fedeltà appartiene al lavoro successivo. |
| Perdita da interpretazione impropria | Campo dedicato in ciascuna scheda AUDIT; §§D/H e REG §B2 | Recuperabile per 34/34, con guardrail specifici. |

I **24 gruppi di copertura** e le **22 schede H** non sono conteggi concorrenti. ASM1 §K documenta già che i gruppi 1 e 2 confluiscono nelle due capacità di H1 e il gruppo 24 vive nel piano operativo presso i proprietari delle attività. I gruppi 3–23 corrispondono a H2–H22. REG D07 verifica e motiva l’accorpamento in H1. La candidata v2.1 §K conserva la stessa mappa: non è stata usata per inventarla retroattivamente.

Il percorso componenti dispone dunque di tutte le fonti richieste per essere costruito. Non è ancora stata prodotta qui la matrice genealogica completa componente per componente.

## 5. Readiness del percorso Core / primitive

**Esito: ricostruibile combinando più fonti effettivamente disponibili.** Nessuno dei concetti minimi richiesti risulta documentato soltanto dalla candidata successiva.

### 5.1 Quali Round hanno effettivamente esercitato lo stress

| Passaggio | Evidenza disponibile | Limite da preservare |
|---|---|---|
| V1 §3.5 | Elenco iniziale delle forme candidate e distinzioni; altre sezioni trattano Source, Observation, Candidate e Knowledge | Un nome nell’elenco non prova autonomia o approvazione come primitiva. |
| R1 §§R3–R7 e contraddizioni nuove | Confini fra attività, risultati, Work, autorità, Disposition/Admission e Quality | È soprattutto stress dell’anatomia operativa; non è un audit completo di tutte le primitive. |
| R2 §§R2.1–R2.9 | Documenti, cardinalità Source, contributi umani, supporto, lavoro riprendibile e candidati incompleti | Le soluzioni iniziali sono successivamente corrette da R2C. |
| R2C §§1–7 e 9–13 | Audit esplicito delle primitive storiche; stress Assertion, Relation, Value, Knowledge State e nuovi nomi | Identifier è dichiarato non testato; Derivation non testata come primitiva. Non vanno retrodatati i test successivi. |
| R3 §§R3.1–R3.10 e delta D | Tempo/Validity, Current State, Derivation, aspettative, impatto e applicabilità | Identifier è dichiarato non coinvolto significativamente. |
| R4 §§R4.1–R4.10 e delta E | Quality, supporto, indipendenza, Provenance/Lineage, riproducibilità e regole | La forza di una distinzione non decide la forma autonoma nel Core. |
| R5 §§R5.1–R5.11, delta e Core minimo provvisorio | Stress diretto di Referent, Identifier, Assertion, Relation, Value, documento, Candidate e Knowledge | Derivation non è al centro del Round; le aperture del Core minimo restano tali. |
| R6 §§I–V e VII | Contraddizioni cross-round, bersagli di Admission, famiglie informative, collocazioni candidate, negativo e modalità | Una soluzione candidata sufficiente per costruire v2 non è una canonizzazione. |
| GATE §§A–D | Raffinamento contenuto/contributo/commitment, impatto e Derivation/Policy | L’equivalenza dei contenuti proposizionali resta aperta. |

### 5.2 Mappa di accesso alle fonti per i concetti richiesti

Le righe seguenti indicano dove recuperare ipotesi, stress e conclusioni; non sono la genealogia definitiva e non assegnano nuovi stati ai concetti.

| Concetto | Fonti primarie utili | Cosa è effettivamente documentato | Localizzazione terminale v2.1 | Readiness |
|---|---|---|---|---|
| Referent | V1 §3.5; R2C §2; R5 §§R5.1/R5.4/R5.5; R6 §III.8 e §V.1 | Passaggio dal linguaggio della cosa rappresentata al locus interno; proposta referenziale, soggetto e coreferenza distinti. Necessità forte e definizione candidata non coincidono. | I, H7/H8, E | Combinazione sufficiente. |
| Assertion | V1 §3.5; R2C §3; R5 §R5.6; R6 §V.3; GATE A/controllo 1 e C | Stress della super-primitiva; contenuto proposizionale, contributo attribuito e commitment esplicitamente distinti nel controllo finale. | I, D/E, J | Combinazione sufficiente, incluso il raffinamento dopo R6. |
| Identifier | V1 §3.5; R2C §2; R4 delta E; R5 §R5.3; R6 §V.4 | Non testato in R2, poi schema/valore/assegnazione sottoposti a casi espliciti, incluso identificatore stampato errato. | I/Identifier, H6–H8, J | Combinazione sufficiente; cronologia del test dimostrabile. |
| Value | V1 §3.5; R2C §5; R5 §§R5.3/R5.8 | Autonomia dell’entità non dimostrata; necessità del contenuto strutturato non referenziale e dei diversi endpoint. | I/Value, J | Combinazione sufficiente. |
| Source | V1 §1.6; R2 §§R2.1–R2.4; R2C §T1; R4 §R4.3; R5 §R5.9; R6 §V.5 | Definizioni messe in crisi e riformulate; origine recuperabile distinta da processabilità, documento e affidabilità; collocazione adiacente candidata. | H4, G, I/Documenti | Combinazione sufficiente. |
| Observation | V1 §§2.7/3.5; R2C §T2; R4 §R4.1; R5 §§R5.3/R5.9; R6 §V.5 | Risultato dell’osservazione distinto dal materiale e dal significato; abbandono del passaggio universale per ogni ingresso. | H5, D, I | Combinazione sufficiente. |
| Relation | V1 §3.5; R2C §4; R5 §R5.7; R6 §V.3 | Alternative esplicite e famiglie con semantiche differenti; respinta l’uniformità semantica universale, non deciso un formalismo tecnico. | I/J | Combinazione sufficiente. |
| Candidate / Proposal | V1 §§3.7/4.1/4.9; R2 §R2.9; R2C §T3; R5 §R5.10; R6 §III.3 e §V.2 | Bundle, proposte indirizzabili, risultati incompleti e posizione rispetto all’ammissione; Candidate universale non sostenuto. | D/E/G/I | Combinazione sufficiente. |
| Knowledge | V1 §4.9; R2C §§6/10; R5 §R5.11; R6 §V.2; GATE | Confronto esplicito fra deposito, vista e corpo governato; substrato informativo raggiungibile distinto dai commitment. | E/G/I | Combinazione sufficiente. |
| Quality / Quality Assessment | V1 §§4.2/4.3; R1 §R7; R4 §§R4.1/R4.2/R4.9; R6 §III.10 | Risorsa condivisa, attività e risultato locale distinti; target, basi e storia; nessuno score o controllore universale. | G, I/Quality, obblighi H | Combinazione sufficiente; non presupporre che ogni accezione fosse una primitiva. |
| Evidence / supporto | V1 §3.8; R2 §§R2.4/R2.5; R2C §T4; R4 §§R4.4/R4.5; GATE | Confronto oggetto/ruolo/relazione; portata e indipendenza; attribuzione distinta dall’adeguatezza del supporto. | D, I/Supporto, J | Combinazione sufficiente. |
| Documento / document identity | V1 §4.4.2; R2 §§R2.1/R2.2; R2C §§T5/T6; R5 §§R5.2/R5.9 e Document Identity Reconciliation; AUDIT §B/25b | Alternative al Logical Document; documento possibile Referent; copie, composizione, versioni e coreferenza non equivalenti. | H3/H7/H8, I/Documenti | Combinazione sufficiente; non risolve i criteri documentali ancora aperti. |
| Derivation | V1 §§3.5/4.4.7; R2C §2; R3 §R3.4; R4 §R4.4; GATE A/controllo 3 e C | Da candidato poco testato alla distinzione fra attività, conclusione e giustificazione; confine semantico con Policy corretto esplicitamente. | H11, D/G/J | Combinazione sufficiente; non impone un oggetto per ogni derivazione. |
| Decision / Disposition / Application | V1 §§4.6–4.8; R1 §R6; R3 §R3.10; R6 §V.9; GATE; REG §B1/D06 | Scelta, disposizione e applicazione con storie distinte; origini non-Policy e applicabilità; ownership residua esplicitamente problematizzata. | E/F, H14–H16/H19, O | Combinazione sufficiente, compresa la storia dell’apertura D06. |
| Work | V1 §§1.2/1.5/6.5; R1 §§R3/R5; R2 §§R2.6–R2.8; R2C §9; R6 §V.9 | Obiettivo durevole, tentativi, attese e risultati; natura operativa distinta dal Core informativo. | F/G, K gruppo 24 | Combinazione sufficiente. |

Tutti i concetti minimi richiesti hanno materiale anteriore all’assemblaggio v2.1. La loro catena non è necessariamente contenuta in un unico messaggio: il fatto che sia ricostruibile attraverso più fonti non autorizza a uniformarne gli stati intermedi.

### 5.3 Altri concetti realmente presenti da non perdere nell’inventario futuro

L’elenco del mandato non esaurisce ciò che le fonti hanno esaminato. Sono disponibili anche le seguenti piste; elencarle qui non le promuove a primitive.

| Concetto/famiglia trovato nelle fonti | Localizzazioni originarie per verificarne il percorso |
|---|---|
| Subject / soggetto; Property / attributo | V1 §3.5; R5 §§R5.1/R5.8; R6 §V.1. Da distinguere dal Referent e dai tipi di endpoint, senza assumere una proposta autonoma per ogni nome. |
| Validity / temporal qualifications | V1 §3.5; R2C §2; R3 §§R3.1/R3.2; R6 §III.6 e §V.6. |
| Knowledge State | V1 §3.5; R2C §6; R4 §R4.2; R5 delta I; R6 §III. È documentata la decomposizione del contenitore unitario. |
| Current State / Current Reconstruction | V1 §4.4.8; R3 §R3.3; GATE controllo 2; AUDIT 25h. |
| Expectation / attesa e temporal attention | R3 §§R3.6/R3.7, con alternative e base/finestra/riscontro; nessuna necessità automatica di super-primitiva. |
| Logical Document; Source Portion / locator | R2 §§R2.1/R2.2; R2C §§T5/T6 e §7; R5 §§R5.2/R5.9. |
| Human Statement / contributo attribuito | R2 §R2.4; R2C §§T1/T4/7; GATE controlli 1 e delta C. |
| Interpretation Result / Bundle | R2 §R2.9; R2C §§T3/7/9/10; R5 §R5.10. È disponibile anche la storia delle forme operative iniziali, da non riscrivere come conclusione già definitiva. |
| Attempt, Reception/Event, risultato/esito | R2 §§R2.6/R2.7; R2C §§7/9. Event e Result generali non sono resi necessari dai casi. |
| Verification, Admission e Policy | V1 §§3.5/4.5–4.8; R1 §R6; R2 §R2.4; R4 §R4.10; R6 e GATE. Vanno distinte risorsa, lavoro, qualificazione e autorità. |
| Provenance / Lineage / giustificazione inferenziale | V1 §§2.9/6.1; R4 §§R4.4/R4.6–R4.8; R5 §R5.6. |
| Impatto e qualificazione del risultato affetto | R3 §§R3.8/R3.9; R6 §V.9; GATE controllo 2. |
| Informazione negativa e modalità del contenuto | R3 §§R3.4/R3.7; R6 §§I.L/I.M e V.7/V.8; GATE. |

Queste fonti consentono di costruire un inventario fedele ai concetti realmente stressati, includendo i casi dichiarati non testati o lasciati aperti. Non è necessario inventare una primitiva precedente per ogni concetto oggi nominato.

## 6. Gap documentali e limiti

**Non è stato individuato un gap di disponibilità che impedisca la costruzione delle due genealogie nel perimetro richiesto.** Sono invece presenti questi limiti, che devono restare espliciti:

| Limite | Conseguenza per il lavoro successivo | Blocca la costruzione? |
|---|---|---|
| I testi integrali V1, Round, GATE e AUDIT sono nell’archivio locale della conversazione, esterno al repository | Le future genealogie devono distillare problemi, passaggi e motivazioni necessari e citarne ordinal/hash. Questa source map da sola non rende il repository autosufficiente rispetto alla storia integrale. | No: le fonti sono disponibili ora. È una lacuna di preservazione, non di accesso. |
| AUDIT racconta retrospettivamente cosa hanno mostrato i Round | La ricostruzione deve associare la disposizione dell’audit ai passaggi effettivi dei Round; non attribuire all’audit la produzione originaria di tutti quei ragionamenti. | No: i Round originali sono recuperati. |
| Non tutti i concetti sono testati in ogni Round | Registrare “non testato/non coinvolto” dove lo dice la fonte. Identifier e Derivation nel Round 2 sono casi espliciti. | No: è un dato genealogico, non un vuoto da riempire. |
| Gli stati storici e le aperture non sono tutti definitivi | Conservare definizioni candidate, autonomia non dimostrata e aperture; non confondere necessità forte con decisione finale sulla forma. | No: genealogia di un’apertura e soluzione dell’apertura sono lavori diversi. |
| Fonti remote esterne o review iniziali non incluse nel corpus verificato | Non rivendicare di averle lette né attribuire loro formulazioni esatte. I Round recuperati conservano casi, alternative e ragionamenti sufficienti per questo perimetro. | No per le due catene richieste. Un’eventuale attribuzione testuale a una review esterna richiederebbe la sua fonte. |

Non sono emerse contraddizioni fra repository e conversazione che obblighino a scegliere implicitamente una storia alternativa per dichiarare la disponibilità delle fonti. Due cautele sono invece dimostrate: 24 gruppi e 22 schede hanno granularità differenti; REG D06 conserva un’ownership ancora non completamente assegnata. Nessuna delle due va trasformata in una falsa perdita o in una falsa chiusura.

## 7. Informazioni conservate integralmente solo nella conversazione

Nel corpus consultato, rimangono esterni al repository nella loro forma integrale:

- l’anatomia V1 con le schede originali e le forme Core allora candidate;
- l’audit di ciascuno dei 34, comprese motivazioni, perdite da eliminazione impropria e disposizioni;
- la matrice 25a–25i e l’inventario dei 24 al momento della loro produzione;
- i confronti di alternative dei Round, compreso R2C che corregge la risposta R2 prima del Round 3;
- i test nei quali Assertion, Relation, Value, Candidate, Source e Knowledge State mostrano limiti diversi;
- i passaggi specifici che dichiarano Identifier non testato, poi ne esercitano lo stress;
- il confronto finale fra contenuto, contributo e commitment, con i tre stress del GATE;
- le motivazioni complete del Regression Audit, incluse D07 e la cautela D06.

Il repository contiene già molte conclusioni e localizzazioni di questi materiali; “solo nella conversazione” qui significa **testo originale integrale e percorso argomentativo completo**, non assenza di qualsiasi traccia nel Ledger. Il corpo integrato ASM2 costituisce un’eccezione: è già preservato integralmente nello snapshot v2.

## 8. Perché gli artefatti successivi non sostituiscono gli originali

Ledger, Coverage, delta, candidate e Gate consentono di controllare conclusioni, stati, perdite e ripristini. Non consentono, da soli, di dimostrare tutte le alternative precedenti o in quale passaggio una distinzione sia stata ottenuta.

In particolare:

- una riga K con un’origine R5 non sostituisce il confronto fra alternative di R5;
- “SUPPORTED BY LEDGER” non prova la conservazione dell’intera trasformazione strutturale;
- la sezione K della candidata permette di localizzare i 24 gruppi, ma non ricrea le 34 disposizioni originarie;
- le 22 schede H non permettono di dedurre quali componenti iniziali fossero autonomi, accorpati o distribuiti;
- la presenza attuale di un concetto in I non prova che fosse stato proposto come primitiva né che sia stato testato in un certo Round;
- un Gate Knowledge Preservation superato non costituisce il Model Preservation Gate.

La costruzione successiva deve quindi partire da V1 e dai Round, usare AUDIT per le disposizioni e l’inventario finale, confrontarsi con il Ledger e arrivare solo infine alla collocazione in v2.1. Le fonti di assemblaggio e REG spiegano gli adattamenti di esposizione senza retrodatare le conclusioni.

## 9. Verdetto finale

**MODEL PRESERVATION SOURCE READY**

Entrambe le genealogie possono essere costruite usando le fonti identificate:

- **componenti:** recuperati inventario, problemi e 34 schede; contabilità verificata 7/9/7/7/2/2; disponibili inventario dei 24 e passaggio documentato alle 22 schede H;
- **Core/primitive:** disponibili ipotesi iniziali, stress e confronti dei Round, correzioni cross-round, conclusioni candidate e aperture per tutti i concetti minimi richiesti e per ulteriori concetti effettivamente trattati.

Questo controllo autorizza la costruzione delle due genealogie di FOL-40 usando le fonti identificate. Non autorizza il Model Preservation Gate, il freeze della v2.1, l’implementazione o la chiusura di FOL-36.

Il verdetto riguarda la sufficienza delle fonti, non anticipa l’esito della futura verifica delle genealogie o della candidata.

## 10. Integrità e stato finale

È stato creato soltanto `docs/ricerca/fold-model-preservation-source-map-2026-09-05.md`. I 24 file preesistenti sotto `docs/` sono stati confrontati tramite SHA-256 prima e dopo la creazione del rapporto e risultano invariati. Nessuna modifica alla candidata, ai Ledger, al delta, allo snapshot o ai Gate. Il controllo di integrità dei file non costituisce una ripetizione del Knowledge Preservation re-check.

SHA-256 della candidata invariata: `98ef21e3128b217afaa863c616fc3c12eb579507103b495ffcc9c7f90e8de754`.

Nessuna genealogia definitiva creata; nessuna nuova K-ID, primitiva o responsabilità. Linear è stato consultato in sola lettura; nessuna modifica a Linear o Notion, nessun Fold Sync, commit, push o branch.

`git status --short` finale:

```text
?? docs/ricerca/fold-anatomia-v2.1-candidate-2026-09-04.md
?? docs/ricerca/fold-knowledge-preservation-gate-v2.1-2026-09-04.md
?? docs/ricerca/fold-knowledge-preservation-recheck-v2.1-2026-09-05.md
?? docs/ricerca/fold-model-preservation-source-map-2026-09-05.md
```
