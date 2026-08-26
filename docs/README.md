# Documentazione di Fold

**Status:** Canonical  
**Scope:** governo della conoscenza nel repository

## Scopo

Questa cartella contiene la conoscenza che deve poter essere compresa anche senza accesso alle conversazioni esterne al repository.

Il repository non deve diventare un archivio indiscriminato di tutto ciò che è stato discusso. Deve distinguere chiaramente tra evidenza, lavoro in corso, decisioni consolidate e specifiche implementabili.

## Struttura

### `product/`
Definizione corrente del prodotto e del perimetro del MVP: problema, comportamento, utenti, scope e vincoli di prodotto già consolidati.

### `architecture/`
Modello concettuale e architettura tecnica quando vengono verificati e consolidati.

### `decisions/`
Decisioni importanti che devono restare comprensibili nel tempo, incluse motivazione, conseguenze ed eventuali decisioni sostituite.

### `specs/`
Specifiche di funzioni o componenti sufficientemente mature da guidare l'implementazione e la verifica.

### `ricerca/`
Ricerca, evidenze e analisi. Il contenuto di questa cartella non diventa automaticamente una regola di Fold.

## Stati ammessi

Ogni nuovo documento significativo dovrebbe dichiarare uno stato vicino all'inizio:

- `Canonical` — conoscenza corrente approvata;
- `Draft` — ancora in elaborazione;
- `Research` — evidenza o analisi;
- `Historical` — fotografia di una fase precedente;
- `Superseded` — sostituito, con riferimento alla fonte successiva.

Quando utile, aggiungere anche `Supersedes:` o `Superseded by:`.

## Precedenza

Una fonte più recente non prevale soltanto perché è più recente. La precedenza deve derivare dalla sua natura e da un'esplicita decisione di consolidamento.

In caso di divergenza:

1. seguire una sostituzione esplicitamente dichiarata;
2. privilegiare le decisioni e specifiche canoniche pertinenti;
3. non usare ricerca o materiale storico per correggere implicitamente una decisione canonica;
4. se la divergenza rimane irrisolta, considerarla un problema progettuale da chiarire prima dell'implementazione.

## Materiale precedente già presente

### `fondamenti-fold.md`
È la prima baseline formale del progetto, creata il 19 agosto 2026. Ha valore storico e contiene decisioni che hanno guidato la fase successiva, ma **non va trattata oggi come descrizione automaticamente canonica dell'intero modello di Fold**: il core informativo è attualmente sottoposto a nuova verifica e alcune distinzioni si sono evolute.

Per ora il file viene preservato senza riscriverlo. Le parti che superano la verifica corrente verranno promosse nei documenti canonici appropriati; le altre resteranno come storia progettuale.

### `ricerca/bollette-luce-gas-arera.md`
Materiale di ricerca sul dominio delle utenze. Non definisce il modello generale di Fold.

### `ricerca/semantica-identificatori.md`
Materiale di ricerca sul significato degli identificatori osservati nelle bollette. Non definisce da solo il modello generale degli identificatori di Fold.

## Passaggio verso il repository

Il flusso desiderato è:

```text
ricerca / conversazione / lavoro in Linear
                ↓
       conclusione verificata
                ↓
    consolidamento nel repository
                ↓
       specifica implementabile
                ↓
              Codex
                ↓
      implementazione + verifica
```

Una conversazione non è una dipendenza accettabile dell'implementazione.