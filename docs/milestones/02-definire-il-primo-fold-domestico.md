# Milestone 2 — Definire il primo Fold domestico

**Status:** Historical  
**Completamento ricostruito:** 2026-08-26 — entrambe le issue della milestone risultano concluse in Linear e il checkpoint finale della milestone è datato 26 agosto 2026.  
**Ricostruzione storica:** 2026-08-28  
**Scope:** ricostruzione autosufficiente della seconda milestone di Fold — MVP domestico

**Nota metodologica:** questa sintesi usa come ancoraggi temporali principali il checkpoint Linear di chiusura della milestone e i commenti contemporanei al lavoro. Le descrizioni correnti di FOL-9 e FOL-10 sono state usate per ricostruire il dettaglio consolidato; il successivo audit FOL-22 conferma che le issue storiche non sono state riscritte con il metodo introdotto dopo. La ricerca nel repository è trattata come evidenza, non come decisione di prodotto. Non è stato necessario ricorrere a Notion per colmare lacune narrative.

## 1. Situazione iniziale

La milestone precedente aveva dato a Fold una roadmap, un metodo orientato a risultati verificabili e un progetto operativo in Linear. Esisteva inoltre una prima baseline formale, [`../fondamenti-fold.md`](../fondamenti-fold.md), che descriveva Fold come una memoria documentale della realtà e distingueva documento, informazione, identificatore, entità, relazione e contesto.

Quella base non definiva però ancora il primo prodotto domestico con sufficiente precisione. Non era stato stabilito in modo concreto:

- chi avrebbe usato la prima versione;
- in quali situazioni reali avrebbe dovuto essere utile;
- quali problemi domestici dovesse risolvere;
- quali ambiti e operazioni appartenessero al perimetro;
- che cosa dovesse rimanere fuori o essere rinviato alla progettazione.

Erano già presenti documenti e ricerca sulle utenze, ma non dovevano trasformarsi automaticamente nel modello di Fold né spingere il progetto verso un elenco di funzioni inventate a tavolino. Serviva passare dalla natura generale del prodotto a un primo contesto d'uso osservabile, senza anticipare tecnologia, interfaccia o modello dati tecnico.

## 2. Problema, obiettivo e criterio di completamento

La milestone doveva:

> Decidere chi usa il MVP, quali problemi deve risolvere, quali operazioni fondamentali deve permettere e cosa resta volutamente fuori.

Il criterio di completamento registrato in Linear era:

> Il primo Fold può essere descritto con precisione senza parlare ancora di tecnologie.

Il problema non consisteva quindi nello scegliere subito una soluzione tecnica. Occorreva produrre un perimetro di prodotto sufficientemente concreto da poter guidare la milestone successiva, **Progettare il MVP**.

## 3. Lavoro effettivamente svolto

La milestone comprendeva due issue strettamente collegate, affrontate come due prospettive sullo stesso risultato. I dati Linear non dimostrano una sequenza rigida tra le due: utenti, situazioni e ambiti si sono precisati reciprocamente fino alla chiusura comune del 26 agosto.

### FOL-9 — Definire chi usa il MVP domestico e in quali situazioni

Il lavoro ha descritto l'utente di riferimento non attraverso un livello di competenza astratto, ma attraverso il contesto reale: persone che usano strumenti digitali comuni, possono avere poca dimestichezza tecnica e soprattutto gestiscono documenti frammentati tra email, WhatsApp, telefono, computer e carta.

Sono state raccolte situazioni concrete, tra cui:

- ritrovare documenti personali senza ricordare il canale di provenienza o il nome originale del file;
- evitare di rifotografare o riscansionare documenti già posseduti;
- verificare lo stato di una bolletta e ricostruire costi, consumi o periodi senza cercare in più posti;
- aggregare spese documentate riferite a una persona, un immobile, un'utenza, un veicolo o un bene;
- recuperare documenti, garanzie e manutenzioni di beni durevoli;
- riconoscere documenti o movimenti ricorrenti attesi, segnalarne l'eventuale assenza e chiedere conferma quando Fold non può verificare autonomamente l'accaduto.

È inoltre emersa una situazione multi-persona: ciascun membro del nucleo deve poter trovare in primo piano i contenuti che lo riguardano. Il lavoro ha distinto il bisogno di prodotto dalla sua futura soluzione:

- la persona rappresentata nei dati;
- l'account che accede all'applicazione;
- i permessi di quell'account;
- l'hub personale come vista pertinente, non come archivio separato.

FOL-9 ha registrato il bisogno e ha rinviato la definizione di account, hub e autorizzazioni alla milestone di progettazione.

### FOL-10 — Mappare gli ambiti domestici candidati del MVP

Il secondo filone ha messo alla prova il perimetro partendo da documenti, soggetti e domande operative reali. La mappa finale comprendeva:

- persone del nucleo domestico;
- salute e spese sanitarie, con particolare concretezza nella raccolta di documentazione e importi utili anche per 730 o commercialista;
- immobile o residenza;
- utenze e servizi della casa;
- veicoli;
- beni e impianti domestici da seguire nel tempo;
- dimensioni trasversali come spesa, tempo, scadenza, stato, provenienza, periodicità e attesa.

Il lavoro non si è limitato a compilare categorie. Ha chiarito come leggere gli ambiti:

- un'assicurazione si collega alla persona, al veicolo, all'immobile o al bene a cui si riferisce; non diventa un ambito autonomo soltanto perché è un tipo documentale;
- una spesa è una dimensione trasversale e può riguardare referenti diversi;
- l'acquisto di un bene durevole può far nascere qualcosa da seguire nel tempo, mentre una spesa corrente può restare una semplice informazione economica;
- una casa è un referente stabile con documenti, costi e obblighi propri, non soltanto il contenitore delle utenze;
- una periodicità può motivare un'attesa, ma ciò che è atteso non diventa automaticamente un fatto avvenuto.

## 4. Evidenze e ragionamento

### Osservazioni d'uso

Il problema osservato era la frammentazione, non una presunta incapacità personale di organizzarsi. Le frizioni concrete comprendevano allegati dispersi nelle chat, documenti accessibili soltanto recuperando credenziali di altre applicazioni, PDF con nomi composti da codici poco comprensibili, copie cartacee e digitali separate e ricostruzioni manuali di importi o scadenze.

Queste osservazioni hanno spostato il centro del MVP dal semplice archivio di file alla capacità di raccogliere, comprendere, collegare e riusare documenti e informazioni.

### Documenti reali e ricerca sulle utenze

La ricerca precedente alla milestone, conservata in [`../ricerca/bollette-luce-gas-arera.md`](../ricerca/bollette-luce-gas-arera.md), aveva confrontato la disciplina ARERA con tre bollette reali. Aveva reso osservabili informazioni come intestatario, punto di fornitura, periodo, consumi, importi, scadenza, pagamento, offerta e storico, mantenendo distinti obblighi regolatori, valori concreti, scelte del venditore e contenuti condizionali.

La ricerca sugli identificatori, [`../ricerca/semantica-identificatori.md`](../ricerca/semantica-identificatori.md), aveva inoltre mostrato che numero di bolletta, codici del venditore, POD o PDR, codice offerta e matricola del misuratore riconoscono referenti e continuità differenti.

Queste evidenze hanno reso le utenze il caso domestico più maturo e hanno sostenuto alcune domande operative della milestone. Non hanno però definito da sole il modello generale di Fold né le regole tecniche di identità, rimaste lavoro successivo.

### Raffinamento dei candidati

La revisione intermedia di FOL-10 distingueva candidati già solidi da ambiti ancora deboli o formulati in modo troppo ampio. Invece di ampliare artificialmente la lista, il lavoro ha cercato casi più concreti e una classificazione migliore.

In particolare:

- “salute” è stata resa concreta attraverso documenti sanitari, spese e recupero del materiale utile, senza trasformare Fold in un sistema generale di gestione della salute;
- “spese e disponibilità economica” è stata riconosciuta soprattutto come capacità trasversale, non come ambito equivalente a persone, immobili o veicoli;
- l'immobile è stato distinto dai servizi che vi insistono;
- la diversa qualità prevedibile di PDF, scansioni e fotografie è emersa come questione di ingestione, affidabilità e verifica da progettare dopo, non come nuovo ambito.

## 5. Decisioni appartenenti alla milestone

Alla chiusura erano state prese e consolidate operativamente le seguenti decisioni di perimetro.

### Utente e problema

Il primo Fold domestico era destinato a persone in un nucleo domestico con una gestione documentale distribuita tra più canali. Doveva ridurre la difficoltà di trovare, comprendere, collegare e riutilizzare documenti e informazioni, comprese spese, scadenze e ricorrenze.

### Operazioni fondamentali

Il MVP doveva permettere di:

- acquisire documenti da più canali;
- riconoscerli e classificarli in modo comprensibile;
- collegare documenti e informazioni al referente corretto;
- ritrovarli e riutilizzarli senza dipendere dal nome file o dal canale originale;
- estrarre e consultare importi, date, periodi, scadenze, consumi e riferimenti;
- aggregare spese documentate per periodo e referente;
- gestire scadenze e avvisi;
- rappresentare periodicità e attese motivate;
- distinguere atteso o stimato da confermato;
- mantenere un saldo di riferimento confermato e un saldo stimato basato su movimenti attesi, senza collegamento diretto alla banca.

### Regole concettuali di perimetro

La fase consolidò inoltre quattro distinzioni che avrebbero guidato la progettazione:

1. il documento si collega al soggetto o bene corretto e il suo tipo non definisce automaticamente un ambito;
2. persona rappresentata, account, permesso e hub personale non coincidono;
3. una spesa può generare un bene da seguire oppure restare informazione economica;
4. un elemento atteso non equivale a un fatto avvenuto e un saldo stimato non equivale a un saldo confermato.

Queste erano decisioni sul comportamento e sul perimetro del primo prodotto, non ancora un modello dati o un'architettura software.

## 6. Risultato raggiunto

Alla chiusura il primo Fold domestico poteva essere descritto senza ricorrere a scelte tecniche:

- aveva un utente di riferimento e un contesto d'uso riconoscibile;
- affrontava problemi documentali e informativi osservabili;
- possedeva un insieme di operazioni fondamentali;
- disponeva di un perimetro domestico abbastanza concreto da fornire casi di prova;
- distingueva contenuti personali e condivisi come bisogno, senza anticipare i permessi;
- riconosceva spese, scadenze, periodicità e attese come dimensioni trasversali;
- aveva confini espliciti rispetto a capacità più ampie o rischiose.

Il risultato non era una specifica implementabile. Era il brief di prodotto necessario per iniziare a progettare il MVP su casi reali.

## 7. Verifica e criterio di chiusura

FOL-9 è stata considerata conclusa quando utenti e situazioni erano descritti abbastanza bene da progettare operazioni, viste personali e regole minime di accesso.

FOL-10 è stata considerata conclusa quando il perimetro domestico era sufficiente per selezionare documenti reali e verificare su di essi un core dati trasversale.

Il checkpoint finale della milestone ha verificato congiuntamente:

- chi usa Fold;
- quali problemi deve risolvere;
- quali operazioni fondamentali deve sostenere;
- quali ambiti include;
- che cosa resta fuori;
- quale milestone può iniziare dopo.

Poiché questi elementi permettevano di descrivere il primo Fold senza scegliere tecnologie, il criterio di completamento della milestone risultava soddisfatto.

## 8. Fuori scope e questioni ancora aperte

### Escluso dal primo MVP

La chiusura escluse esplicitamente:

- gestione di password o credenziali personali;
- collegamento bancario e open banking;
- budgeting o contabilità domestica completa;
- comparazione di offerte o raccomandazione automatica di cambio operatore;
- automazione fiscale completa del 730;
- event engine generale, timeline e ricostruzione storica completa;
- ruoli e permessi enterprise complessi.

Le idee sulle credenziali e sugli alert di convenienza furono preservate come lavoro futuro, senza diventare requisiti del MVP.

### Rinviato alla progettazione del MVP

Non erano stati ancora definiti:

- schermate e user flow dettagliati;
- account, hub personali e matrice minima dei permessi;
- canali e flussi concreti di ingestione;
- modello Core/Dominio e modello dati tecnico;
- regole di identità e riconciliazione;
- tecnologia di autenticazione, database, stack e architettura di implementazione;
- algoritmo per apprendere o confermare periodicità;
- logica automatica con cui una spesa genera un bene da seguire;
- trattamento operativo dell'affidabilità variabile delle fonti.

Questi punti non invalidavano la chiusura: erano precisamente il lavoro che il perimetro appena definito consentiva di affrontare dopo.

## 9. Lavoro sbloccato

La milestone ha consegnato casi, vincoli e distinzioni alla milestone successiva, **Progettare il MVP**.

### Dipendenza formale in Linear

- **FOL-13 — Definire e verificare il core dati trasversale sul dominio domestico** risultava bloccata da FOL-10. La conclusione della mappa domestica ha quindi sbloccato formalmente il primo lavoro centrale della milestone successiva.

FOL-13 avrebbe usato bollette, documenti personali o sanitari, documenti dell'immobile, veicoli e beni durevoli come casi di prova per distinguere Core, Dominio e dati reali. Il checkpoint di chiusura indicava infatti che la milestone successiva poteva iniziare proprio da questo lavoro.

### Lavori resi progettualmente affrontabili

FOL-9 indicava esplicitamente che la definizione di utenti e situazioni avrebbe consentito di progettare core dati, hub personali, permessi, attese periodiche e flussi principali. Nella milestone successiva questo passaggio è riconoscibile soprattutto in:

- **FOL-14 — Definire account, hub personali e permessi del nucleo domestico**, collegata a FOL-9;
- **FOL-18 — Definire attese periodiche, conferme e saldo stimato**, collegata a FOL-9 e FOL-10 e dipendente da FOL-13.

I casi emersi prepararono inoltre il lavoro sui canali di ingestione da smartphone e da cartella locale, registrato in FOL-11 e FOL-15. Linear non registra però per queste due issue una dipendenza formale da FOL-9 o FOL-10: vanno considerate continuazioni rese concrete dal perimetro, non lavori formalmente sbloccati dalla chiusura.

## 10. Evoluzioni successive, non appartenenti alla milestone

Dopo la chiusura, il progetto ha sviluppato ulteriormente il core informativo, la governance della conoscenza e il metodo di lavoro. In particolare, FOL-22 ha riallineato Linear e Notion al metodo corrente e ha creato FOL-24 per colmare retrospettivamente l'assenza di questa sintesi.

Queste evoluzioni spiegano perché il documento esiste, ma non modificano il contenuto storico della milestone 2. Le formulazioni successive del core, le nuove decisioni architetturali e lo stato corrente della milestone **Progettare il MVP** devono essere letti nelle fonti proprie del lavoro successivo, non retrodatati qui.

## 11. Artefatti e fonti collegate

- [FOL-9 — Definire chi usa il MVP domestico e in quali situazioni](https://linear.app/folderapp/issue/FOL-9/definire-chi-usa-il-mvp-domestico-e-in-quali-situazioni)
- [FOL-10 — Mappare gli ambiti domestici candidati del MVP](https://linear.app/folderapp/issue/FOL-10/mappare-gli-ambiti-domestici-candidati-del-mvp)
- [FOL-13 — Definire e verificare il core dati trasversale sul dominio domestico](https://linear.app/folderapp/issue/FOL-13/definire-e-verificare-il-core-dati-trasversale-sul-dominio-domestico)
- [FOL-14 — Definire account, hub personali e permessi del nucleo domestico](https://linear.app/folderapp/issue/FOL-14/definire-account-hub-personali-e-permessi-del-nucleo-domestico)
- [FOL-18 — Definire attese periodiche, conferme e saldo stimato](https://linear.app/folderapp/issue/FOL-18/definire-attese-periodiche-conferme-e-saldo-stimato)
- [FOL-24 — Ricostruire la sintesi autosufficiente della milestone 2](https://linear.app/folderapp/issue/FOL-24/ricostruire-la-sintesi-autosufficiente-della-milestone-2)
- [`01-organizzare-il-progetto.md`](01-organizzare-il-progetto.md), sintesi della milestone precedente
- [`../fondamenti-fold.md`](../fondamenti-fold.md), baseline storica disponibile all'inizio della milestone
- [`../ricerca/bollette-luce-gas-arera.md`](../ricerca/bollette-luce-gas-arera.md), evidenza documentale
- [`../ricerca/semantica-identificatori.md`](../ricerca/semantica-identificatori.md), evidenza sugli identificatori
