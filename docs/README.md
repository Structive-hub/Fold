# Documentazione di Fold

**Status:** Canonical  
**Scope:** governo della conoscenza nel repository

## Scopo

Questa cartella contiene la conoscenza che deve poter essere compresa anche senza accesso alle conversazioni esterne al repository.

Il repository non deve diventare un archivio indiscriminato di tutto ciò che è stato discusso. Deve distinguere chiaramente tra evidenza, lavoro in corso, decisioni consolidate e specifiche implementabili.

Repository e Linear devono contenere insieme il contesto sufficiente perché Codex possa continuare il progetto. Notion resta utile per ricerca estesa, intuizioni, percorso narrativo e case study, ma non deve contenere requisiti o stato operativo indispensabili e assenti dalle prime due fonti.

## Struttura

### `metodo-di-lavoro.md`
Metodo corrente con cui Fold viene esplorato, progettato, documentato, realizzato e verificato. Definisce anche il passaggio dall'esplorazione alla memoria persistente.

### `product/`
Definizione corrente del prodotto e del perimetro del MVP: problema, comportamento, utenti, scope e vincoli di prodotto già consolidati.

### `architecture/`
Modello concettuale e architettura tecnica quando vengono verificati e consolidati.

### `decisions/`
Decisioni importanti che devono restare comprensibili nel tempo, incluse motivazione, conseguenze ed eventuali decisioni sostituite.

### `specs/`
Specifiche di funzioni o componenti sufficientemente mature da guidare l'implementazione e la verifica.

### `milestones/`
Sintesi storiche autosufficienti delle milestone concluse. Riassumono e collegano il lavoro senza duplicare integralmente issue e checkpoint. Nelle milestone ricostruite retrospettivamente possono indicare, in una sezione separata, le evoluzioni già note al momento della ricostruzione; dopo il consolidamento non diventano registri continuamente aggiornati.

### `ricerca/`
Ricerca, evidenze e analisi. Il contenuto di questa cartella non diventa automaticamente una regola di Fold.

## Stati ammessi

Ogni documento significativo deve dichiarare uno stato vicino all'inizio:

- `Canonical` — conoscenza sufficientemente consolidata per guidare il lavoro corrente;
- `Draft` — materiale in elaborazione che può sostenere esplorazione e progettazione, ma non costituisce implicitamente requisito implementativo;
- `Research` — evidenza o analisi, non automaticamente decisione;
- `Historical` — fotografia di una fase precedente;
- `Superseded` — documento sostituito da una fonte successiva esplicitamente indicata.

Per un documento `Superseded`, `Superseded by:` è obbligatorio. `Supersedes:` può essere indicato quando un nuovo documento sostituisce esplicitamente una fonte precedente.

Il processo con cui una conoscenza viene consolidata come `Canonical` è definito in `metodo-di-lavoro.md`.

## Precedenza

Una fonte più recente non prevale soltanto perché è più recente. La precedenza deve derivare dalla sua natura e da un'esplicita decisione di consolidamento.

In caso di divergenza:

1. seguire una sostituzione esplicitamente dichiarata;
2. privilegiare le decisioni e specifiche canoniche pertinenti;
3. non usare ricerca o materiale storico per correggere implicitamente una decisione canonica;
4. se la divergenza rimane irrisolta, considerarla un problema progettuale da chiarire prima dell'implementazione.

## Materiale precedente già presente

### `fondamenti-fold.md`
È la prima baseline formale del progetto, creata il 19 agosto 2026. Ha valore storico e contiene decisioni che hanno guidato una fase precedente, ma non costituisce automaticamente il modello corrente di Fold.

Ciò che resta valido deve vivere nei documenti canonici appropriati. Per il lavoro corrente fanno fede le fonti canoniche pertinenti.

### `ricerca/bollette-luce-gas-arera.md`
Materiale di ricerca sul dominio delle utenze. Non definisce il modello generale di Fold.

### `ricerca/semantica-identificatori.md`
Materiale di ricerca sul significato degli identificatori osservati nelle bollette. Non definisce da solo il modello generale degli identificatori di Fold.

## Mappa degli artefatti del lavoro concettuale

Questa mappa risponde alla domanda «quale documento devo leggere per capire X?». Non cambia lo stato dei documenti e non trasforma ricerca, verifiche o memorie genealogiche in specifiche implementative.

Chiave di autorità:

- i documenti `Canonical` nelle cartelle di prodotto, architettura, decisioni e specifiche restano i riferimenti consolidati secondo il loro scope;
- la baseline v2.1 congelata resta `Draft`, mentre genealogie, Source Map, Gate e coverage sono ricerca o evidenza di verifica;
- il Ledger è memoria di controllo e genealogia, non modello operativo;
- lo snapshot v2 è `Historical`;
- nessuno di questi stati viene promosso dalla sola presenza nella mappa.

### Baseline concettuale congelata per la falsificazione

#### [`ricerca/fold-anatomia-v2.1-candidate-2026-09-04.md`](ricerca/fold-anatomia-v2.1-candidate-2026-09-04.md)

È la baseline v2.1 congelata e il riferimento corrente per la falsificazione FOL-37. Resta `Draft`, non canonica, non validata sui casi domestici o cross-domain e non autorizza implementazione. Il filename conserva `candidate` per mantenere la tracciabilità storica dei Gate già prodotti; il freeze non la promuove a documento di architettura.

- **Freeze date:** 2026-09-06
- **SHA-256:** `f5d109ead9f896801657f738d91ab81066d6da171535439605032c7c4a8dc057`

### Genealogia di componenti e responsabilità

#### [`ricerca/fold-component-responsibility-genealogy-2026-09-05.md`](ricerca/fold-component-responsibility-genealogy-2026-09-05.md)

Ricostruisce il percorso dai 34 componenti storici, attraverso le trasformazioni e i 24 gruppi di copertura, fino alle 22 schede H e al piano operativo della candidata. Serve a capire perché l'anatomia attuale non coincide con le precedenti 34 scatole. Ha stato `Research — Model Preservation`: documenta la genealogia, non definisce componenti software.

### Genealogia del Core e dei concetti

#### [`ricerca/fold-core-concept-genealogy-2026-09-05.md`](ricerca/fold-core-concept-genealogy-2026-09-05.md)

Ricostruisce il percorso da concetti iniziali e stress progettuali a primitive fortemente sostenute, distinzioni necessarie, governance, aperture e forme universali non sostenute. Serve in particolare a comprendere perché `Referent` e `Assertion` abbiano uno stato diverso da `Identifier`, `Value`, `Source`, `Observation` e dalle altre forme considerate. Ha stato `Research — Model Preservation` e non promuove le forme candidate.

### Memoria di controllo e genealogia delle conoscenze

#### [`ricerca/fold-knowledge-decision-ledger-2026-09-04.md`](ricerca/fold-knowledge-decision-ledger-2026-09-04.md)

Conserva la genealogia, la formulazione e lo stato delle conoscenze emerse nel percorso. È una **memoria di controllo / genealogia**: non è il modello operativo di Fold, non è una sorgente runtime e non deve essere tradotto K-ID per K-ID nell'implementazione.

### Knowledge Preservation

- [`ricerca/fold-knowledge-preservation-gate-v2.1-2026-09-04.md`](ricerca/fold-knowledge-preservation-gate-v2.1-2026-09-04.md) — primo Gate, **NON SUPERATO**;
- patch controllata — applicata alla candidata in risposta ai finding autorizzati;
- [`ricerca/fold-knowledge-preservation-recheck-v2.1-2026-09-05.md`](ricerca/fold-knowledge-preservation-recheck-v2.1-2026-09-05.md) — re-check mirato, **SUPERATO**.

Questa sequenza ha autorizzato il passaggio al lavoro di Model Preservation. Non ha autorizzato freeze, implementazione o validazione sui casi reali.

### Model Preservation

- [`ricerca/fold-model-preservation-source-map-2026-09-05.md`](ricerca/fold-model-preservation-source-map-2026-09-05.md) — identifica le fonti originali usate per rendere ricostruibili le due genealogie;
- [`ricerca/fold-model-preservation-gate-v2.1-2026-09-06.md`](ricerca/fold-model-preservation-gate-v2.1-2026-09-06.md) — verifica la preservazione e la ricostruibilità dell'evoluzione strutturale; **MODEL PRESERVATION GATE SUPERATO**.

Il Gate è evidenza di verifica: non rende la candidata canonica, congelata, validata o pronta per l'implementazione.

### Storia e baseline precedente

- [`ricerca/fold-anatomia-v2-snapshot-2026-09-04.md`](ricerca/fold-anatomia-v2-snapshot-2026-09-04.md) — snapshot immutabile e `Historical` della candidata v2 precedente alla review indipendente;
- [`ricerca/fold-delta-v2-v2.1-2026-09-04.md`](ricerca/fold-delta-v2-v2.1-2026-09-04.md) — registro `Draft` delle destinazioni e dei ripristini autorizzati fra v2 e v2.1; non è un'anatomia;
- [`ricerca/fold-coverage-ledger-v2-2026-09-04.md`](ricerca/fold-coverage-ledger-v2-2026-09-04.md) — evidenza `Research` della copertura fra Ledger e snapshot v2.

Questi artefatti permettono di ricostruire la baseline precedente e il delta, ma non rappresentano la baseline v2.1 corrente congelata.

### Altra ricerca e modelli esplorativi precedenti

#### [`ricerca/fondamenti-rappresentazione-conoscenza.md`](ricerca/fondamenti-rappresentazione-conoscenza.md)
Ricerca metodologica e fondazionale su realtà vs conoscenza, identità, tempo, provenienza, revisione, relazioni ed eventi. Serve a far emergere distinzioni necessarie senza scegliere primitive o tecnologie in anticipo. Ha stato `Research`.

#### [`ricerca/esempio-operativo-core-dominio.md`](ricerca/esempio-operativo-core-dominio.md)
Worked example neutro che mette sotto pressione la separazione analitica tra rappresentazione della realtà, Domain, conoscenza del sistema e meccanismi. Ha stato `Research` e non definisce un'architettura.

#### [`architecture/core-domain-working-model.md`](architecture/core-domain-working-model.md)
Working model esplorativo precedente, con stato `Draft`. Conserva ipotesi e questioni da falsificare, ma non è la baseline concettuale corrente congelata né una specifica implementabile.

## Passaggio verso il repository

Non ogni esplorazione produce memoria persistente. Il passaggio concettuale è:

```text
esplorazione
     ↓
classificazione dell'esito
     ↓
persistenza nella fonte appropriata
     ↓
eventuale consolidamento nel repository
     ↓
realizzazione e verifica
```

La classificazione degli esiti e le regole operative per intuizioni, cambiamenti progettuali, checkpoint, fallback e chiusure sono definite in `metodo-di-lavoro.md`.
