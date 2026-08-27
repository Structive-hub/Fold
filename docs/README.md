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
