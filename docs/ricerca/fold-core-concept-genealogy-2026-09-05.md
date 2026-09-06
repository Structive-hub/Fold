# Fold — Genealogia dei concetti del Core e delle distinzioni adiacenti

**Status: Research — Model Preservation**  
**Data di riferimento / nome dell’artefatto:** 2026-09-05  
**Redazione:** 2026-09-06  
**Percorso:** FOL-40, nel contesto di FOL-36  
**Oggetto:** seconda genealogia strutturale; candidata v2.1 invariata e ancora Draft.

## 1. Scopo e limiti

Questo documento preserva l’evoluzione di **35 concetti o gruppi concettuali**, non propone un inventario di 35 primitive. Comprende i 15 nuclei obbligatori del mandato e altre distinzioni realmente stressate. Le denominazioni accostate in una scheda indicano un problema genealogico comune, non una fusione delle rispettive nature: Decision, Disposition e Application, per esempio, rimangono distinte. Documento e Logical Document hanno schede differenti per distinguere il problema dell’identità dalla candidatura storica di un contenitore universale.

La catena conservata è: ipotesi iniziale → problema → casi e contraddizioni → alternative effettivamente considerate → conclusione acquisita → stato strutturale → collocazione successiva → rischio di perdita. Le spiegazioni rendono il percorso leggibile senza riaprire la chat; i rinvii consentono di controllare la distillazione.

Non è una nuova revisione teorica, un’architettura tecnica o il Model Preservation Gate. Non autorizza freeze, implementazione o chiusura di FOL-36/FOL-40. Non riesegue Source Readiness, Knowledge Preservation, genealogia dei componenti o audit dei 34. La consultazione di AUDIT riguarda esclusivamente disposizioni storiche pertinenti ai concetti, non un nuovo audit.

### Tre dimensioni da non confondere

1. **Stato documentale:** questo artefatto è Research; la candidata resta Draft, non Canonical.
2. **Stato genealogico del Ledger:** STABILE, CANDIDATA, APERTA e SUPERATA appartengono alle specifiche conoscenze. Nessuna scheda li modifica.
3. **Classificazione strutturale descrittiva:** «primitiva fortemente sostenuta», «distinzione necessaria», «informazione adiacente», «governance/processo», «forma candidata», «apertura» e «forma universale non sostenuta» spiegano l’esito, senza istituire nuovi stati genealogici.

Una distinzione FORTE nella candidata può avere forma autonoma non dimostrata; una formulazione CANDIDATA può preservare una necessità stabile. Essere indirizzabile non prova né subjecthood né autonomia ontologica. Non essere una primitiva non autorizza a eliminare il problema.

«Universale non sostenuto» comprende casi diversi: forma esplicitamente superata, decomposizione necessaria, oppure necessità non dimostrata. Non significa che ogni futura soluzione locale con un nome simile sia impossibile. Una futura scelta richiederebbe una decisione propria.

## 2. Fonti e metodo genealogico

### Registro primario

Le sigle sono quelle del [Model Preservation Source Map](fold-model-preservation-source-map-2026-09-05.md), già approvato. È stato consultato l’archivio originale identificato da quella mappa:

```text
C:\Users\giuseppe\.codex\sessions\2026\09\01\rollout-2026-09-01T14-56-30-01a05d0a-e483-7793-a648-e46306e04177.jsonl
```

Gli ordinal identificano messaggi JSONL, **non numeri di riga**. Il corpo è quello del messaggio assistant con phase final_answer; le impronte sotto sono riusate dal Source Map, non costituiscono un nuovo Source Readiness Check.

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

V1 e i Round sono fonti primarie delle proprie ipotesi, prove e conclusioni; R2C è il chiarimento del Round 2. Le sezioni del primo Round si chiamano R1–R8: «R1 §R6» significa la sesta sezione del primo Round, non Round 6.

GATE è la fonte delle tre correzioni finali a R6. AUDIT e REG sono fonti primarie dei rispettivi ragionamenti successivi, non sostituiscono le prove dei Round cui rinviano. ASM1/ASM2 documentano l’assemblaggio: non si retrodatano le loro formulazioni.

### Controlli e preservazioni successive

- [Knowledge / Decision Ledger](fold-knowledge-decision-ledger-2026-09-04.md): autorità genealogica per stati, superamenti e conclusioni distillate. Non è il verbale integrale dello stress originario.
- [Coverage v2](fold-coverage-ledger-v2-2026-09-04.md): evidenza della copertura successiva, non prova di come nacquero le distinzioni.
- [Delta v2 → v2.1](fold-delta-v2-v2.1-2026-09-04.md): ripristini autorizzati, aperture e tesi da non reintrodurre. Le review vi sono classificate come evidenza di stress, non autorità superiore alle conoscenze stabili.
- [Snapshot v2](fold-anatomia-v2-snapshot-2026-09-04.md): preservazione di ASM2, usata per il tratto di assemblaggio.
- [Candidata v2.1](fold-anatomia-v2.1-candidate-2026-09-04.md): destinazioni odierne D–O e H1–H22, non fonte da cui dedurre il passato.
- [Prima genealogia strutturale](fold-component-responsibility-genealogy-2026-09-05.md): riferimento complementare per responsabilità e per EG-01; non viene riscritta.

Consultati il contesto metodologico del repository e, in sola lettura, descrizione, relazioni e checkpoint di FOL-40. L’issue risulta In Progress e conferma la prima genealogia completata; non viene aggiornata o chiusa da questo task.

### Passaggi che non possono essere retrodatati

- **V1:** elenco di forme candidate, non primitive software approvate.
- **R1:** separazione del piano operativo, dell’autorità e dei risultati; non nuova ontologia di Work/Event.
- **R2 → R2C:** correzione interna di Source, Candidate, Evidence e composizione documentale. R2C dichiara **Identifier e Derivation non testati come primitive dal Round 2**; i ruoli temporali non equivalgono a verifica della Validity generale.
- **R3:** stress diretto di tempo, derivazione, ricostruzione, attenzione e impatto.
- **R4:** supporto/attribuzione, indipendenza, assessment locali e materialità delle basi recuperabili.
- **R5:** test diretto di Identifier e Referent, famiglie di relazione e memoria delle proposte; due centri forti, non un catalogo definitivo.
- **R6:** soluzioni minime sufficienti e candidate, inclusa l’esistenza pre-Admission di proposte; non chiusura automatica di ogni apertura.
- **GATE:** corregge Assertion sovrapposta a claim/commitment, Policy che può ignorare l’impatto e Policy arbitra dell’applicabilità inferenziale.
- **REG/assemblaggi:** preservano trasformazioni e correggono regressioni, lasciando D06 aperta. Non dimostrano che una lacuna di esposizione sia sempre una nuova scoperta fondazionale.
- **Delta/v2.1:** recuperano conoscenze già conquistate senza promuovere K-080, K-143 o altre candidate.

## 3. Schede genealogiche

Nelle collocazioni, lettere e H si riferiscono esclusivamente alla candidata v2.1. I K-ID sono controlli genealogici successivi: una loro citazione non attribuisce alla candidata copertura esplicita di ogni dettaglio del Ledger.

### Referent

**Ipotesi / forma iniziale**

In V1 §3.5 è una forma candidata per il soggetto di cui si parla. R2C lo rafforza senza identificarlo con ogni elemento indirizzabile; R5 propone il soggetto della realtà o del dominio documentale con identità indipendente da Source, etichetta e Identifier.

**Problema che cercava di rappresentare**

Tenere separati i soggetti anche quando nomi, rappresentazioni e proprietà coincidono o cambiano: i due Mario Rossi di R5 non diventano una sola persona perché condividono una stringa.

**Stress e contraddizioni**

R5 esclude il criterio «qualsiasi cosa citabile»: anche una regione o un Attempt devono essere richiamabili. R6 mette poi in crisi la formulazione troppo esterna di R5: un soggetto pianificato, ipotetico o contestato deve essere rappresentabile prima che esistenza e natura siano accertate.

**Alternative considerate**

R5 confronta qualsiasi cosa referenziabile, cosa distinta del mondo e identità persistente che raccoglie Assertion. R6 adotta come soluzione minima candidata un locus interno per un soggetto proposto o riconosciuto; non aggiunge una seconda primitiva per la cosa esterna.

**Conclusione acquisita**

La necessità referenziale è fortemente sostenuta. Il Referent non coincide con la cosa esterna e non ne prova esistenza o classificazione: queste richiedono contenuti sostenuti. Può precedere l’Admission come proposta. La continuità dipende dal soggetto definito dal Domain, non dalla persistenza del nome.

**Stato strutturale risultante**

PRIMITIVA FORTEMENTE SOSTENUTA quanto alla necessità del locus; FORMA CANDIDATA quanto alla definizione K-143, che supera K-120. Non è una promozione di K-143 a STABILE.

**Collocazione v2.1**

I, «Elementi e famiglie» e «Referent, Assertion e commitment»; D/E per proposta e Admission; H7/H8; O per i criteri residui.

**Rischio di perdita o promozione indebita**

Leggere FORTE come definizione canonica; creare un Referent per qualunque elemento indirizzabile; assumere che un Referent ammesso provi esistenza certa; eliminare le proposte perché non ammesse.

**Fonti primarie**

V1 §3.5; R2C §T5, §2; R5 §R5.1; R6 §II Q1–Q3, §III.8, §V.1–2.

Controllo/preservazione successiva: K-056, K-120→K-143, K-144–K-146, K-138.

### Assertion

**Ipotesi / forma iniziale**

V1 la propone per esprimere ciò che viene affermato su un soggetto, con valore, tempo ed evidenza. I successivi usi oscillano fra proposizione, ciò che una fonte sostiene e ciò che Fold accetta.

**Problema che cercava di rappresentare**

Rendere valutabile un contenuto preciso senza trasferire all’intero documento il sostegno o l’incertezza di una sua parte.

**Stress e contraddizioni**

R2C: una cifra in una foto con due scontrini non determina ancora una proposizione sull’importo di uno specifico documento. R5: descrivere supporti, Work o derivazioni mediante proposizioni non sostituisce tali strutture. GATE: «ho pagato», ricevuta e movimento bancario non sono automaticamente tre Assertion identiche; il movimento può sostenere una diversa proposizione Q, collegata inferenzialmente al pagamento P.

**Alternative considerate**

R2C e R5 verificano l’assorbimento di ogni informazione in Assertion e ne mostrano la perdita di struttura. GATE separa contenuto proposizionale, contributo attribuito e commitment senza imporre tre primitive. La formulazione R6 ancora sovrapposta viene corretta, non retroattivamente dichiarata già precisa.

**Conclusione acquisita**

Assertion è un elemento semantico indirizzabile che porta contenuto proposizionale. Attribuzione, supporto, qualità e commitment sono collegabili ma non coincidono con quel contenuto. Admission introduce la posizione di Fold, non la paternità del claim. Una proposta può esistere senza essere già sostenuta: non può essere presentata come sostenuta perdendo la giustificazione.

**Stato strutturale risultante**

PRIMITIVA FORTEMENTE SOSTENUTA, non super-primitiva. K-158 sostituisce K-155; identità/equivalenza del contenuto resta APERTURA K-160 e il caso specifico delle meta-Assertion interne resta K-066 APERTA.

**Collocazione v2.1**

I, «Referent, Assertion e commitment»; D/E; H7/H11/H16; O.

**Rischio di perdita o promozione indebita**

Fondere contributi e cancellarne origini; far diventare ogni risultato un’Assertion; scambiare Admission per verità o nuova testimonianza; dichiarare risolta K-066 grazie alla sola definizione generale.

**Fonti primarie**

V1 §3.5; R2C §3 e §13.D; R5 §R5.6; R6 §V.3; GATE §A controllo 1, §B, §C, §D.

Controllo/preservazione successiva: K-055, K-066, K-114→K-115, K-130, K-155→K-158, K-159–K-160.

### Identifier

**Ipotesi / forma iniziale**

In V1 §3.5 compare fra le forme candidate del Core, mentre il Domain fornisce schemi identificativi. R2C dichiara espressamente Identifier NON TESTATO nelle sue proprietà specifiche: la conferma di un link non costituisce quel test.

**Problema che cercava di rappresentare**

Distinguere segno presente, ruolo identificativo e soggetto cui è assegnato; preservare continuità e correzioni senza usare la stringa come identità assoluta.

**Stress e contraddizioni**

R5 esercita POD osservato ma non associato, POD stampato errato e schema con ambito non noto. Una Observation può riportare correttamente la stringa sbagliata nel documento: è l’assegnazione, non necessariamente la lettura, a perdere sostegno. Un identificatore può riguardare contratto e non persona.

**Alternative considerate**

R5 scarta l’insufficienza di Identifier come sola Assertion, che non copre bene schema e valore non assegnato, e come solo Value, che perde ruolo e assegnazione. La soluzione articolata distingue schema, valore e assegnazione senza imporre tre oggetti.

**Conclusione acquisita**

Scheme/type fornisce significato e scope Domain; value è contenuto identificativo strutturato; assignment è proposizione verso un Referent, sostenibile, temporale e correggibile. Normalizzazione non corregge silenziosamente la Source. Uguaglianza di stringa non prova identità e non autorizza auto-link.

**Stato strutturale risultante**

DISTINZIONE NECESSARIA, FORMA AUTONOMA NON DIMOSTRATA; forma ontologica e criteri specifici APERTI K-141. Non tre primitive autonome.

**Collocazione v2.1**

I, «Identifier» e «Value»; G Domain/Mapping; H5/H7/H8; O.

**Rischio di perdita o promozione indebita**

Attribuire il test al Round 2; equiparare stringa conforme a assegnazione vera; promuovere schema–valore–assegnazione a inventario software; far dipendere la continuità soltanto dal POD.

**Fonti primarie**

V1 §3.4–3.5; R2C §2; R5 §R5.3 e Delta §D/§M; R6 §V.4.

Controllo/preservazione successiva: K-121–K-124, K-138, K-141.

### Value

**Ipotesi / forma iniziale**

In V1 §3.5 è una forma candidata distinta da Referent e Assertion; il lessico poteva suggerire un elemento con autonomia propria.

**Problema che cercava di rappresentare**

Preservare quantità, valuta, precisione e contenuti strutturati non referenziali, invece di ridurli a testo indistinto.

**Stress e contraddizioni**

R2C verifica 84,72 €: stesso numero non significa stessa occorrenza, obbligazione o pagamento. Evidenza, tempo e correzione riguardano lettura o attribuzione, non il numero astratto. Cercare tutte le occorrenze non prova l’esistenza di un’entità Value. R5 rafforza il bisogno attraverso il valore identificativo non ancora assegnato.

**Alternative considerate**

Contenuto strutturato in Observation/Assertion contro entità con identità, Evidence e lifecycle autonomi; R5 mantiene la distinzione endpoint referenziale/contenuto letterale o strutturato.

**Conclusione acquisita**

Value resta necessario come forma di contenuto non referenziale. Forma letta, interpretazione numerica, unità, precisione e ruolo non collassano; il contenuto strutturato non viene per questo promosso a entità indipendente.

**Stato strutturale risultante**

DISTINZIONE NECESSARIA, FORMA AUTONOMA NON DIMOSTRATA. Il FORTE locale della v2.1 qualifica la distinzione, non l’autonomia ontologica.

**Collocazione v2.1**

I, «Value» e «Identifier»; H5/H7.

**Rischio di perdita o promozione indebita**

Eliminare i valori perché non sono entità, oppure attribuire al numero astratto la storia della proposizione che lo usa.

**Fonti primarie**

V1 §3.5; R2C §2, §3 «Value può essere contenuto dell’Assertion?», §5; R5 §R5.3 e §R5.8.

Controllo/preservazione successiva: K-058, K-121, K-132.

### Source

**Ipotesi / forma iniziale**

V1 §1.6 riceve l’artefatto tecnicamente valido e ne preserva il contenuto. R2 usa formulazioni non equivalenti di materiale ricevuto, origine conservata e origine utilizzabile.

**Problema che cercava di rappresentare**

Consentire di recuperare ciò che è stato realmente fornito o dichiarato, distinguendolo dalle trasformazioni prodotte da Fold.

**Stress e contraddizioni**

R2C prova PDF conservato ma non processabile, fotografia, risposta «sì» e dichiarazione di pagamento. Un evento «ricevuto PDF» senza contenuto recuperabile non basta; un PDF indecifrabile può invece restare Source. R4 mostra che autenticità, leggibilità e verità della dichiarazione non coincidono.

**Alternative considerate**

R2C confronta qualsiasi materiale tracciabile, materiale ammesso/utilizzabile, sola registrazione di provenienza e contenuto d’origine referenziabile con condizioni d’uso separate. La quarta corregge le sovrapposizioni: le prime includono troppo, confondono Admission o perdono il contenuto.

**Conclusione acquisita**

Source è contenuto d’origine determinato e referenziabile mantenuto per ricostruire ciò che fu fornito/dichiarato. Non coincide con attore, canale, ricezione, documento o Evidence. Processabilità e affidabilità qualificano usi e supporti, non la definizione.

**Stato strutturale risultante**

INFORMAZIONE ADIACENTE AL CORE nella collocazione CANDIDATA K-148; definizione K-049 STABILE. Necessità del contenuto d’origine non equivale a primitiva centrale autonoma.

**Collocazione v2.1**

D; G memorie/Provenance; H1/H2/H4; I «Elementi e famiglie» e «Documenti e rappresentazioni».

**Rischio di perdita o promozione indebita**

Far sparire una Source quando fallisce OCR; sostituirla con la sola provenance; ammettere il contenuto come vero perché preservato; rendere canonica l’adiacenza candidata.

**Fonti primarie**

V1 §1.6; R2 §R2.4 e §R2.7; R2C §T1; R4 §R4.3; R6 §V.5.

Controllo/preservazione successiva: K-049, K-100, K-148.

### Observation

**Ipotesi / forma iniziale**

V1 §2.7 compone stringhe, localizzazioni e risultati estrattivi prima dell’interpretazione; la sequenza documentale può sembrare un passaggio universale.

**Problema che cercava di rappresentare**

Separare ciò che un metodo rileva nella Source dal significato che Fold vi attribuisce.

**Stress e contraddizioni**

R2C confronta fotografia e risposta strutturata: duplicare quest’ultima in un’Observation non aggiunge necessariamente una distinzione. R5: un POD stampato errato può essere osservato fedelmente. La correzione di una lettura non deve cancellare l’esito automatico precedente.

**Alternative considerate**

R2C considera Observation specifica, Observation estesa a qualunque ricezione e percorsi differenti. La prima e la terza sono compatibili; la seconda non è dimostrata necessaria, non semplicemente dichiarata impossibile.

**Conclusione acquisita**

Risultato indirizzabile dell’osservazione di una Source con metodo, localizzazione, forma e qualità propri. Observation ≠ Assertion. Ingressi umani o sistemici strutturati possono proporre semantica senza Observation fittizia, preservando origine e percorso. La forma della conferma di lettura resta aperta.

**Stato strutturale risultante**

Definizione K-050 STABILE; INFORMAZIONE ADIACENTE AL CORE con collocazione K-148 CANDIDATA. Distinzione necessaria, non pedaggio universale.

**Collocazione v2.1**

D; H5 e assessment locali; G memoria delle Observation; I/O.

**Rischio di perdita o promozione indebita**

Trasformare ogni ingresso in estrazione; dichiarare falsa una lettura perché il documento mente; fondere confidenza OCR e semantica; chiudere K-119 senza decisione.

**Fonti primarie**

V1 §2.7; R2C §T2 e §2; R4 §R4.2 situazione 2; R5 §R5.3; R6 §V.5.

Controllo/preservazione successiva: K-050, K-119, K-122, K-148.

### Relation

**Ipotesi / forma iniziale**

V1 §3.5 affianca Property/Relation alle forme Core; una freccia generica rischia di unire fatti del mondo, supporti e dipendenze operative.

**Problema che cercava di rappresentare**

Preservare il significato del collegamento e le conseguenze di una sua revisione, non soltanto i suoi endpoint.

**Stress e contraddizioni**

R1 distingue produce, legge, autorizza e applica. R2C separa documento–utenza, rappresentazione, attesa del Work e dipendenza interpretativa: una foto rappresenta una parte del documento, non ne è automaticamente parte. R5 verifica che same_as, supporto e attesa non abbiano la stessa semantica.

**Alternative considerate**

R5 confronta Relation universale; relazioni di dominio come Assertion; separazione rigida attributi/relazioni che duplica la qualificazione epistemica; famiglie tipizzate. Quest’ultima preserva differenze che la forma uniforme non spiega.

**Conclusione acquisita**

Relazioni descrittive come contenuto di Assertion; famiglie epistemiche, rappresentative/provenienziali, inferenziali e operative distinguibili. Una struttura tecnica comune resta possibile, ma non autorizza semantica uniforme o un unico regime di validazione.

**Stato strutturale risultante**

RESPINTA COME SUPER-PRIMITIVA / CONTENITORE UNIVERSALE; DISTINZIONI NECESSARIE tra famiglie. Vocabolario finale e autonomia delle relazioni epistemiche restano aperti.

**Collocazione v2.1**

I e J Relation map; D/E/F per piani distinti; O.

**Rischio di perdita o promozione indebita**

Confondere una freccia con un’Assertion, supporto con dipendenza operativa o autorizzazione con fatto; introdurre un nuovo predicato identitario per ogni stato di certezza.

**Fonti primarie**

V1 §3.5; R1 §R2; R2C §4 e §11; R5 §R5.7–R5.8; R6 §V.3; GATE §C Relation families.

Controllo/preservazione successiva: K-059, K-128, K-131–K-132, K-142.

### Candidate / Proposal

**Ipotesi / forma iniziale**

V1 produce Referent Candidate e Candidate Knowledge Bundle prima di Candidate Validator/Admission; R2 usa Candidate per proposizioni, incompletezza, link e raggruppamenti.

**Problema che cercava di rappresentare**

Conservare contenuti utili che Fold non ha ancora assunto come propria posizione, incluse alternative non risolte.

**Stress e contraddizioni**

R2C: importo determinato, ruolo della data ambiguo e utenza irrisolta non hanno un’unica maturità. R5: la proposta POD→A/B deve sopravvivere alla verifica sospesa o al Work chiuso. Un semplice stato candidate su un’Assertion non rappresenta ciò che non è ancora proposizione.

**Alternative considerate**

Oggetto Candidate; Assertion con posizione proposta; involucro Proposal; Interpretation Result; soluzione ibrida di R5. Il contenitore unico mischia nature, mentre il solo stato non preserva incompletezza e contesto.

**Conclusione acquisita**

Una Assertion completa conserva il proprio contenuto prima e dopo Admission; referenti proposti e risultati interpretativi mantengono natura, alternative, supporti e dipendenze. Proposal memory ≠ Work ≠ Knowledge ammessa. R6 chiarisce l’esistenza informativa senza Work, non ogni forma concreta.

**Stato strutturale risultante**

RESPINTA COME SUPER-PRIMITIVA / CONTENITORE UNIVERSALE. Posizione proposta necessaria; composizione Interpretation Result CANDIDATA; forme concrete ancora aperte.

**Collocazione v2.1**

D/E; G memoria informativa delle proposte; H7/H8/H16; I/O.

**Rischio di perdita o promozione indebita**

Eliminare le proposte con il nome Candidate; rendere ogni risultato un involucro; trasformare la persistenza in Admission; considerare incompatibili tutte le alternative come fatti già ammessi.

**Fonti primarie**

V1 §3.7, §3.9, §4.1; R2 §R2.9; R2C §T3 e §10.2; R5 §R5.10; R6 §V.1–2, §VI.C; REG §B2 L01.

Controllo/preservazione successiva: K-051→K-052, K-053, K-119, K-134, K-137→K-144, K-151.

### Knowledge

**Ipotesi / forma iniziale**

V1 §4.9 parla di Knowledge Repository con affermazioni accettate e contesto, distinguendo la memoria candidata. La formula «insieme di Assertion ammesse» diventa un possibile riassunto troppo stretto.

**Problema che cercava di rappresentare**

Rendere comprensibile la posizione assunta da Fold senza confonderla con tutto il materiale conservato.

**Stress e contraddizioni**

R5 mostra che il solo insieme di Assertion non basta per Referent e giustificazioni, se queste vengono forzate in una super-Assertion. Il nome repository non determina la natura di ogni elemento conservato. R6 chiarisce i target; GATE separa commitment e contenuto.

**Alternative considerate**

R5 confronta insieme di Assertion, Assertion+Referent+contesto raggiungibile, vista/corpo governato e repository eterogeneo. Il corpo governato risponde alla domanda epistemico-governativa; il deposito è una questione distinta.

**Conclusione acquisita**

Forma candidata: Referent e Assertion ammessi con accesso recuperabile a supporti, qualificazioni, revisioni, derivazioni e storie. Source, Observation e proposte appartengono alla memoria informativa più ampia, senza diventare automaticamente commitment. Admission non duplica la sostanza né aumenta la verità.

**Stato strutturale risultante**

FORMA CANDIDATA K-136 e assetto dei target K-146 CANDIDATA. Non nuova primitiva informativa chiamata Knowledge.

**Collocazione v2.1**

E e G memorie; H16; I «Knowledge come corpo governato»; O.

**Rischio di perdita o promozione indebita**

Trasformare tutta la memoria in fatti ammessi; duplicare Assertion in una nuova sostanza Knowledge; rendere qualsiasi uso universale conseguenza dell’Admission.

**Fonti primarie**

V1 §4.8–4.9; R5 §R5.11; R6 §V.2; GATE §A controllo 1 e §C Governance.

Controllo/preservazione successiva: K-135→K-136, K-144, K-146, K-158.

### Quality / Quality Assessment

**Ipotesi / forma iniziale**

V1 distingue risorsa Quality Model, valutazioni estrattive/semantiche e Quality Assessment nella gestione della conoscenza; il ciclo con il Core Engine può però sembrare centrale e globalmente sintetico.

**Problema che cercava di rappresentare**

Far vedere quale aspetto di quale risultato è affidabile, incerto o incompleto, sulla base di quali elementi.

**Stress e contraddizioni**

R1: leggere 84,72 perché lo si attende dalla Knowledge e poi usarlo per confermare quella Knowledge crea autoconferma. R4: OCR nitido non decide se 30/09 sia scadenza; link referenziale debole non rende automaticamente il numero illeggibile. Ripetizione o Admission non producono una nuova base.

**Alternative considerate**

Assessment centrale indistinto e punteggio complessivo vengono confrontati con valutazioni locali per target/aspetto e sintesi per scopo. R4 mantiene Quality Model come risorsa e assessment come attività/risultato storico: non un giudice universale.

**Conclusione acquisita**

L’assessment conserva target, dimensione, base, scopo e storia. Qualità ≠ certezza ≠ Admission ≠ azione; factual correctness, conformità procedurale e autorizzazione non si assorbono. Nuova valutazione richiede nuova base, criterio o contesto pertinente. L’indipendenza ignota non viene presunta.

**Stato strutturale risultante**

INFORMAZIONE ADIACENTE AL CORE; distinzione di assessment necessaria. K-097 STABILE; le cinque famiglie K-098 restano CANDIDATE nel numero/confine; formule e criteri empirici K-118 APERTI.

**Collocazione v2.1**

G Quality Model e cattura locale; assessment presso H5/H7/H8/H11 e produttori competenti; I «Quality Assessment»; E/O.

**Rischio di perdita o promozione indebita**

Promuovere cinque famiglie a tassonomia definitiva; inventare un truth score; trattare una conferma umana come qualità globale; far decidere a Quality l’automazione.

**Fonti primarie**

V1 §2.8, §3.10, §4.2–4.3; R1 §R7; R4 §R4.1–R4.3, §R4.5, §R4.9 e Delta §I; REG §B2 L07.

Controllo/preservazione successiva: K-097–K-102, K-111, K-118.

### Evidence / supporto

**Ipotesi / forma iniziale**

V1 §3.8 presenta Evidence Construction e Evidence tra le forme del Core. R2 oscilla tra cosa autonoma e ruolo di Source, Observation o contributo umano.

**Problema che cercava di rappresentare**

Rendere recuperabile che cosa sostiene quale contenuto o aspetto, con quale portata e adeguatezza.

**Stress e contraddizioni**

Una conferma della lettura 34,72 non conferma il debito; una conferma del link non sostiene tutti i campi. R4: PDF, foto della stampa e inoltro non sono tre origini indipendenti. GATE distingue chi dichiara P da ciò che sostiene adeguatamente P; un movimento Q può sostenere P soltanto attraverso un collegamento pertinente.

**Alternative considerate**

R2C confronta oggetto Evidence, relazione tipizzata, registrazione esplicita e supporto con bersaglio qualificato. R4 contrappone oggetto autonomo, SUPPORTED_BY qualificato e relazione indirizzabile quando occorre. Un arco binario non qualificato perde scope e contestabilità.

**Conclusione acquisita**

Necessario il supporto qualificato, con base, target, attribuzione distinta, scope, valutazioni e storia. Può riguardare lettura o aspetto valutabile, non soltanto Assertion di dominio. Supporto inferenziale mantiene premesse e metodo; non produce corroborazione indipendente delle premesse. Origini ignote non dimostrano indipendenza né dipendenza accertata.

**Stato strutturale risultante**

DISTINZIONE NECESSARIA, FORMA AUTONOMA NON DIMOSTRATA; INFORMAZIONE ADIACENTE AL CORE; K-065 APERTA per la forma concreta indirizzabile.

**Collocazione v2.1**

I «Supporto, dipendenze e indipendenza»; G; H7/H8/H11/H15 e H20; O.

**Rischio di perdita o promozione indebita**

Copiare la Source in un oggetto Evidence; scambiare attribuzione per adeguatezza; eliminare il supporto perché non primitiva; introdurre enum o controllore universali d’indipendenza.

**Fonti primarie**

V1 §3.8; R2 §R2.5; R2C §T4; R4 §R4.4–R4.5; GATE §A controllo 1 e §C; REG D02–D03 e L02.

Controllo/preservazione successiva: K-054, K-065, K-101–K-104, K-159.

### Documento / document identity

**Ipotesi / forma iniziale**

V1 §4.4.2 raggruppa copie, versioni e rappresentazioni sotto Document identity reconciliation. R2 domanda se occorra un’identità documentale distinta dalle Source.

**Problema che cercava di rappresentare**

Parlare dello stesso documento attraverso PDF, stampa fotografata e allegato, distinguendolo da un documento che lo rettifica.

**Stress e contraddizioni**

R2/R5 esercitano più immagini per documento, due ricevute in una foto, frammenti di due documenti e D2 che corregge D1. Uguali byte, raggruppamento operativo e identità dell’atto documentale sono prove di natura diversa.

**Alternative considerate**

R5 confronta documento sempre Referent, concetto documentale separato, nessun oggetto documento e possibile Referent documentale. Il primo anticipa identità, il secondo rischia di duplicarla, il terzo la rende implicita proprio quando deve essere sostenuta.

**Conclusione acquisita**

Documento può essere Referent quando occorre mantenerne identità indipendente ed esiste una base pertinente. Quattro problemi restano separati: dedup tecnica, grouping/composition della rappresentazione, coreferenza documentale, versione/correzione secondo Domain. Non c’è rapporto Source–documento 1:1.

**Stato strutturale risultante**

FORMA CANDIDATA K-029 come Referent documentale; distinzione documentale necessaria, nessuna primitiva universale. Criteri specifici K-142 APERTI.

**Collocazione v2.1**

I «Documenti e rappresentazioni»; H3, H7, H8, H9/H10 e H16 nei rispettivi confini; J; O.

**Rischio di perdita o promozione indebita**

Creare un documento per ogni file o bundle; cancellare le rappresentazioni dopo coreferenza; imporre che ogni rettifica mantenga o cambi identità secondo una legge universale.

**Fonti primarie**

V1 §4.4.2; R2 §R2.1–R2.2; R2C §T5; R5 §R5.2, §R5.9 e «Document Identity Reconciliation»; AUDIT §B 25b; REG L06. EG-01 già noto: per K-133 il rinvio corretto è 25b, non 25h.

Controllo/preservazione successiva: K-028–K-032, K-127, K-133, K-142.

### Derivation

**Ipotesi / forma iniziale**

V1 la elenca tra le forme candidate e come meccanismo §4.4.7; il nome mescola facilmente attività e risultato. R2C dichiara NON TESTATO il suo statuto di primitiva nel Round 2.

**Problema che cercava di rappresentare**

Distinguere una conclusione ottenuta da premesse/regole da una lettura diretta, preservandone giustificazione e limiti.

**Stress e contraddizioni**

R3: scadenza trascorsa non significa non pagato; nessuna conferma conosciuta è un riscontro limitato; previsione da cadenza non è fatto osservato. R5 non ne fa un nuovo test centrale. GATE corregge R6: «Policy decide se applicare una derivazione» confonde applicabilità semantica e comportamento.

**Alternative considerate**

R3 separa attività, conclusione e giustificazione e distingue calcolo richiesto, uso decisionale e conservazione. R5 verifica e respinge l’assorbimento della struttura inferenziale in sole Assertion; GATE separa validità semantica, esecuzione opzionale e usi autorizzati.

**Conclusione acquisita**

Domain/Core e regole inferenziali determinano applicabilità; Derivation produce conclusione e Lineage; Policy governa automazione, materializzazione e usi, non la validità. Basi materialmente usate per Decision/spiegazioni restano recuperabili senza conservare ogni calcolo. Materializzare non crea supporto indipendente.

**Stato strutturale risultante**

Meccanismo di ragionamento con conclusione informativa e giustificazione adiacente; DISTINZIONE NECESSARIA, FORMA AUTONOMA NON DIMOSTRATA per un unico oggetto Derivation.

**Collocazione v2.1**

D; H11; G Lineage; I «Derivation record / justification»; E per gli usi.

**Rischio di perdita o promozione indebita**

Attribuire al Round 2 un test non avvenuto; trattare output derivato come Observation; fare della Policy l’arbitro della validità; cambiare natura al risultato perché usato da una Decision.

**Fonti primarie**

V1 §3.5 e §4.4.7; R2C §2; R3 §R3.4; R5 §R5.6 e Delta §I; R6 §V.8; GATE §A controllo 3, §C; AUDIT §B 25g.

Controllo/preservazione successiva: K-075–K-076, K-109, K-130, K-154→K-162.

### Decision / Disposition / Application

**Ipotesi / forma iniziale**

V1 distingue policies, loro valutazione, Verification Decision e Admission, ma non rende sempre inequivoci scelta, disposizione e applicazione. R1 esplicita questi tre ruoli.

**Problema che cercava di rappresentare**

Ricordare chi ha autorizzato che cosa, con quali basi e scope, e se l’effetto sia stato realmente applicato.

**Stress e contraddizioni**

R1/R3: una Disposition può essere autorizzata quando nasce e non applicabile quando eseguita; una conferma tardiva resta riferita alla domanda originaria. Controllare condizioni già stabilite non è automaticamente scegliere di nuovo. REG D06 rileva che l’ownership dei percorsi non-Policy non è completamente specificata.

**Alternative considerate**

R1 distingue Policy Evaluation, decisione esplicita autorizzata e continuazione di una decisione esistente. Propone il responsabile del flusso Function/Verification per formalizzare i casi non-Policy; il percorso successivo non ne consolida un contratto completo. Non si cancella quella proposta storica, ma K-185 supera la sua sufficienza.

**Conclusione acquisita**

Decision conserva scelta motivata, origine, autorità, target, scope e contesto; Disposition il trattamento autorizzato; Application l’effetto e il suo esito. Decision può avere origine Policy o non-Policy. Esattezza fattuale, conformità procedurale e autorizzazione restano giudizi diversi. Applicabilità non implica una nuova Decision; effetto già applicato e storia non si duplicano.

**Stato strutturale risultante**

GOVERNANCE / PROCESSO, NON PRIMITIVA INFORMATIVA. Distinzione forte; ownership D06/K-185 APERTA, non nuovo Decision Manager.

**Collocazione v2.1**

E; F; H14/H15/H16/H19; G memoria di governo; O C01 e C07/D06.

**Rischio di perdita o promozione indebita**

Attribuire automaticamente l’ownership a Intake; usare una conferma abilitante come supporto universale; rieseguire un effetto già applicato; chiudere D06 con un nome di componente.

**Fonti primarie**

V1 §4.6–4.8; R1 §R6; R2 §R2.5; R3 §R3.10; R4 §R4.2; R6 §V.9; REG §B1 D06.

Controllo/preservazione successiva: K-015–K-019, K-038–K-039, K-094–K-095, K-017→K-185.

### Work

**Ipotesi / forma iniziale**

V1 ha lifecycle tecnico, orchestrazione e verifica, ma non un’unità operativa uniforme. R1 distingue lavoro, tentativo, accadimento e risultato; non ne dimostra quattro primitive.

**Problema che cercava di rappresentare**

Ritrovare dopo interruzione o attesa obiettivo, perimetro, presupposti, risultati disponibili e responsabilità di continuazione.

**Stress e contraddizioni**

R2: OCR produce 22 pagine su 40, poi fallisce; una verifica attende due settimane. Fallimento di Attempt non cancella Observation riuscite. Solo eventi/provenance nascondono la continuità dell’obiettivo invece di eliminarne il bisogno. Work in attesa non è informazione sul mondo.

**Alternative considerate**

R1 confronta lifecycle centrale e lifecycle locali. R2 confronta Work/Attempt autonomi, Work con cronologia, soli eventi e ibrido minimo. Preferisce quest’ultimo: lavoro riconoscibile, tentativi distinguibili quando necessario, risultati nelle proprie forme.

**Conclusione acquisita**

Work durevole quando serve riprendere, attendere, verificare o spiegare. Attempt, attesa e risultato possono restarne aspetti. Non ogni attività crea un Work; il medesimo obiettivo può avere tentativi diversi, mentre una rivalutazione sotto presupposti diversi può richiedere lavoro collegato. Le proposte informative sopravvivono senza Work attivo.

**Stato strutturale risultante**

GOVERNANCE / PROCESSO, NON PRIMITIVA INFORMATIVA; FORMA CANDIDATA K-012. Continuità operativa necessaria, granularità e forma concrete APERTE.

**Collocazione v2.1**

F; G memoria operativa; I/O; H15 per verifica.

**Rischio di perdita o promozione indebita**

Creare un workflow engine universale, un Work per ogni trasformazione o per ogni Source; contenere tutta la proposal memory nel Work; far provare al suo stato il mancato pagamento.

**Fonti primarie**

V1 §1.5, §4.7, §6.5; R1 §R5; R2 §R2.6; R2C §9–10; R5 §R5.10; R6 §V.9.

Controllo/preservazione successiva: K-011–K-013, K-026, K-042–K-043, K-062, K-144.

### Subject / soggetto e Property / attributo

**Ipotesi / forma iniziale**

V1 §3.5 usa Subject e Property/Relation nella grammatica candidata; il soggetto può sembrare la cosa esterna e l’attributo un valore direttamente appeso ad essa.

**Problema che cercava di rappresentare**

Esprimere di chi si parla e quale contenuto viene attribuito, senza scambiare valore, endpoint e qualificazione epistemica.

**Stress e contraddizioni**

R2C: la cifra di una foto con due scontrini non ha ancora soggetto determinato. R5 distingue relazione tra Referent, attribuzione di Value e qualificazione del contenuto; avere endpoint non basta per ricondurre tutte queste forme alla stessa natura. R6 include soggetti ipotetici e pianificati.

**Alternative considerate**

R5 §R5.8 confronta l’uso di relazioni descrittive, valori e qualificazioni senza duplicare il regime epistemico delle proprietà. R6 separa soggetto del discorso e locus interno; non introduce una coppia di primitive Subject/Referent.

**Conclusione acquisita**

Subjecthood designa il ruolo di ciò di cui si parla; il Referent ne è il locus interno. Property e relazione descrittiva hanno significato Domain e possono entrare nel contenuto proposizionale. Una qualità del supporto riguarda invece il target epistemico, non automaticamente il soggetto. Non è stata dimostrata l’autonomia di Subject o Property.

**Stato strutturale risultante**

DISTINZIONE NECESSARIA, FORMA AUTONOMA NON DIMOSTRATA. Questa scheda accosta due ruoli storici, non li fonde in un nuovo concetto.

**Collocazione v2.1**

I «Referent, Assertion e commitment» e «Value»; G Domain; H7; J.

**Rischio di perdita o promozione indebita**

Duplicare il Referent in Subject; far esistere il soggetto perché nominato; trasferire la confidenza della lettura alla proprietà del mondo; rimuovere il ruolo semantico lasciando solo il valore.

**Fonti primarie**

V1 §3.5; R2C §3; R5 §R5.1 e §R5.8; R6 §V.1–3.

Controllo/preservazione successiva: K-055–K-058, K-132, K-143.

### Validity / qualificazioni temporali

**Ipotesi / forma iniziale**

V1 presenta Validity tra le forme candidate; R2C rafforza la distinzione di ruoli temporali ma dichiara non verificato il modello generale di validità.

**Problema che cercava di rappresentare**

Distinguere quando vale il contenuto, quando Fold lo riceve o valuta e rispetto a quale momento lo usa.

**Stress e contraddizioni**

R3 separa periodo fatturato, emissione, ricezione, interpretazione, Admission e reference time. Una data disponibile non sostituisce una data ignota. Assenza di fine non prova durata infinita; un periodo documentato non dimostra continuità. Cambiamento di Policy non riscrive il periodo del fatto.

**Alternative considerate**

R3 §R3.2 confronta validità come intervallo di verità e come intervallo di utilizzabilità per Fold. Entrambe diventano fuorvianti se universali; vengono mantenuti ruoli temporali e applicabilità qualificati per bersaglio.

**Conclusione acquisita**

Temporalità del contenuto, storia epistemica, storia operativa, pertinenza d’uso e reference time restano distinti. Precisione e limiti si conservano; la semantica Domain sostiene continuità e confrontabilità. Nessuna Validity unica per verità, ammissione e utilizzabilità.

**Stato strutturale risultante**

RESPINTA COME SUPER-PRIMITIVA / CONTENITORE UNIVERSALE; qualificazioni necessarie. Forme concrete e criteri specifici K-096 APERTI.

**Collocazione v2.1**

I «Tempo»; H10/H12; E/F/G; O.

**Rischio di perdita o promozione indebita**

Trasformare il superamento di Validity in eliminazione del tempo; leggere la data più recente come stato corrente; assegnare durata illimitata a un contenuto senza fine nota.

**Fonti primarie**

V1 §3.5 e §4.4.4; R2C §2; R3 §R3.1–R3.3; R5 «Identità e tempo»; R6 §V.6; REG L04.

Controllo/preservazione successiva: K-067–K-071, K-069→K-070, K-096.

### Knowledge State

**Ipotesi / forma iniziale**

V1 §4.8 raccoglie accepted, provisional, contested, rejected, superseded e corrected; Candidate/Verification aggiungono incompletezza e pending.

**Problema che cercava di rappresentare**

Mostrare che cosa Fold può sostenere, che cosa manca e quale verifica o transizione sia in corso.

**Stress e contraddizioni**

R2C mostra la coesistenza di Source conservata, importo determinato, data ambigua, verifica aperta e ammissione parziale. Non sono passi di una state machine dello stesso oggetto. R4/R5 aggiungono separazione fra qualità, conflitto, Admission e merge operativo.

**Alternative considerate**

Stato globale o piccola partizione epistemico/operativo/decisionale contro qualificazioni locali con target; R2C avverte che anche tre assi prefissati possono perdere determinazione semantica e posizione di ammissione.

**Conclusione acquisita**

La funzione del contenitore unitario viene decomposta: completezza/alternative dell’Interpretation Result, assessment epistemici, posizione di Admission, storia della Decision e stato del Work. Ammesso non significa vero e verifica pending non è una proprietà della Source.

**Stato strutturale risultante**

RESPINTA COME SUPER-PRIMITIVA / CONTENITORE UNIVERSALE. K-060 SUPERATA da K-061, senza nuovo stato universale STALE.

**Collocazione v2.1**

D/E/F; I qualificazioni, Quality e proposte; G memorie separate.

**Rischio di perdita o promozione indebita**

Reintrodurre un unico enum di conoscenza; distribuire la stessa incertezza a ogni campo; confondere stato Work con qualità dell’Assertion.

**Fonti primarie**

V1 §3.5 e §4.8; R2C §6; R4 §R4.1–R4.2; R5 §R5.5 e Delta §I; REG L03.

Controllo/preservazione successiva: K-060→K-061, K-097–K-099.

### Current State / Current Reconstruction

**Ipotesi / forma iniziale**

V1 §4.4.8 chiama Current-state derivation la ricostruzione dello stato corrente, suggerendo che ogni risposta sia una nuova conclusione derivata.

**Problema che cercava di rappresentare**

Rispondere rispetto a soggetto, domanda, scope e reference time senza cancellare storia, conflitti e limiti.

**Stress e contraddizioni**

R3 distingue selezionare contenuti pertinenti dal produrre una nuova proposizione. «Ciò che Fold sosteneva allora» non equivale al passato ricostruito oggi con nuove conoscenze. GATE impone di considerare un impatto noto anche se la rivalutazione è rinviata.

**Alternative considerate**

Current-state sempre derivativo contro ricostruzione contestualizzata che seleziona/compara e, solo se necessario, deriva. La forma del risultato può restare effimera o essere recuperabile secondo il suo uso materiale, senza diventare automaticamente Knowledge.

**Conclusione acquisita**

Responsabilità di Current Reconstruction acquisita; tiene espliciti domanda, tempo, scope, basi e qualificazioni. Un risultato usato materialmente per decidere o spiegare deve essere recuperabile insieme alle basi; non cambia natura. La materializzazione e l’Admission sono distinte.

**Stato strutturale risultante**

Responsabilità K-073 STABILE; FORMA CANDIDATA del risultato. Non nuova primitiva CurrentState; C03/C06 restano APERTE.

**Collocazione v2.1**

D/E; H12; H17/H18/H20 utilizzatori; I/O.

**Rischio di perdita o promozione indebita**

Dedurre tutto dall’ultimo dato; ammettere implicitamente una vista; omettere impatti noti; leggere FORMA CANDIDATA come facoltatività della responsabilità.

**Fonti primarie**

V1 §4.4.8; R3 §R3.3–R3.4; GATE §A controllo 2 e §C; AUDIT §B 25h; REG L05. EG-01 già noto: K-072/K-073 rinviano impropriamente a 25g.

Controllo/preservazione successiva: K-072→K-073, K-074–K-075, K-109, K-161.

### Expectation / temporal attention

**Ipotesi / forma iniziale**

Il bisogno di scadenze e promemoria esiste in V1; R3 formula esplicitamente Expectation come possibile forma per qualcosa atteso ma non riscontrato.

**Problema che cercava di rappresentare**

Consentire attenzione pertinente anche senza una nuova Source, mantenendo la ragione per attendersi qualcosa e il limite del controllo effettuato.

**Stress e contraddizioni**

R3 distingue previsione da sei bollette, scadenza esplicita della revisione auto e manutenzione raccomandata. Una pagina illeggibile può contenere il documento atteso: non riconosciuto ≠ non arrivato. Tempo trascorso non è osservazione di mancato pagamento.

**Alternative considerate**

R3 §R3.7 confronta primitiva Expectation, Assertion inferita, risultato operativo, regola Domain/Policy e composizione minima E. Le forme singole perdono base informativa o fondono significato e comportamento.

**Conclusione acquisita**

Base dell’attesa, condizioni/finestra, riscontro delimitato e comportamento restano distinguibili. Derivation può produrre previsione, Query verificare, Policy scegliere attenzione e Function presentare. Work mantiene la prosecuzione autorizzata, non la base epistemica. L’obbligo di attenzione autonoma dipende dalla promessa della funzione.

**Stato strutturale risultante**

FORMA CANDIDATA della composizione K-080; non dimostrate primitiva Expectation e responsabilità Temporal Controller universali. C02 rimane APERTURA, non una nuova teoria del conflitto predittivo.

**Collocazione v2.1**

D «Attenzione temporale»; F; H10/H11/H17/H14/H19; I «Tempo»; O C02.

**Rischio di perdita o promozione indebita**

Reintrodurre un manager universale; far dipendere l’attesa solo da Work; assumere conflitto fra previsione e ricerca negativa; far provare l’assenza nel mondo a un corpus incompleto.

**Fonti primarie**

V1 §4.4.4 e §5.3; R3 §R3.6–R3.7; R6 §V.7–8.

Controllo/preservazione successiva: K-077–K-081, K-096, K-147–K-149; delta Δ01/C02.

### Logical Document

**Ipotesi / forma iniziale**

R2 §R2.1 introduce il nome per non dipendere dalla singola Source quando più fotografie sembrano rappresentare un documento.

**Problema che cercava di rappresentare**

Preservare unità documentale e composizione senza imporre una corrispondenza con file o acquisizione.

**Stress e contraddizioni**

R2C: tre immagini elaborate insieme possono rappresentare scontrino, garanzia e prodotto, non un documento unico. Richiamare un raggruppamento indipendentemente dalle Source non prova subjecthood. R5 verifica documenti con rappresentazioni multiple.

**Alternative considerate**

R2 confronta documento come Referent, composizione interna, sole relazioni fra Source e grouping operativo. R2C restringe il criterio del possibile Referent; R5 respinge l’obbligatorietà di una radice documentale.

**Conclusione acquisita**

Il problema sopravvive in rappresentazioni/porzioni, composizione interpretativa e possibile Referent documentale. Logical Document non diventa una natura obbligatoria fra Source e Assertion, né requisito preliminare dell’Observation.

**Stato strutturale risultante**

RESPINTA COME SUPER-PRIMITIVA / CONTENITORE UNIVERSALE; possibile Referent documentale CANDIDATO. Scheda del nome storico, non secondo oggetto oltre «Documento».

**Collocazione v2.1**

H7/H8; I «Documenti e rappresentazioni»; G/O.

**Rischio di perdita o promozione indebita**

Trasformare grouping tecnico in identità documentale; eliminare l’identità perché il nome è respinto; imporre una segmentazione completa prima di leggere.

**Fonti primarie**

R2 §R2.1; R2C §T5 e §7; R5 §R5.2 e §R5.9; R6 §III.9.

Controllo/preservazione successiva: K-029, K-030–K-032, K-133.

### Source Portion / locator

**Ipotesi / forma iniziale**

R2 §R2.2 richiede porzioni per rappresentazioni molti-a-molti. R2C verifica se Source Portion debba essere oggetto autonomo.

**Problema che cercava di rappresentare**

Individuare il materiale pertinente a una lettura o supporto anche quando i confini documentali sono irrisolti.

**Stress e contraddizioni**

Regione superiore della foto, parte dello scontrino e totale dovuto sono localizzazione, interpretazione documentale e significato diversi. Un’immagine trasformata richiede anche il percorso verso la rappresentazione di origine.

**Alternative considerate**

R2C confronta oggetto Core, informazione di Provenance, locator/anchor, elemento documentale e combinazione minima. Provenance da sola non localizza; identità documentale da sola presume troppo.

**Conclusione acquisita**

Riferimento localizzato a Source/rappresentazione, collegato alle trasformazioni pertinenti. Può riferire pagina, regione, intervallo o sequenza; porzioni possono sovrapporsi ed essere incomplete. Non occorre promuoverle a Referent o primitiva.

**Stato strutturale risultante**

DISTINZIONE NECESSARIA, FORMA AUTONOMA NON DIMOSTRATA; locator CANDIDATO, forma/confini K-032 APERTI.

**Collocazione v2.1**

D; G; H5/H7; I «Locator / anchor» e «Documenti e rappresentazioni»; O.

**Rischio di perdita o promozione indebita**

Ancorare l’Observation a un documento ancora non identificato; confondere rappresenta con part_of; imporre un’entità per ogni regione.

**Fonti primarie**

R2 §R2.2; R2C §T6; R5 §R5.9; R6 §VII.2.

Controllo/preservazione successiva: K-031–K-032, K-057.

### Human Statement / contributo attribuito

**Ipotesi / forma iniziale**

V1 Feedback Handler riceve correzioni e conferme; R2 distingue dichiarazione umana, nuova informazione e autorizzazione. Il nome Human Statement è candidato per la base ricevuta.

**Problema che cercava di rappresentare**

Preservare ciò che l’utente ha effettivamente detto e su quale domanda, distinguendolo dalla formulazione ricavata da Fold.

**Stress e contraddizioni**

«Sì» può confermare una lettura o autorizzare un link. «Ho pagato» può essere testimonianza senza documento, ma non riscontro indipendente. GATE: utente, ricevuta e movimento hanno attribuzioni e contenuti non automaticamente identici. REG D01 rileva la perdita della base originaria nell’assemblaggio.

**Alternative considerate**

R2 considera ogni contributo deliberato come Source, Human Statement/Evidence distinto e Source come qualunque origine. R2C distingue contenuto d’origine e ruolo; GATE generalizza l’attribuzione anche a Source, documento o sistema senza primitiva specificamente umana.

**Conclusione acquisita**

Contributo attribuito collega contenuto, origine/contributore e contesto; la base umana effettivamente ricevuta resta recuperabile. Attribuzione non garantisce supporto adeguato, indipendenza o autorità d’azione. Persona rappresentata, account/attore e autorità concreta restano distinti.

**Stato strutturale risultante**

INFORMAZIONE ADIACENTE AL CORE; distinzione forte. Indirizzabilità quando richiesta da qualifiche/contestazioni non impone una primitiva HumanStatement.

**Collocazione v2.1**

H22; D/E; G; I «Contributo attribuito»; H15/H20.

**Rischio di perdita o promozione indebita**

Sostituire la risposta con la sola Assertion interpretata; far confermare a un «sì» l’intero documento; trasferire l’autorità dell’account a ogni proposizione.

**Fonti primarie**

V1 §5.6 e §6.2; R2 §R2.4–R2.5; R2C §T1 e §7; GATE §A controllo 1; REG D01.

Controllo/preservazione successiva: K-035–K-039, K-049, K-158–K-159, K-178–K-179.

### Interpretation Result / Bundle

**Ipotesi / forma iniziale**

V1 Interpretation Coordinator produce Candidate Knowledge Bundle. R1 lo rilegge come composizione semantica; R2 usa bundle con Candidate indirizzabili.

**Problema che cercava di rappresentare**

Conservare insieme contesto, alternative, risultati determinati, parti mancanti e dipendenze, senza trasferire loro uno stato comune.

**Stress e contraddizioni**

Importo riuscito, data ambigua e attribuzione irrisolta non giustificano né Admission atomica né perdita di tutto il risultato. R2C §7 colloca ancora Bundle come NON CORE OPERATIVO per il raggruppamento; R5/R6 chiariscono la memoria informativa delle proposte anche senza Work.

**Alternative considerate**

R2 §R2.9 confronta bundle unico parziale, Candidate separati, bundle di contesto con elementi indirizzabili e soli campi con confidenza. R2C/R5 preferiscono composizione contestuale e proposte con natura distinta; il solo campo grezzo perde ragioni e dipendenze.

**Conclusione acquisita**

Interpretation Result è forma candidata per alternative/incompletezza; Bundle non è documento, Work né unità atomica d’ammissione. La successiva collocazione informativa non va retrodatata alla classificazione del grouping in R2C. Capacità interne e successi parziali non obbligano a scindere H7.

**Stato strutturale risultante**

FORMA CANDIDATA K-053, INFORMAZIONE ADIACENTE AL CORE. Recuperabilità pre-Admission K-144 STABILE; forma concreta e C04 APERTE.

**Collocazione v2.1**

D; G memoria delle proposte; H7; I/O.

**Rischio di perdita o promozione indebita**

Far vivere tutte le proposte soltanto nel Work; trattare tutte le alternative come fatti congiunti; trasformare C04 in scissione obbligatoria o nuovo contenitore universale.

**Fonti primarie**

V1 §3.9; R1 §R4; R2 §R2.9; R2C §T3, §7, §10.2; R5 §R5.10; R6 §V.1–2 e §VII.2; REG L10.

Controllo/preservazione successiva: K-010, K-052–K-053, K-119, K-144, K-151; delta C04.

### Attempt

**Ipotesi / forma iniziale**

R1 §R5 introduce la distinzione tra lavoro durevole e sue esecuzioni; R2 verifica se il tentativo debba essere autonomo.

**Problema che cercava di rappresentare**

Attribuire risultati, interruzioni ed errori a una specifica esecuzione senza perdere la continuità del lavoro.

**Stress e contraddizioni**

Il primo OCR produce 22 pagine, il secondo altre 18 e una lettura diversa di una pagina precedente. «Secondo tentativo riuscito» non autorizza a sovrascrivere indiscriminatamente il primo.

**Alternative considerate**

R2 confronta Attempt autonomi e cronologia interna al Work, adottando l’ibrido minimo con tentativi localmente distinguibili. Non è dimostrata un’entità indipendente per ogni tentativo.

**Conclusione acquisita**

Tentativi distinguibili nella storia del Work e indirizzabili nel contesto quando necessari per Decision/spiegazione; output e loro qualità mantengono natura e storia. Retry operativo non equivale automaticamente a rivalutazione semantica.

**Stato strutturale risultante**

GOVERNANCE / PROCESSO, NON PRIMITIVA INFORMATIVA; forma/autonomia concrete APERTE.

**Collocazione v2.1**

F; G memoria operativa; I/O in relazione al Work.

**Rischio di perdita o promozione indebita**

Confondere Work fallito con invalidità di ogni risultato; trasformare ogni esecuzione in primitiva; conteggiare riletture come nuove fonti indipendenti.

**Fonti primarie**

R1 §R5; R2 §R2.6; R2C §7 e §9; R6 §V.9.

Controllo/preservazione successiva: K-011–K-013, K-026, K-042–K-043.

### Event / Reception

**Ipotesi / forma iniziale**

V1 registra evento di acquisizione e lifecycle tecnico; R1/R2 separano ricezione, lavoro di acquisizione ed esito.

**Problema che cercava di rappresentare**

Conservare che una consegna è avvenuta, anche quando elaborazione o presa in carico falliscono.

**Stress e contraddizioni**

Un file viene ricevuto e preservato ma non è processabile; un OCR fallisce dopo acquisizione riuscita. Non si può rendere «fallito» retroattivamente l’accadimento di ricezione o dedurne assenza del materiale.

**Alternative considerate**

R2 considera unico concetto con molti stati, separazione ricezione/lavoro ed eliminazione dell’accadimento a favore dello stato corrente. La separazione preserva la consegna; Event generale non è necessario per registrarla.

**Conclusione acquisita**

Reception è fatto di Provenance del percorso; Acquisition Work ha esito e stato propri. Segnalare un cambiamento e reagirvi sono relazioni diverse, non prova di un sistema universale di eventi. Un risultato negativo o positivo conserva la propria natura senza involucro Result obbligatorio.

**Stato strutturale risultante**

INFORMAZIONE ADIACENTE AL CORE per la ricezione; Event/Result universali NON SOSTENUTI come primitive. Grammatica emissione/reazione K-006 CANDIDATA.

**Collocazione v2.1**

H1; F/G; J; O F2d.

**Rischio di perdita o promozione indebita**

Introdurre un event engine; trasformare ricezione in documento o fatto di dominio; assegnare implicitamente il produttore di ogni cambiamento di versione.

**Fonti primarie**

V1 §1.2 e §6.5; R1 §R2 e §R5; R2 §R2.6–R2.7; R2C §7; REG D07.

Controllo/preservazione successiva: K-006, K-011, K-041–K-042, K-063, K-187.

### Verification

**Ipotesi / forma iniziale**

V1 §3.5 menziona Verification fra forme candidate e §4.7 la realizza come workflow che raccoglie conferme e produce Verification Decision.

**Problema che cercava di rappresentare**

Ottenere un contributo o controllo mirato senza confondere ciò che è stato verificato con l’intero contenuto o con una scelta operativa.

**Stress e contraddizioni**

R2: confermare lettura, ruolo, link, fatto nuovo e autorizzazione sono cinque casi diversi. R3: la risposta arriva due settimane dopo su basi cambiate. L’attesa appartiene al Work; il contributo può avere valore informativo nel suo scope anche se non abilita più l’effetto previsto.

**Alternative considerate**

R1 separa flusso e formalizzazione della decisione; R2/R2C sostituiscono conferma globale con target/aspetto e distinguono workflow, contributo e autorità. R4 lascia aperto se una conferma di lettura produca nuova Observation qualificata o supporto alla lettura esistente.

**Conclusione acquisita**

Verification organizza domanda/contributo e conserva contesto mostrato, risposta, scope e storia; le valutazioni pertinenti restano distinguibili. Non crea verità globale e non è una primitiva informativa soltanto perché il processo deve essere tracciato.

**Stato strutturale risultante**

GOVERNANCE / PROCESSO, NON PRIMITIVA INFORMATIVA; contributi e valutazioni adiacenti. C01, K-119 e D06 restano APERTI.

**Collocazione v2.1**

F; H15/H22; E; G; O.

**Rischio di perdita o promozione indebita**

Usare una conferma come supporto universale; chiudere il contratto di ripresa tardiva per supposizione; attribuire automaticamente ogni Decision non-Policy al workflow.

**Fonti primarie**

V1 §3.5 e §4.7; R1 §R6; R2 §R2.4–R2.5; R2C §8.12; R3 §R3.10; R4 §R4.2; REG D06.

Controllo/preservazione successiva: K-035–K-039, K-046, K-095, K-119, K-185.

### Admission

**Ipotesi / forma iniziale**

V1 §4.8 separa produzione del candidato e accettazione, ma raccoglie anche state management. R1 precisa il confine verso Policy e applicazione.

**Problema che cercava di rappresentare**

Rendere esplicito il commitment assunto da Fold senza riscrivere contenuto, origini o qualità.

**Stress e contraddizioni**

Una Disposition può non essere più applicabile; una proposta completa può restare non ammessa; un Referent proposto può esistere prima del suo riconoscimento. GATE mostra che accettare P non rende Fold autore del contributo che presenta P.

**Alternative considerate**

R1 considera decisione Policy, autorità esplicita e continuazione autorizzata; respinge Admission come secondo decisore implicito. R5/R6 confrontano Knowledge limitata alle Assertion con target referenziali e proposizionali più substrato raggiungibile.

**Conclusione acquisita**

Admission applica una disposizione pertinente e può verificarne condizioni/invarianti, motivando mancata applicazione senza inventare una nuova scelta. Introduce commitment, non paternità, verità o incremento di Quality. Il modello corrente dei target primari Referent/Assertion resta candidato; conservare Source o supporto non è ammetterlo come fatto.

**Stato strutturale risultante**

GOVERNANCE / PROCESSO, NON PRIMITIVA INFORMATIVA; assetto K-146 CANDIDATO; K-145 APERTA per il Referent senza Assertion già ammessa.

**Collocazione v2.1**

E; H16; I/O.

**Rischio di perdita o promozione indebita**

Scambiare controllo di applicabilità per nuova Decision; dedurre usabilità universale; richiedere retroattivamente Assertion ammessa per la semplice esistenza di ogni Referent proposto.

**Fonti primarie**

V1 §4.8; R1 §R6; R2C §8.14; R5 §R5.11; R6 §V.1–2; GATE §A controllo 1.

Controllo/preservazione successiva: K-015–K-019, K-137→K-144, K-145–K-146, K-158.

### Policy

**Ipotesi / forma iniziale**

V1 introduce Application Decision Policies come risorsa trasversale e Policy Evaluation come attività; non sono una forma della realtà rappresentata.

**Problema che cercava di rappresentare**

Selezionare il comportamento autorizzato fra alternative semanticamente ammissibili, con prudenza e automazione appropriate.

**Stress e contraddizioni**

R3: una nuova Policy non riscrive le dichiarazioni precedenti; R4 separa regole composte. R6 usa due formule troppo larghe: ignorare l’impatto e applicare/non applicare una derivazione. GATE le corregge: impatto determinato non occultabile e applicabilità inferenziale non decisa dalla Policy.

**Alternative considerate**

Separazione Domain/Core/meccanismi/Quality/Policy contro contenitore unico di regole; decisioni Policy e autorità esplicita contro passaggio obbligatorio da Policy Evaluation.

**Conclusione acquisita**

Risorsa di criteri comportamentali distinta dalla valutazione e dalla Decision del caso. Può autorizzare verifica, automazione, rivalutazione e usi, non verità, indipendenza, validità semantica o soppressione di qualificazioni. Un obbligo contrattuale conosciuto non è una Policy di Fold.

**Stato strutturale risultante**

GOVERNANCE / PROCESSO, NON PRIMITIVA INFORMATIVA per il ruolo decisionale; risorsa di riferimento, non attore autonomo. Regole concrete non decise qui.

**Collocazione v2.1**

G; E; H14; I modalità; O.

**Rischio di perdita o promozione indebita**

Riutilizzare letteralmente le due formule R6 superate; collocare qui i Core invariants o tutta la semantica Domain; far credere che solo Policy possa originare Decision.

**Fonti primarie**

V1 §4.5–4.6; R1 §R6; R3 §R3.9; R4 §R4.10; R6 §V.8–9; GATE §A controlli 2–3 e §C.

Controllo/preservazione successiva: K-014–K-016, K-064, K-091, K-112–K-113, K-147, K-153→K-161, K-154→K-162.

### Provenance

**Ipotesi / forma iniziale**

V1 §6.1 conserva origine e contesto di acquisizione/produzione insieme alla Lineage; il disegno può suggerire un recorder centrale.

**Problema che cercava di rappresentare**

Spiegare da dove proviene un contenuto, chi lo ha fornito e in quale contesto, senza dedurne automaticamente attendibilità.

**Stress e contraddizioni**

R2C: una registrazione di ricezione non sostituisce il contenuto originale; un contributo umano richiede domanda e risposta. R4 distingue origine, dipendenze informative, storia epistemica e log operativo. Un ricostruttore successivo non può inventare dettagli mai catturati.

**Alternative considerate**

Cattura centralizzata finale contro produzione locale delle tracce e attraversamento successivo; memoria di soli eventi/provenance contro memoria operativa di obiettivi e attese.

**Conclusione acquisita**

Origine e contesto catturati dai produttori competenti, raggiungibili da Query/Explanation. Provenance non basta per supporto, indipendenza o stato Work. Se una base contribuisce materialmente a Decision/spiegazione deve essere recuperabile; solo nome di versione o log di successo non bastano.

**Stato strutturale risultante**

INFORMAZIONE ADIACENTE AL CORE; distinzione necessaria, non obbligo di primitiva o recorder centrale.

**Collocazione v2.1**

G, cattura presso i produttori; H20 attraversamento per spiegazione; I/J.

**Rischio di perdita o promozione indebita**

Confonderla con una prova di verità; sostituire Source con metadati; pretendere di ricostruire dopo ciò che non è stato preservato; conservare indiscriminatamente tutto.

**Fonti primarie**

V1 §2.9 e §6.1; R2C §T1 e §10; R4 §R4.3, §R4.6–R4.8; REG L08.

Controllo/preservazione successiva: K-049, K-062, K-075, K-093, K-105–K-110.

### Lineage

**Ipotesi / forma iniziale**

V1 §6.1 la affianca alla Provenance per seguire trasformazioni da Source a risultati. R1 porta il problema dell’autoconferma nel ciclo Quality/Engine.

**Problema che cercava di rappresentare**

Rendere recuperabili le basi materialmente usate e distinguere dipendenza informativa da semplice successione operativa.

**Stress e contraddizioni**

R2C: DEPENDS_ON può indicare prosecuzione del lavoro o giustificazione della conclusione, non la stessa cosa. R4: copie e riuso della Knowledge non generano indipendenza; versione nominale non riproduce una definizione. R5: asserire che una derivazione esiste non ne sostituisce il percorso.

**Alternative considerate**

Grammatica universale delle dipendenze contro famiglie tipizzate; sola storia di esecuzione contro dipendenze di contenuto; archivio indiscriminato contro recuperabilità delle basi materiali.

**Conclusione acquisita**

Lineage conserva trasformazioni, premesse, metodi e risorse pertinenti; permette attraversamento e controlli locali senza controllore centrale obbligatorio. Un ciclo non legittima auto-supporto. Più percorsi non provano indipendenza e nessuna dipendenza nota non prova assenza d’impatto.

**Stato strutturale risultante**

INFORMAZIONE ADIACENTE AL CORE; distinzione forte. Forme/granularità concrete non fissate come primitive.

**Collocazione v2.1**

G e produttori pertinenti; H11/H13/H20; I supporto e J.

**Rischio di perdita o promozione indebita**

Confondere grafo attraversabile con supporto valido; conteggiare materializzazione come nuova fonte; conservare soli identificativi di versione senza basi recuperabili.

**Fonti primarie**

V1 §6.1 e §6.6; R1 §R7; R2C §11; R3 §R3.8–R3.9; R4 §R4.5–R4.8; R5 §R5.6; REG D02–D03.

Controllo/preservazione successiva: K-021, K-059, K-085–K-086, K-093, K-101–K-102, K-105–K-109.

### Impact

**Ipotesi / forma iniziale**

V1 tratta correzione, versionamento e ricalcolo; R3 rende esplicita la valutazione d’impatto di nuovi contenuti e cambiamenti di risorse.

**Problema che cercava di rappresentare**

Individuare quali risultati potrebbero perdere adeguatezza per uno scopo, senza dichiararli automaticamente falsi o rieseguirli tutti.

**Stress e contraddizioni**

R3: una nuova Source modifica il perimetro di una precedente assenza; Mapping cambiato può alterare un ruolo ma non la stringa osservata. Dipendenza non trovata non basta per escludere impatto su assenze, perimetri e continuità. GATE corregge R6, che permetteva alla Policy di «ignorare» l’impatto.

**Alternative considerate**

R3 distingue impatto potenziale, rivalutazione e risultato confermato/corretto invece di una invalidazione universale. GATE separa qualificazione informativa, decisione sui tempi e trattamento della funzione; non introduce STALE globale.

**Conclusione acquisita**

Potenziale impatto, basi messe in dubbio, rivalutazione e risultato accertato non sono sinonimi. Un impatto determinato resta recuperabile e vincola usi pertinenti anche se si rinvia il lavoro. Non occorre conoscere già la nuova conclusione per riconoscere una base in dubbio.

**Stato strutturale risultante**

INFORMAZIONE ADIACENTE AL CORE per la qualificazione, meccanismo per la valutazione e governo distinto della rivalutazione. K-087/K-161 STABILI; criteri d’uso C03 APERTI.

**Collocazione v2.1**

E; H13/H12; G/I; O C03/F2d.

**Rischio di perdita o promozione indebita**

Far diventare tutto falso o STALE; far cancellare l’impatto alla Policy; confondere rinvio e adeguatezza; risolvere C03 inventando un asse universale Admission/Usability.

**Fonti primarie**

R3 §R3.8–R3.9; R6 §V.9; GATE §A controllo 2 e §C.

Controllo/preservazione successiva: K-085–K-090, K-153→K-161; delta Δ03/Δ04/C03.

### Contenuto negativo / modalità

**Ipotesi / forma iniziale**

V1 separa scadenza superata e pagamento non provato; R2 richiede recupero negativo delimitato. R3 affronta attese, obblighi e previsioni; R6 esplicita le forme.

**Problema che cercava di rappresentare**

Esprimere assenze e contenuti non descrittivi senza trasformarli in fatti negativi universali o comandi per Fold.

**Stress e contraddizioni**

Materiale non interpretato può contenere la conferma cercata; corpus accessibile può escludere altri materiali. Una raccomandazione di manutenzione non è obbligo; intenzione di pagare non è pagamento e previsione non è riscontro.

**Alternative considerate**

R3 confronta le forme dell’attesa; R6 separa quattro forme negative e modalità del contenuto invece di introdurre NegativeInformation o una Policy che contenga tutti gli obblighi.

**Conclusione acquisita**

Distinguere negazione esplicita sostenuta, assenza osservata locale, ricerca negativa delimitata e Assertion/inferenza negativa sul mondo. Quest’ultima richiede basi e condizioni Domain. Contenuti descrittivi, normativi, intenzionali e predittivi mantengono modalità semantica. H17 è già produttore del risultato negativo; C02 e C05 restano aperti.

**Stato strutturale risultante**

DISTINZIONI NECESSARIE, FORME AUTONOME NON DIMOSTRATE; risultati negativi adiacenti e contenuti proposizionali qualificati, non nuova primitiva.

**Collocazione v2.1**

D; H5/H11/H17; I «Informazione negativa e modalità»; O.

**Rischio di perdita o promozione indebita**

Equiparare non trovato e non avvenuto; dichiarare assente un produttore già presente; rendere la previsione un fatto o l’obbligo una autorizzazione d’azione.

**Fonti primarie**

V1 §4.5 esempio scadenza; R2 §R2.3; R3 §R3.4 e §R3.7; R6 §II Q4–Q7 e §V.7–8.

Controllo/preservazione successiva: K-033–K-034, K-077–K-078, K-147–K-149; delta C02/C05.

### Identity Reconciliation / coreferenza

**Ipotesi / forma iniziale**

V1 §4.4.1 collega un candidato a referenti esistenti; il lessico di identità e merge può far sembrare l’unione l’esito naturale del riconoscimento.

**Problema che cercava di rappresentare**

Valutare se descrizioni diverse riguardano lo stesso soggetto senza perdere alternative, contesto o possibilità di correzione.

**Stress e contraddizioni**

R5 verifica omonimi, POD errato, identificatori di rapporti diversi e cambiamenti di proprietà. Una ipotesi same_as può essere sostenuta senza che sia autorizzato l’uso unitario; una falsa fusione distruttiva rende impossibile tornare ai soggetti distinti.

**Alternative considerate**

R5 separa proposizione di coreferenza, sostegno, autorizzazione d’uso unitario/proiezione e applicazione operativa. Valuta e respinge il merge distruttivo come conseguenza automatica e il proliferare di predicati identitari per ogni grado epistemico.

**Conclusione acquisita**

Reconciliation propone e valuta, non scopre identità infallibile. Identifier è indizio qualificato; Domain determina quale soggetto continua. Uso unitario non cancella origini e differenze: deve restare revisionabile quando l’informazione legittimamente conservata consente di distinguere. La proposta non diventa supporto indipendente di sé.

**Stato strutturale risultante**

Meccanismo di ragionamento, non primitiva. Proposizioni, assessment e decisioni restano distinti; algoritmi e criteri specifici APERTI.

**Collocazione v2.1**

H8; E/H16; I Identifier/Documenti; J; O.

**Rischio di perdita o promozione indebita**

Confondere coreferenza con merge fisico; usare un match come autorizzazione; cancellare la storia; introdurre una primitiva per ogni esito di riconciliazione.

**Fonti primarie**

V1 §4.4.1; R2C §4; R5 §R5.4–R5.5, «Identità e tempo»; R6 §IV; REG D05.

Controllo/preservazione successiva: K-124–K-129, K-138–K-141.

### Correction / Supersession / conflitto

**Ipotesi / forma iniziale**

V1 §4.4.5–4.4.6 distingue conflitto e Correction/Supersession, ma il secondo nome raccoglie riconoscimento del rapporto e revisione della Knowledge.

**Problema che cercava di rappresentare**

Preservare perché una nuova informazione cambia una ricostruzione: errore precedente, cambiamento reale, incompatibilità o apprendimento tardivo.

**Stress e contraddizioni**

R3: 84,72→34,72 può essere rettifica soltanto se riguarda lo stesso bersaglio; due fornitori in periodi diversi non sono automaticamente incompatibili. Un rapporto finito può restare vero per gennaio. La notizia tardiva di B non rende B più corrente di C né cambia quando Fold apprese A.

**Alternative considerate**

R3 confronta il contenitore indistinto superseded con quattro fenomeni separati; R6 distingue proposizione documentale «D2 corregge D1», effetto governato «B sostituisce A nella ricostruzione» e relazione storica recuperabile.

**Conclusione acquisita**

Riconoscere una rettifica non equivale ad applicarla; confronto e semantica Domain determinano pertinenza/incompatibilità, la Governance governa gli effetti. Il precedente resta nel proprio contesto. Preferire una fonte non cancella conflitto; un ranking generico non sostituisce l’analisi di una rettifica pertinente.

**Stato strutturale risultante**

DISTINZIONI NECESSARIE fra contenuti, relazioni epistemiche, tempo e GOVERNANCE; non primitiva universale Correction/Supersession.

**Collocazione v2.1**

H7/H9/H10/H12/H13 per significato e conseguenze; E/H16 per revisioni; I/J; O.

**Rischio di perdita o promozione indebita**

Sovrascrivere la storia con l’ultimo valore; trattare successione come errore; far diventare una dichiarazione di rettifica effetto già applicato; eliminare un conflitto perché una fonte è preferita.

**Fonti primarie**

V1 §4.4.5–4.4.6; R3 §R3.5; R4 §R4.4 e §R4.10; R6 §V.3; GATE §B.

Controllo/preservazione successiva: K-082–K-084, K-117, K-131, K-159–K-161.

## 4. Super-primitive e contenitori universali non sostenuti

Le dodici righe seguenti preservano il problema reale anche quando il nome perde universalità. «Rifiuto» nella tabella indica il rifiuto dell’obbligatorietà o del collasso semantico, non una dimostrazione d’impossibilità di ogni forma futura. Result/Event non erano stati provati impossibili; Assertion resta fortemente sostenuta nel proprio ambito; Quality può avere sintesi per scopo senza diventare truth scorer universale.

### Concetti / forme universali respinte

| forma | problema reale preservato | motivo del rifiuto | destinazione attuale |
|---|---|---|---|
| Relation universale uniforme | Collegare fatti, supporti, rappresentazioni, inferenze e lavoro. | R2C §4 e R5 §R5.7: una semantica unica confonde fatti, giustificazioni e autorizzazioni. Non viene vietata una futura forma tecnica comune. | Famiglie I/J; Assertion descrittive, supporto, Provenance/Lineage e piano operativo. |
| Candidate universale | Conservare proposte complete e incomplete, alternative e contesto. | R2C §T3 e R5 §R5.10: l’unico involucro non ha natura comune dimostrata; il solo stato non basta per risultati ancora indeterminati. | Proposte referenziali/proposizionali, Interpretation Result, memoria informativa e Work distinto. |
| Knowledge State unitario | Distinguere disponibilità, determinazione, qualità, ammissione e attesa. | R2C §6: sono qualificazioni su bersagli differenti, non stati successivi dello stesso oggetto. K-060 superata da K-061. | D/E/F; assessment, posizione proposta/ammessa e lifecycle operativo. |
| Validity universale | Conservare tempo, durata e pertinenza dell’uso. | R3 §R3.1–R3.2: tempo del contenuto, storia e applicabilità non sono un intervallo unico. K-069 superata da K-070. | Qualificazioni temporali, reference time, Domain e controlli di applicabilità. |
| LogicalDocument universale | Mantenere identità documentale attraverso rappresentazioni diverse. | R2C §T5 e R5 §R5.2: grouping e indirizzabilità non provano identità; una Source può rappresentare più documenti. | Possibile Referent documentale, porzioni, composizione e coreferenza distinte. |
| Expectation universale | Motivare un atteso e verificare il mancato riscontro. | R3 §R3.7: previsione, obbligo, raccomandazione e attenzione non dimostrano una natura unica obbligatoria. | Composizione candidata K-080; basi e finestre informative, Query negativa, Policy/Function e Work. |
| Temporal Controller universale | Riconoscere una condizione temporale anche senza nuovo ingresso. | R3 §R3.6: il problema dipende dal comportamento promesso; è distribuibile tra valutazione temporale, funzione e coordinamento autorizzato, senza un nuovo owner universale. | H10, funzioni pertinenti e F; K-079/K-081, non scheduler scelto. |
| Result / Event universali | Distinguere ciò che è accaduto, ciò che è prodotto e l’esito del lavoro. | R2 §R2.6–R2.7 e R2C §7/§9: i risultati hanno già nature proprie; la ricezione può essere registrata senza Event generale. Non dimostrata l’impossibilità di un futuro uso locale. | Observation, Interpretation Result e altri risultati tipizzati; Provenance della ricezione e storia Work/Attempt. |
| Quality / truth scorer universale | Valutare adeguatezza e incertezza per usi concreti. | R1 §R7 e R4 §R4.1–R4.2/§R4.9: un punteggio globale cancella target e dimensioni e può autoconfermarsi. Sintesi per scopo non è vietata se conserva le basi. | Assessment locali, risorsa Quality Model, eventuale sintesi pertinente; comportamento nella Policy. |
| Reliability globale intrinseca della Source | Valutare come una Source possa sostenere una proposizione. | R4 §R4.3–R4.5: provenienza, integrità, competenza, indipendenza e corroborazione non coincidono; una fonte competente su P non lo è automaticamente su Q. | Provenance e assessment relativi a target/supporto; nessuna affidabilità dentro la definizione di Source. |
| Assertion come super-primitiva di ogni informazione | Rappresentare unitariamente contenuti, supporti e storia. | R2C §3 e R5 §R5.6: soggetto irrisolto, materiale d’origine e struttura inferenziale non sono sostituiti da proposizioni che ne parlano. | Assertion per il contenuto; Source/Observation, supporti, Lineage e Work nelle rispettive nature. |
| STALE globale | Non usare come aggiornato ciò le cui basi sono cambiate. | R3 §R3.9 e GATE controllo 2: impatto potenziale, basi in dubbio e risultato accertato non sono uno stato universale di falsità; il rinvio non cancella l’impatto. | H13, qualificazione d’impatto, H12 e usi governati; C03 aperta. |

L’indipendenza non richiede enum/primitiva obbligatori, l’auto-supporto non richiede un controllore centrale e l’applicabilità non è automaticamente una nuova Decision: sono limiti preservati nelle schede, non ulteriori forme del Core. Ugualmente, respingere un Candidate universale non elimina proposte recuperabili; respingere Expectation non elimina attenzione temporale; respingere STALE non elimina la qualificazione d’impatto.

## 5. Aperture preservate, senza risoluzione

La tabella distingue la domanda residua dal vincolo già acquisito. Il presente documento non propone criteri aggiuntivi né considera l’omissione nominale di una domanda in una sintesi successiva prova della sua chiusura.

| Apertura / forma non definitiva | Genealogia e controllo | Ciò che resta da precisare | Ciò che non viene riaperto |
|---|---|---|---|
| Identità/equivalenza proposizionale | GATE §D; K-160 APERTA; v2.1 O | Quando formulazioni/contributi possano condividere una sola Assertion. | Default conservativo: Assertion distinte; equivalenza, compatibilità o implicazione collegate quando stabilite. Non fondere automaticamente. |
| Proposizioni su letture/interpretazioni interne | R2C §3 e §13.D; K-066 APERTA | Confine specifico delle meta-Assertion interne. | La definizione generale GATE non prova da sola una chiusura esplicita di questo caso. |
| Forma concreta del supporto indirizzabile | R2C §T4; R4 §R4.4; K-065 APERTA; O | Relazione, registrazione, autonomia e granularità nei casi pertinenti. | Target, base, attribuzione distinta, scope, qualificazioni e storia sono necessari. |
| Work e Attempt concreti | R1 §R5; R2 §R2.6; R6 §V.9; K-012 CANDIDATA, K-026 APERTA; O | Granularità, stati, ripresa, retry, condizioni di riapertura e quando un Attempt sia autonomamente indirizzabile. | Continuità operativa e risultati distinguibili non sono facoltativi quando servono. Nessun Work per ogni attività. |
| Locator e composizione | R2 §R2.1–R2.2; R2C §T6; K-032 APERTA | Individuazione manuale/automatica, confini incerti, ordine e completezza. | Localizzazione ≠ ruolo documentale ≠ ruolo semantico; nessuna segmentazione totale obbligatoria. |
| Contratti di acquisizione/verifica/ammissione parziale | R2 §R2.4–R2.9; K-046 APERTA | Successo dell’acquisizione, rifiuti/incompletezza, domande multiple e scope, regole specifiche di Admission parziale. | Ricezione, Source, risultato e stato Work sono distinti. |
| Dettagli temporali e rivalutazione | R3 Delta §G; K-096 APERTA | Forme/precisioni, continuità specifica, applicabilità/revoca concreta, riconoscimento rettifiche e politiche di rivalutazione. | K-067–K-075 preservano ruoli temporali e basi materiali. La conservazione oltre i casi necessari non diventa universale. |
| Quality e indipendenza empirica | R4 Delta §I; K-118 APERTA, K-098 CANDIDATA; O | Dimensioni dettagliate, composizione per scopo, origini parzialmente ignote, soglie concrete di automazione. | K-097/K-102: assessment contestualizzato e indipendenza non determinata legittimi; nessuno score/enum universale imposto. |
| Forma delle proposte e conferma delle Observation | R4 §R4.2 e Delta §I; R5 §R5.10; R6 §V.1–2; K-119 APERTA | Forma concreta della memoria; nuova Observation qualificata o supporto alla lettura esistente. | K-144 ha chiarito l’esistenza delle proposte nella memoria informativa senza Work o Admission: non è ancora dubbia quella necessità. |
| Identifier e criteri specifici | R5 Delta §M; R6 §V.4; K-141 APERTA; O | Forma ontologica, schemi/validità, unicità/riassegnazione Domain e politiche di auto-link. | Schema, valore e assegnazione restano distinguibili. |
| Identità/versione documentale e relazioni | R5 Delta §M; R6 §VII.9; K-142 APERTA; O | Quando rettifica sia nuovo documento/versione/rappresentazione; classificazione vs identità; vocabolario finale e indirizzabilità epistemica. | Nessun 1:1 Source/documento; coreferenza non distruttiva; famiglie semantiche non uniformi. |
| Admission di Referent senza Assertion già ammessa | R5 Delta §M; R6 §V.1–2 e §VI.C; K-145 APERTA | Criteri completi di riconoscimento nel caso specifico. | K-137 è superata da K-144 quanto all’esistenza pre-Admission; il residuo K-145 non è stato chiuso né trasformato in prerequisito universale. |
| Granularità finale dei raggruppamenti | AUDIT §H.5; K-183 APERTA; O | Forma organizzativa futura; nei suoi riflessi su risultati e memorie, non nuova genealogia dei componenti. | Distinzioni informative e responsabilità sopravvivono anche agli accorpamenti. |
| C01 — applicabilità nei rami | Delta C01; v2.1 E/F/O; basi R1 §R6 e R3 §R3.10 | Contratto uniforme di applicabilità in Verification/Work/Application, anche alla ripresa. | H16 può controllare condizioni senza nuova Decision; nessun nuovo controllore. |
| C02 — previsione e riscontro successivo | Delta C02; v2.1 I/O; R3 §R3.7 e R6 §V.7–8 | Rapporto tra base predittiva e successivo risultato negativo. | Base, finestra, riscontro e comportamento distinti; il risultato negativo non è automaticamente conflitto con la previsione né fatto non avvenuto. |
| C03 — uso di contenuti ammessi e impattati | Delta C03; GATE controllo 2; K-161 STABILE; v2.1 O | Criteri d’uso concreti per scopo e situazione. | L’impatto determinato non può essere occultato o ignorato presentando il risultato come pienamente aggiornato. |
| C04 — esiti parziali interni di Interpretation | Delta C04; v2.1 H7/O; R2C §T3 e R5 §R5.10 | Visibilità dei sub-risultati e degli esiti parziali. | Sono rappresentabili; nessuna scissione obbligatoria di H7. |
| C05 — corpus e copertura negativa | Delta C05; v2.1 H17/I/O; R2 §R2.3 e R6 §V.7 | Distinzione operativa fra corpus richiesto, accessibile, esaminato e copertura. | Produttore Query già presente; non trovato resta delimitato. |
| C06 — proposte nelle Reconstruction | Delta C06; v2.1 H12/O; R5 §R5.10–R5.11 | Criteri con cui considerare proposte non ammesse per una ricostruzione. | Conservazione, presentazione e uso pertinente non equivalgono ad Admission. |
| C07 / D06 — formalizzazione non-Policy | R1 §R6 → REG D06; K-017 SUPERATA da K-185 APERTA; delta e v2.1 O | Ownership concreta della formalizzazione della Decision/Disposition. | La proposta storica Function/Verification esisteva, ma non è contratto completo acquisito. Autorità, target, scope, contesto e storia restano obbligatori; nessun Decision Manager. |
| F2d — disponibilità del cambiamento di versione | R1 §R2; R3 §R3.9 e Delta §G; K-006 CANDIDATA, K-090 STABILE, K-096 APERTA; delta/v2.1 O | Chi rende disponibile il cambiamento alle responsabilità pertinenti. | Non viene assegnato un produttore né creato C08, event bus, scheduler o nuovo owner. |

### Collocazioni e formulazioni candidate che rimangono tali

Queste non sono nuove aperture: sono limiti già presenti nelle conclusioni e nel raccordo genealogico della candidata.

| Conoscenza / forma | Limite conservato |
|---|---|
| K-143 — definizione di Referent | Necessità del locus forte; formulazione esatta candidata, non STABILE per effetto di questa genealogia. |
| K-049/K-050 rispetto a K-148 | Definizioni Source/Observation STABILI; adiacenza alla grammatica centrale CANDIDATA. |
| K-136 e K-146 | Knowledge come corpo governato e assetto dei target primari dell’Admission restano CANDIDATI. |
| K-053 | Interpretation Result è una forma CANDIDATA; non involucro universale. |
| K-029 e K-032 | Possibile Referent documentale candidato e forma del locator/composizione aperta. |
| K-080 | Composizione dell’attesa CANDIDATA; nessuna primitiva Expectation. |
| K-098 | Numero/confini delle cinque famiglie di qualità CANDIDATI, non le differenze che impediscono lo score globale. |
| K-012 | Work durevole come forma CANDIDATA; granularità concreta aperta. |
| K-073 | Responsabilità STABILE di Current Reconstruction; forma concreta del risultato CANDIDATA nella v2.1. |
| K-006 | Grammatica emissione/reazione CANDIDATA; non architettura a eventi già scelta. |

K-004 sulla lettura qualificata CONSULTS resta proposta terminologica CANDIDATA, non divieto canonico: la genealogia delle famiglie Relation non ne decreta il superamento. K-022/K-023 e K-091 mantengono la destinazione Ledger-only prevista dal delta e da O: lifecycle/calcolo/effetti e test di parallelizzabilità, non progettazione qui della concorrenza; governance fondazionale dei Core invariants, non Application Policy runtime. K-023 rimane CANDIDATA.

Le altre aperture tecniche già esplicite in O — algoritmi di Reconciliation, formule Quality, forma software e storage — rimangono tali. Non sono pretesto per scegliere tecnologie in questa genealogia e non diventano nuove lacune fondazionali.

## 6. Matrice finale dei concetti

La matrice riassume tutte le 35 schede, nello stesso ordine. Le celle di stato sono descrittive; non assegnano un unico stato Ledger all’intero concetto, che può comprendere conoscenze di stato diverso.

| concetto | forma iniziale | stress principale | conclusione | stato strutturale risultante | collocazione v2.1 | fonti primarie |
|---|---|---|---|---|---|---|
| Referent | In V1 §3.5 è una forma candidata per il soggetto di cui si parla. | R5 esclude il criterio «qualsiasi cosa citabile»: anche una regione o un Attempt devono essere richiamabili. | La necessità referenziale è fortemente sostenuta. | PRIMITIVA FORTEMENTE SOSTENUTA quanto alla necessità del locus; FORMA CANDIDATA quanto alla definizione K-143, che supera K-120. Non è una promozione di K-143 a STABILE. | I, «Elementi e famiglie» e «Referent, Assertion e commitment»; D/E per proposta e Admission; H7/H8; O per i criteri residui. | V1 §3.5; R2C §T5, §2; R5 §R5.1; R6 §II Q1–Q3, §III.8, §V.1–2. |
| Assertion | V1 la propone per esprimere ciò che viene affermato su un soggetto, con valore, tempo ed evidenza. | R2C: una cifra in una foto con due scontrini non determina ancora una proposizione sull’importo di uno specifico documento. | Assertion è un elemento semantico indirizzabile che porta contenuto proposizionale. | PRIMITIVA FORTEMENTE SOSTENUTA, non super-primitiva. K-158 sostituisce K-155; identità/equivalenza del contenuto resta APERTURA K-160 e il caso specifico delle meta-Assertion interne resta K-066 APERTA. | I, «Referent, Assertion e commitment»; D/E; H7/H11/H16; O. | V1 §3.5; R2C §3 e §13.D; R5 §R5.6; R6 §V.3; GATE §A controllo 1, §B, §C, §D. |
| Identifier | In V1 §3.5 compare fra le forme candidate del Core, mentre il Domain fornisce schemi identificativi. | R5 esercita POD osservato ma non associato, POD stampato errato e schema con ambito non noto. | Scheme/type fornisce significato e scope Domain; value è contenuto identificativo strutturato; assignment è proposizione verso un Referent, sostenibile, temporale e correggibile. | DISTINZIONE NECESSARIA, FORMA AUTONOMA NON DIMOSTRATA; forma ontologica e criteri specifici APERTI K-141. Non tre primitive autonome. | I, «Identifier» e «Value»; G Domain/Mapping; H5/H7/H8; O. | V1 §3.4–3.5; R2C §2; R5 §R5.3 e Delta §D/§M; R6 §V.4. |
| Value | In V1 §3.5 è una forma candidata distinta da Referent e Assertion; il lessico poteva suggerire un elemento con autonomia propria. | R2C verifica 84,72 €: stesso numero non significa stessa occorrenza, obbligazione o pagamento. | Value resta necessario come forma di contenuto non referenziale. | DISTINZIONE NECESSARIA, FORMA AUTONOMA NON DIMOSTRATA. Il FORTE locale della v2.1 qualifica la distinzione, non l’autonomia ontologica. | I, «Value» e «Identifier»; H5/H7. | V1 §3.5; R2C §2, §3 «Value può essere contenuto dell’Assertion?», §5; R5 §R5.3 e §R5.8. |
| Source | V1 §1.6 riceve l’artefatto tecnicamente valido e ne preserva il contenuto. | R2C prova PDF conservato ma non processabile, fotografia, risposta «sì» e dichiarazione di pagamento. | Source è contenuto d’origine determinato e referenziabile mantenuto per ricostruire ciò che fu fornito/dichiarato. | INFORMAZIONE ADIACENTE AL CORE nella collocazione CANDIDATA K-148; definizione K-049 STABILE. Necessità del contenuto d’origine non equivale a primitiva centrale autonoma. | D; G memorie/Provenance; H1/H2/H4; I «Elementi e famiglie» e «Documenti e rappresentazioni». | V1 §1.6; R2 §R2.4 e §R2.7; R2C §T1; R4 §R4.3; R6 §V.5. |
| Observation | V1 §2.7 compone stringhe, localizzazioni e risultati estrattivi prima dell’interpretazione; la sequenza documentale può sembrare un passaggio universale. | R2C confronta fotografia e risposta strutturata: duplicare quest’ultima in un’Observation non aggiunge necessariamente una distinzione. | Risultato indirizzabile dell’osservazione di una Source con metodo, localizzazione, forma e qualità propri. | Definizione K-050 STABILE; INFORMAZIONE ADIACENTE AL CORE con collocazione K-148 CANDIDATA. Distinzione necessaria, non pedaggio universale. | D; H5 e assessment locali; G memoria delle Observation; I/O. | V1 §2.7; R2C §T2 e §2; R4 §R4.2 situazione 2; R5 §R5.3; R6 §V.5. |
| Relation | V1 §3.5 affianca Property/Relation alle forme Core; una freccia generica rischia di unire fatti del mondo, supporti e dipendenze operative. | R1 distingue produce, legge, autorizza e applica. | Relazioni descrittive come contenuto di Assertion; famiglie epistemiche, rappresentative/provenienziali, inferenziali e operative distinguibili. | RESPINTA COME SUPER-PRIMITIVA / CONTENITORE UNIVERSALE; DISTINZIONI NECESSARIE tra famiglie. Vocabolario finale e autonomia delle relazioni epistemiche restano aperti. | I e J Relation map; D/E/F per piani distinti; O. | V1 §3.5; R1 §R2; R2C §4 e §11; R5 §R5.7–R5.8; R6 §V.3; GATE §C Relation families. |
| Candidate / Proposal | V1 produce Referent Candidate e Candidate Knowledge Bundle prima di Candidate Validator/Admission; R2 usa Candidate per proposizioni, incompletezza, link e raggruppamenti. | R2C: importo determinato, ruolo della data ambiguo e utenza irrisolta non hanno un’unica maturità. | Una Assertion completa conserva il proprio contenuto prima e dopo Admission; referenti proposti e risultati interpretativi mantengono natura, alternative, supporti e dipendenze. | RESPINTA COME SUPER-PRIMITIVA / CONTENITORE UNIVERSALE. Posizione proposta necessaria; composizione Interpretation Result CANDIDATA; forme concrete ancora aperte. | D/E; G memoria informativa delle proposte; H7/H8/H16; I/O. | V1 §3.7, §3.9, §4.1; R2 §R2.9; R2C §T3 e §10.2; R5 §R5.10; R6 §V.1–2, §VI.C; REG §B2 L01. |
| Knowledge | V1 §4.9 parla di Knowledge Repository con affermazioni accettate e contesto, distinguendo la memoria candidata. | R5 mostra che il solo insieme di Assertion non basta per Referent e giustificazioni, se queste vengono forzate in una super-Assertion. | Forma candidata: Referent e Assertion ammessi con accesso recuperabile a supporti, qualificazioni, revisioni, derivazioni e storie. | FORMA CANDIDATA K-136 e assetto dei target K-146 CANDIDATA. Non nuova primitiva informativa chiamata Knowledge. | E e G memorie; H16; I «Knowledge come corpo governato»; O. | V1 §4.8–4.9; R5 §R5.11; R6 §V.2; GATE §A controllo 1 e §C Governance. |
| Quality / Quality Assessment | V1 distingue risorsa Quality Model, valutazioni estrattive/semantiche e Quality Assessment nella gestione della conoscenza; il ciclo con il Core Engine può però sembrare centrale e globalmente sintetico. | R1: leggere 84,72 perché lo si attende dalla Knowledge e poi usarlo per confermare quella Knowledge crea autoconferma. | L’assessment conserva target, dimensione, base, scopo e storia. | INFORMAZIONE ADIACENTE AL CORE; distinzione di assessment necessaria. K-097 STABILE; le cinque famiglie K-098 restano CANDIDATE nel numero/confine; formule e criteri empirici K-118 APERTI. | G Quality Model e cattura locale; assessment presso H5/H7/H8/H11 e produttori competenti; I «Quality Assessment»; E/O. | V1 §2.8, §3.10, §4.2–4.3; R1 §R7; R4 §R4.1–R4.3, §R4.5, §R4.9 e Delta §I; REG §B2 L07. |
| Evidence / supporto | V1 §3.8 presenta Evidence Construction e Evidence tra le forme del Core. | Una conferma della lettura 34,72 non conferma il debito; una conferma del link non sostiene tutti i campi. | Necessario il supporto qualificato, con base, target, attribuzione distinta, scope, valutazioni e storia. | DISTINZIONE NECESSARIA, FORMA AUTONOMA NON DIMOSTRATA; INFORMAZIONE ADIACENTE AL CORE; K-065 APERTA per la forma concreta indirizzabile. | I «Supporto, dipendenze e indipendenza»; G; H7/H8/H11/H15 e H20; O. | V1 §3.8; R2 §R2.5; R2C §T4; R4 §R4.4–R4.5; GATE §A controllo 1 e §C; REG D02–D03 e L02. |
| Documento / document identity | V1 §4.4.2 raggruppa copie, versioni e rappresentazioni sotto Document identity reconciliation. | R2/R5 esercitano più immagini per documento, due ricevute in una foto, frammenti di due documenti e D2 che corregge D1. | Documento può essere Referent quando occorre mantenerne identità indipendente ed esiste una base pertinente. | FORMA CANDIDATA K-029 come Referent documentale; distinzione documentale necessaria, nessuna primitiva universale. Criteri specifici K-142 APERTI. | I «Documenti e rappresentazioni»; H3, H7, H8, H9/H10 e H16 nei rispettivi confini; J; O. | V1 §4.4.2; R2 §R2.1–R2.2; R2C §T5; R5 §R5.2, §R5.9 e «Document Identity Reconciliation»; AUDIT §B 25b; REG L06. EG-01 già noto: per K-133 il rinvio corretto è 25b, non 25h. |
| Derivation | V1 la elenca tra le forme candidate e come meccanismo §4.4.7; il nome mescola facilmente attività e risultato. | R3: scadenza trascorsa non significa non pagato; nessuna conferma conosciuta è un riscontro limitato; previsione da cadenza non è fatto osservato. | Domain/Core e regole inferenziali determinano applicabilità; Derivation produce conclusione e Lineage; Policy governa automazione, materializzazione e usi, non la validità. | Meccanismo di ragionamento con conclusione informativa e giustificazione adiacente; DISTINZIONE NECESSARIA, FORMA AUTONOMA NON DIMOSTRATA per un unico oggetto Derivation. | D; H11; G Lineage; I «Derivation record / justification»; E per gli usi. | V1 §3.5 e §4.4.7; R2C §2; R3 §R3.4; R5 §R5.6 e Delta §I; R6 §V.8; GATE §A controllo 3, §C; AUDIT §B 25g. |
| Decision / Disposition / Application | V1 distingue policies, loro valutazione, Verification Decision e Admission, ma non rende sempre inequivoci scelta, disposizione e applicazione. | R1/R3: una Disposition può essere autorizzata quando nasce e non applicabile quando eseguita; una conferma tardiva resta riferita alla domanda originaria. | Decision conserva scelta motivata, origine, autorità, target, scope e contesto; Disposition il trattamento autorizzato; Application l’effetto e il suo esito. | GOVERNANCE / PROCESSO, NON PRIMITIVA INFORMATIVA. Distinzione forte; ownership D06/K-185 APERTA, non nuovo Decision Manager. | E; F; H14/H15/H16/H19; G memoria di governo; O C01 e C07/D06. | V1 §4.6–4.8; R1 §R6; R2 §R2.5; R3 §R3.10; R4 §R4.2; R6 §V.9; REG §B1 D06. |
| Work | V1 ha lifecycle tecnico, orchestrazione e verifica, ma non un’unità operativa uniforme. | R2: OCR produce 22 pagine su 40, poi fallisce; una verifica attende due settimane. | Work durevole quando serve riprendere, attendere, verificare o spiegare. | GOVERNANCE / PROCESSO, NON PRIMITIVA INFORMATIVA; FORMA CANDIDATA K-012. Continuità operativa necessaria, granularità e forma concrete APERTE. | F; G memoria operativa; I/O; H15 per verifica. | V1 §1.5, §4.7, §6.5; R1 §R5; R2 §R2.6; R2C §9–10; R5 §R5.10; R6 §V.9. |
| Subject / soggetto e Property / attributo | V1 §3.5 usa Subject e Property/Relation nella grammatica candidata; il soggetto può sembrare la cosa esterna e l’attributo un valore direttamente appeso ad essa. | R2C: la cifra di una foto con due scontrini non ha ancora soggetto determinato. | Subjecthood designa il ruolo di ciò di cui si parla; il Referent ne è il locus interno. | DISTINZIONE NECESSARIA, FORMA AUTONOMA NON DIMOSTRATA. Questa scheda accosta due ruoli storici, non li fonde in un nuovo concetto. | I «Referent, Assertion e commitment» e «Value»; G Domain; H7; J. | V1 §3.5; R2C §3; R5 §R5.1 e §R5.8; R6 §V.1–3. |
| Validity / qualificazioni temporali | V1 presenta Validity tra le forme candidate; R2C rafforza la distinzione di ruoli temporali ma dichiara non verificato il modello generale di validità. | R3 separa periodo fatturato, emissione, ricezione, interpretazione, Admission e reference time. | Temporalità del contenuto, storia epistemica, storia operativa, pertinenza d’uso e reference time restano distinti. | RESPINTA COME SUPER-PRIMITIVA / CONTENITORE UNIVERSALE; qualificazioni necessarie. Forme concrete e criteri specifici K-096 APERTI. | I «Tempo»; H10/H12; E/F/G; O. | V1 §3.5 e §4.4.4; R2C §2; R3 §R3.1–R3.3; R5 «Identità e tempo»; R6 §V.6; REG L04. |
| Knowledge State | V1 §4.8 raccoglie accepted, provisional, contested, rejected, superseded e corrected; Candidate/Verification aggiungono incompletezza e pending. | R2C mostra la coesistenza di Source conservata, importo determinato, data ambigua, verifica aperta e ammissione parziale. | La funzione del contenitore unitario viene decomposta: completezza/alternative dell’Interpretation Result, assessment epistemici, posizione di Admission, storia della Decision e stato del Work. | RESPINTA COME SUPER-PRIMITIVA / CONTENITORE UNIVERSALE. K-060 SUPERATA da K-061, senza nuovo stato universale STALE. | D/E/F; I qualificazioni, Quality e proposte; G memorie separate. | V1 §3.5 e §4.8; R2C §6; R4 §R4.1–R4.2; R5 §R5.5 e Delta §I; REG L03. |
| Current State / Current Reconstruction | V1 §4.4.8 chiama Current-state derivation la ricostruzione dello stato corrente, suggerendo che ogni risposta sia una nuova conclusione derivata. | R3 distingue selezionare contenuti pertinenti dal produrre una nuova proposizione. | Responsabilità di Current Reconstruction acquisita; tiene espliciti domanda, tempo, scope, basi e qualificazioni. | Responsabilità K-073 STABILE; FORMA CANDIDATA del risultato. Non nuova primitiva CurrentState; C03/C06 restano APERTE. | D/E; H12; H17/H18/H20 utilizzatori; I/O. | V1 §4.4.8; R3 §R3.3–R3.4; GATE §A controllo 2 e §C; AUDIT §B 25h; REG L05. EG-01 già noto: K-072/K-073 rinviano impropriamente a 25g. |
| Expectation / temporal attention | Il bisogno di scadenze e promemoria esiste in V1; R3 formula esplicitamente Expectation come possibile forma per qualcosa atteso ma non riscontrato. | R3 distingue previsione da sei bollette, scadenza esplicita della revisione auto e manutenzione raccomandata. | Base dell’attesa, condizioni/finestra, riscontro delimitato e comportamento restano distinguibili. | FORMA CANDIDATA della composizione K-080; non dimostrate primitiva Expectation e responsabilità Temporal Controller universali. C02 rimane APERTURA, non una nuova teoria del conflitto predittivo. | D «Attenzione temporale»; F; H10/H11/H17/H14/H19; I «Tempo»; O C02. | V1 §4.4.4 e §5.3; R3 §R3.6–R3.7; R6 §V.7–8. |
| Logical Document | R2 §R2.1 introduce il nome per non dipendere dalla singola Source quando più fotografie sembrano rappresentare un documento. | R2C: tre immagini elaborate insieme possono rappresentare scontrino, garanzia e prodotto, non un documento unico. | Il problema sopravvive in rappresentazioni/porzioni, composizione interpretativa e possibile Referent documentale. | RESPINTA COME SUPER-PRIMITIVA / CONTENITORE UNIVERSALE; possibile Referent documentale CANDIDATO. Scheda del nome storico, non secondo oggetto oltre «Documento». | H7/H8; I «Documenti e rappresentazioni»; G/O. | R2 §R2.1; R2C §T5 e §7; R5 §R5.2 e §R5.9; R6 §III.9. |
| Source Portion / locator | R2 §R2.2 richiede porzioni per rappresentazioni molti-a-molti. | Regione superiore della foto, parte dello scontrino e totale dovuto sono localizzazione, interpretazione documentale e significato diversi. | Riferimento localizzato a Source/rappresentazione, collegato alle trasformazioni pertinenti. | DISTINZIONE NECESSARIA, FORMA AUTONOMA NON DIMOSTRATA; locator CANDIDATO, forma/confini K-032 APERTI. | D; G; H5/H7; I «Locator / anchor» e «Documenti e rappresentazioni»; O. | R2 §R2.2; R2C §T6; R5 §R5.9; R6 §VII.2. |
| Human Statement / contributo attribuito | V1 Feedback Handler riceve correzioni e conferme; R2 distingue dichiarazione umana, nuova informazione e autorizzazione. | «Sì» può confermare una lettura o autorizzare un link. | Contributo attribuito collega contenuto, origine/contributore e contesto; la base umana effettivamente ricevuta resta recuperabile. | INFORMAZIONE ADIACENTE AL CORE; distinzione forte. Indirizzabilità quando richiesta da qualifiche/contestazioni non impone una primitiva HumanStatement. | H22; D/E; G; I «Contributo attribuito»; H15/H20. | V1 §5.6 e §6.2; R2 §R2.4–R2.5; R2C §T1 e §7; GATE §A controllo 1; REG D01. |
| Interpretation Result / Bundle | V1 Interpretation Coordinator produce Candidate Knowledge Bundle. | Importo riuscito, data ambigua e attribuzione irrisolta non giustificano né Admission atomica né perdita di tutto il risultato. | Interpretation Result è forma candidata per alternative/incompletezza; Bundle non è documento, Work né unità atomica d’ammissione. | FORMA CANDIDATA K-053, INFORMAZIONE ADIACENTE AL CORE. Recuperabilità pre-Admission K-144 STABILE; forma concreta e C04 APERTE. | D; G memoria delle proposte; H7; I/O. | V1 §3.9; R1 §R4; R2 §R2.9; R2C §T3, §7, §10.2; R5 §R5.10; R6 §V.1–2 e §VII.2; REG L10. |
| Attempt | R1 §R5 introduce la distinzione tra lavoro durevole e sue esecuzioni; R2 verifica se il tentativo debba essere autonomo. | Il primo OCR produce 22 pagine, il secondo altre 18 e una lettura diversa di una pagina precedente. | Tentativi distinguibili nella storia del Work e indirizzabili nel contesto quando necessari per Decision/spiegazione; output e loro qualità mantengono natura e storia. | GOVERNANCE / PROCESSO, NON PRIMITIVA INFORMATIVA; forma/autonomia concrete APERTE. | F; G memoria operativa; I/O in relazione al Work. | R1 §R5; R2 §R2.6; R2C §7 e §9; R6 §V.9. |
| Event / Reception | V1 registra evento di acquisizione e lifecycle tecnico; R1/R2 separano ricezione, lavoro di acquisizione ed esito. | Un file viene ricevuto e preservato ma non è processabile; un OCR fallisce dopo acquisizione riuscita. | Reception è fatto di Provenance del percorso; Acquisition Work ha esito e stato propri. | INFORMAZIONE ADIACENTE AL CORE per la ricezione; Event/Result universali NON SOSTENUTI come primitive. Grammatica emissione/reazione K-006 CANDIDATA. | H1; F/G; J; O F2d. | V1 §1.2 e §6.5; R1 §R2 e §R5; R2 §R2.6–R2.7; R2C §7; REG D07. |
| Verification | V1 §3.5 menziona Verification fra forme candidate e §4.7 la realizza come workflow che raccoglie conferme e produce Verification Decision. | R2: confermare lettura, ruolo, link, fatto nuovo e autorizzazione sono cinque casi diversi. | Verification organizza domanda/contributo e conserva contesto mostrato, risposta, scope e storia; le valutazioni pertinenti restano distinguibili. | GOVERNANCE / PROCESSO, NON PRIMITIVA INFORMATIVA; contributi e valutazioni adiacenti. C01, K-119 e D06 restano APERTI. | F; H15/H22; E; G; O. | V1 §3.5 e §4.7; R1 §R6; R2 §R2.4–R2.5; R2C §8.12; R3 §R3.10; R4 §R4.2; REG D06. |
| Admission | V1 §4.8 separa produzione del candidato e accettazione, ma raccoglie anche state management. | Una Disposition può non essere più applicabile; una proposta completa può restare non ammessa; un Referent proposto può esistere prima del suo riconoscimento. | Admission applica una disposizione pertinente e può verificarne condizioni/invarianti, motivando mancata applicazione senza inventare una nuova scelta. | GOVERNANCE / PROCESSO, NON PRIMITIVA INFORMATIVA; assetto K-146 CANDIDATO; K-145 APERTA per il Referent senza Assertion già ammessa. | E; H16; I/O. | V1 §4.8; R1 §R6; R2C §8.14; R5 §R5.11; R6 §V.1–2; GATE §A controllo 1. |
| Policy | V1 introduce Application Decision Policies come risorsa trasversale e Policy Evaluation come attività; non sono una forma della realtà rappresentata. | R3: una nuova Policy non riscrive le dichiarazioni precedenti; R4 separa regole composte. | Risorsa di criteri comportamentali distinta dalla valutazione e dalla Decision del caso. | GOVERNANCE / PROCESSO, NON PRIMITIVA INFORMATIVA per il ruolo decisionale; risorsa di riferimento, non attore autonomo. Regole concrete non decise qui. | G; E; H14; I modalità; O. | V1 §4.5–4.6; R1 §R6; R3 §R3.9; R4 §R4.10; R6 §V.8–9; GATE §A controlli 2–3 e §C. |
| Provenance | V1 §6.1 conserva origine e contesto di acquisizione/produzione insieme alla Lineage; il disegno può suggerire un recorder centrale. | R2C: una registrazione di ricezione non sostituisce il contenuto originale; un contributo umano richiede domanda e risposta. | Origine e contesto catturati dai produttori competenti, raggiungibili da Query/Explanation. | INFORMAZIONE ADIACENTE AL CORE; distinzione necessaria, non obbligo di primitiva o recorder centrale. | G, cattura presso i produttori; H20 attraversamento per spiegazione; I/J. | V1 §2.9 e §6.1; R2C §T1 e §10; R4 §R4.3, §R4.6–R4.8; REG L08. |
| Lineage | V1 §6.1 la affianca alla Provenance per seguire trasformazioni da Source a risultati. | R2C: DEPENDS_ON può indicare prosecuzione del lavoro o giustificazione della conclusione, non la stessa cosa. | Lineage conserva trasformazioni, premesse, metodi e risorse pertinenti; permette attraversamento e controlli locali senza controllore centrale obbligatorio. | INFORMAZIONE ADIACENTE AL CORE; distinzione forte. Forme/granularità concrete non fissate come primitive. | G e produttori pertinenti; H11/H13/H20; I supporto e J. | V1 §6.1 e §6.6; R1 §R7; R2C §11; R3 §R3.8–R3.9; R4 §R4.5–R4.8; R5 §R5.6; REG D02–D03. |
| Impact | V1 tratta correzione, versionamento e ricalcolo; R3 rende esplicita la valutazione d’impatto di nuovi contenuti e cambiamenti di risorse. | R3: una nuova Source modifica il perimetro di una precedente assenza; Mapping cambiato può alterare un ruolo ma non la stringa osservata. | Potenziale impatto, basi messe in dubbio, rivalutazione e risultato accertato non sono sinonimi. | INFORMAZIONE ADIACENTE AL CORE per la qualificazione, meccanismo per la valutazione e governo distinto della rivalutazione. K-087/K-161 STABILI; criteri d’uso C03 APERTI. | E; H13/H12; G/I; O C03/F2d. | R3 §R3.8–R3.9; R6 §V.9; GATE §A controllo 2 e §C. |
| Contenuto negativo / modalità | V1 separa scadenza superata e pagamento non provato; R2 richiede recupero negativo delimitato. | Materiale non interpretato può contenere la conferma cercata; corpus accessibile può escludere altri materiali. | Distinguere negazione esplicita sostenuta, assenza osservata locale, ricerca negativa delimitata e Assertion/inferenza negativa sul mondo. | DISTINZIONI NECESSARIE, FORME AUTONOME NON DIMOSTRATE; risultati negativi adiacenti e contenuti proposizionali qualificati, non nuova primitiva. | D; H5/H11/H17; I «Informazione negativa e modalità»; O. | V1 §4.5 esempio scadenza; R2 §R2.3; R3 §R3.4 e §R3.7; R6 §II Q4–Q7 e §V.7–8. |
| Identity Reconciliation / coreferenza | V1 §4.4.1 collega un candidato a referenti esistenti; il lessico di identità e merge può far sembrare l’unione l’esito naturale del riconoscimento. | R5 verifica omonimi, POD errato, identificatori di rapporti diversi e cambiamenti di proprietà. | Reconciliation propone e valuta, non scopre identità infallibile. | Meccanismo di ragionamento, non primitiva. Proposizioni, assessment e decisioni restano distinti; algoritmi e criteri specifici APERTI. | H8; E/H16; I Identifier/Documenti; J; O. | V1 §4.4.1; R2C §4; R5 §R5.4–R5.5, «Identità e tempo»; R6 §IV; REG D05. |
| Correction / Supersession / conflitto | V1 §4.4.5–4.4.6 distingue conflitto e Correction/Supersession, ma il secondo nome raccoglie riconoscimento del rapporto e revisione della Knowledge. | R3: 84,72→34,72 può essere rettifica soltanto se riguarda lo stesso bersaglio; due fornitori in periodi diversi non sono automaticamente incompatibili. | Riconoscere una rettifica non equivale ad applicarla; confronto e semantica Domain determinano pertinenza/incompatibilità, la Governance governa gli effetti. | DISTINZIONI NECESSARIE fra contenuti, relazioni epistemiche, tempo e GOVERNANCE; non primitiva universale Correction/Supersession. | H7/H9/H10/H12/H13 per significato e conseguenze; E/H16 per revisioni; I/J; O. | V1 §4.4.5–4.4.6; R3 §R3.5; R4 §R4.4 e §R4.10; R6 §V.3; GATE §B. |

## 7. Evidence gap e limiti di questa preservazione

**Nessun nuovo evidence gap rilevato nella ricostruzione effettuata.** Questo non è un verdetto del Model Preservation Gate, che non viene eseguito.

**EG-01 resta già noto e non corretto:**

- K-072/K-073 rinviano a AUDIT 25g; il percorso Current-State Derivation → Current Reconstruction è in **AUDIT §B 25h**, oltre che direttamente in R3 §R3.3–R3.4.
- K-133 rinvia a AUDIT 25h; Document Identity Reconciliation è in **AUDIT §B 25b**, oltre che in R2/R5.

Le schede e la matrice usano i rinvii primari corretti. Il difetto riguarda i collegamenti del Ledger, non prova assenza della conclusione. Il Ledger non viene corretto qui; EG-01 va gestito separatamente prima del futuro Model Preservation Gate secondo il mandato.

I testi integrali dei Round restano nell’archivio locale esterno al repository, limite già noto nel Source Map e nel checkpoint FOL-40. Le schede trasferiscono qui ipotesi, casi, alternative, ragioni e conclusioni necessarie; i riferimenti esterni servono per il riscontro del testo originale, non come sostituto della spiegazione.

K-066 e K-145 non sono nuovi gap scoperti da questa task: sono aperture già registrate nel Ledger che non vanno perse perché una successiva sintesi generale sembra sufficiente. Analogamente D06 non prova l’assenza storica di ogni proposta di ownership.

## 8. Anti-promotion check

Verifica mirata del documento prodotto, non ripetizione dei Gate precedenti.

| Controllo richiesto | Esito e riscontro nel documento |
|---|---|
| Nessuna candidata promossa a STABILE | Preservati esplicitamente K-012, K-029, K-053, K-080, K-098, K-136, K-143, K-146 e K-148; nessuna nuova decisione modifica il Ledger. |
| Nessuna distinzione necessaria resa primitiva autonoma | Identifier, Value, Evidence, locator, contributo attribuito e qualificazioni restano distinti senza inventario di oggetti obbligatori. Le sole primitive fortemente sostenute sono Referent e Assertion, con i limiti delle rispettive schede. |
| Nessuna collocazione candidata resa canonica | Source/Observation: K-049/K-050 STABILI nella definizione, K-148 CANDIDATA nella collocazione; Knowledge e forme operative mantengono i propri limiti. |
| Nessun problema eliminato con la forma universale | Ogni riga della sezione 4 ha problema preservato, ragione e destinazione; anche le forme non dimostrate, invece che impossibili, sono distinte. |
| Stato genealogico non confuso con FORTE/CANDIDATO locale | §1 e §5 distinguono i tre assi; Value FORTE non significa entità autonoma; K-073 STABILE non significa risultato definitivamente materializzato. |
| D06, C01–C07 e F2d non risolti | §5 conserva domanda residua e vincolo acquisito; nessun owner, asse Admission/Usability, controller o regola predittiva nuovi. |
| Nessuna nuova primitiva creata | Le 35 schede sono unità di esposizione genealogica, non elementi del modello; le 12 righe sulle forme universali non istituiscono nuovi tipi. |
| Nessun test retrodatato | Identifier/Derivation NON TESTATI come primitive in R2C; tempo non ancora Validity generale. Le tre correzioni GATE non sono attribuite a R6 come già precise. |
| Nessun superamento storico cancellato | Conservati K-120→K-143, K-051→K-052, K-060→K-061, K-069→K-070, K-072→K-073, K-135→K-136, K-137→K-144 con residuo K-145, K-155→K-158, K-153→K-161, K-154→K-162 e K-017→K-185. |
| Nessuna nuova verifica generale o autorità | Nessun nuovo Round, Source Readiness, Knowledge Preservation, audit34 o Model Preservation Gate; nessuna promozione Research/Draft a Canonical. |

## 9. Perimetro materiale dell’intervento

Creato soltanto `docs/ricerca/fold-core-concept-genealogy-2026-09-05.md`. Non vengono aggiornati indice docs, candidata, prima genealogia, Source Map, Ledger, Coverage, delta, snapshot o Gate.

Le cinque aggiunte non versionate già presenti all’inizio appartengono al lavoro precedente e rimangono intatte. I 26 file preesistenti sotto `docs/` sono stati confrontati tramite SHA-256 e risultano invariati. Il controllo di integrità non rivaluta il loro contenuto e non modifica né sostituisce i precedenti controlli progettuali.

Verifica meccanica dell’artefatto: 35 schede univoche, ciascuna con tutti i nove campi richiesti; 35 righe corrispondenti nella matrice finale, nello stesso ordine; 12 forme nella tabella dei contenitori universali; collegamenti documentali locali risolti. Nessun K-ID citato risulta inesistente nel Ledger.

Linear consultato soltanto in lettura; nessuna modifica a Linear o Notion. Nessun commit, push, branch, Fold Sync o chiusura di issue. La successiva verifica del modello resta lavoro distinto e non è anticipata da questo documento.
