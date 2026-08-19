# Fondamenti di Fold

## Scopo del documento

Questo documento consolida i fondamenti di Fold già stabiliti. Costituisce una base condivisa per le decisioni successive e non definisce ancora l'architettura tecnica concreta del sistema.

## 1. Decisioni già acquisite

### 1.1 Natura generale di Fold

Una parte importante della conoscenza relativa a una persona, un'attività o un'organizzazione è contenuta nei documenti. I documenti, tuttavia, normalmente rimangono elementi separati: ciascuno rappresenta o attesta soltanto una parte della realtà.

Fold nasce per superare questa separazione. Utilizza i documenti come fonti attraverso cui ricostruire progressivamente una rappresentazione della realtà. Il suo valore non deriva soltanto dal possesso dei documenti, ma dalla capacità di comprendere ciò che descrivono e di mantenere nel tempo i collegamenti tra le informazioni che emergono.

Fold può quindi essere considerato una memoria documentale della realtà.

### 1.2 Modello concettuale

Per descrivere la natura di Fold sono stati distinti sei concetti fondamentali.

#### Documento

È una fonte che rappresenta, registra o attesta qualcosa. Non coincide con ciò che descrive.

#### Informazione

È qualcosa che può essere conosciuto attraverso un documento. Un documento può contenere molte informazioni e la stessa informazione può essere presente o confermata da più documenti.

#### Identificatore

È qualcosa che permette di riconoscere nel tempo che informazioni provenienti da fonti differenti fanno riferimento allo stesso elemento. La sua funzione principale è creare continuità.

#### Entità

È qualcosa che può essere riconosciuto come elemento persistente della realtà. Più documenti e più informazioni possono riferirsi alla stessa entità.

#### Relazione

È il rapporto significativo tra due elementi. Permette di passare da elementi isolati a una struttura interconnessa.

#### Contesto

È la situazione più ampia all'interno della quale documenti, informazioni, entità e relazioni acquistano un significato comune. Permette di ricostruire non soltanto elementi separati, ma una storia o una situazione.

### 1.3 Una memoria strutturata e progressiva

Fold trasforma progressivamente un insieme di documenti indipendenti in una memoria strutturata e collegata della realtà che quei documenti rappresentano:

```text
documenti separati
        ↓
informazioni comprese
        ↓
elementi riconosciuti nel tempo
        ↓
collegamenti tra gli elementi
        ↓
situazioni ricostruite
        ↓
memoria della realtà rappresentata
```

Questa rappresentazione esprime l'obiettivo generale di Fold e non definisce una pipeline tecnica obbligatoria.

Documento, Informazione, Identificatore, Entità, Relazione e Contesto sono concetti distinti e interconnessi. Non costituiscono una catena lineare rigida. Un documento può contenere molte informazioni, riferirsi a più entità, contenere più identificatori, essere collegato ad altri documenti e contribuire a più relazioni e contesti. Analogamente, un'entità può comparire in molti documenti, avere più identificatori, essere collegata a molte altre entità e partecipare a contesti differenti.

### 1.4 Obiettivo del prototipo domestico

Il prototipo domestico sarà la prima istanza reale di Fold. Sarà utilizzato per progettare e validare soprattutto:

- il funzionamento del sistema;
- il modello documentale;
- la struttura della memoria;
- le relazioni tra le informazioni;
- le funzionalità del prodotto.

Il vecchio laptop domestico sarà il primo host dell'istanza Fold. L'istanza dovrà essere accessibile contemporaneamente da almeno due dispositivi attraverso la rete locale. Fold non sarà quindi concepito come un'applicazione utilizzabile esclusivamente dalla macchina sulla quale viene eseguito.

### 1.5 Continuità verso il prodotto futuro

Il prototipo domestico non è un prototipo usa-e-getta e non rappresenta il modello definitivo di distribuzione di Fold.

L'obiettivo successivo è l'evoluzione di Fold in un prodotto destinato alle attività, utilizzabile come applicazione web, con l'istanza operativa ospitata su infrastruttura server o cloud e accessibile dai dispositivi autorizzati.

Il prototipo locale deve pertanto essere progettato in modo sufficientemente indipendente dall'ambiente di esecuzione. La logica, il modello dei dati, le regole fondamentali e quanto più possibile delle funzionalità validate devono poter essere trasferiti o evoluti verso la futura applicazione web e cloud senza riprogettare Fold dalle fondamenta.

Il laptop domestico è il primo host dell'istanza Fold, non la forma definitiva del prodotto.

### 1.6 Livelli da distinguere

Nel ragionamento sul sistema devono essere distinti progressivamente quattro livelli.

#### Natura di Fold

Comprende ciò che definisce Fold indipendentemente dal luogo in cui viene eseguito: i suoi concetti, la sua logica e le sue regole fondamentali.

#### Istanza di Fold

È una memoria operativa concreta di Fold, con i documenti, le informazioni, gli elementi riconosciuti, le relazioni e lo stato costruito nel tempo.

#### Ambiente di esecuzione

È l'ambiente nel quale una specifica istanza viene eseguita e conservata, come il laptop domestico nella prima fase o un'infrastruttura server o cloud in futuro.

#### Modalità di distribuzione

È il modo in cui Fold viene reso operativo e accessibile in una determinata fase: inizialmente come istanza ospitata sul laptop e raggiungibile dalla rete locale; successivamente come applicazione web con istanza ospitata su infrastruttura server o cloud.

## 2. Conseguenze dirette delle decisioni acquisite

Le decisioni precedenti comportano direttamente che:

- l'identità e il significato degli elementi gestiti da Fold non devono dipendere essenzialmente dalla macchina che ospita l'istanza;
- architettura e organizzazione delle cartelle non devono basarsi su percorsi assoluti, nomi utente, lettere di unità o altre caratteristiche proprie della macchina di sviluppo;
- il trasferimento del progetto sul laptop non deve richiedere una riprogettazione del sistema;
- l'accesso da più dispositivi richiede che l'istanza ospitata sul laptop mantenga uno stato condiviso;
- i dispositivi attraverso cui si accede a Fold non devono essere confusi con la macchina che ospita l'istanza;
- ciò che appartiene alla natura e alla logica di Fold deve essere distinguibile da ciò che appartiene alla singola istanza;
- ciò che appartiene all'istanza deve essere distinguibile dalle caratteristiche dell'ambiente che la ospita;
- le semplificazioni adottate per il prototipo domestico devono rimanere riconoscibili come tali;
- le decisioni locali che potrebbero creare vincoli costosi nel futuro passaggio al cloud devono essere individuate e valutate esplicitamente;
- il programma, la configurazione dell'installazione, i dati dell'istanza e i dati temporanei o ricostruibili devono essere mantenuti concettualmente distinti;
- trasferire il programma e trasferire la memoria costruita da un'istanza sono operazioni concettualmente differenti, anche quando vengono eseguite insieme.

Queste conseguenze non determinano ancora le soluzioni tecniche con cui saranno realizzate.

## 3. Questioni ancora aperte

Non sono ancora stati scelti o definiti:

- lo stack applicativo;
- il database e il relativo modello tecnico;
- il sistema di storage dei documenti e degli altri dati;
- l'eventuale uso di container;
- la forma e l'organizzazione delle API;
- il sistema di autenticazione e autorizzazione;
- il provider e la struttura dell'infrastruttura cloud;
- l'architettura tecnica concreta del prototipo domestico;
- l'architettura tecnica concreta del futuro prodotto web e cloud.

Questi aspetti dovranno essere discussi progressivamente, mantenendo la distinzione tra decisioni intrinseche a Fold, decisioni proprie del prototipo domestico, scelte destinate ad adattarsi nel passaggio al cloud e dipendenze evitabili dall'ambiente locale.
