# Esempio operativo neutro di separazione tra realtà, conoscenza e motore

**Status:** Research  
**Data:** 2026-08-30  
**Scope:** analisi esemplificativa per mettere sotto pressione le distinzioni tra rappresentazione della realtà, conoscenza del sistema, dominio e meccanismi; non costituisce architettura canonica

## Scopo

Questa ricerca usa un caso volutamente neutro per verificare se abbia senso distinguere, almeno analiticamente:

- strutture con cui rappresentare ciò di cui si parla;
- semantica specifica fornita da un dominio;
- strutture con cui rappresentare ciò che il sistema sostiene di sapere;
- meccanismi che operano su quella conoscenza.

La tripartizione è un modello di ragionamento, non una lista di primitive approvate.

## Scenario

Esiste un oggetto fisico chiamato **Thing-42**. Il sistema deve conoscere in quale posto si trova. I posti possibili sono **Place-A** e **Place-B**.

Il mini-dominio stabilisce soltanto:

```text
TrackedThing è un tipo di Thing
Place è un tipo di Thing

locatedAt:
    TrackedThing → Place

vincolo:
    nello stesso istante uno stesso TrackedThing
    non può essere locatedAt in due Place differenti
```

Il vincolo è importante: un motore generico può confrontare due relazioni, ma non può inventare autonomamente che due valori di `locatedAt` siano incompatibili. Questa informazione appartiene alla semantica del dominio.

## Separazione analitica usata nell'esempio

| Livello | Domanda | Esempi illustrativi |
| --- | --- | --- |
| Rappresentazione della realtà | Di che cosa posso parlare? | Thing, Relation, Value, Identifier |
| Domain | Che cosa significano queste strutture qui? | TrackedThing, Place, locatedAt, vincolo di unicità |
| Rappresentazione della conoscenza | Che cosa sostiene il sistema e perché? | Assertion, Evidence, valid-time, knowledge-time, derivation, verification |
| Meccanismi | Che cosa faccio con tutto questo? | reconcile, detect conflict, supersede, derive current state, trace provenance |

Questa tabella non prova che le categorie debbano esistere esattamente in questa forma. Serve a osservare problemi differenti senza confonderli.

## Primo ingresso — dato proveniente da una sorgente

Il 1 febbraio arriva:

```json
{
  "tag": "Q7",
  "place": "A",
  "effective_from": "2026-02-01"
}
```

Questo è input. Non è ancora conoscenza canonica.

Un processo di interpretazione deve stabilire, usando mapping e semantica disponibile, che:

```text
"Q7" → identificatore di un TrackedThing
"A" → identificatore di un Place
"effective_from" → inizio della validità dichiarata
```

La riconciliazione collega `Q7` al referente interno `Thing-42`.

Una possibile rappresentazione della conoscenza risultante è:

```text
A1

proposition:
    Thing-42 locatedAt Place-A

valid-time:
    [2026-02-01, ?)

knowledge-time:
    2026-02-01 09:05

evidence:
    API-message-101

source:
    API-source-1

verification:
    accepted
```

I campi sono illustrativi. Il punto importante è la distinzione fra ciò che viene sostenuto, quando dovrebbe valere e quando il sistema lo ha appreso.

## Secondo ingresso — nuova osservazione

Il 10 febbraio un sensore produce:

```text
tag Q7 observed at Place-B
observation time: 2026-02-10 14:00
```

Il sistema può conservare una nuova affermazione:

```text
A2

Thing-42 locatedAt Place-B
valid-time: 2026-02-10 14:00
knowledge-time: 2026-02-10 14:00:05
evidence: SensorReading-55
verification: provisional
```

Ora esistono due affermazioni:

```text
A1: Thing-42 locatedAt Place-A
A2: Thing-42 locatedAt Place-B
```

Il Domain informa il motore che `locatedAt` è esclusiva nello stesso istante.

Il sistema non dovrebbe inventare l'istante preciso del passaggio da A a B. Può sapere soltanto che esistono evidenze compatibili con un cambiamento e che il momento esatto resta indeterminato.

## Terzo ingresso — conoscenza tardiva

Il 20 febbraio viene acquisito un documento che dichiara:

```text
Thing-42 transferred to Place-B
effective: 2026-02-04
```

Si può produrre:

```text
A3

Thing-42 locatedAt Place-B
valid-time: [2026-02-04, ?)
knowledge-time: 2026-02-20
evidence: Document-7
verification: accepted
```

Qui emerge una distinzione decisiva:

```text
quando sarebbe vero:
4 febbraio

quando il sistema lo scopre:
20 febbraio
```

Il 20 febbraio non è necessariamente la data di un cambiamento nel mondo. È la data in cui cambia la conoscenza del sistema.

## Quarto ingresso — correzione

Il 21 febbraio arriva una correzione:

```text
Correction to Document-7:
effective date was 2026-02-05, not 2026-02-04
```

Una possibile gestione non distruttiva è:

```text
A4

Thing-42 locatedAt Place-B
valid-time: [2026-02-05, ?)
knowledge-time: 2026-02-21
evidence: Correction-8
verification: verified

supersedes:
    A3
```

A3 rimane ricostruibile come precedente conoscenza poi corretta.

Questo permette di rispondere sia a:

- qual è oggi la ricostruzione considerata valida?
- che cosa sosteneva il sistema il 20 febbraio?

## Quinto ingresso — fonte conflittuale

Il 22 febbraio una seconda fonte dichiara:

```text
Thing-42 remained at Place-A
through 2026-02-06
```

Nasce:

```text
A5

Thing-42 locatedAt Place-A
valid-time: [2026-02-01, 2026-02-06]
knowledge-time: 2026-02-22
evidence: API-message-302
verification: accepted
```

A4 e A5 sono incompatibili nell'intervallo 5–6 febbraio **perché il Domain ha dichiarato `locatedAt` esclusiva**.

Un motore generico potrebbe quindi produrre qualcosa del tipo:

```text
Conflict C1
assertions: A4, A5
overlap: [2026-02-05, 2026-02-06]
reason:
    incompatible values for exclusive relation
resolution:
    unresolved
```

Il conflitto viene conservato invece di cancellare automaticamente una delle due fonti.

## Che cosa fa il motore nell'esempio

### Reconciliation

Risolve identificatori provenienti dalle sorgenti verso il referente interno `Thing-42`.

Il comportamento generale può essere trasversale; il significato di un certo identificatore e le regole che lo rendono affidabile possono dipendere dal Domain o dai mapping.

### Conflict detection

Confronta affermazioni potenzialmente sovrapposte.

Il meccanismo può essere generale, ma la semantica che stabilisce quando due valori sono realmente incompatibili può essere specifica del dominio.

### Supersession

Una correzione può sostituire epistemicamente una precedente affermazione senza cancellarla dalla storia.

### Current-state derivation

Lo stato corrente può essere una conclusione prodotta considerando:

- validità temporale;
- supersession;
- conflitti;
- politiche di selezione eventualmente applicabili.

Lo stato corrente non deve coincidere necessariamente con un singolo campo sorgente.

### Provenance tracing

Una conclusione può essere ricondotta alle affermazioni e da queste alle evidenze e alle attività che le hanno prodotte.

### Explanation

Una vista o funzione può usare la stessa struttura per spiegare perché il sistema sostiene una certa conclusione, senza trasformare la spiegazione testuale in una nuova verità primaria.

## Realtà e conoscenza non devono essere confuse

L'esempio mostra una distinzione importante:

```text
Thing-42 locatedAt Place-B dal 5 febbraio
```

può essere il contenuto di una proposizione sulla realtà.

Invece:

```text
questa proposizione è sostenuta da Correction-8,
è stata appresa il 21 febbraio,
corregge A3
```

descrive il rapporto del sistema con quella proposizione.

Il periodo di validità può descrivere il fenomeno reale; evidenza, acquisizione, stato di verifica e correzione descrivono la conoscenza del sistema.

## Core e Domain: ciò che l'esempio suggerisce

L'esempio non dimostra una struttura definitiva, ma sostiene alcune ipotesi da verificare.

### Il Domain dovrebbe spiegare il significato

Qui stabilisce:

- che cosa sono TrackedThing e Place;
- che cosa significa `locatedAt`;
- quali tipi possono partecipare alla relazione;
- quali valori sono incompatibili nello stesso istante.

### Il Core dovrebbe fornire capacità trasversali

Candidati analitici:

- rappresentare referenti e relazioni senza conoscere in anticipo ogni significato di dominio;
- rappresentare ciò che il sistema sostiene;
- qualificare conoscenza con tempo, evidenza e provenienza quando necessario;
- confrontare, revisionare, riconciliare e derivare senza hardcodare la semantica di un singolo dominio.

### Le primitive della conoscenza non sono il motore

Se concetti equivalenti ad Assertion, valid-time, Evidence o Derivation risultassero necessari, il loro ruolo sarebbe rendere la conoscenza operabile. I meccanismi userebbero poi quella struttura per produrre confronti, revisioni, stati e spiegazioni.

## Limite dell'esempio

Il caso non stabilisce:

- quali primitive debbano esistere davvero;
- se le primitive possano essere divise nettamente in due famiglie;
- quale parte appartenga a mapping, Core Model o Domain Model;
- quale tecnologia implementi il modello;
- se ogni dominio necessiti gli stessi meccanismi;
- se la pipeline debba essere sequenziale.

L'esempio serve precisamente a rendere visibili queste domande.

## Direzione emersa dalla ricerca successiva

Il confronto con ontology-based data access, mapping standards e sistemi semantic-driven suggerisce di non trattare Core e Domain come due stazioni consecutive.

È più plausibile distinguere responsabilità che collaborano:

```text
Source / Extraction
Mapping / Interpretation
Core Model
Domain Model
Knowledge
Core Engine
Views / Functions
```

`Core Model` e `Domain Model` possono essere risorse semantiche consultate durante interpretazione e ragionamento. Il mapping collega strutture delle sorgenti a significati interni; il motore opera sulla conoscenza risultante.

Questa direzione è ancora da verificare su casi reali.

## Riferimenti utili

- W3C — RDF 1.2 Concepts: https://www.w3.org/TR/rdf12-concepts/
- Wikibase — Data Model: https://www.mediawiki.org/wiki/Wikibase/DataModel
- W3C — PROV-O: https://www.w3.org/TR/prov-o/
- W3C/OGC — Time Ontology in OWL: https://www.w3.org/TR/owl-time/
- W3C — N-ary Relations: https://www.w3.org/TR/swbp-n-aryRelations/

## Provenienza di questo documento

Questo testo distilla la seconda ricerca approfondita completata il 30 agosto 2026. Il worked example è materiale di analisi e non autorizza da solo alcuna scelta architetturale.