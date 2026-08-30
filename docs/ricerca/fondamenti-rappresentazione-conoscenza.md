# Fondamenti della rappresentazione della conoscenza

**Status:** Research  
**Data:** 2026-08-30  
**Scope:** ricerca metodologica e fondazionale utile alla progettazione del nucleo informativo di Fold; non costituisce architettura, modello dati o requisito implementativo

## Scopo

Questa ricerca raccoglie i risultati rilevanti di un approfondimento su come progettare un sistema capace di rappresentare conoscenza su una realtà mutevole senza scegliere prematuramente primitive, formalismi o tecnologie.

La domanda di partenza era:

> Come si progetta un modello capace di rappresentare ciò che sappiamo su una realtà che può cambiare nel tempo, mantenendo distinguibili identità, relazioni, tempo, provenienza, evidenza, conflitti e aggiornamenti della conoscenza, senza sovramodellare il problema?

Il risultato principale non è una lista di primitive. È un metodo per far emergere le distinzioni necessarie dai requisiti, dai casi e dai controesempi.

## Conclusioni forti

### 1. Lo scopo precede il modello

Ontology Development 101, LOT e metodologie affini convergono su un principio: non esiste un'unica ontologia corretta indipendente dall'uso. Prima di decidere classi, proprietà o altre strutture bisogna chiarire scopo, utilizzatori e domande che il modello deve rendere risolvibili.

Le competency questions sono quindi requisiti di conoscenza: aiutano a delimitare ciò che il modello deve poter esprimere e verificare.

### 2. Non partire dalle primitive

Una sequenza difendibile è:

```text
scopo e utilizzatori
        ↓
domande che devono poter ricevere risposta
        ↓
casi e controesempi reali
        ↓
distinzioni semantiche necessarie
        ↓
modello concettuale minimo candidato
        ↓
falsificazione
        ↓
revisione
        ↺
formalizzazione
        ↓
solo successivamente: tecnologia
```

Un concetto dovrebbe entrare nel modello perché senza di esso una domanda o un caso fallisce, non perché appare genericamente utile.

### 3. Realtà e conoscenza della realtà sono problemi distinti

La ricerca sostiene con forza la necessità di non confondere automaticamente:

- ciò che esiste o accade;
- il dato che lo rappresenta;
- una proposizione o affermazione su quella realtà;
- l'evidenza che sostiene l'affermazione;
- il fatto che il sistema accetti o meno quell'affermazione;
- una conclusione derivata.

RDF 1.2 rende particolarmente visibile questa distinzione: una proposizione può essere oggetto di ulteriori affermazioni senza dover essere automaticamente asserita come vera. Wikibase adotta una soluzione pragmatica analoga separando item e statement e qualificando gli statement con qualifier, reference e rank.

Questa evidenza non implica che Fold debba usare RDF o copiare Wikibase. Dimostra che il problema è reale e ricorrente.

### 4. Il dato non coincide con il referente

Una stringa, un record o un identificatore non sono automaticamente la cosa reale a cui si riferiscono. La riconciliazione dell'identità è un problema distinto dall'uguaglianza di chiavi o attributi.

Prima di modellare qualcosa come persistente occorre chiedere:

- che cosa può cambiare mantenendo la stessa identità?
- che cosa ne determina invece la fine e l'inizio di qualcosa di nuovo?
- gli identificatori possono cambiare, essere molteplici o essere riutilizzati?
- due descrizioni simili implicano identità o soltanto somiglianza?
- possiamo essere incerti sulla co-referenza?

Le condizioni concrete di identità dipendono dal tipo di fenomeno e dal dominio.

### 5. Tempo della realtà e tempo della conoscenza possono divergere

La letteratura sui database temporali distingue almeno:

- **valid time** — quando qualcosa vale nella realtà modellata;
- **transaction/knowledge time** — quando quella informazione entra nello stato conosciuto o registrato dal sistema.

Questa distinzione consente di separare fenomeni che altrimenti sembrerebbero tutti semplici update:

- cambiamento reale;
- conoscenza tardiva;
- correzione;
- contraddizione fra fonti;
- superamento storico;
- ritrattazione;
- conoscenza temporale imprecisa.

Un modello bitemporale completo non è automaticamente necessario: lo diventa solo quando le domande richiedono di distinguere i due assi.

### 6. Cambiamento, correzione e conflitto non sono equivalenti

Una nuova informazione può:

- aggiungere qualcosa senza modificare la precedente;
- precisare qualcosa;
- correggere una precedente interpretazione;
- contraddirla senza che il sistema sappia ancora quale preferire;
- descrivere uno stato successivo realmente cambiato;
- ritirare l'impegno verso una precedente affermazione.

La ricerca sui truth-maintenance systems è utile non come tecnologia da adottare, ma perché dimostra che la revisione della conoscenza richiede di preservare giustificazioni e dipendenze quando queste contano.

### 7. Provenienza non significa semplicemente source

PROV-O distingue entità, attività e agenti e permette di rappresentare generazione, uso, attribuzione e derivazione.

Questa distinzione suggerisce di non comprimere automaticamente in un singolo campo `source` concetti potenzialmente diversi come:

- artefatto sorgente;
- autore o agente responsabile;
- canale di acquisizione;
- processo di estrazione o trasformazione;
- evidenza che sostiene un'affermazione;
- derivazione di una conclusione.

Il livello di dettaglio necessario rimane dipendente dalle domande di audit, verifica e spiegazione.

### 8. Le relazioni semplici non devono diventare automaticamente oggetti

Una relazione binaria può essere sufficiente finché interessa soltanto sapere che A è collegato a B.

Quando la relazione possiede caratteristiche proprie — periodo, ruolo, ulteriori partecipanti o altre qualificazioni — possono diventare necessari pattern n-ari o una rappresentazione autonoma della relazione.

Occorre inoltre distinguere caratteristiche della relazione nella realtà da caratteristiche dell'affermazione sulla relazione. Per esempio, il periodo può descrivere il collegamento reale; la fonte o la certezza possono descrivere invece ciò che il sistema sostiene sul collegamento.

### 9. Eventi e processi non sono primitive universali

Un cambiamento fra due stati non obbliga automaticamente a introdurre una primitiva Event.

Affermazioni o relazioni temporalmente qualificate possono essere sufficienti quando interessa soprattutto sapere che cosa valeva prima e dopo.

Evento o Processo diventano candidati autonomi quando l'accadimento stesso deve essere identificato e interrogato, per esempio quando servono partecipanti, durata, fasi, ordine, causalità o risultati propri.

BFO, DOLCE, UFO e sistemi object-centric sono quindi lenti da consultare quando il problema lo richiede, non modelli da adottare a priori.

### 10. Stato corrente e conoscenza completa non coincidono

Lo stato corrente può essere una derivazione o una vista prodotta dalla conoscenza conservata.

Conservare soltanto lo stato corrente rischia di perdere:

- storia;
- provenienza;
- conflitti;
- correzioni;
- capacità di spiegare perché una conclusione è valida.

La scelta fra stato materializzato, derivato o ibrido non è determinabile in astratto.

### 11. Conoscenza primaria e derivata devono restare distinguibili quando necessario

Una conclusione prodotta da più informazioni e da una regola non è semanticamente identica alle informazioni che la sostengono.

Se spiegabilità, audit o revisione sono requisiti, il sistema deve poter ricostruire almeno concettualmente:

```text
conclusione
   ↓ deriva da
regola + informazioni
   ↓ sostenute da
evidenze / provenienza
```

Persistenza o ricalcolo della conclusione sono decisioni successive.

## Metodo operativo emerso

La ricerca suggerisce questo ciclo:

1. **Perimetro** — chiarire perché stiamo modellando e che cosa è fuori scope.
2. **Competency questions** — formulare domande verificabili in linguaggio naturale.
3. **Corpus di casi** — usare casi reali e casi deliberatamente avversariali.
4. **Inventario neutro** — elencare ciò di cui dobbiamo parlare senza decidere subito se sarà classe, proprietà, relazione o altro.
5. **Distinzioni forzate** — fondere concetti e osservare quali domande smettono di essere risolvibili.
6. **Modello minimo candidato** — introdurre soltanto le strutture necessarie.
7. **Stress epistemico e temporale** — cambiamento, tardività, correzione, conflitto, identità incerta, provenienza multipla.
8. **Analisi ontologica mirata** — consultare pattern o foundational ontology solo per un fallimento concreto.
9. **Falsificazione cross-domain** — verificare che ciò che appare generale non dipenda accidentalmente dal primo dominio.
10. **Formalizzazione e tecnologia** — solo quando le decisioni semantiche sono sufficientemente stabili.

## Failure modes da tenere presenti

Particolarmente rilevanti per il futuro lavoro su Fold:

- ogni sostantivo diventa una classe;
- record = cosa reale;
- identificatore = identità;
- valore = informazione;
- affermazione = realtà;
- un unico campo source per tutto;
- un unico timestamp per validità e conoscenza;
- overwrite distruttivo;
- forzare sempre un vincitore nei conflitti;
- reificare ogni relazione;
- ogni cambiamento = evento;
- nessun evento è mai necessario;
- stato corrente = conoscenza completa;
- conclusione derivata indistinguibile dal dato sorgente;
- scegliere la tecnologia e derivarne il modello concettuale.

## Questioni che la ricerca lascia intenzionalmente aperte

Non è determinabile in astratto:

- se `Assertion` debba essere una primitiva;
- se `Event`, `Process`, `State`, `Situation` o `Role` debbano essere primitive;
- se serva una vera bitemporalità;
- quale granularità di provenienza mantenere;
- se e quando persistere conclusioni derivate;
- dove passi il confine fra un modello generale e un'ontologia di dominio;
- quale formalismo o tecnologia utilizzare.

Queste decisioni devono essere giustificate dai casi e dalle domande del sistema.

## Protocollo minimo di falsificazione

Un modello candidato dovrebbe essere provato almeno con:

- stesso referente, proprietà cambiata;
- stesso referente, identificatore cambiato;
- informazione scoperta in ritardo;
- nuova fonte conflittuale;
- precedente interpretazione corretta;
- relazione che inizia o termina;
- conoscenza incompleta;
- più evidenze per la stessa proposizione;
- conclusione derivata la cui premessa viene ritirata;
- caso appartenente a un dominio strutturalmente diverso;
- caso in cui l'accadimento stesso diventa oggetto delle domande.

Quando un test fallisce, il criterio è introdurre la più piccola distinzione necessaria e ripetere i test precedenti.

## Implicazione per Fold

Questa ricerca non definisce il Core di Fold.

Fornisce invece una regola di lavoro:

> Una struttura è candidata a diventare parte del Core soltanto quando una distinzione necessaria sopravvive a casi e domini differenti mantenendo significato e comportamento sufficientemente stabili.

Il fatto che un concetto sembri generico non è sufficiente.

## Fonti principali

- Natalya Noy, Deborah McGuinness — *Ontology Development 101: A Guide to Creating Your First Ontology*: https://protege.stanford.edu/publications/ontology_development/ontology101-noy-mcguinness.html
- LOT — Linked Open Terms methodology: https://lot.linkeddata.es/
- W3C — *RDF 1.2 Concepts and Abstract Data Model*: https://www.w3.org/TR/rdf12-concepts/
- W3C — *PROV-O: The PROV Ontology*: https://www.w3.org/TR/prov-o/
- W3C/OGC — *Time Ontology in OWL*: https://www.w3.org/TR/owl-time/
- W3C — *Defining N-ary Relations on the Semantic Web*: https://www.w3.org/TR/swbp-n-aryRelations/
- Wikibase — *Data Model*: https://www.mediawiki.org/wiki/Wikibase/DataModel
- ISO/IEC 21838-2:2021 — Basic Formal Ontology: https://webstore.iec.ch/en/publication/72703

## Provenienza di questo documento

Questo testo è una distillazione per il repository della ricerca approfondita completata il 29–30 agosto 2026. Il report esteso è materiale di ricerca, non specifica. Questa sintesi conserva le conclusioni e i limiti necessari a continuare il lavoro senza dipendere dalla conversazione che l'ha prodotta.