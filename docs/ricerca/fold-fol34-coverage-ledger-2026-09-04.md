---
title: "Fold — FOL-34 research coverage ledger"
status: Research
date: 2026-09-04
scope: "Audit delle 28 domande fondazionali Q1.1–Q8.3"
linear_issue: "FOL-34"
baseline_commit: "ea768518e9b00fb11cb3b4b80d0ad640158cab5d"
---

# Fold — FOL-34 Research Coverage Ledger

## 0 — Scopo ed esito in una frase

Questo documento verifica quanta parte della ricerca fondazionale prevista da FOL-34 sia già stata realmente acquisita dal progetto e quale lavoro residuo sia ancora necessario prima della chiusura di FOL-13 e del passaggio a FOL-36.

È un **audit di coverage della ricerca**: non svolge nuova ricerca, non modifica l’anatomia, non costruisce la v2.1 e non trasforma domande aperte in decisioni. La copertura è valutata domanda per domanda rispetto alla conoscenza genealogica, non contando K-ID o cercando formulazioni simili nella candidata.

**Verdetto:** `FOL-34 COVERAGE SUPERATA — NESSUNA RICERCA FONDAZIONALE RESIDUA BLOCCANTE`.

Questo verdetto non chiude automaticamente FOL-13. Significa che il suo residuo bloccante non è altra ricerca teorica: occorrono ancora la preservazione controllata della conoscenza in FOL-36 e la falsificazione domestica/cross-domain in FOL-37.

## 1 — Fonti e gerarchia

### 1.1 — Autorità sulla conoscenza acquisita

1. [Knowledge / Decision Ledger](fold-knowledge-decision-ledger-2026-09-04.md) — autorità genealogica primaria. Determina formulazione, stato, origine e superamento delle K-ID.
2. Linear FOL-34 — descrizione con la matrice Q1.1–Q8.3 e checkpoint «Criterio di rientro aggiornato — 4 settembre 2026». Determina domande e contratto operativo dell’audit.
3. Linear FOL-13 — descrizione, criteri di chiusura e checkpoint operativo del 4 settembre. Determina ciò che deve essere sufficientemente fondato e la sequenza FOL-36 → FOL-37 → FOL-38 → FOL-39.
4. [Decisione 0001](../decisions/0001-perimetro-implementazione-validazione-fondazionale.md) — autorità canonica sul rapporto fra MVP, pressioni fondazionali e falsificazione.
5. [Coverage Map v2](fold-coverage-ledger-v2-2026-09-04.md) — consultata **solo dopo** il mapping domanda→K-ID, per distinguere conoscenza acquisita da conoscenza rappresentata nella v2. Un’assenza nella candidata non rende assente la conoscenza.
6. Documenti storici/research — consultabili solo per controllare origine o significato quando il Ledger non basta. Per le 28 classificazioni non è stato necessario usarli come autorità aggiuntiva.

La candidata v2 e [il delta v2→v2.1](fold-delta-v2-v2.1-2026-09-04.md) **non sono stati usati come indice retrospettivo** di ciò che Fold sapeva. Il delta resta immutato e appartiene al lavoro di FOL-36.

La nuova review indipendente è usata soltanto come ulteriore evidenza di stress per due pressioni — continuità tramite identificatori e attesa senza riscontro — nella sezione 5. Le sue soluzioni tecniche non sono autorità.

### 1.2 — Gerarchia interna alle K-ID

Le sigle nella colonna «K-ID principali» significano:

- `S` — STABILE;
- `C` — CANDIDATA;
- `A` — APERTA;
- `X` — SUPERATA.

Una K-ID CANDIDATA può fornire una forma promettente ma non viene presentata come stabile. Una K-ID APERTA delimita il residuo senza cancellare i principi STABILE circostanti. Una posizione SUPERATA è mostrata soltanto per rendere leggibile la genealogia, mai come risposta corrente.

Le transizioni superate materialmente richiamate nell’audit sono, fra le altre: K-048→K-049, K-051→K-052, K-060→K-061, K-069→K-070, K-072→K-073, K-114→K-115, K-120→K-143, K-135→K-136, K-137→K-144, K-153→K-161, K-154→K-162, K-155→K-158 e K-017→K-185. L’ultima conduce a un’apertura, non a una nuova assegnazione già decisa.

## 2 — Criteri di classificazione

Ogni domanda riceve uno e un solo stato principale:

### SUFFICIENTEMENTE COPERTA

Il problema reale possiede principi acquisiti abbastanza solidi da non richiedere ulteriore ricerca fondazionale prima di FOL-36. Possono restare:

- forme CANDIDATA;
- criteri Domain o algoritmi specifici;
- contratti da verificare su casi;
- scelte della slice;
- decisioni tecniche di FOL-39.

Questi residui sono esplicitati e destinati, ma **non autorizzano nuova ricerca FOL-34**.

### PARZIALMENTE COPERTA — RICERCA RESIDUA NECESSARIA

Manca una conoscenza fondazionale senza la quale FOL-13/FOL-36 congelerebbero un’assunzione non sufficientemente sostenuta. Solo questo stato autorizza nuova ricerca FOL-34, con evidenza minima e criterio di arresto dichiarati.

### NON PIÙ NECESSARIA / SUPERATA DAL PERCORSO SUCCESSIVO

La domanda non viene dichiarata risolta. Il mezzo originario — per esempio un confronto teorico esteso fra prodotti maturi — non è più necessario a una decisione bloccante, perché il problema è stato assorbito da distinzioni più precise e da una falsificazione successiva già assegnata.

### 2.1 — Come viene valutato il nucleo

La quantità di K-ID non misura la coverage. Una domanda è coperta quando le conoscenze correnti:

1. rispondono al problema che la domanda doveva decidere;
2. preservano la distinzione e la perdita prodotta dal suo collasso;
3. separano ciò che è stabile da forma, algoritmo o criterio ancora aperto;
4. consentono a FOL-36 di procedere senza inventare una fondazione;
5. dichiarano se la prova restante è ricerca, progettazione o falsificazione.

Il fatto che FOL-37 debba ancora falsificare una distinzione non trasforma automaticamente quella distinzione in ricerca residua FOL-34.

## 3 — Coverage completa Q1.1–Q8.3

| Q-ID | Problema reale | K-ID principali | Stato | Cosa sappiamo | Residuo | Destinazione del residuo |
|---|---|---|---|---|---|---|
| Q1.1 | Separare forma e semantica della sorgente dal significato interno, senza rendere documento o schema esterno la radice del Core. | S: K-049, K-050, K-057, K-170, K-172; C: K-148; X: K-048 | **SUFFICIENTEMENTE COPERTA** | Source, Observation, localizzazione, lettura sintattica, Mapping e Interpretation hanno significati distinti; il Mapping non trasforma lo schema sorgente in commitment Fold. | Nessun vuoto fondazionale. FOL-36 deve soltanto preservare le distinzioni già acquisite nella v2.1. | FOL-36 |
| Q1.2 | Distinguere ricezione, interpretazione, riconciliazione e scelta/applicazione del trattamento. | S: K-003, K-008, K-009, K-015, K-125, K-163, K-172, K-178; A: K-185 | **SUFFICIENTEMENTE COPERTA** | Produzione, conservazione, Admission, Work e Application non coincidono; Interpretation propone significati e Reconciliation propone coreferenze senza ammetterle. | Resta l’ownership concreta della formalizzazione non-Policy (D06). Serve chiarirla attraverso integrazione/test del contratto, non nuova ricerca teorica. | FOL-36 / FOL-37 |
| Q1.3 | Stabilire il confine fra adattamento/classificazione dell’ingresso e costruzione del significato. | S: K-008, K-009, K-042, K-163, K-171, K-172; C: K-187 | **SUFFICIENTEMENTE COPERTA** | La classificazione locale propone contesti e Mapping; Mapping applica corrispondenze; Interpretation compone significati. Acquisition non orchestra il futuro semantico. | Nessun residuo fondazionale; contratti e accorpamenti restano materia della futura anatomia/implementazione. | FOL-36 |
| Q2.1 | Preservare le distinzioni che consentono di raffinare la riconciliazione senza reinterpretare o fondere distruttivamente i dati. | S: K-071, K-121, K-122, K-123, K-124, K-125, K-127, K-133, K-138, K-139, K-144; C: K-143; A: K-141; X: K-120, K-137 | **SUFFICIENTEMENTE COPERTA** | Schema, valore e assegnazione sono distinti; match, ipotesi di coreferenza, uso unitario e identità non coincidono; la coreferenza resta contestabile e reversibile. Identificatori documentali nominati possono quindi fornire indizi di continuità, ma il loro soggetto e la loro assegnazione non sono dedotti dalla stringa. | Criteri Domain di unicità, riassegnazione e auto-link sono aperti. Sono necessari alla progettazione della riconciliazione, non alla fondazione generale prima di FOL-36. | FOL-12 / FOL-37 |
| Q2.2 | Evitare che uguaglianza dell’identificatore venga assunta come identità del referente fuori dal suo schema, ambito e tempo. | S: K-121, K-122, K-123, K-124, K-138 | **SUFFICIENTEMENTE COPERTA** | Un identificatore è schema + valore + assegnazione qualificabile; corrispondenza esatta o simile non prova identità e il Domain determina il soggetto e la continuità. | Restano criteri specifici per ciascuno schema e dominio. Non serve ulteriore ricerca fondazionale per conservarne il confine. | FOL-12 |
| Q2.3 | Gestire identità multi-sorgente senza confondere autorità, qualità, indipendenza e certezza della riconciliazione. | S: K-097, K-100, K-101, K-102, K-124, K-125, K-127, K-139; A: K-118, K-141 | **SUFFICIENTEMENTE COPERTA** | Quality è riferita a target/base/scopo; più origini non sono automaticamente indipendenti; Reconciliation conserva alternative e indizi contrari e può restare indeterminata. | Algoritmi, dimensioni dettagliate di Quality e soglie concrete di auto-link restano aperti. Servono ai casi e alla slice, non come teoria bloccante di FOL-13. | FOL-12 / FOL-37 / FOL-38 |
| Q3.1 | Definire il minimo di supporto, Provenance e Lineage necessario a spiegare origine, trasformazioni e qualità senza uno score o source unico. | S: K-049, K-054, K-061, K-097, K-100, K-103, K-105, K-106, K-109; C: K-098; A: K-065, K-118 | **SUFFICIENTEMENTE COPERTA** | Origine, supporto, trasformazioni, assessment e audit operativo sono separati; produttori conservano tracce materiali e il test di materialità limita la conservazione. | Forma tecnica/ontologica del supporto e tassonomia finale della Quality restano aperte. FOL-36 preserva il requisito; FOL-39 sceglierà la forma tecnica. | FOL-36 / FOL-39 |
| Q3.2 | Mantenere recuperabili e non intercambiabili osservazione, dichiarazione, interpretazione, verifica, derivazione e commitment. | S: K-035, K-037, K-050, K-055, K-076, K-115, K-158, K-159, K-176; X: K-155 | **SUFFICIENTEMENTE COPERTA** | Observation non è Assertion; contributo attribuito non è commitment; Verification non è Admission; Derivation conserva attività, conclusione e giustificazione. | Nessun residuo di ricerca fondazionale. Le forme concrete possono restare candidate senza perdere le distinzioni. | FOL-36 |
| Q3.3 | Stabilire quando basi originarie, supporti, Mapping e decisioni umane devono essere interrogabili separatamente. | S: K-033, K-034, K-035, K-054, K-075, K-093, K-105, K-106, K-108, K-109, K-110, K-116, K-149, K-175 | **SUFFICIENTEMENTE COPERTA** | Query può attraversare nature diverse; risultati materialmente usati mantengono basi e definizioni effettive; Explanation segue tracce reali senza inventarle. | Va verificato sui casi che la spiegazione utile recuperi davvero il minimo richiesto. È prova end-to-end/prodotto, non ricerca fondazionale. | FOL-37 / FOL-20 |
| Q4.1 | Preservare ruoli temporali e revisioni sufficienti a descrivere conoscenza longitudinale senza un timestamp o stato globale. | S: K-034, K-067, K-068, K-070, K-071, K-074, K-077, K-078, K-079, K-081, K-082, K-084, K-149; C: K-080; A: K-096; X: K-069 | **SUFFICIENTEMENTE COPERTA** | Tempo del contenuto, acquisizione, conoscenza, decisione e reference time sono distinti; tempo ignoto non si completa e continuità non si presume. Un’attesa motivata conserva base/finestra e può attivare attenzione, mentre il riscontro resta delimitato. | Precisioni, continuità per rapporto e regole temporali di specifici casi sono aperte. Vanno provate su attese e casi longitudinali, non ricercate in astratto. | FOL-18 / FOL-37 |
| Q4.2 | Separare un cambiamento nel mondo da una correzione o evoluzione di ciò che Fold sa sul medesimo mondo. | S: K-067, K-074, K-082, K-084, K-090, K-095 | **SUFFICIENTEMENTE COPERTA** | Successione reale, correzione, conflitto e informazione tardiva hanno storie diverse; una regola nuova non retrodata né riscrive il patrimonio precedente. | Nessun residuo fondazionale; restano classificazioni Domain dei casi concreti. | nessuna |
| Q4.3 | Distinguere cambiamento, rettifica, conflitto, supersession e risoluzione senza imporre bitemporalità o timeline universali. | S: K-070, K-082, K-083, K-084, K-088, K-089, K-090, K-095; A: K-096; X: K-069 | **SUFFICIENTEMENTE COPERTA** | Comparabilità precede conflitto; rettifica dichiarata/riconosciuta/applicata, impatto e rivalutazione sono separati; STALE/Validity globali sono respinti. | Criteri Domain per riconoscere rettifiche e conflitti e Policy di rivalutazione restano aperti. Devono emergere dai casi. | FOL-37 / FOL-18 |
| Q4.4 | Ricostruire uno stato corrente per tempo e scopo senza sostituire storia, conflitti o basi con l’ultimo valore. | S: K-034, K-070, K-073, K-074, K-076, K-077, K-079, K-140, K-149, K-150, K-161; C: K-080; X: K-072 | **SUFFICIENTEMENTE COPERTA** | Current Reconstruction è contestualizzata e può essere incompleta; Projection non crea semantica; aggregazioni hanno basi e impatti noti qualificano l’uso. Un mancato reperimento resta qualificato per corpus/finestra e non prova il mancato accadimento. | Occorre falsificare ricostruzioni e spiegazioni su casi end-to-end e composti. Non manca una distinzione teorica da cercare prima. | FOL-37 / FOL-20 |
| Q5.1 | Rappresentare realtà con relazioni, attività e situazioni nel tempo senza promuovere Activity/Event/Process a primitive universali. | S: K-024, K-047, K-055, K-059, K-076, K-131, K-147 | **SUFFICIENTEMENTE COPERTA** | Operatività interna non prova primitive del mondo; proposizioni, famiglie relazionali, modalità e derivazioni possono descrivere fenomeni senza un Event universale. | Non è ancora falsificato su una catena composta reale. Questo blocca la validazione finale di FOL-13, ma richiede il test cross-domain di FOL-37, non nuova teoria. | FOL-37 |
| Q5.2 | Capire quali proprietà di un sistema composto appartengono alle parti e quali dipendono dalle relazioni/composizione. | S: K-056, K-059, K-073, K-076, K-113, K-131, K-132, K-150; C: K-143 | **SUFFICIENTEMENTE COPERTA** | Referent, Value, contenuti proposizionali, relazioni e derivazioni non collassano; una ricostruzione può usare rete e aggregazioni mantenendo criteri e basi. | Non esiste né serve ora una tassonomia universale delle proprietà emergenti. La sufficienza della composizione va falsificata sulla commessa/organizzazione. | FOL-37 |
| Q5.3 | Derivare e spiegare lo stato di un sistema composto senza ridurlo a una somma opaca delle parti. | S: K-073, K-075, K-076, K-085, K-105, K-109, K-110, K-150, K-162 | **SUFFICIENTEMENTE COPERTA** | Derivation, Current Reconstruction e Explanation conservano premesse, inclusioni, regole, tempo, impatti e limiti; una nuova aggregazione non è osservazione. | La capacità è concettualmente rappresentabile ma non ancora dimostrata su uno stato composto. Serve falsificazione in FOL-37; il comportamento di risposta utile resta FOL-20. | FOL-37 / FOL-20 |
| Q5.4 | Stabilire se un referente composto possa avere conoscenza propria e conclusioni derivate dalla rete senza fonderle. | S: K-055, K-059, K-073, K-076, K-132, K-150; C: K-143 | **SUFFICIENTEMENTE COPERTA** | Un locus referenziale può ricevere contenuti propri; relazioni e derivazioni mantengono natura e Lineage; la Projection non ridefinisce l’identità del referente. | Il limite pratico della composizione non è deciso a priori e va stressato sul caso cross-domain, non convertito in nuova primitiva. | FOL-37 |
| Q6.1 | Individuare le assunzioni perse verificando il Core solo su referenti semplici e casi documentali object-centric. | S: K-024, K-047, K-056, K-059, K-131, K-156, K-157 | **SUFFICIENTEMENTE COPERTA** | Il progetto ha già identificato i collassi da evitare: ogni indirizzabile non è Referent, relazioni/operatività non sono uniformi e distinzioni non fissano l’inventario software. | Resta da dimostrare quali di questi rischi falliscano davvero sulla catena cantieristica. È esattamente il gate empirico di FOL-37 e non ricerca teorica aggiuntiva. | FOL-37 |
| Q6.2 | Separare domande epistemiche trasversali da problemi che emergono soltanto con composizione, attività e dipendenze. | S: K-047, K-055, K-059, K-067, K-076, K-097, K-105, K-113, K-131, K-150 | **SUFFICIENTEMENTE COPERTA** | Identità, contenuto, tempo, qualità, origine e giustificazione restano domande trasversali; composizione introduce relazioni, inclusioni e dipendenze senza cambiare automaticamente quelle nature. | Il confine deve reggere in un caso composto reale; non occorre completare una teoria generale object/process/system-centric. | FOL-37 |
| Q6.3 | Verificare se Referent basti per ogni fenomeno o se servano forme informative differenti senza trasformare tutto in oggetto. | S: K-024, K-047, K-055, K-056, K-130, K-131, K-132, K-186; C: K-143; X: K-120 | **SUFFICIENTEMENTE COPERTA** | Referent è distinto dall’indirizzabilità; Assertion non assorbe tutto; famiglie epistemiche, rappresentative, inferenziali e operative mantengono obblighi differenti. | La forma finale di Referent resta candidata e va attivamente falsificata in FOL-37. Questo non autorizza ricerca per scegliere ora Activity/Event/Process. | FOL-37 |
| Q7.1 | Preservare confini che consentano a sorgenti, Mapping, Domain e Policy di cambiare senza rifondare o reinterpretare tutto. | S: K-064, K-090, K-091, K-093, K-112, K-113, K-116, K-162, K-172 | **SUFFICIENTEMENTE COPERTA** | Risorse, memorie e attività sono distinte; cambiamenti a Mapping/Domain/Core/Policy hanno effetti diversi e seguono dipendenze materiali, non retroattività generale. | FOL-36 deve ripristinare nella v2.1 i vincoli già acquisiti e superare il Knowledge Preservation Gate. Non serve altra ricerca per definirli. | FOL-36 |
| Q7.2 | Distinguere le forme generali della conoscenza dai significati e criteri che solo un Domain può stabilire. | S: K-047, K-064, K-071, K-113, K-121, K-138, K-147, K-162 | **SUFFICIENTEMENTE COPERTA** | Core preserva distinzioni trasversali; Domain stabilisce soggetti, schemi, significati, vincoli e continuità; meccanismi operano sulla semantica fornita. | Nessun residuo fondazionale; la semantica dei singoli domini resta deliberatamente locale. | nessuna |
| Q7.3 | Stabilire se Domain debba fornire semantica e regole oltre alla classificazione. | S: K-112, K-113, K-121, K-138, K-162, K-170, K-171, K-172 | **SUFFICIENTEMENTE COPERTA** | Domain non è un classificatore: definisce significati, tipi di soggetto, schemi, vincoli e regole inferenziali; classificazione, Mapping e Interpretation restano separati. | Nessun residuo di ricerca fondazionale; i contenuti Domain specifici verranno definiti nei casi pertinenti. | nessuna |
| Q7.4 | Collocare traduzione sorgente, semantica Domain, valutazione Quality, Policy, Decision e Admission senza fonderne l’autorità. | S: K-003, K-014, K-015, K-016, K-018, K-064, K-090, K-112, K-113, K-162, K-172, K-173; A: K-185; X: K-017, K-153, K-154 | **SUFFICIENTEMENTE COPERTA** | Il test di collocazione distingue corrispondenze, significati/vincoli, valutazioni, meccanismi, scelte di comportamento e applicazione; Policy non decide correttezza inferenziale. | D06 lascia aperta la formalizzazione delle Decision non-Policy e il test domestico deve verificare l’applicabilità nei rami. È contratto progettuale, non nuova ricerca. | FOL-36 / FOL-37 |
| Q7.5 | Distinguere Mapping e Domain pur riconoscendo che il Mapping traduce fra semantica sorgente e significato di destinazione. | S: K-090, K-112, K-113, K-116, K-121, K-170, K-172 | **SUFFICIENTEMENTE COPERTA** | Mapping verifica/applica corrispondenze versionate; Domain definisce il significato e i vincoli a cui esse puntano; fonderli nasconde dipendenze e impatto delle revisioni. | Nessun residuo fondazionale; restano definizioni e Mapping concreti del dominio scelto. | nessuna |
| Q8.1 | Usare la crescita di sorgenti, modelli, identità, tempo e relazioni per trovare problemi ricorrenti senza importare un prodotto maturo. | S: K-047, K-082, K-090, K-101, K-121, K-131, K-138, K-156, K-157 | **NON PIÙ NECESSARIA / SUPERATA DAL PERCORSO SUCCESSIVO** | Il Ledger contiene già i collassi concreti da evitare e la decisione 0001 autorizza pressioni limitate; non contiene però un catalogo comparativo che provi la ricorrenza indipendente nei prodotti citati. | Quel catalogo non è più necessario per chiudere FOL-13: l’evidenza decisiva sarà il failure osservato sui casi Fold. Non va dichiarato “risposto” né riaperto come ricerca accademica. | FOL-37 |
| Q8.2 | Distinguere separazioni ricorrenti fra approcci indipendenti da scelte specifiche di un prodotto. | S: K-047, K-113, K-156, K-157, K-184, K-186 | **NON PIÙ NECESSARIA / SUPERATA DAL PERCORSO SUCCESSIVO** | È stabile il criterio negativo: ricorrenza esterna o nome di una risorsa non bastano a creare primitive/componenti; ogni separazione deve conservare un problema Fold dimostrato. | Il confronto sistematico fra Palantir/Cognite/Celonis non è stato consolidato nel Ledger, ma non blocca FOL-13 perché nessuna scelta esterna verrà adottata come blueprint. La verifica passa ai casi. | FOL-37 |
| Q8.3 | Definire il gate con cui una separazione osservata altrove diventa pressione fondazionale legittima per Fold. | S: K-047, K-091, K-156, K-157, K-184, K-186 | **SUFFICIENTEMENTE COPERTA** | La decisione canonica 0001 richiede direzione autorizzata e una perdita semantica, falsa equivalenza o responsabilità resa irrecuperabile; complessità o diffusione esterna non bastano. | Resta applicare il gate senza adattare preventivamente la v2.1 al cantiere. È falsificazione FOL-37, non nuova ricerca FOL-34. | FOL-37 |

## 4 — Ricerca fondazionale residua autorizzata

**Elenco vuoto.**

Nessuna delle 28 domande è classificata `PARZIALMENTE COPERTA — RICERCA RESIDUA NECESSARIA`. Di conseguenza questo audit non autorizza:

- una nuova deep research generalista;
- una ricerca comparativa estesa su Palantir, Cognite o Celonis;
- la scelta preventiva di primitive Activity/Event/Process;
- la progettazione del caso cantieristico prima di FOL-37;
- la trasformazione di un algoritmo o schema tecnico in risposta fondazionale.

Non viene quindi compilata una scheda «cosa non sappiamo / perché blocca / evidenza / ricerca minima / abbastanza»: non esiste un residuo che superi il test di necessità per FOL-13/FOL-36.

Questa conclusione è più stretta di «sappiamo tutto». Significa soltanto che i vuoti rimasti si risolvono meglio tramite integrazione controllata, test su casi, progettazione di prodotto o scelta tecnica.

## 5 — Verifica genealogica delle due pressioni riemerse nella review

### 5.1 — Continuità documentale tramite identificatori reali

**Pressione.** POD, PDR, numero contratto, IBAN o altri identificatori nominati nei documenti possono aiutare a collegare documenti alla stessa realtà oppure a relazioni correlate.

**Genealogia già presente.**

| Passaggio necessario | K-ID | Stato | Conseguenza acquisita |
|---|---|---|---|
| Distinguere identità documentale da file/rappresentazioni | K-028, K-133 | STABILE | Il numero o raggruppamento dei file non decide quanti documenti o soggetti esistano. |
| Distinguere schema, valore e assegnazione | K-121 | STABILE | Il Domain stabilisce genere di soggetto, ambito e condizioni; la stringa non incorpora da sola il suo referente. |
| Distinguere osservazione da assegnazione | K-122, K-123 | STABILE | Presenza e normalizzazione dell’identificatore non sono ancora una coreferenza corretta. |
| Usare il match come indizio, non come verità o autorizzazione | K-124, K-125 | STABILE | Reconciliation conserva alternative, supporti, contrari e indeterminatezza. |
| Preservare correzione e reversibilità | K-127 | STABILE | Un collegamento non distrugge differenze e può essere contestato. |
| Determinare quale continuità è in gioco | K-071, K-138 | STABILE | Domain distingue, per esempio, punto, rapporto e contratto; nessun cambio o uguaglianza di Identifier decide automaticamente l’identità. |
| Lasciare aperti criteri e algoritmi specifici | K-141 | APERTA | Univocità, riuso e auto-link per schema non sono stati falsamente stabilizzati. |

**Valutazione.** La pressione è già coperta genealogicamente e rafforza Q2.1–Q2.3, in particolare Q2.1/Q2.2. Non emerge una nuova lacuna fondazionale. Ciò che manca sono i criteri specifici di riconciliazione e unicità, già destinati a FOL-12 e alla falsificazione FOL-37.

Non vengono adottati `identifiers(type, value, position)`, una tabella, un campo, regex, fallback LLM o una fase backend. Sono possibili scelte tecniche/implementative di FOL-39, non conoscenza prodotta da questo audit.

### 5.2 — Elemento atteso ma non reperito

**Pressione.** Recuperare soltanto ciò che è presente non dimostra la capacità di riconoscere che un elemento previsto non sia stato reperito entro un perimetro e una finestra pertinenti.

**Genealogia già presente.**

| Passaggio necessario | K-ID | Stato | Conseguenza acquisita |
|---|---|---|---|
| Delimitare il risultato negativo | K-034, K-149 | STABILE | «Non trovato» vale entro corpus, tempo, criteri, copertura e limiti; non diventa assenza nel mondo. |
| Non confondere mancato riscontro e mancato ingresso | K-077 | STABILE | Materiale arrivato ma non interpretato può coesistere con nessun riscontro riconosciuto. |
| Separare periodicità, previsione e obbligo | K-078 | STABILE | Una cadenza osservata non crea un obbligo o un fatto. |
| Rendere possibile l’attenzione nel tempo quando promessa | K-079 | STABILE | Reference time e Work autorizzato consentono di tornare sulla condizione senza creare Source o alert universali. |
| Separare base, finestra/riscontro e comportamento | K-080 | CANDIDATA | È acquisita una composizione candidata; il suo stato non viene promosso. |
| Evitare una nuova primitiva/controller universale | K-081 | STABILE | Expectation, Temporal Controller ed Event temporale Core non sono dimostrati necessari. |
| Conservare il seguito operativo | K-062 | STABILE | Work mantiene obiettivo, scope, esiti, dipendenze e proprietario della prosecuzione. |
| Recuperare il corpus informativo effettivo | K-175 | STABILE | Query attraversa Source, Observation, proposte e commitment senza forzare nuovi dati dentro l’attesa. |

**Valutazione.** Il problema fondazionale è già coperto e rafforza Q4.1/Q4.4, con collegamento a Q3.3. K-080 resta CANDIDATA, ma la necessità di distinguere previsione, risultato delimitato e comportamento è sostenuta dalle K-ID STABILE circostanti. Non emerge una lacuna bloccante per FOL-36.

Restano da verificare su casi reali:

- la forma concreta con cui il lavoro torna pertinente;
- l’adeguatezza del corpus e della copertura;
- il comportamento quando esiste materiale ricevuto ma non interpretato;
- le condizioni per coinvolgere una persona.

Questi sono test di FOL-37 e regole di FOL-18/FOL-20. Non autorizzano un algoritmo di cadenza, uno scheduler specifico o una fase backend.

## 6 — Questioni ancora aperte, ma non nuova ricerca FOL-34

La chiusura della coverage non significa assenza di domande aperte. Tutte le 14 K-ID APERTA del Ledger restano tali.

| K-ID APERTA | Residuo preservato | Destinazione più pertinente | Perché non è nuova ricerca bloccante |
|---|---|---|---|
| K-026, K-046 | Percorsi MVP, granularità Work, retry, acquisizione, verifiche e domande multiple | FOL-37 / FOL-38 / FOL-39 | Richiedono casi, slice e contratti concreti. |
| K-032, K-142 | Locator, composizione/identità documentale e vocabolario finale delle relazioni | FOL-37 / FOL-39 | Le distinzioni sono acquisite; restano forma e criteri specifici. |
| K-065 | Forma indirizzabile del supporto | FOL-36 / FOL-39 | Target, base e scope sono stabili; non è decisa la forma tecnica/ontologica. |
| K-066 | Confine delle meta-Assertion su interpretazioni interne | FOL-37 | Va falsificato con un caso che dimostri la perdita, non chiuso per generalità. |
| K-096 | Precisione temporale, continuità specifica, rettifiche, rivalutazione e retention ulteriore | FOL-18 / FOL-37 / FOL-39 | I principi temporali sono acquisiti; restano regole del caso e conservazione concreta. |
| K-118 | Dimensioni dettagliate di Quality, indipendenza empirica e soglie | FOL-12 / FOL-37 | Occorrono evidenze del caso e rischio applicativo, non una formula universale. |
| K-119 | Forma della conferma di Observation e persistenza concreta delle proposte | FOL-37 / FOL-39 | Esistenza e recuperabilità delle proposte sono già acquisite. |
| K-141 | Forma Identifier, unicità/riassegnazione e auto-link | FOL-12 / FOL-39 | Schema–valore–assegnazione sono stabili; restano Domain e algoritmo. |
| K-145 | Ammissione di Referent senza Assertion già ammessa | FOL-37 | Serve un contratto verificato su casi, non una primitiva preventiva. |
| K-160 | Equivalenza/identità del contenuto proposizionale | FOL-37 | Il default conservativo evita la fusione; il criterio va falsificato. |
| K-183 | Granularità finale degli accorpamenti | FOL-36 / FOL-39 | Numero di responsabilità e componenti non è un quesito fondazionale autonomo. |
| K-185 | Ownership della formalizzazione Decision/Disposition non-Policy | FOL-36 / FOL-37 | Autorità e memoria sono acquisite; manca un contratto/proprietario concreto. |

Le 15 K-ID CANDIDATA restano anch’esse candidate: K-004, K-006, K-012, K-023, K-029, K-053, K-080, K-098, K-136, K-143, K-146, K-148, K-168, K-182 e K-187. Il verdetto di coverage non le promuove a STABILE.

## 7 — Q5, Q6 e Q8: ricerca nuova oppure falsificazione?

### Q5 — Sistemi composti

Il Ledger stabilisce già le separazioni necessarie fra Referent, Value, proposizioni, relazioni, derivazioni, ricostruzioni, supporti e operatività. Stabilisce anche che queste distinzioni non dimostrano primitive Activity/Event/Process.

Ciò che manca è sapere se la composizione regga **in un caso reale completo**. Questa è la sequenza di FOL-37: freeze della struttura, stress cross-domain, registrazione e classificazione dei failure point. Ricercare prima una teoria generale della composizione adattando il modello al cantiere invaliderebbe il test.

### Q6 — Object/process/system-centric

Il progetto non deve scegliere una filosofia unica. Ha già acquisito che «interrogabile», «referente», «assertion», «relazione» e «operatività» non sono sinonimi. La forma candidata di Referent va però messa attivamente sotto stress.

Il residuo è quindi falsificazione successiva della v2.1. Se FOL-37 dimostrerà una perdita semantica non rappresentabile con le distinzioni esistenti, quel failure potrà riaprire il lavoro fondazionale con evidenza concreta. Non lo si anticipa qui.

### Q8 — Sistemi maturi come pressione

Q8.1 e Q8.2 non vengono marcate sufficientemente coperte: il Ledger non conserva un confronto sistematico fra i prodotti citati che dimostri ricorrenza indipendente. Vengono invece classificate **non più necessarie / superate dal percorso successivo** perché:

1. la decisione 0001 vieta di trasformare ricorrenza esterna in requisito automatico;
2. i Round hanno già identificato collassi concreti nei problemi Fold;
3. FOL-37 verifica la struttura su pressioni reali senza usarne una come blueprint;
4. nessuna decisione bloccante di FOL-13 richiede oggi il catalogo comparativo esteso.

Q8.3 resta sufficientemente coperta: la decisione 0001 contiene il gate positivo. Una pressione influenza le fondamenta solo se è autorizzata e rende osservabile una perdita semantica, una falsa equivalenza o una responsabilità resa irrecuperabile.

## 8 — Problemi genealogici e allineamenti da non correggere silenziosamente

### 8.1 — Nessuna contraddizione Ledger↔FOL-34 che autorizzi nuova ricerca

Non è stata trovata una domanda per la quale il Ledger dichiari chiuso ciò che una K-ID corrente mantiene aperto, né una conoscenza STABILE incompatibile con il nucleo delle Q. I residui sono stati preservati con i rispettivi stati.

### 8.2 — Evoluzioni operative presenti in Linear

Esistono due disallineamenti storici/operativi da rendere visibili, senza modificarli in questo lavoro:

- la descrizione originaria di FOL-34 attendeva una campagna comparativa e relativi artefatti; il checkpoint del 4 settembre ne cambia esplicitamente il risultato immediato in coverage controllata. Q8.1/Q8.2 sono quindi assorbite, non retroattivamente “risposte”;
- la descrizione di FOL-13 conserva ancora il piccolo controesempio non domestico come controllo diretto; il checkpoint operativo più recente assegna la sequenza a FOL-36 e poi FOL-37, con test domestico e cross-domain. Questo audit segue il checkpoint più recente per la destinazione operativa, senza riscrivere il testo storico.

Inoltre la matrice FOL-34 consentiva in astratto di accorpare domande equivalenti; il mandato di questo audit richiede invece 28 righe esatte. Le domande restano quindi separate anche quando condividono K-ID.

Queste sono note di allineamento, non discrepanze genealogiche del Ledger e non vengono corrette in Linear.

## 9 — Controlli conclusivi

| Controllo | Esito |
|---|---|
| Esistono esattamente 28 righe Q1.1–Q8.3 | Sì: 28 ID unici, sequenza completa |
| Domande saltate o fuse | Nessuna |
| SUFFICIENTEMENTE COPERTA sostenuta da conoscenza acquisita | Sì: ogni riga contiene almeno una K-ID STABILE pertinente |
| K-ID CANDIDATA/APERTA presentate come STABILE | Nessuna; sigle e stati sono espliciti |
| Posizioni SUPERATE usate come risposte correnti | Nessuna; compaiono solo per genealogia |
| Ricerca residua veramente bloccante | Nessuna identificata |
| Questioni Q5/Q6 destinate a nuova teoria | No: destinate a falsificazione FOL-37 |
| Q8.1/Q8.2 dichiarate falsamente risolte | No: classificate non più necessarie/superate dal percorso |
| Nuove primitive/responsabilità/soluzioni | Nessuna |
| Soluzioni tecniche della review adottate | Nessuna |
| v2, Ledger, Coverage Map o delta modificati | No |
| Notion o Linear modificati | No |
| Commit, push o branch | Nessuno |

## 10 — Conteggio e verdict

| Stato principale | Numero |
|---|---:|
| SUFFICIENTEMENTE COPERTA | 26 |
| PARZIALMENTE COPERTA — RICERCA RESIDUA NECESSARIA | 0 |
| NON PIÙ NECESSARIA / SUPERATA DAL PERCORSO SUCCESSIVO | 2 |
| **Totale** | **28** |

Domande che autorizzano nuova ricerca: **nessuna**.

Verdetto finale:

> **FOL-34 COVERAGE SUPERATA — NESSUNA RICERCA FONDAZIONALE RESIDUA BLOCCANTE**

Conseguenza operativa dell’audit: FOL-34 non deve avviare altra ricerca per completezza. Dopo la verifica e il versionamento separato di questo artefatto, il progetto può procedere a FOL-36; FOL-13 resta da consolidare e falsificare secondo la sequenza Linear, non è chiusa da questo solo verdetto.
