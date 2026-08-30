# Distinguere perimetro di implementazione e perimetro di validazione fondazionale

Status: Canonical
Date: 2026-08-30

## Contesto

Fold viene realizzato prima come **MVP domestico**. Questo perimetro rende possibile costruire e verificare un prodotto realmente utile senza anticipare funzioni, tecnologie o architetture che non servono alla fase corrente.

La direzione già riconosciuta di Fold comprende però classi di complessità più ampie della prima realizzazione domestica. Se la semplicità corrente del MVP venisse assunta come semplicità intrinseca del problema, le fondamenta potrebbero fondere differenze informative che diventano necessarie quando le stesse capacità vengono applicate a sorgenti, domini o situazioni più articolati.

## Problema

Occorre evitare due errori opposti:

1. anticipare nel MVP funzionalità, tecnologie e architetture future non necessarie;
2. modellare come semplici per natura capacità che oggi sono semplici soltanto perché il MVP ne usa una forma ridotta.

Considerare soltanto i casi da implementare può produrre un modello adeguato al comportamento corrente ma semanticamente chiuso. Considerare senza limiti ogni futuro plausibile produrrebbe invece sovraprogettazione e generalità speculativa.

## Decisione

Fold distingue due perimetri:

### Perimetro di implementazione

Determina ciò che Fold costruisce e verifica adesso. Il perimetro corrente è **Fold — MVP domestico**.

### Perimetro di validazione fondazionale

Determina contro quali pressioni vengono falsificate le fondamenta e i contratti strutturali, allo scopo di riconoscere e prevenire collassi semantici. Comprende soltanto un insieme deliberato, limitato e strategicamente rappresentativo di pressioni già riconosciute nella direzione di Fold.

Il principio di riferimento è:

> **Fold implementa entro il perimetro corrente, mentre le sue fondamenta vengono validate contro un insieme deliberato di pressioni strategiche già riconosciute, per evitare collassi semantici senza anticipare funzionalità future.**

Il caso semplice deve poter essere raffinato dal caso più ricco senza diventare semanticamente falso e senza richiedere di ricostruire differenze informative che il modello precedente aveva distrutto o fuso.

Questa proprietà riguarda la continuità del significato, non l'immutabilità della soluzione tecnica. Migrazioni, nuove strutture o nuovi algoritmi possono essere normali durante l'evoluzione del prodotto.

## Significato di MVP-first

Essere MVP-first significa:

- implementare e verificare soltanto comportamenti richiesti dal MVP;
- preferire la realizzazione più semplice che conserva il significato corretto e le informazioni essenziali;
- non introdurre componenti, astrazioni o tecnologie soltanto per possibilità future;
- usare pressioni esterne al MVP esclusivamente per falsificare una fondazione o un contratto, non per ampliare implicitamente il prodotto corrente.

Una pressione di validazione non diventa per questo una feature, una dipendenza implementativa o un elemento di backlog.

## Pressioni ammesse nella validazione fondazionale

Quando sono pertinenti alla fondazione esaminata, il perimetro di validazione può includere in modo deliberatamente limitato classi di pressione quali:

- domini differenti;
- sorgenti eterogenee;
- sistemi esterni con modelli e identificatori propri;
- realtà multi-referente;
- conoscenza longitudinale;
- attività e dipendenze;
- organizzazioni, ruoli e decisioni;
- informazioni concorrenti o incomplete;
- maggiore complessità del ragionamento sulla conoscenza.

Queste classi non sono requisiti del MVP e non approvano una famiglia definitiva di casi di falsificazione. Ogni uso deve avere una domanda precisa, una capacità da mettere sotto pressione e una condizione di arresto; non autorizza l'esplorazione indiscriminata di sistemi futuri.

Una pressione può orientare una decisione fondazionale soltanto quando è già sostenuta dalla direzione canonica del progetto oppure viene deliberatamente approvata come pertinente per il lavoro corrente. Conversazioni, intuizioni, documenti `Research` e sistemi esterni possono produrre evidenza o suggerire ipotesi, ma non trasformano autonomamente una possibilità futura in un vincolo fondazionale.

Il fatto che un caso futuro sia più complesso non dimostra da solo che il Core debba diventare più astratto o acquisire nuove primitive. Una falsificazione ha conseguenze fondazionali quando rende osservabile una perdita semantica specifica, una falsa equivalenza oppure una responsabilità fondamentale che l'assunzione corrente eliminerebbe o renderebbe non recuperabile con sufficiente affidabilità:

```text
caso futuro più complicato
≠
automaticamente nuova astrazione Core

assunzione corrente
→
perdita semantica concreta
```

## Raffinamento, scala ed evoluzione

Le possibilità successive possono essere analizzate secondo almeno tre dimensioni utili ma non necessariamente esclusive. Uno stesso cambiamento può coinvolgerne più di una e non deve essere forzato in una sola categoria.

### Raffinamento della stessa capacità

La responsabilità e il significato fondamentale restano stabili, mentre aumenta la sofisticazione della strategia, la precisione o il numero delle qualificazioni. Per esempio, una riconciliazione deterministica può diventare multi-indizio o incerta senza cambiare il significato di referente e identificatore; eventuali nuove responsabilità operative introdotte insieme devono essere valutate anche come evoluzione di prodotto.

### Scala / operazionalizzazione

Il significato resta stabile, ma cambiano volume, frequenza, distribuzione o automazione. Il passaggio da import periodico a sincronizzazione frequente o streaming può essere una questione di scala, ma può coinvolgere anche raffinamenti temporali o nuove responsabilità quando cambiano effettivamente la semantica o il comportamento del prodotto.

### Evoluzione di prodotto

Fold assume una responsabilità nuova. Rappresentare e spiegare lo stato di un'attività non equivale ad assegnarla, governarne l'esecuzione o aggiornare sistemi esterni. Questi comportamenti ulteriori appartengono a un'evoluzione del prodotto e non entrano nel perimetro corrente senza una decisione esplicita.

## Criterio per le semplificazioni

### Buona semplificazione

Il modello mantiene il significato corretto e le informazioni essenziali. Un caso più ricco richiede prevalentemente più dati o qualificazioni, configurazioni, algoritmi migliori o maggiore precisione.

### Debito tecnico gestibile

La semantica resta corretta, ma l'implementazione è limitata, accoppiata o inefficiente. Una migrazione tecnica può correggerla perché l'informazione necessaria non è stata distrutta.

### Collasso semantico

Concetti semanticamente differenti vengono dichiarati equivalenti oppure una distinzione necessaria viene eliminata in modo tale da non essere più recuperabile con sufficiente affidabilità. Per evolvere occorrerebbe reinterpretare retroattivamente i dati, indovinarne il significato o riacquisire informazioni ormai perse.

Un limite tecnico non è automaticamente una perdita semantica. La stessa forma tecnica può essere una buona semplificazione o un debito gestibile quando il significato corretto e le distinzioni necessarie restano recuperabili. Diventa un collasso quando il modello tratta come equivalenti concetti differenti o distrugge l'unica informazione dalla quale la distinzione potrebbe essere ricostruita.

Esempi contestuali, non schemi tecnici approvati:

- usare il POD come chiave tecnica non è da solo un collasso; lo diventa se identificatore e identità vengono dichiarati semanticamente equivalenti e la distinzione non è più ricostruibile;
- un solo campo `date` può essere sufficiente quando possiede un ruolo temporale unico ed esplicito; è un collasso se fonde significati temporali necessari e non più recuperabili;
- un campo `source` può essere un riferimento adeguato a una provenienza conservata altrove; è un collasso se riduce origini, evidenze o trasformazioni semanticamente differenti a un valore dal quale non possono più essere distinte;
- sovrascrivere un valore può essere un limite tecnico recuperabile quando la storia autorevole resta disponibile; è un collasso se una correzione cancella l'affermazione precedente, la sua evidenza o il significato della revisione senza altra possibilità di ricostruzione;
- conservare una proiezione corrente non equivale a dichiararla verità completa; il collasso avviene se l'ultimo valore elimina storia, conflitti o qualificazioni che il modello deve poter distinguere;
- un campo CRM può essere mappato a un significato Fold; il collasso avviene se struttura o stato della sorgente vengono assunti come significato o stato accettato da Fold senza mantenere distinguibili interpretazione e accettazione;
- un risultato derivato può essere memorizzato direttamente; il collasso avviene se viene reso semanticamente indistinguibile da un'osservazione e non restano recuperabili derivazione, premesse o regola quando necessarie.

## Ruolo delle pressioni future e dei sistemi maturi

Sistemi e approcci molto più complessi possono essere studiati come fonti di pressione progettuale, non come blueprint:

```text
problemi ricorrenti osservati
→ evidenza utile

separazioni fondazionali adottate da più approcci
→ ipotesi da verificare su Fold

architettura o funzionalità specifiche del prodotto
→ non requisito di Fold
```

Una separazione osservata altrove resta un'ipotesi: deve essere verificata sui problemi di Fold e superare il gate previsto per le pressioni fondazionali prima di influenzarne le fondamenta.

## Cosa questa decisione non autorizza

Questa decisione non autorizza:

- l'ampliamento del MVP domestico;
- la progettazione anticipata di funzionalità future;
- un'architettura enterprise o un sistema universale;
- primitive dedicate a ogni complessità possibile;
- l'approvazione di `Event`, `Process` o altri candidati concettuali;
- integrazioni CRM/ERP;
- process engine, event engine o reasoning general-purpose;
- la scelta di tecnologie;
- l'adozione dell'architettura o delle funzionalità di sistemi maturi;
- la creazione automatica di lavoro futuro o dipendenze operative.

## Motivazione

La distinzione permette di mantenere contemporaneamente due discipline necessarie:

- costruire un prodotto piccolo, reale e verificabile;
- evitare che una semplificazione locale distrugga significati già riconosciuti come importanti per il possibile raffinamento delle stesse capacità.

Il perimetro di implementazione protegge Fold dalla sovraprogettazione. Il perimetro di validazione fondazionale protegge Fold dall'assumere che la semplicità del primo caso sia una proprietà permanente del problema.

## Conseguenze

Da questa decisione segue che:

- ogni implementazione continua a essere valutata sul perimetro corrente;
- la progettazione di una fondazione deve dichiarare sia ciò che implementa sia le pressioni limitate usate per falsificarla;
- una pressione futura non produce automaticamente requisiti, issue, componenti o astrazioni;
- una semplificazione deve essere valutata per la perdita di significato, non soltanto per la facilità di implementazione;
- una migrazione tecnica futura è accettabile quando preserva un significato recuperabile;
- un contratto fondazionale non è sufficientemente verificato se funziona soltanto assumendo come intrinseca la semplicità contingente del MVP;
- casi, primitive, architetture e tecnologie restano oggetto di decisioni separate.
