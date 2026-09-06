# Fold — Genealogia dei componenti e delle responsabilità

Questo documento preserva la genealogia strutturale dei componenti e delle responsabilità. Non stabilisce confini software e non autorizza il freeze della v2.1.

**Status: Research — Model Preservation**  
**Data:** 2026-09-05  
**Percorso:** FOL-40, nel contesto di FOL-36  
**Artefatto:** prima genealogia strutturale; non Canonical e non Model Preservation Gate.

## 1. Scopo e chiave di lettura

Il documento preserva il percorso dai 34 elementi attivi della v1 ai 24 gruppi di copertura dell’audit e alla loro esposizione in 22 schede H nella candidata v2/v2.1. Le schede conservano il problema e il motivo della trasformazione, così da poter comprendere il percorso senza riaprire la conversazione originale. I riferimenti alle fonti permettono di controllare questa distillazione, non sostituiscono le spiegazioni.

Il Source Readiness Check già superato costituisce il punto di partenza e non viene rieseguito. La candidata v2.1 viene consultata soltanto come destinazione successiva: non è la fonte da cui dedurre l’esistenza o la natura originaria dei componenti.

Ogni scheda separa:

- **fonte originale:** forma in v1 e ciò che mostrarono realmente i Round;
- **conclusione e disposizione:** risultato del percorso, registrato dall’audit successivo;
- **stato successivo:** gruppo di copertura, collocazione H e viste della v2.1;
- **rischio di perdita:** distinzione che scomparirebbe interpretando male il cambiamento.

Le sei disposizioni sono classi dell’audit storico, non nuovi stati epistemici del prodotto. “MANTENUTO / RIDEFINITO” rende qui la formula “MANTENUTO MA RIDEFINITO” dell’audit senza cambiarne il significato. “MANTENUTO AUTONOMO” significa autonomia del problema al momento dell’audit: non garantisce una scheda H dedicata nell’assemblaggio successivo. Il caso Channel Adapter lo mostra esplicitamente.

Le “fasi” nelle cinque sezioni seguenti identificano la posizione storica in v1. R1 §R1 le riclassificava come aree funzionali: la loro numerazione non impone una sequenza runtime.

## 2. Fonti e tracciabilità della ricostruzione

### Fonti originali

V1, R1, R2, R2C, R3, R4, R5, R6 e GATE sono i messaggi originali recuperati e identificati nel Source Map. R2C è il chiarimento del Round 2, non un Round aggiuntivo. R1 contiene sezioni denominate R1–R8: una citazione “R1 §R7” indica la settima sezione del primo Round.

L’archivio è:

```text
C:\Users\giuseppe\.codex\sessions\2026\09\01\rollout-2026-09-01T14-56-30-01a05d0a-e483-7793-a648-e46306e04177.jsonl
```

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

Gli ordinal identificano messaggi, non righe del file. Le impronte si riferiscono ai corpi originali UTF-8 e sono quelle verificate nel Source Map; questo lavoro ne riusa l’identificazione, senza ripetere il Source Readiness Check.

### Preservazioni successive e controllo

- **AUDIT §A e schede 1–34:** disposizione, motivazione e rischio di perdita registrati successivamente ai Round. **AUDIT §B:** meccanismi 25a–25i. **AUDIT §F:** inventario dei 24. **AUDIT §G/H:** trasversali e limiti della copertura. Qui l’audit è usato come registrazione successiva delle disposizioni, non come sostituto delle evidenze dei Round.
- **ASM1 §K:** prima mappa esplicita dei 24 gruppi verso le schede H.
- **REG:** controllo dell’assemblaggio. È evidenza originale del confronto svolto in quella fase; quando riepiloga un Round, non ne sostituisce il testo. D07 motiva l’aggregazione della ricezione; D01–D05 registrano recuperi; D06 mantiene la riserva sull’ownership non-Policy.
- **ASM2 e snapshot v2:** stato integrato dopo REG, incluse le correzioni già applicate allora.
- **Knowledge / Decision Ledger:** controllo delle conclusioni e degli stati genealogici; conserva autorità sul percorso senza diventare il modello operativo.
- **Coverage v2, delta, candidata v2.1 e Patch Record:** controllo e localizzazione degli esiti successivi; non provano retroattivamente le trasformazioni originarie.
- **Source Map:** registro delle fonti disponibili già verificato.

Documenti di accompagnamento nel repository:

- [Source Map](fold-model-preservation-source-map-2026-09-05.md);
- [Knowledge / Decision Ledger](fold-knowledge-decision-ledger-2026-09-04.md);
- [Coverage v2](fold-coverage-ledger-v2-2026-09-04.md);
- [Snapshot v2](fold-anatomia-v2-snapshot-2026-09-04.md);
- [Delta v2→v2.1](fold-delta-v2-v2.1-2026-09-04.md);
- [Candidata v2.1](fold-anatomia-v2.1-candidate-2026-09-04.md).

Non si presume che ogni componente abbia subito uno stress nominativo in ogni Round. Dove la forma v1 era già circoscritta e l’accorpamento viene formalizzato dall’audit, la scheda lo dichiara. Questo evita di inventare un precedente conflitto soltanto per rendere uniforme la narrazione.

### Perimetro dei 34

I 34 sono gli elementi attivi selezionati nell’audit. Le risorse Mapping Definitions, Domain Model, Core Model, Quality Model, Application Decision Policies e la Knowledge Repository non sono ulteriori righe del conteggio. Le trasversali dell’area 6 restano fuori dall’inventario dei 34 e non vengono eliminate.

I nove meccanismi 25a–25i sono articolazioni interne del n. 25: hanno una tabella dedicata ma non si sommano ai 34. Il passaggio numerico non è una sottrazione di capacità: comprende accorpamenti, distribuzioni ed esplicitazioni di problemi già emersi.

## 3. Schede genealogiche dei 34 elementi

## FASE 1 — INGESTIONE

### 1 Channel Adapter

**Problema originario posseduto**  
Ricevere contenuti da canali differenti senza perdere le circostanze della consegna.

**Forma in v1**  
Adattava file e metadati del canale a una consegna uniforme, conservando mittente, modalità e informazioni originali. Non classificava semanticamente il documento. Fonte: V1 §1.1.

**Stress / evidenza dei Round**  
V1 distingue già consegna e significato. R2 §R2.7 separa ricezione, lavoro ed esito; R4 §R4.3, «Channel Adapter», distingue origine del canale e attendibilità del contenuto. Non è documentata nei Round una necessità di mantenerlo separato dalla registrazione della ricezione.

**Conclusione**  
Rimane il problema dell’adattamento fedele del canale. AUDIT §A.1 lo mantiene autonomo; soltanto l’assemblaggio successivo lo raccoglie con la registrazione in H1, scelta motivata da REG D07.

**Disposizione**  
MANTENUTO AUTONOMO. Riscontro della disposizione: AUDIT §A.1 e §C.

**Destinazione**  
Gruppo/i 1. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H1 — capacità interna di adattamento della consegna; G per Provenance. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
Un upload normalizzato senza contesto farebbe perdere chi ha fornito il materiale e attraverso quale canale; raccogliere le due capacità in H1 non consente di fonderne i significati.

**Riferimenti puntuali**  
V1 §1.1; R2 §R2.7; R4 §R4.3; REG §B1/D07; AUDIT §A.1 come registrazione successiva.


### 2 Acquisition Controller

**Problema originario posseduto**  
Rendere riconoscibile ciascun ingresso, anche quando riutilizza contenuto già ricevuto.

**Forma in v1**  
Creava l’evento di acquisizione e governava il ciclo tecnico iniziale, registrando controlli, errori e collegamento all’artefatto. Fonte: V1 §1.2.

**Stress / evidenza dei Round**  
R1 §R3 distingue coordinamento funzionale ed esecuzione: un OCR interrotto non rende fallita una ricezione riuscita. R2 §R2.7 e R2C §8.1 distinguono accadimento, lavoro di acquisizione ed esito; il controller non possiede l’intero futuro semantico della Source.

**Conclusione**  
La responsabilità sopravvive con un confine più stretto. AUDIT §A.2/F.2 conserva storia e governo dell’acquisizione; il coordinamento dei lavori successivi è nel gruppo 24. ASM1 §K e REG D07 raccolgono registrazione e adattamento in H1.

**Disposizione**  
MANTENUTO / RIDEFINITO. Riscontro della disposizione: AUDIT §A.2 e §C.

**Destinazione**  
Gruppo/i 2; collaborazione con 24. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H1 — registrazione dell’Acquisition; F e gruppo 24 per avanzamento operativo. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
Estendere l’Acquisition a ogni elaborazione futura creerebbe una regia documentale universale; cancellarla perderebbe la storia delle ricezioni distinte.

**Riferimenti puntuali**  
V1 §1.2; R1 §R3; R2 §R2.7; R2C §8.1; REG §B1/D07; AUDIT §A.2 come registrazione successiva.


### 3 Technical Validation

**Problema originario posseduto**  
Stabilire se il materiale possa essere sottoposto alle operazioni tecniche pertinenti.

**Forma in v1**  
Controllava formato reale, integrità, dimensioni, leggibilità e sicurezza; produceva diagnosi tecniche, non un giudizio di verità. Fonte: V1 §1.3.

**Stress / evidenza dei Round**  
R2C §8.2 precisa il limite del generico «Source valida»: leggibilità, completezza documentale e attendibilità non coincidono. R1 §R2 distingue il prerequisito della conservazione autorizzata dalla possibilità di trattenere materiale in staging o quarantena.

**Conclusione**  
AUDIT §A.3 mantiene un problema tecnico autonomo. L’ammissibilità riguarda l’operazione e i suoi vincoli; non diventa certificazione epistemica o obbligo di completa interpretazione.

**Disposizione**  
MANTENUTO AUTONOMO. Riscontro della disposizione: AUDIT §A.3 e §C.

**Destinazione**  
Gruppo/i 3. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H2 — validazione tecnica; cooperazione con H1/H4 e condizioni operative. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
Un file sicuro o decodificabile potrebbe essere presentato come contenuto attendibile; un errore di elaborazione potrebbe essere confuso con falsità del documento.

**Riferimenti puntuali**  
V1 §1.3; R1 §R2; R2C §8.2; AUDIT §A.3 come registrazione successiva.


### 4 Fingerprinting / Technical Deduplication

**Problema originario posseduto**  
Riconoscere ripetizioni tecniche e prevenire effetti duplicati preservando le ricezioni.

**Forma in v1**  
Usava l’impronta del contenuto per riconoscere uguaglianza binaria, riuso dell’artefatto e duplicazione della consegna. Escludeva già identità di scansioni differenti e correzioni semantiche. Fonte: V1 §1.4.

**Stress / evidenza dei Round**  
R5 §R5.9 e «Document Identity Reconciliation» separano copie tecniche, composizione, coreferenza e versioni. R3 §R3.9 mostra inoltre che nuove definizioni di Mapping possono richiedere nuova elaborazione della stessa Source: riusare i byte non prova che si possa riusare il risultato.

**Conclusione**  
AUDIT §A.4/B.25b mantiene autonomo il riconoscimento tecnico. Il caso documentale non lo sostituisce e non gli trasferisce il diritto di dichiarare identità semantica.

**Disposizione**  
MANTENUTO AUTONOMO. Riscontro della disposizione: AUDIT §A.4 e §C.

**Destinazione**  
Gruppo/i 4. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H3 — identificazione/deduplicazione tecnica; storia delle Acquisition in H1. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
Il riuso tecnico potrebbe cancellare un ingresso distinto o scambiare due rappresentazioni diverse per documenti diversi; un hash uguale potrebbe giustificare indebitamente il riuso di un’interpretazione.

**Riferimenti puntuali**  
V1 §1.4; R3 §R3.9; R5 §R5.9 e Document Identity Reconciliation; AUDIT §A.4 come registrazione successiva.


### 5 Staging / Technical Lifecycle

**Problema originario posseduto**  
Conservare condizioni tecniche, prerequisiti, attese, errori e tentativi durante il trattamento dell’ingresso.

**Forma in v1**  
Esponeva un lifecycle dell’artefatto con stati quali ricevuto, in controllo, quarantena, fallito e pronto per l’estrazione; conservava transizioni e tentativi. Fonte: V1 §1.5.

**Stress / evidenza dei Round**  
R1 §R5 separa eventi, lavoro, tentativi e risultati. R2 §R2.6 consente che 22 pagine utilizzabili sopravvivano al tentativo interrotto; R2C §9 separa esito operativo e contenuto. Lo staging non può essere la posizione epistemica unica di tutto ciò che non è ancora ammesso.

**Conclusione**  
AUDIT §A.5 lo riclassifica: condizioni tecniche del materiale e aspetti del Work sopravvivono, mentre la memoria delle proposte non si identifica con una zona transitoria destinata a svuotarsi.

**Disposizione**  
RICLASSIFICATO. Riscontro della disposizione: AUDIT §A.5 e §C.

**Destinazione**  
Gruppo/i 24; condizioni di ingresso pertinenti a 2 e 3. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
F/G — piano e memoria operativi; condizioni tecniche in H1/H2/H4. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
Eliminare lo staging come scatola potrebbe eliminare le attese; mantenerlo come contenitore universale farebbe dipendere la sopravvivenza delle proposte da un lavoro attivo.

**Riferimenti puntuali**  
V1 §1.5; R1 §R5; R2 §R2.6; R2C §9; AUDIT §A.5 come registrazione successiva.


### 6 Source Preservation

**Problema originario posseduto**  
Permettere di tornare al contenuto originario dopo le trasformazioni.

**Forma in v1**  
Riceveva l’artefatto tecnicamente valido e l’Acquisition; conservava originale o riferimento stabile, metadati, impronta, rappresentazioni tecniche e collegamenti agli ingressi. Fonte: V1 §1.6.

**Stress / evidenza dei Round**  
R2 §R2.3 mantiene recuperabile materiale non interpretato. R2C §T1 corregge la Source definita attraverso utilizzabilità o processabilità; §8.3 conferma la conservazione come responsabilità. R5 §R5.9 mostra più Source per documento e più documenti rappresentati da una Source.

**Conclusione**  
AUDIT §A.6 preserva la responsabilità, ridefinendola sul contenuto d’origine e le rappresentazioni. La conservazione segue le condizioni applicabili, senza richiedere successo semantico o attribuire identità documentale.

**Disposizione**  
MANTENUTO / RIDEFINITO. Riscontro della disposizione: AUDIT §A.6 e §C.

**Destinazione**  
Gruppo/i 5. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H4; G — memoria delle Source/rappresentazioni; I per distinzione documentale. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
Subordinare l’origine alla riuscita dell’interpretazione farebbe perdere proprio il materiale necessario per verificarla o ripeterla. Source e documento non possono essere identificati automaticamente.

**Riferimenti puntuali**  
V1 §1.6; R2 §R2.3; R2C §§T1/8.3; R5 §R5.9; AUDIT §A.6 come registrazione successiva.


## FASE 2 — ESTRAZIONE

### 7 Format Decoder

**Problema originario posseduto**  
Rendere accessibile il contenuto codificato nel formato ricevuto.

**Forma in v1**  
Apriva la struttura tecnica, individuava pagine, testo e immagini e rendeva disponibili errori e percorso estrattivo applicabile; non attribuiva significato. Fonte: V1 §2.1.

**Stress / evidenza dei Round**  
V1 distingue già decodifica e interpretazione. R2C §8.2 precisa l’ammissibilità per operazione, senza provare l’autonomia di ogni capacità tecnica. La disposizione specifica è formalizzata da AUDIT §A.7: nessun problema semantico o di governance ulteriore giustifica un gruppo indipendente.

**Conclusione**  
La capacità resta necessaria ed è accorpata nell’estrazione. Non si attribuisce ai Round una decisione nominativa di accorpamento antecedente a quella registrata dall’audit.

**Disposizione**  
ACCORPATO. Riscontro della disposizione: AUDIT §A.7 e §C.

**Destinazione**  
Gruppo/i 6. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H5 — capacità interna di decodifica. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
L’accorpamento non permette di assumere che ogni Source sia già leggibile: esiti, limiti del formato e impedimenti devono sopravvivere.

**Riferimenti puntuali**  
V1 §2.1; R2C §8.2; disposizione successiva AUDIT §A.7; AUDIT §A.7 come registrazione successiva.


### 8 Text Extraction

**Problema originario posseduto**  
Recuperare il testo già digitale con posizione e struttura tecnica.

**Forma in v1**  
Estraeva stringhe, ordine, font e coordinate. Avvertiva già che l’ordine tecnico di un PDF a colonne può differire da quello visivo. Fonte: V1 §2.2.

**Stress / evidenza dei Round**  
Il limite è esplicito in V1. R4 §§R4.1/R4.6 richiede target, metodo e storia delle letture, senza renderle semanticamente certe. AUDIT §A.8 precisa che il testo incorporato non prova coincidenza con la rappresentazione visuale e lo distingue dall’OCR.

**Conclusione**  
La lettura nativa sopravvive come specializzazione dell’estrazione, con limiti propri. La formula più esplicita dell’audit non viene retrodatata come test specifico presente in ogni Round.

**Disposizione**  
SPECIALIZZAZIONE. Riscontro della disposizione: AUDIT §A.8 e §C.

**Destinazione**  
Gruppo/i 6. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H5 — estrazione da testo nativo; I/Documenti. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
Fondere lettura nativa e OCR cancellerebbe la possibilità di spiegare divergenze fra testo incorporato e ciò che la pagina mostra.

**Riferimenti puntuali**  
V1 §2.2; R4 §§R4.1/R4.6; disposizione successiva AUDIT §A.8; AUDIT §A.8 come registrazione successiva.


### 9 OCR

**Problema originario posseduto**  
Rilevare caratteri e alternative da immagini e scansioni.

**Forma in v1**  
Produceva testo localizzato, confidenza di lettura, metodo e alternative; non concludeva che un importo letto fosse dovuto o riferito al documento pertinente. Fonte: V1 §2.3.

**Stress / evidenza dei Round**  
R1 §R7 usa l’ambiguità 84,72/34,72 per mostrare che un importo atteso può guidare la lettura senza diventare conferma ottica indipendente. R2 §R2.6 preserva risultati per tentativo; R4 §§R4.1/R4.2 distingue qualità estrattiva e semantica.

**Conclusione**  
AUDIT §A.9 mantiene OCR come specializzazione, non come autorità semantica. Letture precedenti e qualità locale restano recuperabili anche dopo un tentativo riuscito.

**Disposizione**  
SPECIALIZZAZIONE. Riscontro della disposizione: AUDIT §A.9 e §C.

**Destinazione**  
Gruppo/i 6. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H5 — estrazione ottica e valutazioni locali. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
Una correzione contestuale potrebbe apparire osservazione diretta certa, oppure il retry cancellare le alternative che ne spiegavano l’incertezza.

**Riferimenti puntuali**  
V1 §2.3; R1 §R7; R2 §R2.6; R4 §§R4.1/R4.2; AUDIT §A.9 come registrazione successiva.


### 10 Layout Analyzer

**Problema originario posseduto**  
Rilevare l’organizzazione visuale e le relazioni spaziali utili alla comprensione.

**Forma in v1**  
Riconosceva blocchi, colonne, celle e adiacenze, senza equiparare la vicinanza fra etichetta e valore a una relazione di dominio. Fonte: V1 §2.4.

**Stress / evidenza dei Round**  
V1 contiene già il confine. R4 §R4.1 richiede valutazioni su bersagli locali: una buona lettura dei caratteri non prova una buona associazione strutturale. AUDIT §A.10 conserva le associazioni visuali come struttura osservata e ne dispone l’accorpamento.

**Conclusione**  
Sopravvive una capacità estrattiva strutturale distinta nel significato, anche se raccolta nello stesso gruppo delle altre estrazioni.

**Disposizione**  
ACCORPATO. Riscontro della disposizione: AUDIT §A.10 e §C.

**Destinazione**  
Gruppo/i 6. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H5 — analisi del layout con target/qualità locali. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
Senza la relazione visuale tracciata un valore potrebbe essere assegnato all’etichetta sbagliata e il successivo Mapping non permetterebbe di ricostruire l’errore.

**Riferimenti puntuali**  
V1 §2.4; R4 §R4.1; disposizione successiva AUDIT §A.10; AUDIT §A.10 come registrazione successiva.


### 11 Structure Detector

**Problema originario posseduto**  
Rendere riconoscibili campi, righe e sezioni sorgente riutilizzabili dal Mapping.

**Forma in v1**  
Produceva proposte di coppie etichetta–valore e strutture tabellari; non assegnava ruoli di dominio. Fonte: V1 §2.5.

**Stress / evidenza dei Round**  
V1 distingue struttura sorgente e significato. R4 §§R4.1/R4.7 richiede granularità sufficiente a qualificare e correggere parti diverse. AUDIT §A.11 riscontra il confine sottile con Layout Analyzer, conservando la differenza fra geometria e struttura composta.

**Conclusione**  
La capacità viene accorpata nell’estrazione, senza rendere intercambiabili osservazione geometrica, campo proposto e ruolo semantico.

**Disposizione**  
ACCORPATO. Riscontro della disposizione: AUDIT §A.11 e §C.

**Destinazione**  
Gruppo/i 6. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H5 — riconoscimento della struttura sorgente. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
Il Mapping riceverebbe frammenti senza poter distinguere una riga osservata da un’associazione inferita; un accorpamento improprio nasconderebbe errori strutturali locali.

**Riferimenti puntuali**  
V1 §2.5; R4 §§R4.1/R4.7; disposizione successiva AUDIT §A.11; AUDIT §A.11 come registrazione successiva.


### 12 Lexical Parser

**Problema originario posseduto**  
Riconoscere e normalizzare forme sintattiche mantenendo distinta la forma letta.

**Forma in v1**  
Riconosceva numeri, date, valute, codici e unità; 84,72 EUR normalizzato non significava ancora importo dovuto. Fonte: V1 §2.6.

**Stress / evidenza dei Round**  
R2C §5 distingue occorrenza, contenuto numerico e ruolo. R3 §R3.1 distingue i ruoli temporali: riconoscere una data non basta a chiamarla scadenza. AUDIT §A.12 vieta che la normalizzazione sovrascriva l’osservazione o nasconda una scelta semantica.

**Conclusione**  
Il parsing resta una capacità interna dell’estrazione. Quando la scelta richiede semantica, il suo significato e la sua giustificazione appartengono al percorso interpretativo pertinente.

**Disposizione**  
ACCORPATO. Riscontro della disposizione: AUDIT §A.12 e §C.

**Destinazione**  
Gruppo/i 6; passaggio a 7/8 quando occorre interpretare. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H5 — parsing sintattico; H6/H7 per significato. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
Un valore normalizzato potrebbe sembrare certo e originario, cancellando la forma ambigua o il ruolo che era ancora da interpretare.

**Riferimenti puntuali**  
V1 §2.6; R2C §5; R3 §R3.1; AUDIT §A.12 come registrazione successiva.


### 13 Observation Builder

**Problema originario posseduto**  
Rendere indirizzabile ciò che un processo ha rilevato, con localizzazione, metodo e qualificazioni.

**Forma in v1**  
Costruiva Observation a partire dalle letture, distinguendole dalle Assertion semanticamente interpretate. Fonte: V1 §2.7.

**Stress / evidenza dei Round**  
R2C §T2 respinge l’Observation come passaggio obbligatorio per ogni ingresso; §8.4 propone esplicitamente l’accorpamento con Extraction. R4, audit componenti, rafforza il contratto del risultato ma non dimostra un costruttore centrale. Un contributo strutturato non deve ricevere un’Observation fittizia.

**Conclusione**  
AUDIT §A.13 raccoglie la produzione delle Observation nell’estrazione: ogni produttore competente può produrre risultati indirizzabili. Si conserva la distinzione informativa, senza aggiungere un passaggio comune obbligatorio.

**Disposizione**  
ACCORPATO. Riscontro della disposizione: AUDIT §A.13 e §C.

**Destinazione**  
Gruppo/i 6. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H5 — produzione delle Observation; D per percorsi alternativi. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
Sopprimere il nome non permette di conservare frammenti senza origine e target; imporre il costruttore a tutti gli ingressi ricreerebbe una pipeline universale.

**Riferimenti puntuali**  
V1 §2.7; R2C §§T2/8.4; R4, audit componenti/Observation Builder; AUDIT §A.13 come registrazione successiva.


### 14 Extraction Quality Assessment

**Problema originario posseduto**  
Valutare errori e incertezze differenti prodotti dalle capacità estrattive.

**Forma in v1**  
Valutava OCR, immagine, completezza, layout, tabella e normalizzazione; già distingueva tali dimensioni dalla comprensione semantica. Fonte: V1 §2.8.

**Stress / evidenza dei Round**  
R1 §R7 ammette che i produttori forniscano direttamente qualificazioni. R4 §§R4.1/R4.9 e audit componenti richiede target, dimensione, base e storia: un buon OCR non rende buona una tabella ricostruita male. L’accorpamento è ancora possibile nel Round, la distribuzione è registrata in AUDIT §A.14.

**Conclusione**  
Gli assessment vengono prodotti dai processi estrattivi competenti, secondo il Quality Model condiviso. Un’eventuale sintesi non sostituisce target e basi locali.

**Disposizione**  
DISTRIBUITO. Riscontro della disposizione: AUDIT §A.14 e §C.

**Destinazione**  
Gruppo/i 6 — produttori estrattivi locali. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H5; G/I per modello, conservazione e natura degli assessment. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
Un unico punteggio del documento nasconderebbe l’errore locale che rende inutilizzabile proprio il campo consumato dall’interpretazione.

**Riferimenti puntuali**  
V1 §2.8; R1 §R7; R4 §§R4.1/R4.9 e audit componenti; AUDIT §A.14 come registrazione successiva.


### 15 Extraction Provenance Recorder

**Problema originario posseduto**  
Risalire dal risultato estrattivo al materiale, metodo, versione e tentativo che lo hanno prodotto.

**Forma in v1**  
Registrava Source, trasformazioni, tempi, parametri rilevanti e letture precedenti; non si limitava al valore finale. Fonte: V1 §2.9.

**Stress / evidenza dei Round**  
R4 §R4.6 separa Provenance, Lineage, storia epistemica e log operativo; §§R4.7/R4.8 precisano granularità e recuperabilità materiale. Il relativo audit mette in crisi il nome Recorder se suggerisce un unico registratore che ricostruisce tutto dopo l’esecuzione.

**Conclusione**  
AUDIT §A.15/G distribuisce la cattura presso i produttori e applicatori. La responsabilità estrattiva vive innanzitutto nel gruppo 6; il principio di cattura locale vale per le altre trasformazioni pertinenti. Conservazione, traversal e spiegazione restano distinti.

**Disposizione**  
DISTRIBUITO. Riscontro della disposizione: AUDIT §A.15 e §C.

**Destinazione**  
Gruppo/i 6 per l’origine estrattiva; obbligo trasversale dei produttori/applicatori; 18 per il solo recupero. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H5 e obblighi comuni H; G per conservazione; H17 traversal, H20 spiegazione. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
Un registratore a valle potrebbe inventare la storia mancante; accorpare il traversal non trasferisce a Query la produzione originaria delle tracce.

**Riferimenti puntuali**  
V1 §2.9; R4 §§R4.6–R4.8 e audit componenti/Provenance Recorder; AUDIT §A.15 come registrazione successiva.


## FASE 3 — INTERPRETAZIONE

### 16 Source Classifier

**Problema originario posseduto**  
Formulare contesti documentali e mapping plausibili per il materiale.

**Forma in v1**  
Usava contenuto, struttura e metadati per proporre famiglia documentale, fornitore e layout e selezionare mapping candidati; non ammetteva automaticamente le interpretazioni. Fonte: V1 §3.1.

**Stress / evidenza dei Round**  
R2 §R2.2 introduce Source con contenuti documentali molteplici. R5 §R5.9 e audit componenti mostrano che classificare il contenitore non determina tipo, numero o identità delle unità interne. Il nome diventa insufficiente per classificazioni locali.

**Conclusione**  
AUDIT §A.16 lo accorpa nell’Interpretation contestuale della Source e delle porzioni. Il risultato rimane una proposta utile al Mapping, non un tipo globale trasferibile a tutte le parti.

**Disposizione**  
ACCORPATO. Riscontro della disposizione: AUDIT §A.16 e §C.

**Destinazione**  
Gruppo/i 8; cooperazione con 7 per applicabilità del Mapping. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H7 — classificazione contestuale interna; H6 ne usa il contesto. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
Una fotografia con più documenti potrebbe ricevere un unico tipo che contamina le parti; la scelta del mapping potrebbe diventare implicita e non spiegabile.

**Riferimenti puntuali**  
V1 §3.1; R2 §R2.2; R5 §R5.9 e audit componenti/Source Classifier; AUDIT §A.16 come registrazione successiva.


### 17 Mapping Executor

**Problema originario posseduto**  
Applicare corrispondenze riutilizzabili fra forma sorgente e significato.

**Forma in v1**  
Riceveva Observation, classificazione e Mapping Definitions; produceva candidati di campo con versione del Mapping e supporto. Non riconciliava definitivamente né ammetteva. Fonte: V1 §3.3.

**Stress / evidenza dei Round**  
R3 §R3.9, caso Mapping, mostra che la stessa data può essere stata interpretata con una definizione poi modificata. R4 §R4.8 richiede di recuperare le parti delle risorse materialmente usate. La definizione è risorsa, la sua applicazione è lavoro con un risultato proprio.

**Conclusione**  
AUDIT §A.17 mantiene autonomo il problema di valutare applicabilità ed eseguire corrispondenze. Interpretation conserva il problema ulteriore di comporre il significato contestuale.

**Disposizione**  
MANTENUTO AUTONOMO. Riscontro della disposizione: AUDIT §A.17 e §C.

**Destinazione**  
Gruppo/i 7. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H6; G per Mapping Definitions e dipendenze; cooperazione con H7. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
Un campo semanticamente plausibile potrebbe perdere il riferimento alla definizione applicata, rendendo opaco l’impatto di una sua correzione.

**Riferimenti puntuali**  
V1 §3.3; R3 §R3.9; R4 §R4.8; AUDIT §A.17 come registrazione successiva.


### 18 Existing Knowledge Reader

**Problema originario posseduto**  
Fornire il contesto già disponibile senza riscrivere il significato del nuovo ingresso.

**Forma in v1**  
Consultava referenti, identificatori, affermazioni, conflitti e storia; avvertiva già che la nuova Source può contraddire ciò che Fold si aspetta. Fonte: V1 §3.6.

**Stress / evidenza dei Round**  
R2C §8.6 propone l’accorpamento nel recupero semantico, conservando qualificazioni e ammissione distinguibili. R5, audit componenti, conferma il possibile assorbimento in Query. R6 §IV, Interpretation↔Knowledge, richiede che il riuso del contesto non diventi autoconferma.

**Conclusione**  
AUDIT §A.18/A.29 lo accorpa in Query & Retrieval: è un uso interno del recupero, non un lettore che garantisce la verità del materiale consultato.

**Disposizione**  
ACCORPATO. Riscontro della disposizione: AUDIT §A.18 e §C.

**Destinazione**  
Gruppo/i 18. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H17; H7/H8 come consumatori del contesto. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
Il contesto potrebbe diventare una premessa invisibile o una conferma indipendente della conclusione che aveva contribuito a produrre.

**Riferimenti puntuali**  
V1 §3.6; R2C §8.6; R5, audit componenti/Existing Knowledge Reader; R6 §IV; AUDIT §A.18 come registrazione successiva.


### 19 Referent Candidate Generator

**Problema originario posseduto**  
Mantenere ipotesi su soggetti nuovi o già rappresentati senza saltare alla loro identità accettata.

**Forma in v1**  
Produceva candidati da identificatori, nomi e contesto, conservando indizi favorevoli, contrari e motivazioni; non fondeva definitivamente. Fonte: V1 §3.7.

**Stress / evidenza dei Round**  
R2C §8.7 segnala la sovrapposizione fra interpretazione e riconciliazione e il rischio che Generator implichi sempre nuovi oggetti. R5 §R5.4 mostra che riconciliare può produrre soltanto alternative di collegamento. R6 §V.1 consente il locus referenziale proposto senza confonderlo con esistenza accertata.

**Conclusione**  
AUDIT §A.19 distribuisce l’ipotesi di soggetto all’Interpretation e il confronto di coreferenza alla Reconciliation. Non esiste un generatore unico indispensabile.

**Disposizione**  
DISTRIBUITO. Riscontro della disposizione: AUDIT §A.19 e §C.

**Destinazione**  
Gruppo/i 8 e 9. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H7 — proposta referenziale; H8 — alternative di coreferenza; G memoria proposte. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
Una menzione potrebbe essere trasformata direttamente in identità ammessa; oppure la sparizione del Generator potrebbe eliminare le alternative ancora irrisolte.

**Riferimenti puntuali**  
V1 §3.7; R2C §8.7; R5 §R5.4; R6 §V.1; AUDIT §A.19 come registrazione successiva.


### 20 Evidence Construction

**Problema originario posseduto**  
Precisare quale origine o contributo sostenga quale contenuto e sotto quale aspetto.

**Forma in v1**  
Collegava Observation o regioni della Source a un’interpretazione candidata, distinguendo presenza del testo e verità del fatto rappresentato. Fonte: V1 §3.8.

**Stress / evidenza dei Round**  
R2C §§T4/8.8 mette in dubbio il costruttore autonomo senza eliminare il supporto. R4 §R4.4 lo colloca nei produttori competenti. GATE controllo 1 distingue contenuto, contributo attribuito e commitment: una dichiarazione non è automaticamente supporto adeguato.

**Conclusione**  
AUDIT §A.20 distribuisce i collegamenti fra Interpretation, Reconciliation, Verification e Derivation, mantenendo la giustificazione inferenziale distinta dall’evidenza documentale. AUDIT §F assegna anche le quote pertinenti al Mapping.

**Disposizione**  
DISTRIBUITO. Riscontro della disposizione: AUDIT §A.20 e §C.

**Destinazione**  
Gruppo/i 8, 9, 12 e 16; quota locale nel 7. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H7/H8/H11/H15 e H6 per collegamenti pertinenti; D/G/I/J. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
Una Source diventerebbe prova universale del documento, oppure una derivazione sarebbe contata come nuova evidenza indipendente delle proprie premesse.

**Riferimenti puntuali**  
V1 §3.8; R2C §§T4/8.8; R4 §R4.4; GATE §A/controllo 1; AUDIT §A.20 come registrazione successiva.


### 21 Interpretation Coordinator

**Problema originario posseduto**  
Comporre letture, mapping, contesto e riferimenti in una proposta semanticamente coerente.

**Forma in v1**  
Costruiva Candidate Knowledge Bundle, alternative, evidenze e informazioni mancanti; il nome Coordinator suggeriva anche un governo del lavoro non dimostrato dalla scheda. Fonte: V1 §3.9.

**Stress / evidenza dei Round**  
R1 §R4 chiarisce che è composizione semantica, non regia di tutte le attività. R2C §§T3/8.5 ammette proposte e dipendenze parziali. R5 §R5.10 e R6 §VI.C separano la memoria delle proposte da Work attivo e Knowledge ammessa.

**Conclusione**  
AUDIT §A.21 mantiene la responsabilità ridefinita come Interpretation. Il bundle non è un gate atomico e produrre un risultato non implica ammetterlo. La visibilità degli esiti parziali di H7 resta nell’apertura C04.

**Disposizione**  
MANTENUTO / RIDEFINITO. Riscontro della disposizione: AUDIT §A.21 e §C.

**Destinazione**  
Gruppo/i 8. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H7 — composizione semantica; F per Work; G per proposte. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
Ridurre tutto a campi mappati perderebbe il significato composto; chiamare Coordinator la composizione potrebbe ripristinare una regia universale o far sparire risultati parziali.

**Riferimenti puntuali**  
V1 §3.9; R1 §R4; R2C §§T3/8.5; R5 §R5.10; R6 §VI.C; AUDIT §A.21 come registrazione successiva.


### 22 Semantic Quality Assessment

**Problema originario posseduto**  
Valutare l’incertezza del significato separatamente dalla correttezza della lettura.

**Forma in v1**  
Distingueva confidenza OCR, Mapping, Interpretation e qualità della riconciliazione; non presumeva equivalenza delle dimensioni. Fonte: V1 §3.10.

**Stress / evidenza dei Round**  
R4 §§R4.1/R4.9 e audit componenti mantiene target e basi delle singole valutazioni: una classificazione buona non garantisce un’attribuzione corretta. R1 §R7 aveva già escluso una fase Quality completa una volta per tutte.

**Conclusione**  
AUDIT §A.22 distribuisce gli assessment semantici fra Mapping, Interpretation e Reconciliation. Il Quality Model rimane condiviso, senza ulteriore valutatore centrale tra Interpretation e Knowledge.

**Disposizione**  
DISTRIBUITO. Riscontro della disposizione: AUDIT §A.22 e §C.

**Destinazione**  
Gruppo/i 7, 8 e 9. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H6/H7/H8; G/I per modello e storia della Quality. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
Un unico grado di confidenza ereditato dall’intero bundle nasconderebbe il campo ambiguo o il collegamento errato proprio dove si decide di usarlo.

**Riferimenti puntuali**  
V1 §3.10; R1 §R7; R4 §§R4.1/R4.9 e audit componenti; AUDIT §A.22 come registrazione successiva.


## FASE 4 — CONOSCENZA E RAGIONAMENTO

### 23 Candidate Validator

**Problema originario posseduto**  
Diagnosticare violazioni, incompletezza e incompatibilità di una proposta prima del suo uso.

**Forma in v1**  
Controllava forme Core, tipi, vincoli, completezza e conflitti nel Candidate Knowledge; già non aveva normalmente autorità di ammissione. Fonte: V1 §4.1.

**Stress / evidenza dei Round**  
R2C §§T3/8.9 indebolisce il Candidate universale mantenendo i controlli. R5, audit componenti, riconosce nome fuorviante e possibile accorpamento. R6 §§III.3/III.11 distingue proposte eterogenee, giudizi di validazione e applicazione governata.

**Conclusione**  
AUDIT §A.23 distribuisce i controlli ai produttori locali, a Comparison e ad Admission. La premessa del validatore universale viene superata; il bisogno di diagnosi non viene eliminato.

**Disposizione**  
DISTRIBUITO. Riscontro della disposizione: AUDIT §A.23 e §C.

**Destinazione**  
Gruppo/i 6, 7, 8, 9, 10 e 17. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H5–H9 — controlli locali e Comparison; H16 — invarianti/applicabilità. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
Eliminare il Validator insieme al Candidate universale potrebbe lasciare proposte senza controlli; trasferire tutto ad Admission la renderebbe un nuovo decisore semantico.

**Riferimenti puntuali**  
V1 §4.1; R2C §§T3/8.9; R5, audit componenti/Candidate Validator; R6 §§III.3/III.11; AUDIT §A.23 come registrazione successiva.


### 24 Quality Assessment

**Problema originario posseduto**  
Produrre valutazioni concrete che una risorsa descrittiva Quality Model non produce da sola.

**Forma in v1**  
Raccoglieva elementi di qualità di Source, estrazione, semantica, riconciliazione e verifica, rendendoli disponibili alle decisioni. Fonte: V1 §4.3.

**Stress / evidenza dei Round**  
R1 §R7 rende la qualità incrementale. R4 §§R4.1/R4.2/R4.9 distingue target, attività, risultato storico e criteri d’azione: Admission non aumenta la solidità e ripetere la stessa conclusione non aggiunge supporto.

**Conclusione**  
AUDIT §A.24 assegna gli assessment a produttori e verificatori competenti. Possono esistere sintesi per scopo, purché conservino basi locali; la scelta applicativa rimane distinta.

**Disposizione**  
DISTRIBUITO. Riscontro della disposizione: AUDIT §A.24 e §C.

**Destinazione**  
Gruppo/i Produttori/verificatori competenti, in particolare 6–12 e 16; 15 consulta le valutazioni. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
Obblighi comuni H, H5–H11/H15 secondo il target; Quality Model e assessment in G/I. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
Senza valutazioni locali la Policy riceverebbe risultati senza basi di prudenza; un valutatore unico potrebbe produrre un truth score o attribuire qualità per la sola Admission.

**Riferimenti puntuali**  
V1 §4.3; R1 §R7; R4 §§R4.1/R4.2/R4.9; AUDIT §A.24 come registrazione successiva.


### 25 Core Engine

**Problema originario posseduto**  
Fornire capacità di confronto, riconciliazione, valutazione temporale, derivazione e ricostruzione spiegabile.

**Forma in v1**  
Raccoglieva nove meccanismi su Knowledge e candidati, dichiarando già di non possedere implicitamente la prudenza del prodotto. Fonte: V1 §4.4.

**Stress / evidenza dei Round**  
R3, delta componenti, distingue confronto, tempo, correzione e ricostruzione. R4 §R4.10 separa significato, meccanismo e Policy. R6 §V.9 e GATE controlli 2–3 distinguono impatto, esito inferenziale e seguito operativo. Nessuno di questi introduce un’autorità ulteriore sopra i meccanismi.

**Conclusione**  
AUDIT §A.25/B lo riclassifica come famiglia; REG L09 conferma che rimuovere la scatola non elimina le capacità. I nove percorsi sono preservati separatamente sotto. Impact Assessment è l’esplicitazione acquisita nei Round, non un’aggiunta di questo documento.

**Disposizione**  
RICLASSIFICATO. Riscontro della disposizione: AUDIT §A.25 e §C.

**Destinazione**  
Gruppo/i 9–14 come famiglia di ragionamento; quote di 4, 8, 17 e 18 secondo 25a–25i. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H8–H13; H3/H7/H16/H17 per capacità distribuite; nessuna H del Core Engine sopra i meccanismi. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
La rimozione dell’etichetta potrebbe cancellare confronto o ragionamento; mantenerla come decisore comune duplicherebbe le responsabilità e assorbirebbe impropriamente la Policy.

**Riferimenti puntuali**  
V1 §4.4; R3, delta E; R4 §R4.10; R6 §V.9; GATE controlli 2–3; REG §B2/L09; AUDIT §A.25 come registrazione successiva.


### 26 Policy Evaluation

**Problema originario posseduto**  
Scegliere il comportamento autorizzato per una situazione concreta mediante le policy applicabili.

**Forma in v1**  
Produceva una Disposition motivata da assessment, bersaglio e policy; non eseguiva verifica, fusione o notifica. Fonte: V1 §4.6.

**Stress / evidenza dei Round**  
R1 §R6 mostra autorità esplicite e riprese che non richiedono una nuova valutazione prudenziale; R3 §R3.10 distingue decisione storica e applicabilità. GATE controlli 2–3 vieta alla Policy di cancellare impatto accertato o decidere la validità inferenziale.

**Conclusione**  
AUDIT §A.26 mantiene la valutazione ridefinendone confine e scope. Decision, Disposition e Application restano distinte; REG D06 mantiene aperta l’ownership della formalizzazione non-Policy.

**Disposizione**  
MANTENUTO / RIDEFINITO. Riscontro della disposizione: AUDIT §A.26 e §C.

**Destinazione**  
Gruppo/i 15. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H14; E governance, F applicazione e O/D06. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
La Policy potrebbe diventare l’origine obbligatoria di ogni autorità oppure decidere quali fatti siano semanticamente validi. Questa genealogia non assegna a H14 i percorsi non-Policy.

**Riferimenti puntuali**  
V1 §4.6; R1 §R6; R3 §R3.10; GATE controlli 2–3; REG §B1/D06; AUDIT §A.26 come registrazione successiva.


### 27 Verification Workflow

**Problema originario posseduto**  
Ottenere una verifica mirata conservando domanda, materiale mostrato, risposta e contesto.

**Forma in v1**  
Riceveva richiesta e target, formulava domande e produceva una Verification Decision, nomenclatura che poteva unificare risposte di natura diversa. Fonte: V1 §4.7.

**Stress / evidenza dei Round**  
R2 §§R2.4/R2.5 distingue lettura confermata, fatto dichiarato, link e autorizzazione. R2C §8.12 conserva l’attesa durevole senza esecuzione continua. R3 §R3.10 mostra che una risposta tardiva non si estende a un target cambiato.

**Conclusione**  
AUDIT §A.27 mantiene ridefinita la gestione della verifica: contributo, assessment e stato del Work non coincidono con una Decision di Admission. Il contratto uniforme di applicabilità alla ripresa rimane aperto in C01.

**Disposizione**  
MANTENUTO / RIDEFINITO. Riscontro della disposizione: AUDIT §A.27 e §C.

**Destinazione**  
Gruppo/i 16; usa 23 per l’ingresso e 24 per la continuità. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H15; H22 — Intake; F — Work. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
Un «sì» tardivo potrebbe autorizzare o confermare più di ciò che era stato mostrato; la chiusura del Work potrebbe essere scambiata per aumento di certezza.

**Riferimenti puntuali**  
V1 §4.7; R2 §§R2.4/R2.5; R2C §8.12; R3 §R3.10; AUDIT §A.27 come registrazione successiva.


### 28 Knowledge Admission & State Management

**Problema originario posseduto**  
Applicare commitment e revisioni autorizzate mantenendo il percorso precedente.

**Forma in v1**  
Associava accepted, provisional, contested, corrected e superseded a Candidate/Knowledge e ne registrava transizioni e supporti. Già distingueva accepted da verità assoluta. Fonte: V1 §4.8.

**Stress / evidenza dei Round**  
R1 §R6 distingue verifica d’applicabilità da nuova scelta. R2C §6 e R4 §R4.2 smontano lo stato unico: qualità, incompletezza, Work e ammissione hanno bersagli diversi. R6 §V.2 e GATE controllo 1 precisano commitment su Referent/Assertion senza trasformare l’origine del claim.

**Conclusione**  
AUDIT §A.28 conserva Admission ridefinita; non le attribuisce tutti gli stati informativi. Applica la disposizione pertinente, controlla effetto già applicato e condizioni, conserva storia e mancata applicazione.

**Disposizione**  
MANTENUTO / RIDEFINITO. Riscontro della disposizione: AUDIT §A.28 e §C.

**Destinazione**  
Gruppo/i 17; gli altri stati restano ai produttori e al 24. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H16 — governance; E/G per commitment/storia; F per operatività. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
Un esito tecnico o una conferma verrebbero promossi a Knowledge senza autorità; concentrare tutti gli stati qui fonderebbe qualità, conflitto, tempo e lavoro.

**Riferimenti puntuali**  
V1 §4.8; R1 §R6; R2C §6; R4 §R4.2; R6 §V.2; GATE controllo 1; AUDIT §A.28 come registrazione successiva.


## FASE 5 — FUNZIONI

### 29 Query & Retrieval

**Problema originario posseduto**  
Recuperare materiale pertinente mantenendone significato, stato e qualificazioni.

**Forma in v1**  
Rispondeva soprattutto a domande applicative su Knowledge, evidenze, conflitti e derivazioni; non decideva semanticamente fonte prevalente, pagamento o identità. Fonte: V1 §5.1.

**Stress / evidenza dei Round**  
R2 §R2.3 e R2C §8.15 distinguono ritrovare materiale/stringhe da recuperare ciò che Fold sostiene. R3 §R3.3 distingue storia allora conosciuta e ricostruzione attuale del passato. R4 §R4.8 separa recuperare, spiegare e rieseguire.

**Conclusione**  
AUDIT §A.29/A.18/B.25i mantiene il recupero ridefinito e vi accorpa lettura del contesto e traversal. Il risultato negativo resta delimitato; C05 sui diversi perimetri di corpus resta aperta.

**Disposizione**  
MANTENUTO / RIDEFINITO. Riscontro della disposizione: AUDIT §A.29 e §C.

**Destinazione**  
Gruppo/i 18. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H17 — accesso semantico e traversal; D/G per materiale e storie. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
Un risultato potrebbe appiattire proposte e commitment o trasformare «nessun risultato nel corpus» in «non avvenuto». Assorbire traversal non significa produrre la storia mancante.

**Riferimenti puntuali**  
V1 §5.1; R2 §R2.3; R2C §8.15; R3 §R3.3; R4 §R4.8; AUDIT §A.29 come registrazione successiva.


### 30 Projection Builder

**Problema originario posseduto**  
Organizzare risultati determinati per lo scopo di una rappresentazione applicativa.

**Forma in v1**  
Componeva schede e riepiloghi selezionando conoscenza; se serviva risolvere tempo o conflitti rinviava al ragionamento. Fonte: V1 §5.2.

**Stress / evidenza dei Round**  
R3 §R3.3 distingue Current Reconstruction e Projection. R5, audit componenti/Projection Builder, consente viste unitarie secondo coreferenza ammessa senza distruggere rappresentazioni. GATE controllo 2 impedisce di presentare come aggiornato un risultato affetto senza rispettarne la qualificazione.

**Conclusione**  
AUDIT §A.30 mantiene autonomo il problema di composizione. Aggregazioni che producono nuovo significato richiedono Derivation; la presentazione non assorbe la ricostruzione.

**Disposizione**  
MANTENUTO AUTONOMO. Riscontro della disposizione: AUDIT §A.30 e §C.

**Destinazione**  
Gruppo/i 19. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H18; richiede H11/H12 per nuove conclusioni o ricostruzioni; usa H17. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
Una vista potrebbe scegliere silenziosamente la fonte vera o sommare elementi non equivalenti; la coalescenza visuale potrebbe diventare fusione irreversibile.

**Riferimenti puntuali**  
V1 §5.2; R3 §R3.3; R5, audit componenti/Projection Builder; GATE controllo 2; AUDIT §A.30 come registrazione successiva.


### 31 Application Functions

**Problema originario posseduto**  
Realizzare risultati utili e comportamenti autorizzati per i casi d’uso.

**Forma in v1**  
Proponeva acquisizione, ricerca, collegamenti, aggregazioni, scadenze e spiegazioni; separava significato Domain, ragionamento e prudenza applicativa. Fonte: V1 §5.3.

**Stress / evidenza dei Round**  
R1 §R1 consente di entrare da una domanda su dati già presenti. R3 §§R3.3/R3.6 richiede tempo di riferimento e comportamento promesso; GATE controlli 2–3 distingue la conclusione dalla scelta di notificare o avviare lavoro.

**Conclusione**  
AUDIT §A.31 mantiene una famiglia ridefinita di responsabilità per casi d’uso: può attivare altri percorsi e registrare effetti, non è l’ultimo stadio obbligatorio. Applicabilità uniforme C01 e uso di contenuti impattati C03 restano aperti.

**Disposizione**  
MANTENUTO / RIDEFINITO. Riscontro della disposizione: AUDIT §A.31 e §C.

**Destinazione**  
Gruppo/i 20; cooperazione con 24. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H19 — funzioni e Application; F per Work; E per autorità. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
Senza un proprietario l’azione finirebbe dispersa fra interfaccia e ragionamento; una funzione potrebbe convertire l’autorizzazione in prova del fatto o ignorare impatti noti.

**Riferimenti puntuali**  
V1 §5.3; R1 §R1; R3 §§R3.3/R3.6; GATE controlli 2–3; AUDIT §A.31 come registrazione successiva.


### 32 Explanation Composer

**Problema originario posseduto**  
Rendere comprensibile la giustificazione effettiva di ciò che Fold mostra.

**Forma in v1**  
Percorreva la Lineage e componeva una spiegazione da Source, lettura, Mapping, referente e decisione; vietava narrazioni soltanto plausibili. Fonte: V1 §5.4.

**Stress / evidenza dei Round**  
R4 §R4.8 e audit componenti separa recupero, spiegazione e riesecuzione. GATE controllo 1 richiede contenuto, contributori, supporto e commitment distinti; il numero di percorsi non prova indipendenza.

**Conclusione**  
AUDIT §A.32 mantiene la composizione autonoma nel problema. Usa il traversal del gruppo 18, senza sostituirsi al produttore della giustificazione o inventare collegamenti mancanti. La recuperabilità delle basi materiali resta necessaria.

**Disposizione**  
MANTENUTO AUTONOMO. Riscontro della disposizione: AUDIT §A.32 e §C.

**Destinazione**  
Gruppo/i 21; consuma 18. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H20 — spiegazione; H17 — recupero; G — basi/storie. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
Mostrare soltanto tracce grezze non spiegherebbe la conclusione; costruire una narrazione a posteriori potrebbe nascondere assenza di supporto, origine comune o limiti di verificabilità.

**Riferimenti puntuali**  
V1 §5.4; R4 §R4.8 e audit componenti/Explanation Composer; GATE controllo 1; AUDIT §A.32 come registrazione successiva.


### 33 Presentation Layer

**Problema originario posseduto**  
Rendere percepibili informazioni, qualificazioni, esiti e azioni disponibili.

**Forma in v1**  
Mostrava stati, evidenze, incertezza e conflitti, vietando esplicitamente il passaggio linguistico da probabile a certo o da non confermato a non pagato. Fonte: V1 §5.5.

**Stress / evidenza dei Round**  
Il limite è già esplicito in V1. GATE controllo 2 vieta la presentazione non qualificata di risultati materialmente affetti quando usati come aggiornati. Non emerge la necessità di un nuovo decisore di significato al confine dell’interfaccia.

**Conclusione**  
AUDIT §A.33 mantiene la presentazione come problema autonomo. Semplificare la forma espressiva non modifica natura o solidità della conoscenza e non applica Admission.

**Disposizione**  
MANTENUTO AUTONOMO. Riscontro della disposizione: AUDIT §A.33 e §C.

**Destinazione**  
Gruppo/i 22. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H21 — confine di presentazione; coopera con H18/H20. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
Le qualificazioni potrebbero esistere nella memoria ma sparire per l’utente; «nessuna conferma» potrebbe essere mostrato come un fatto negativo accertato.

**Riferimenti puntuali**  
V1 §5.5; GATE controllo 2; AUDIT §A.33 come registrazione successiva.


### 34 Feedback Handler

**Problema originario posseduto**  
Acquisire correzioni, dichiarazioni e scelte dell’utente senza mutazioni silenziose della Knowledge.

**Forma in v1**  
Instradava interazioni verso Verification o Interpretation. L’esempio parlava di nuova Verification Decision e poteva comprimere contenuto ricevuto, interpretazione e autorizzazione. Fonte: V1 §5.6.

**Stress / evidenza dei Round**  
R2 §R2.4 distingue cinque ruoli dei contributi; R2C §T1 lega il «sì» alla domanda presentata. R3 §R3.10 conserva lo scope tardivo. REG D01 rileva nell’assemblaggio la perdita della base umana originaria; D06 mantiene incerta l’ownership della formalizzazione non-Policy.

**Conclusione**  
AUDIT §A.34 mantiene il problema ridefinito come acquisizione e instradamento contestualizzato. Il recupero successivo D01 in ASM2/H22 conserva la base originale distinta dall’Interpretation. Non si assegna qui al confine di ingresso la formalizzazione di ogni Decision.

**Disposizione**  
MANTENUTO / RIDEFINITO. Riscontro della disposizione: AUDIT §A.34 e §C.

**Destinazione**  
Gruppo/i 23; instradamento a 8, 16 e percorsi di governance pertinenti. I numeri rimandano alla mappa dei 24 nella sezione 5, non a nuovi componenti.

**Collocazione v2.1**  
H22 — User Contribution Intake; H7/H15; E/O per D06. Localizzazione successiva: candidata §§H/K e viste indicate.

**Rischio di perdita**  
Un contributo umano verrebbe riscritto come interpretazione certa o autorizzazione globale; una risposta tardiva potrebbe colpire un target diverso da quello originario.

**Riferimenti puntuali**  
V1 §5.6; R2 §R2.4; R2C §T1; R3 §R3.10; REG §§B1/D01/D06; AUDIT §A.34 come registrazione successiva.

## 4. Core Engine — genealogia dei nove meccanismi interni

La tabella verifica e preserva i nove esiti di AUDIT §B contro V1 e i passaggi dei Round. Nessuna riga incrementa il conteggio dei 34. Le disposizioni qui riportate riguardano le sottocapacità, non riclassificano il n. 25, che resta RICLASSIFICATO.

| ID | Meccanismo storico | Forma originaria e stress | Disposizione in AUDIT §B | Destinazione 24 → H/v2.1 | Conclusione e rischio di perdita | Fonti originali e confronto |
|---|---|---|---|---|---|---|
| 25a | Identity Reconciliation | V1 §4.4.1 confrontava identificatori, attributi e contesto per proporre corrispondenze. R2C §8.10 distingue identità da «documento riguarda utenza»; R5 §§R5.3–R5.5 separa stringa, assegnazione, coreferenza e fusione. | MANTENUTO / RIDEFINITO | 9 → H8; E per gli effetti autorizzati | Produce proposta, alternative e assessment. Non effettua merge distruttivo o Admission. Perdere le rappresentazioni precedenti impedirebbe di contestare una coreferenza. | V1 §4.4.1; R2C §8.10; R5 §§R5.3–R5.5; REG D05 |
| 25b | Document Identity Reconciliation | V1 §4.4.2 raccoglieva stesso documento, copia, versione e rettifica. R2C §8.11 propone l’accorpamento; R5, sezione dedicata, mostra quattro problemi con semantiche diverse. | DISTRIBUITO | 4 → H3; 8 → H7; 9 → H8; 10/11 → H9/H10; 17 → H16 per l’effetto correttivo | Dedup tecnica, composizione/grouping, sola coreferenza documentale e versione/correzione conservano proprietari distinti. Un PDF e una fotografia non sono diversi documenti per i soli byte; una rettifica non è una semplice copia. Nessun riconciliatore documentale universale. | V1 §4.4.2; R2C §8.11; R5, Document Identity Reconciliation; R3 §R3.5 |
| 25c | Comparison | V1 §4.4.3 confrontava contenuti dello stesso significato. R3 §R3.5 e R4, audit componenti, richiedono prima referente, ruolo, tempo e scope comparabili. | MANTENUTO AUTONOMO | 10 → H9 | Rileva differenze e relazioni pertinenti senza scegliere quale fonte seguire. Saltare la comparabilità trasformerebbe una successione temporale in conflitto o due importi di natura diversa in disaccordo. | V1 §4.4.3; R3 §R3.5; R4, audit componenti/Comparison |
| 25d | Temporal Evaluation | V1 §4.4.4 enumerava tempi di Source, acquisizione, validità e verifica. R3 §§R3.1/R3.2 separa ruoli del contenuto, storia informativa/operativa e reference time; R6 §V.6 ne preserva le distinzioni. | MANTENUTO / RIDEFINITO | 11 → H10; cooperazione con 13 → H12 | Valuta tempi ricevuti con il loro significato, senza inventarli né decidere l’azione applicativa. Equiparare ultimo arrivo e stato corrente renderebbe falsa la ricostruzione dopo un’informazione tardiva. | V1 §4.4.4; R3 §§R3.1/R3.2; R6 §V.6 |
| 25e | Conflict Detection | V1 §4.4.5 esponeva un rilevatore separato. R3, delta E, e R5, audit componenti, riconoscono l’incompatibilità come possibile esito specializzato di Comparison. | SPECIALIZZAZIONE | 10 → H9 | AUDIT §B.25e formalizza la specializzazione: il conflitto resta informazione anche se una Policy autorizza l’uso di una fonte. Accorpare il rilevatore non elimina conflitto, target e motivazione e non ne decide la soluzione. | V1 §4.4.5; R3, delta E; R5, audit componenti/Conflict Detection |
| 25f | Correction / Supersession | V1 §4.4.6 raccoglieva nuovo fatto, rettifica, reinterpretazione e sostituzione. R3 §R3.5 distingue rettifica, successione, conflitto e ritardo; GATE chiarisce contributi rettificati e impatto. | DISTRIBUITO | 8/10 → H7/H9; 11 → H10; 17 → H16; 14 → H13 | Interpretation/Comparison riconoscono la relazione, il tempo distingue successione, Governance applica la revisione autorizzata e Impact Assessment ne considera le dipendenze. Rilevare una rettifica non autorizza la sostituzione globale né riscrive l’errore come valore prima vero. | V1 §4.4.6; R3 §§R3.5/R3.8/R3.9; GATE controlli 1–2 |
| 25g | Derivation | V1 §4.4.7 produceva conclusioni da premesse e regola. R3 §R3.4 distingue attività, conclusione e giustificazione; R4 §R4.4 distingue quest’ultima dal supporto documentale. GATE controllo 3 corregge il confine con Policy. | MANTENUTO AUTONOMO | 12 → H11 | La conclusione conserva premesse, criterio e contesto materiali. Policy governa attivazione/usi, non validità semantica. La derivazione non è un’Observation né una nuova conferma indipendente delle proprie premesse. | V1 §4.4.7; R3 §R3.4; R4 §R4.4; GATE controllo 3 |
| 25h | Current-State Derivation | V1 §4.4.8 già escludeva l’ultimo valore come stato corrente. R3 §R3.3 mostra che ricostruire per tempo e scopo può combinare recupero, selezione e ragionamento senza produrre sempre una nuova Assertion. | MANTENUTO / RIDEFINITO | 13 → H12 — Current Reconstruction | AUDIT §B.25h registra il nuovo nome contestuale. GATE controllo 2 richiede di rispettare l’impatto noto. La Reconstruction non è Projection né necessariamente nuova Derivation; deve poter mantenere alternative e limiti. C03/C06 restano aperte. | V1 §4.4.8; R3 §R3.3; GATE controllo 2 |
| 25i | Provenance Traversal | V1 §4.4.9 univa Explanation e percorso della Lineage, mentre §5.4 esponeva già il Composer. R4 §§R4.6/R4.8 distingue cattura, accesso, spiegazione e riesecuzione. | ACCORPATO | 18 → H17; consumato da 21 → H20 e dai meccanismi competenti | AUDIT §B.25i assegna il traversal al recupero. Trovare le dipendenze non significa averle prodotte, valutarne ogni effetto o comporre la spiegazione. Trasferire tutto a un Recorder/Composer centrale perderebbe questi confini. | V1 §§4.4.9/5.4; R4 §§R4.6/R4.8 |

Tutti e nove gli esiti attesi trovano riscontro. In particolare, 25b non è trasferito interamente a H8: solo la coreferenza documentale ne è una specializzazione. Per 25f il riconoscimento semantico e l’applicazione della revisione rimangono separati. Il controllo delle fonti ha inoltre rilevato rinvii secondari non allineati ai numeri 25g/25h/25b, registrati nella sezione 8 senza modificare il Ledger.

### Impact Assessment e limiti della famiglia

Il gruppo 14 non proviene da una decima sottovoce inventata oggi. R3 §§R3.8/R3.9 aveva distinto risultati affetti, basi della dipendenza e seguito operativo; R6 §V.9 aveva assegnato la valutazione d’impatto a un meccanismo; GATE controllo 2 aveva richiesto una qualificazione informativa recuperabile che la Policy non può cancellare. AUDIT §E/F lo registra come esplicitazione necessaria e ASM1 lo espone in H13.

Questa storia spiega perché il passaggio dai 34 non sia una semplice operazione di rinomina uno-a-uno. La Policy governa quando e come rivalutare; il Work esegue il seguito autorizzato; Impact Assessment mantiene il problema di individuare e qualificare ciò che è coinvolto. Il presente documento non assegna nuovi criteri d’uso ai contenuti impattati.

## 5. Mappa delle 24 responsabilità / gruppi di copertura

Questa è la mappa di AUDIT §F, seguita attraverso ASM1 §K, REG D07, ASM2 §K e candidata v2.1 §K. Le quote distribuite sono esplicitate mediante le schede AUDIT §A/G; non sono nuovi proprietari creati dalla genealogia. I numeri nella colonna “provenienza” sono quelli dell’inventario v1.

| # gruppo | Responsabilità / gruppo di copertura | Provenienza e quote dell’inventario storico | Collocazione H/v2.1 | Natura e confine preservato |
|---|---|---|---|---|
| 1 | Acquisition from channel / Acquisizione dal canale | 1 | H1 — adattamento della consegna | Capacità interna distinta dalla registrazione. |
| 2 | Acquisition registration/governance / Registrazione e governo dell’acquisizione | 2; condizioni pertinenti di 5 | H1 — registrazione dell’Acquisition e collegamento al risultato | Capacità interna; storia della ricezione, non governo di tutti i Work. |
| 3 | Technical validation / Validazione tecnica | 3 | H2 | Responsabilità autonoma del problema tecnico. |
| 4 | Technical identification/dedup / Identificazione e deduplicazione tecnica | 4; quota tecnica di 25b | H3 | Responsabilità autonoma; distinta dall’identità semantica. |
| 5 | Source preservation / Preservazione delle Source | 6 | H4; G | Responsabilità di conservazione del contenuto originario. |
| 6 | Extraction + Observation production / Estrazione e produzione delle Observation | 7–13; quote locali di 14, 15 e 23 | H5 | Aggregazione con lettura nativa/OCR, layout, struttura e parsing distinguibili. |
| 7 | Mapping evaluation/execution / Valutazione ed esecuzione del Mapping | 17; quote di 20, 22–24 e cattura locale | H6 | Responsabilità con assessment, supporto e controlli locali. |
| 8 | Semantic composition/Interpretation / Composizione semantica | 16, 21; quote di 19, 20, 22, 23 e 25b | H7 | Composizione, classificazione e proposte interne; non regia di tutti i lavori. |
| 9 | Identity Reconciliation | 25a; quote di 19/25b e assessment/controlli pertinenti | H8 | Meccanismo; coreferenza documentale come specializzazione. |
| 10 | Comparison + content relation recognition / Confronto e relazioni fra contenuti | 25c, 25e; quote semantiche di 25f e 23 | H9 | Meccanismo con esiti distinguibili; conflitto specializzato. |
| 11 | Temporal Evaluation | 25d; aspetti temporali di 25f | H10 | Meccanismo temporale contestualizzato. |
| 12 | Derivation | 25g; assessment inferenziale e giustificazione locali | H11 | Meccanismo; conclusione distinta dall’attivazione e dall’uso. |
| 13 | Current Reconstruction | 25h | H12 | Meccanismo distinto dalla Projection. |
| 14 | Impact Assessment | Esplicitazione acquisita R3/R6/GATE; famiglia 25 e Lineage | H13 | Meccanismo; non pianifica autonomamente ogni rivalutazione. |
| 15 | App Decision Policy evaluation / Valutazione delle Application Decision Policies | 26 | H14 | Governance; non origine universale di ogni Decision. |
| 16 | Verification work management / Gestione del lavoro di verifica | 27; supporti/assessment pertinenti | H15; F | Verifica mirata che usa il piano Work. |
| 17 | Admission + governance revisions / Admission e revisioni di governance | 28; quota applicativa di 25f; controlli finali di 23 | H16; E/G | Governance dell’applicazione dei commitment. |
| 18 | Query & Retrieval contextual / Recupero contestualizzato | 29, 18, 25i | H17 | Accesso a contenuti/storie; comprende traversal, non la cattura. |
| 19 | Projection composition / Composizione delle Projection | 30 | H18 | Composizione applicativa; non nuova semantica implicita. |
| 20 | Application cases/use/disposition execution / Casi d’uso e applicazione delle disposizioni | 31 | H19; E/F | Funzioni per caso d’uso; nessun controllore universale. |
| 21 | Explanation composition / Composizione delle spiegazioni | 32; consumo del traversal di 25i | H20 | Composizione fedele delle giustificazioni recuperate. |
| 22 | Faithful presentation / Presentazione fedele | 33 | H21 | Confine di presentazione. |
| 23 | Contextual user contribution acquisition / Acquisizione contestualizzata dei contributi utente | 34 | H22 | Confine d’ingresso del contributo; base originaria e significato distinti. |
| 24 | Operational Work coordination / Coordinamento operativo dei Work | Aspetti di 5; trasversali v1; supporto a 2, 27 e 31 | F/G; presso i proprietari delle attività | Piano operativo trasversale; non richiede una scheda H autonoma. |

Validazione, assessment, supporto e cattura della Provenance sono obblighi locali dei produttori/applicatori competenti. Non ricevono ciascuno un ulteriore gruppo universale e non vengono eliminati perché non hanno una H dedicata. La colonna delle quote non significa che ogni attività debba esercitare tutti quegli obblighi in ogni occasione.

Le memorie conservano risultati e storie; non sostituiscono chi li produce. Il Quality Model è una risorsa condivisa; Query consente il recupero; Explanation compone la spiegazione. Queste tre destinazioni non assorbono la produzione locale degli assessment.

## 6. Perché 24 gruppi diventano 22 schede H

Il passaggio è documentato già in ASM1 §K, prima della v2.1:

1. I gruppi **1 e 2** sono due capacità interne della stessa **H1 — Ricezione tracciata**: adattamento della consegna e registrazione dell’acquisizione. REG D07 giudica giustificata questa aggregazione perché entrambi i problemi restano riconoscibili.
2. I gruppi **3–23** sono esposti rispettivamente in **H2–H22**, come riportato riga per riga nella tabella.
3. Il gruppo **24** è esposto nelle viste **F/G**, presso i proprietari delle attività. Non riceve una H da coordinatore centrale.

Il conteggio dell’esposizione è quindi **1 scheda per i gruppi 1–2 + 21 schede per i gruppi 3–23 = 22 H**. Il coordinamento dei Work rimane presente senza una scheda autonoma.

Non sono scomparse due responsabilità: una coppia condivide una scheda e una responsabilità trasversale è esposta nel piano operativo. “Autonomo” nell’audit e “scheda H autonoma” nell’assemblaggio non sono sinonimi. Neppure le 22 H sono dichiarate confini software.

La composizione è distinta anche sul piano dei problemi:

- H1 conserva la storia della ricezione; il Work conserva l’avanzamento dei lavori, anche successivi.
- H14 valuta le Policy; H15 ottiene verifiche; H16 applica commitment; H19 realizza gli altri comportamenti autorizzati.
- H5 conserva sottocapacità estrattive differenti; H7 conserva composizione, classificazione e proposte; la loro esposizione unitaria non prova atomicità dell’elaborazione.
- H17 recupera e percorre tracce; H20 le usa per spiegare; i produttori originari rimangono responsabili della cattura.

Questa ricostruzione non assegna la formalizzazione delle Decision non-Policy a uno dei gruppi per completare il diagramma. D06 resta aperto.

## 7. Matrice finale di tracciabilità e contabilità

### Matrice dei 34

La matrice è l’indice delle 34 schede, non un secondo inventario. Ogni elemento possiede una sola scheda genealogica e una sola riga in questa matrice. Le fonti originali sono distinte dai riferimenti all’audit successivo: per tutte le righe la disposizione è riscontrata in AUDIT §A, scheda del medesimo numero, e §C; la destinazione si controlla in AUDIT §F/G e negli assemblaggi.

| v1 # | Componente | Disposizione | Destinazione 24 | Collocazione H/v2.1 | Fonti primarie |
|---|---|---|---|---|---|
| 1 | Channel Adapter | MANTENUTO AUTONOMO | 1 | H1 — capacità interna di adattamento della consegna; G per Provenance | V1 §1.1; R2 §R2.7; R4 §R4.3; REG §B1/D07 |
| 2 | Acquisition Controller | MANTENUTO / RIDEFINITO | 2; collaborazione con 24 | H1 — registrazione dell’Acquisition; F e gruppo 24 per avanzamento operativo | V1 §1.2; R1 §R3; R2 §R2.7; R2C §8.1; REG §B1/D07 |
| 3 | Technical Validation | MANTENUTO AUTONOMO | 3 | H2 — validazione tecnica; cooperazione con H1/H4 e condizioni operative | V1 §1.3; R1 §R2; R2C §8.2 |
| 4 | Fingerprinting / Technical Deduplication | MANTENUTO AUTONOMO | 4 | H3 — identificazione/deduplicazione tecnica; storia delle Acquisition in H1 | V1 §1.4; R3 §R3.9; R5 §R5.9 e Document Identity Reconciliation |
| 5 | Staging / Technical Lifecycle | RICLASSIFICATO | 24; condizioni di ingresso pertinenti a 2 e 3 | F/G — piano e memoria operativi; condizioni tecniche in H1/H2/H4 | V1 §1.5; R1 §R5; R2 §R2.6; R2C §9 |
| 6 | Source Preservation | MANTENUTO / RIDEFINITO | 5 | H4; G — memoria delle Source/rappresentazioni; I per distinzione documentale | V1 §1.6; R2 §R2.3; R2C §§T1/8.3; R5 §R5.9 |
| 7 | Format Decoder | ACCORPATO | 6 | H5 — capacità interna di decodifica | V1 §2.1; R2C §8.2; disposizione successiva AUDIT §A.7 |
| 8 | Text Extraction | SPECIALIZZAZIONE | 6 | H5 — estrazione da testo nativo; I/Documenti | V1 §2.2; R4 §§R4.1/R4.6; disposizione successiva AUDIT §A.8 |
| 9 | OCR | SPECIALIZZAZIONE | 6 | H5 — estrazione ottica e valutazioni locali | V1 §2.3; R1 §R7; R2 §R2.6; R4 §§R4.1/R4.2 |
| 10 | Layout Analyzer | ACCORPATO | 6 | H5 — analisi del layout con target/qualità locali | V1 §2.4; R4 §R4.1; disposizione successiva AUDIT §A.10 |
| 11 | Structure Detector | ACCORPATO | 6 | H5 — riconoscimento della struttura sorgente | V1 §2.5; R4 §§R4.1/R4.7; disposizione successiva AUDIT §A.11 |
| 12 | Lexical Parser | ACCORPATO | 6; passaggio a 7/8 quando occorre interpretare | H5 — parsing sintattico; H6/H7 per significato | V1 §2.6; R2C §5; R3 §R3.1 |
| 13 | Observation Builder | ACCORPATO | 6 | H5 — produzione delle Observation; D per percorsi alternativi | V1 §2.7; R2C §§T2/8.4; R4, audit componenti/Observation Builder |
| 14 | Extraction Quality Assessment | DISTRIBUITO | 6 — produttori estrattivi locali | H5; G/I per modello, conservazione e natura degli assessment | V1 §2.8; R1 §R7; R4 §§R4.1/R4.9 e audit componenti |
| 15 | Extraction Provenance Recorder | DISTRIBUITO | 6 per l’origine estrattiva; obbligo trasversale dei produttori/applicatori; 18 per il solo recupero | H5 e obblighi comuni H; G per conservazione; H17 traversal, H20 spiegazione | V1 §2.9; R4 §§R4.6–R4.8 e audit componenti/Provenance Recorder |
| 16 | Source Classifier | ACCORPATO | 8; cooperazione con 7 per applicabilità del Mapping | H7 — classificazione contestuale interna; H6 ne usa il contesto | V1 §3.1; R2 §R2.2; R5 §R5.9 e audit componenti/Source Classifier |
| 17 | Mapping Executor | MANTENUTO AUTONOMO | 7 | H6; G per Mapping Definitions e dipendenze; cooperazione con H7 | V1 §3.3; R3 §R3.9; R4 §R4.8 |
| 18 | Existing Knowledge Reader | ACCORPATO | 18 | H17; H7/H8 come consumatori del contesto | V1 §3.6; R2C §8.6; R5, audit componenti/Existing Knowledge Reader; R6 §IV |
| 19 | Referent Candidate Generator | DISTRIBUITO | 8 e 9 | H7 — proposta referenziale; H8 — alternative di coreferenza; G memoria proposte | V1 §3.7; R2C §8.7; R5 §R5.4; R6 §V.1 |
| 20 | Evidence Construction | DISTRIBUITO | 8, 9, 12 e 16; quota locale nel 7 | H7/H8/H11/H15 e H6 per collegamenti pertinenti; D/G/I/J | V1 §3.8; R2C §§T4/8.8; R4 §R4.4; GATE §A/controllo 1 |
| 21 | Interpretation Coordinator | MANTENUTO / RIDEFINITO | 8 | H7 — composizione semantica; F per Work; G per proposte | V1 §3.9; R1 §R4; R2C §§T3/8.5; R5 §R5.10; R6 §VI.C |
| 22 | Semantic Quality Assessment | DISTRIBUITO | 7, 8 e 9 | H6/H7/H8; G/I per modello e storia della Quality | V1 §3.10; R1 §R7; R4 §§R4.1/R4.9 e audit componenti |
| 23 | Candidate Validator | DISTRIBUITO | 6, 7, 8, 9, 10 e 17 | H5–H9 — controlli locali e Comparison; H16 — invarianti/applicabilità | V1 §4.1; R2C §§T3/8.9; R5, audit componenti/Candidate Validator; R6 §§III.3/III.11 |
| 24 | Quality Assessment | DISTRIBUITO | Produttori/verificatori competenti, in particolare 6–12 e 16; 15 consulta le valutazioni | Obblighi comuni H, H5–H11/H15 secondo il target; Quality Model e assessment in G/I | V1 §4.3; R1 §R7; R4 §§R4.1/R4.2/R4.9 |
| 25 | Core Engine | RICLASSIFICATO | 9–14 come famiglia di ragionamento; quote di 4, 8, 17 e 18 secondo 25a–25i | H8–H13; H3/H7/H16/H17 per capacità distribuite; nessuna H del Core Engine sopra i meccanismi | V1 §4.4; R3, delta E; R4 §R4.10; R6 §V.9; GATE controlli 2–3; REG §B2/L09 |
| 26 | Policy Evaluation | MANTENUTO / RIDEFINITO | 15 | H14; E governance, F applicazione e O/D06 | V1 §4.6; R1 §R6; R3 §R3.10; GATE controlli 2–3; REG §B1/D06 |
| 27 | Verification Workflow | MANTENUTO / RIDEFINITO | 16; usa 23 per l’ingresso e 24 per la continuità | H15; H22 — Intake; F — Work | V1 §4.7; R2 §§R2.4/R2.5; R2C §8.12; R3 §R3.10 |
| 28 | Knowledge Admission & State Management | MANTENUTO / RIDEFINITO | 17; gli altri stati restano ai produttori e al 24 | H16 — governance; E/G per commitment/storia; F per operatività | V1 §4.8; R1 §R6; R2C §6; R4 §R4.2; R6 §V.2; GATE controllo 1 |
| 29 | Query & Retrieval | MANTENUTO / RIDEFINITO | 18 | H17 — accesso semantico e traversal; D/G per materiale e storie | V1 §5.1; R2 §R2.3; R2C §8.15; R3 §R3.3; R4 §R4.8 |
| 30 | Projection Builder | MANTENUTO AUTONOMO | 19 | H18; richiede H11/H12 per nuove conclusioni o ricostruzioni; usa H17 | V1 §5.2; R3 §R3.3; R5, audit componenti/Projection Builder; GATE controllo 2 |
| 31 | Application Functions | MANTENUTO / RIDEFINITO | 20; cooperazione con 24 | H19 — funzioni e Application; F per Work; E per autorità | V1 §5.3; R1 §R1; R3 §§R3.3/R3.6; GATE controlli 2–3 |
| 32 | Explanation Composer | MANTENUTO AUTONOMO | 21; consuma 18 | H20 — spiegazione; H17 — recupero; G — basi/storie | V1 §5.4; R4 §R4.8 e audit componenti/Explanation Composer; GATE controllo 1 |
| 33 | Presentation Layer | MANTENUTO AUTONOMO | 22 | H21 — confine di presentazione; coopera con H18/H20 | V1 §5.5; GATE controllo 2 |
| 34 | Feedback Handler | MANTENUTO / RIDEFINITO | 23; instradamento a 8, 16 e percorsi di governance pertinenti | H22 — User Contribution Intake; H7/H15; E/O per D06 | V1 §5.6; R2 §R2.4; R2C §T1; R3 §R3.10; REG §§B1/D01/D06 |

### Contabilità delle disposizioni

La contabilità è ricavata dalle disposizioni delle schede e confrontata con AUDIT §A/C. Le etichette attese nel mandato non sono state usate per forzare un esito differente dalle fonti.

| Disposizione | Numero | Elementi v1 |
|---|---:|---|
| MANTENUTO AUTONOMO | 7 | 1, 3, 4, 17, 30, 32, 33 |
| MANTENUTO / RIDEFINITO | 9 | 2, 6, 21, 26, 27, 28, 29, 31, 34 |
| ACCORPATO | 7 | 7, 10, 11, 12, 13, 16, 18 |
| DISTRIBUITO | 7 | 14, 15, 19, 20, 22, 23, 24 |
| SPECIALIZZAZIONE | 2 | 8, 9 |
| RICLASSIFICATO | 2 | 5, 25 |
| ELIMINATO PURAMENTE | 0 | Nessuno |
| **Totale** | **34** | Una disposizione principale per elemento |

**7 + 9 + 7 + 7 + 2 + 2 = 34.** Nessuna discrepanza di conteggio rispetto all’audit storico. I nove meccanismi interni e le responsabilità trasversali non sono stati aggiunti alla somma.

Zero eliminazioni pure non significa che sopravvivano 34 autonomie: 18 elementi sono accorpati, distribuiti, specializzati o riclassificati. La conservazione della responsabilità è ciò che impedisce di interpretare queste trasformazioni come cancellazioni.

## 8. Evidence gap, possibili regressioni e aperture preservate

### EG-01 — rinvii del Ledger non allineati alla numerazione dell’audit interno

È stato rilevato un **EVIDENCE GAP di citazione secondaria**, non una perdita dimostrata della conoscenza:

| Rinvio osservato nel Ledger | Contenuto effettivo dell’AUDIT originale | Fonte del percorso disponibile |
|---|---|---|
| K-072/K-073, relative a Current-State Derivation / Current Reconstruction, citano AUDIT §25g | 25g è Derivation; Current-State Derivation è 25h | R3 §R3.3 e AUDIT §B.25h sostengono il percorso. |
| K-133, relativa ai quattro problemi di Document Identity Reconciliation, cita AUDIT §25h | 25h è Current-State Derivation; Document Identity Reconciliation è 25b | R5, sezione Document Identity Reconciliation, e AUDIT §B.25b sostengono il percorso. |

La genealogia cita le sezioni originali effettivamente consultate, ma registra il disallineamento e non modifica gli artefatti precedenti, gli stati delle voci o le loro conclusioni. Il gap riguarda la precisione dei rinvii: non impedisce questa distillazione perché i testi originari sono disponibili e identificati. La correzione del Ledger è fuori dal presente mandato.

Non è stata dimostrata una regressione strutturale della candidata durante questa ricostruzione. Questa constatazione non è un esito del Model Preservation Gate, che non è stato eseguito.

### Risultati aperti conservati come aperti

C01–C07, F2d e D06 restano nella loro destinazione attuale. In particolare questo documento non:

- uniforma il controllo di applicabilità nei rami Verification/Work/Application;
- decide il rapporto fra base predittiva e riscontro negativo;
- stabilisce i criteri d’uso dei contenuti impattati;
- decide la visibilità degli esiti parziali di H7;
- risolve la distinzione operativa fra corpus richiesto, accessibile ed esaminato;
- autorizza nuovi criteri per considerare proposte non ammesse nelle Reconstruction;
- assegna l’ownership della formalizzazione non-Policy;
- assegna un produttore o un meccanismo per il cambiamento di versione F2d.

Non si reintroducono Candidate Validator universale, Quality controller, Provenance Recorder centrale o orchestratore semantico per colmare tali aperture. Non viene costruita qui la genealogia Core/primitive: i concetti sono citati solo nella misura necessaria a spiegare le trasformazioni delle responsabilità.

### Limite documentale residuo

L’archivio originale resta esterno al repository. Questo documento ne distilla i problemi, i passaggi e le conseguenze necessari a leggere la genealogia dei componenti senza riaprire la chat; ordinal e hash consentono un controllo delle fonti. Non è un’esportazione integrale dei Round né una dichiarazione che tutte le loro conoscenze siano state duplicate qui.

## 9. Controlli conclusivi dell’artefatto

| Controllo | Esito |
|---|---|
| Schede genealogiche 1–34 | 34/34, numeri univoci, tutti gli otto campi obbligatori presenti. |
| Matrice finale dei 34 | Esattamente 34 righe, coerenti con le schede. |
| Disposizioni rispetto ad AUDIT §A/C | 7/9/7/7/2/2; nessuna forzatura o discrepanza. |
| Eliminazioni pure | Zero, come nell’audit. |
| Meccanismi interni | Tutti i 9, 25a–25i; esclusi dal conteggio dei 34. |
| Mappa dei gruppi | Tutti i 24 gruppi, con provenienza e destinazione. |
| Passaggio 24 → 22 H | Esplicito: 1–2 in H1; 3–23 in H2–H22; 24 nel piano operativo. |
| Nuove H o responsabilità | Nessuna; anche Impact Assessment è ricondotto ai passaggi storici. |
| Nuove teorie o stati genealogici | Nessuno; nessuna apertura trasformata in decisione. |
| Candidata e altri artefatti protetti | Invariati nel confronto SHA-256 dei 25 file preesistenti sotto docs. |
| Source Readiness / Knowledge Preservation | Non rieseguiti. |
| Model Preservation Gate | Non eseguito. |
| Genealogia Core/primitive | Non creata. |

Il risultato è l’artefatto di preservazione dei componenti richiesto da FOL-40. Non autorizza freeze, implementazione, chiusura di FOL-36 o approvazione complessiva del modello.

## 10. Stato Git e integrità

Branch invariato: `main`. HEAD invariato: `ef3b24f450e21173c07563aee02c96ef39babcf7`.

Il nuovo file è esclusivamente `docs/ricerca/fold-component-responsibility-genealogy-2026-09-05.md`. La candidata conserva SHA-256 `98ef21e3128b217afaa863c616fc3c12eb579507103b495ffcc9c7f90e8de754`.

Non sono stati modificati Source Map, Ledger, Coverage, delta, snapshot o Gate. Nessuna operazione Linear, Notion o Fold Sync; nessun commit, push o branch.

Stato finale:

```text
?? docs/ricerca/fold-anatomia-v2.1-candidate-2026-09-04.md
?? docs/ricerca/fold-component-responsibility-genealogy-2026-09-05.md
?? docs/ricerca/fold-knowledge-preservation-gate-v2.1-2026-09-04.md
?? docs/ricerca/fold-knowledge-preservation-recheck-v2.1-2026-09-05.md
?? docs/ricerca/fold-model-preservation-source-map-2026-09-05.md
```
