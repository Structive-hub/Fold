---
title: "Fold — snapshot immutabile della candidata v2 integrata"
status: Historical
snapshot_date: 2026-09-04
model_status: "candidata provvisoria / non canonica"
gate: "v2 CANDIDATA CORRETTA — PRONTA PER REVIEW INDIPENDENTE"
origin: "Messaggio finale della conversazione Fold, ordinal 1105, sessione 01a05d0a-e483-7793-a648-e46306e04177"
original_body_sha256_utf8: "fad314962da4e44968824c213d44fcd0ac4eef8c02856cfd386d5f2d8dbc2567"
---

Questo file conserva la candidata integrata con D01–D05 e D06 esplicitamente aperto, precedente alla review indipendente di Claude. Non incorpora la review né valutazioni successive.

**Snapshot storico immutabile: non sovrascrivere il corpo con revisioni successive.** Una futura versione deve avere un altro file. L'immutabilità è documentale, non un blocco tecnico del filesystem.

Il corpo delimitato sotto riproduce esattamente il messaggio originale, compreso il suo delta conclusivo. Il digest è calcolato sul testo originale UTF-8, senza questi metadati e delimitatori. Il gate non equivale a canonizzazione o readiness implementativa.

Artefatti associati: [Ledger](fold-knowledge-decision-ledger-2026-09-04.md) · [Coverage Map](fold-coverage-ledger-v2-2026-09-04.md).

<!-- BEGIN ORIGINAL V2 BODY -->
# Fold — Candidata v2 provvisoria integrata

**Stato:** candidata concettuale, non canonica.  
**Scopo:** descrivere in modo autonomo il funzionamento di Fold, mantenendo distinguibili informazione, attività, risorse, governance, operatività, memorie e funzioni.

Questo documento non definisce servizi, classi, database, API, tecnologie o il perimetro dell’MVP.

# A — Scelta della forma organizzativa

| Opzione | Vantaggio | Rischio |
|---|---|---|
| **1. Macro-aree funzionali con piani trasversali** | Rende riconoscibili acquisizione, interpretazione, ragionamento e uso. | Può suggerire una pipeline universale e relegare governance, memorie e operatività a note laterali. |
| **2. Due macro-cicli: assimilazione e uso** | Evidenzia feedback e costruzione progressiva della conoscenza. | Query su materiale grezzo, rivalutazioni e decisioni operative attraversano entrambi i cicli e diventano difficili da collocare. |
| **3. Mappa per nature con una rete di responsabilità** | Separa ciò che esiste, ciò che viene fatto, ciò che guida le attività e ciò che ne governa gli effetti. | Richiede viste specializzate per mostrare i percorsi senza sovraccaricare la vista generale. |

La candidata adotta **l’opzione 3**.

La struttura principale distingue le nature; i percorsi informativi e operativi sono mostrati nelle viste successive. I due macro-cicli rimangono letture possibili della stessa struttura, non contenitori obbligatori.

Le responsabilità sono raggruppate per problema, senza trasformare le 24 voci della checklist di copertura in 24 componenti software.

# B — Principio organizzativo della candidata v2

Fold conserva rappresentazioni e contributi; produce osservazioni, interpretazioni e conclusioni; governa quali commitment può assumere e quali comportamenti può eseguire.

La candidata distingue:

- **informazione:** ciò che esiste e deve restare recuperabile;
- **attività:** trasformazioni, valutazioni e operazioni;
- **risorse:** definizioni e criteri consultati;
- **governance:** commitment, autorità, disposizioni e revisioni;
- **operatività:** lavori, tentativi, attese ed effetti;
- **uso:** risultati e comportamenti utili per l’utente.

Le memorie preservano queste nature senza renderle equivalenti.

Un elemento può comparire in più viste, ma non viene duplicato concettualmente. Nessuna delle viste costituisce una sequenza di esecuzione universale o un’architettura software.

# C — Anatomia v2 candidata completa

## Legenda

- `[informazione]`: contenuto o risultato recuperabile.
- `[attività]`: responsabilità attiva con un problema proprio.
- `[meccanismo]`: capacità di ragionamento distinta.
- `[capacità]`: funzione interna o specializzata.
- `[risorsa]`: definizione consultata.
- `[governance]`: posizione, autorizzazione o effetto governato.
- `[operativo]`: lavoro ed esecuzione.
- `[memoria]`: responsabilità di conservazione.

I raggruppamenti dell’albero sono organizzativi: non sono componenti aggiuntivi.

```text
FOLD — CANDIDATA v2 PROVVISORIA
│
├── 1. MODELLO INFORMATIVO
│   │
│   ├── Grammatica semantica centrale
│   │   ├── Referent
│   │   ├── Assertion e contenuto proposizionale
│   │   ├── Value
│   │   ├── Identifier: schema, valore, assegnazione
│   │   └── qualificazioni temporali e contestuali
│   │
│   ├── Materiale e risultati adiacenti
│   │   ├── Source e rappresentazioni
│   │   ├── locator / anchor
│   │   ├── Observation
│   │   ├── Interpretation Result
│   │   ├── risultati di Query delimitati
│   │   └── ricostruzioni contestualizzate
│   │
│   ├── Giustificazione e qualificazione
│   │   ├── contributi attribuiti, con base originaria recuperabile
│   │   ├── supporti qualificati
│   │   ├── Quality Assessment
│   │   ├── Provenance e Lineage
│   │   ├── giustificazioni di Derivation
│   │   ├── conflitti e relazioni di correzione
│   │   └── qualificazioni d'impatto
│   │
│   └── Posizione rispetto alla Knowledge
│       ├── Referent e Assertion proposti
│       ├── alternative e dipendenze non risolte
│       └── Knowledge governata: commitment ammessi
│
├── 2. RETE DELLE ATTIVITÀ
│   │
│   ├── Disponibilità del materiale
│   │   ├── [attività] ricezione tracciata
│   │   │   ├── [capacità] adattamento del canale
│   │   │   └── [capacità] registrazione dell'Acquisition
│   │   ├── [attività] validazione tecnica
│   │   ├── [attività] deduplicazione tecnica
│   │   └── [attività] preservazione delle Source
│   │
│   ├── Produzione del significato
│   │   ├── [attività] estrazione e produzione delle Observation
│   │   │   ├── accesso al formato
│   │   │   ├── testo nativo / OCR
│   │   │   ├── layout e struttura
│   │   │   └── parsing sintattico con conservazione del grezzo
│   │   ├── [attività] valutazione ed esecuzione del Mapping
│   │   └── [attività] Interpretation
│   │       ├── classificazione contestuale
│   │       ├── composizione delle rappresentazioni documentali
│   │       ├── formulazione delle proposte referenziali
│   │       └── composizione di Assertion, alternative e dipendenze
│   │
│   ├── Ragionamento
│   │   ├── [meccanismo] Identity Reconciliation
│   │   │   └── [specializzazione] document co-reference
│   │   ├── [meccanismo] Comparison
│   │   │   └── [specializzazione] Conflict Detection
│   │   ├── [meccanismo] Temporal Evaluation
│   │   ├── [meccanismo] Derivation
│   │   ├── [meccanismo] Current Reconstruction
│   │   └── [meccanismo] Impact Assessment
│   │
│   ├── Attività di governo
│   │   ├── [attività] valutazione delle Application Decision Policies
│   │   ├── [attività] gestione della Verification
│   │   └── [attività] Admission e applicazione delle revisioni
│   │
│   └── Accesso, uso e interazione
│       ├── [attività] Query & Retrieval
│       │   └── [capacità] traversal delle relazioni conservate
│       ├── [attività] composizione delle Projection
│       ├── [attività] composizione delle Explanation
│       ├── [attività] realizzazione dei casi d'uso
│       ├── [attività] Presentation
│       └── [attività] User Contribution Intake
│
├── 3. RISORSE DI RIFERIMENTO
│   ├── Core Model e Core invariants
│   ├── Domain Model e Identifier Schemes
│   ├── Mapping Definitions
│   ├── Quality Model
│   ├── Application Decision Policies
│   ├── criteri dei casi d'uso
│   └── versioni, scope e condizioni di applicabilità
│
├── 4. GOVERNANCE
│   ├── posizione proposta e commitment ammessi
│   ├── autorità e scelte deliberate
│   ├── Decision
│   ├── Disposition
│   ├── Admission
│   ├── contestazione e revisione governata
│   └── applicabilità della disposizione nel contesto corrente
│
├── 5. PIANO OPERATIVO
│   ├── Acquisition: storia della ricezione
│   ├── Work: lavoro durevole con un proprietario
│   ├── Attempt, attese, dipendenze, riprese, fallimenti ed esiti
│   ├── Application: esecuzione tentata o avvenuta
│   └── coordinamento operativo distribuito presso i proprietari dei Work
│
├── 6. USO DEL PRODOTTO
│   ├── accesso al materiale, anche non interpretato
│   ├── risposte basate su Knowledge e ricostruzioni
│   ├── spiegazioni, verifiche e risultati applicativi
│   └── nuovi contributi e scelte dell'utente
│
└── 7. RESPONSABILITÀ DI CONSERVAZIONE E VINCOLI TRASVERSALI
    ├── memorie informative
    ├── memoria operativa
    ├── cattura locale di Provenance e Lineage
    ├── assessment e validazioni locali
    ├── produzione locale dei supporti
    ├── autorizzazioni, sicurezza e privacy
    └── conservazione, ripristino, versionamento e audit
```

La base originaria del contributo umano è una responsabilità di recuperabilità dell’ingresso, non una nuova primitiva. Il suo rapporto con il contributo interpretato è precisato nelle viste e nelle schede pertinenti.

## Direzioni principali

L’albero indica dove appartengono le responsabilità. Le loro relazioni principali sono:

```text
Attività ──PRODUCES──> risultati informativi
Attività ──CONSULTS──> risorse di riferimento
Attività ──READS/WRITES──> memorie pertinenti

Interpretation ──READS──> Knowledge e contesto recuperato
Ragionamento ──READS──> proposte, Knowledge e giustificazioni
Admission ──WRITES──> commitment e storia della governance

Functions ──CALLS──> Query, ragionamento, Verification o altre attività
Functions ──MAY_OPEN_WORK──> lavoro operativo autorizzato

User Contribution Intake ──WRITES──> base originaria e contesto pertinenti
User Contribution Intake ──PRODUCES──> contributi contestualizzati
Interpretation ──PRODUCES──> significati attribuiti a tali contributi

Ogni produttore ──WRITES──> propria Provenance / Lineage pertinente
Ogni consumatore ──CONSTRAINED_BY──> qualificazioni e invarianti applicabili
```

`Correction / Supersession` non compare come unico componente: Interpretation e Comparison riconoscono le relazioni, Temporal Evaluation distingue la successione, Admission applica la revisione autorizzata e Impact Assessment ne valuta le dipendenze.

## Vincoli comuni ai collegamenti

I feedback fra responsabilità non autorizzano auto-supporto:

> Nessun risultato può diventare supporto epistemico di sé stesso attraverso un ciclo di Interpretation, Reconciliation, supporto, Derivation o riuso della Knowledge.

Un ciclo di elaborazione può esistere e produrre risultati utili. Non può far apparire il risultato iniziale come una nuova giustificazione indipendente di sé stesso.

Analogamente, molteplicità di rappresentazioni, contributi, letture, percorsi o derivazioni non implica indipendenza epistemica. Origine comune e dipendenze pertinenti devono rimanere recuperabili.

Questi sono vincoli sui produttori e consumatori esistenti, non responsabilità affidate a nuovi controllori.

## Controllo anti-bloat della struttura

| Raggruppamento | Perché esiste | Che cosa non diventa |
|---|---|---|
| Modello informativo | Distinguere contenuti e qualificazioni | Un componente che “possiede tutto” |
| Rete delle attività | Assegnare le trasformazioni a proprietari comprensibili | Un orchestratore centrale |
| Risorse | Separare definizioni riutilizzabili dai risultati dei casi | Processi attivi |
| Governance | Separare valutazione, commitment e autorizzazione | Un unico Knowledge State |
| Piano operativo | Conservare avanzamento, attese ed effetti | Stato epistemico della Knowledge |
| Uso | Descrivere valore e interazione | Una nuova copia delle attività sottostanti |
| Memorie e trasversali | Preservare differenze e continuità | Un database distinto per ogni voce |

La denominazione `Core Engine` può indicare la famiglia del ragionamento, ma non aggiunge alcun controllore sopra i meccanismi.

# D — Vista informativa

## Percorso prevalente e accessi laterali

Le frecce indicano produzioni o dipendenze informative, non passaggi obbligatori.

```text
Materiale ricevuto
    │
    └── ricezione + preservazione ──> SOURCE
                                         │
                    ┌────────────────────┴─────────────────┐
                    │                                      │
              eventuale estrazione                    Query diretta
                    │                                      │
               OBSERVATION                         materiale recuperato
                    │
                    ├──────────────────────────────> Query diretta
                    │
                    │            Contributo umano ricevuto
                    │                        │
                    │              User Contribution Intake
                    │                        │
                    │              base originaria recuperabile
                    │              + contributo contestualizzato
                    │                        │
                    └────────────┬───────────┘
                                 │
                          INTERPRETATION
                                 ^
                                 │
                      contesto recuperato dalla KNOWLEDGE
                                 │
                  risultato dell'Interpretation
                                 │
                      INTERPRETATION RESULT
                      ├── Referent proposti
                      ├── Assertion proposte
                      ├── alternative
                      └── dipendenze mancanti
                                 │
                                 ├─────────────────> Query sulle proposte
                                 │
                                 ├── supporti e attribuzioni locali
                                 ├── assessment e validazioni locali
                                 └── eventuale riconciliazione /
                                     confronto / ragionamento
                                                 │
                                         eventuale Decision
                                                 │
                                             Disposition
                                                 │
                                     Admission, se pertinente
                                                 │
                                      KNOWLEDGE GOVERNATA
                                                 │
                            ┌────────────────────┼───────────────────┐
                            │                    │                   │
                          Query              Derivation       Reconstruction
                            │                    │                   │
                            └──────────── risultati qualificati ────┘
                                                 │
                                   Projection / Explanation / Function
                                                 │
                                           Presentation
```

Il contesto recuperato dalla Knowledge è un input dell’Interpretation; non è un passaggio obbligatorio successivo a essa.

Source, Observation e proposte possono restare nei rispettivi insiemi informativi senza procedere oltre. La loro recuperabilità non dipende dall’Admission.

Supporto e qualità non costituiscono una fase successiva alla proposta: vengono prodotti nei punti pertinenti e possono essere rivalutati nel tempo.

## Ingresso umano e significato attribuito

Nel percorso umano devono rimanere distinguibili:

```text
contenuto effettivamente ricevuto
                 ≠
significato attribuito tramite Interpretation
                 ≠
eventuale autorità della scelta
```

User Contribution Intake conserva, quando semanticamente pertinenti:

- contenuto effettivamente ricevuto;
- autore o origine;
- target;
- tempo;
- contesto;
- natura pertinente dell’interazione.

La natura dell’interazione può essere, per esempio, una dichiarazione libera, una risposta a una domanda, una conferma circoscritta o una scelta autorizzativa.

Una risposta «sì» deve quindi rimanere collegata a ciò cui rispondeva e al contesto necessario a comprenderne la portata. L’Interpretation può attribuirle un significato, ma quel significato non sostituisce silenziosamente la base ricevuta.

Non è richiesta una Observation artificiale. Non è deciso che ogni contributo umano debba essere una Source. È invece obbligatoria la recuperabilità di una base originaria distinta dalla sua successiva interpretazione.

Questo non implica conservare indiscriminatamente ogni evento dell’interfaccia.

## Uso della Knowledge come contesto

Interpretation può consultare la Knowledge disponibile. Deve però restare recuperabile quale contesto abbia contribuito al risultato.

Il risultato non può rientrare nel ciclo e apparire come nuova prova indipendente di sé stesso. Il riuso della Knowledge non cancella l’origine e le dipendenze del materiale consultato.

La distinzione è:

- **riutilizzare un risultato come contesto:** ammesso secondo il suo significato e le qualificazioni pertinenti;
- **contarlo come nuova giustificazione indipendente della conclusione da cui proviene:** non ammesso.

## Derivazione e supporto

Una conclusione derivata può:

- essere conservata come proposta e seguire un percorso di Admission;
- essere usata come risultato derivato di una consultazione, secondo i criteri applicabili;
- rimanere distinta da ciò verso cui Fold ha già assunto un commitment.

Mostrarla non la ammette implicitamente.

Materializzarla o riutilizzarla non la rende supporto indipendente delle proprie premesse. Due risultati derivati dalle stesse premesse non costituiscono automaticamente due conferme indipendenti.

## Percorsi che riaprono elaborazioni

```text
Function
   └── richiesta autorizzata ──> Verification
                                   │
                            nuovo contributo
                                   │
                         User Contribution Intake
                                   │
                  base originaria e contesto recuperabili
                                   │
                       Interpretation / nuovo assessment

Query
   └── richiede una conclusione ──> Derivation
                                      │
                           risultato + giustificazione

Cambiamento pertinente
   ├── nuova informazione
   ├── informazione tardiva
   ├── correzione
   └── nuova versione di una risorsa
                    │
             Impact Assessment
                    │
          qualificazione d'impatto
             ┌──────┴──────────────────────┐
             │                             │
     letta da Reconstruction       Decision / autorità
                                           │
                                 eventuale rivalutazione
                                           │
                              usa materiale già conservato
                                           │
                                 nuovi risultati e storia
```

Un’informazione tardiva entra come nuova informazione per Fold, ma conserva il tempo del contenuto a cui si riferisce. Non viene trasformata nel fatto “più recente nel mondo” soltanto perché acquisita per ultima.

Quando il percorso produce una nuova Quality Assessment, questa richiede una nuova base, un nuovo criterio oppure un nuovo contesto materialmente pertinente. La sola riapertura del lavoro non costituisce nuova giustificazione.

## Deviazioni ammesse esplicitamente

| Situazione | Percorso previsto |
|---|---|
| Source conservata senza interpretazione | Preservazione → memoria delle Source → Query |
| Observation non interpretata | Estrazione → memoria delle Observation |
| Proposta mai ammessa | Interpretation → memoria delle proposte |
| Interpretation che usa contesto esistente | Interpretation → Query → Knowledge qualificata, con dipendenze recuperabili |
| Contributo umano diretto | Intake → base originaria recuperabile e contributo contestualizzato → Interpretation, senza Observation artificiale |
| Funzione che chiede verifica | Function → disposizione pertinente → Verification |
| Derivazione richiesta al momento della Query | Query/Function → Derivation → risultato qualificato |
| Rivalutazione senza nuova acquisizione | Work → Source/Observation conservate + nuove risorse pertinenti |
| Informazione fuori sequenza | Nuova interpretazione → valutazione temporale e d’impatto → ricostruzione |
| Work in attesa | Conservazione operativa della dipendenza; la proposta può continuare a esistere indipendentemente |

# E — Vista Governance

## Origine della Decision ed effetti distinti

```text
Proposte, assessment, verifiche, ragionamento, impatti pertinenti
                  │
                  ├── input a Policy Evaluation
                  │             │
                  │       Decision da Policy
                  │
                  └── contesto per una scelta deliberata
                                │
                     utente / attore autorizzato
                                │
                      Decision da autorità esplicita

             Decision motivata e autorizzata
                              │
                         Disposition
                              │
             verifica di applicabilità corrente
                              │
           ┌──────────────────┼─────────────────────┐
           │                  │                     │
        Admission       Verification / Work    Application Function
           │                  │                     │
     commitment o       verifica / attesa /     comportamento
     revisione della    rivalutazione           applicativo
     Knowledge
           └──────────────────┴─────────────────────┘
                              │
                 storia dell'Application effettiva
```

Non esiste un produttore universale delle Decision. La valutazione delle Policy è uno dei percorsi; una scelta deliberata può avere un’autorità differente, purché prevista e tracciabile.

### Ownership dei percorsi non-Policy

È stabilito che una Decision può derivare sia da Policy Evaluation sia da un’autorità esplicita.

Resta da precisare quale responsabilità possieda la formalizzazione della Decision/Disposition nei percorsi non-Policy e se tale ownership sia locale al contesto decisionale o richieda un confine di Governance comune.

La questione è **aperta e non bloccante per la review della candidata**. Non viene introdotto un Decision Manager né viene assegnata per supposizione questa responsabilità all’Intake, alla Verification o alle Functions.

Restano comunque obbligatori:

- origine dell’autorità;
- target;
- scope;
- contesto;
- Decision;
- Disposition;
- storia dell’eventuale Application.

L’apertura riguarda il proprietario della formalizzazione, non la necessità di tali informazioni.

### Quattro significati non intercambiabili

| Concetto | Significato |
|---|---|
| **Decision** | Scelta motivata, con origine, autorità, target, scope e contesto |
| **Disposition** | Trattamento autorizzato da applicare |
| **Admission** | Applicazione governata che stabilisce o revisiona il commitment di Fold |
| **Application** | Storia dell’esecuzione effettivamente tentata o avvenuta |

Admission e Application non sono alternative ontologiche: una Admission applicata produce sia un effetto sulla Knowledge sia una storia operativa dell’applicazione.

Una Disposition può invece non essere applicata, fallire oppure risultare non più applicabile.

## Proposta, commitment e contestazione

`Proposed` qualifica una proposta; non è un nuovo oggetto universale.

Un’Assertion proposta può ricevere:

- nuovi contributi;
- supporti;
- contestazioni;
- verifiche;
- confronti e derivazioni.

Nessuno di questi eventi equivale automaticamente ad Admission.

Una contestazione può essere conservata prima che Fold decida quale comportamento adottare. La scelta di continuare a usare un contenuto non elimina la contestazione.

La correzione conserva almeno tre distinzioni:

1. un contributo o documento dichiara una correzione;
2. Fold riconosce e valuta la relazione fra contenuti;
3. una revisione governata modifica il commitment o il suo uso.

## Coreferenza e uso unitario

Una proposizione di coreferenza può ricevere supporto, essere ammessa, essere usata dalle funzioni e venire successivamente contestata.

L’ammissione o l’uso unitario non devono distruggere:

- le rappresentazioni originarie;
- le loro differenze;
- le relative Provenance;
- la giustificazione necessaria a contestare la conclusione.

Sulla base dell’informazione ancora legittimamente conservata, deve rimanere possibile revisionare la coreferenza e tornare a distinguere le rappresentazioni se una successiva evidenza mostra che riguardano soggetti differenti.

```text
co-reference ≠ merge distruttivo

merge operativo ≠ proposizione di identità
```

Il vincolo riguarda la preservazione concettuale e informativa necessaria alla reversibilità della conclusione. Non definisce una funzione software di unmerge.

## Applicabilità nel tempo

Prima di applicare una Disposition, la responsabilità competente controlla che:

- riguardi ancora il target pertinente;
- le condizioni necessarie siano ancora soddisfatte;
- l’autorità sia applicabile;
- non siano stati violati invarianti o vincoli;
- impatti noti non rendano improprio l’effetto previsto.

Se queste condizioni non reggono, non viene inventata silenziosamente una disposizione alternativa. Rimangono recuperabili la Decision storica e il motivo della mancata applicazione.

## Impatto epistemico e Policy

```text
Impatto determinato
       │
       ├── viene conservato come informazione qualificata
       ├── vincola le ricostruzioni pertinenti
       └── informa una scelta operativa
                 │
          rivalutare ora / dopo
          verificare / segnalare
          limitare un uso
```

La Policy può governare il seguito operativo, non cancellare l’impatto.

L’effetto di un cambiamento dipende dal bersaglio: una modifica del Mapping può affettare un’interpretazione; una modifica esclusivamente comportamentale della Policy può affettare l’applicabilità di una Decision senza cambiare il contenuto semantico dell’Assertion.

Admission continua a non aumentare Quality. Il fatto che un contenuto sia stato ammesso o sia già presente nella Knowledge non costituisce, da solo, nuova giustificazione per una valutazione di qualità.

# F — Vista operativa

## Acquisition e Work

```text
Consegna
   │
Acquisition: registra la ricezione
   │
   ├── si conclude senza Work durevole
   │
   ├── apre un Work pertinente
   │
   └── alimenta un Work già esistente
```

L’Acquisition possiede la ricezione. Il Work possiede il lavoro durevole: obiettivo operativo, proprietario, dipendenze, tentativi ed esiti.

La Source risultante o riutilizzata rimane un elemento informativo distinto.

## Esecuzione, attesa e ripresa

```text
Richiesta / Disposition applicabile
                 │
          Work con proprietario
                 │
          controllo dipendenze
                 │
       ┌─────────┴───────────┐
       │                     │
   disponibili           non disponibili
       │                     │
    Attempt                 attesa
       │                     │
  attività concreta      input / evento pertinente
       │                     │
       │                   ripresa
       │                     │
       └──────── nuovo controllo delle condizioni
       │
       ├── risultato operativo
       ├── risultato informativo, se prodotto
       └── errore / esito parziale
                  │
          seguito autorizzato:
          chiusura / nuovo tentativo / verifica
```

Attempt, attesa ed esito sono aspetti recuperabili della storia del Work; non vengono promossi automaticamente a primitive autonome.

Il coordinamento è presso il proprietario dell’attività:

- Verification possiede la richiesta di verifica e la sua attesa;
- l’elaborazione estrattiva possiede i propri tentativi;
- la funzione possiede il risultato applicativo richiesto;
- la rivalutazione possiede il lavoro autorizzato su risultati affetti.

Questo non introduce un orchestratore che decide il significato di tutto.

## Verifica e nuovo contributo

```text
Work di Verification
        │
   domanda con target e scope
        │
      attesa
        │
User Contribution Intake
        │
        ├── conserva contenuto ricevuto, autore/origine,
        │   target, tempo e contesto pertinenti
        │
        ├── conserva la natura pertinente dell'interazione
        │
        ├── alimenta Interpretation / assessment
        │   senza sostituire la base originaria
        │
        └── soddisfa o modifica la dipendenza operativa
```

La ricezione della risposta può consentire una ripresa operativa senza essere sufficiente a confermare il contenuto.

La stessa interazione può contenere informazione e scelta autorizzativa, ma le due nature devono rimanere distinguibili. L’Intake non acquisisce automaticamente, per questo, l’ownership della formalizzazione delle Decision non-Policy.

## Rivalutazione

Una rivalutazione può usare Source, Observation e proposte già conservate. Produce nuovi risultati con le dipendenze pertinenti, senza creare una falsa nuova Acquisition e senza riscrivere gli esiti storici.

Un nuovo tentativo o un nuovo percorso operativo non creano automaticamente una nuova fonte epistemica.

Quando viene prodotta una nuova Quality Assessment, occorre una nuova base, un nuovo criterio oppure un nuovo contesto materialmente pertinente. Non bastano:

- la mera ripetizione della stessa valutazione;
- l’Admission;
- la presenza del risultato nella Knowledge;
- il riutilizzo dello stesso risultato attraverso un nuovo percorso operativo.

La storia dei tentativi conserva che cosa è stato eseguito; non attribuisce da sola nuova forza epistemica al risultato.

### Separazioni obbligatorie

- OCR fallito ≠ Source falsa.
- Work completato ≠ Assertion ammessa.
- Verification in attesa ≠ Assertion automaticamente incerta.
- Application tentata ≠ effetto riuscito.
- Nuovo tentativo ≠ nuovo contributo indipendente.
- Nuovo percorso operativo ≠ nuova giustificazione.
- Assenza di Work attivo ≠ proposta inesistente.

Un’applicazione semplice può avvenire senza Work durevole, purché resti recuperabile la storia operativa pertinente.

# G — Vista Resources & Memories

## Risorse consultate

| Risorsa | Chi la consulta principalmente | Quale confine impone |
|---|---|---|
| **Core Model** | Interpretation, Reconciliation, Derivation, Admission | Forme rappresentabili e distinzioni fondamentali |
| **Core invariants** | Tutti i produttori e consumatori pertinenti | Divieto di collassi semantici, auto-supporto, falsa indipendenza e perdita delle distinzioni necessarie |
| **Domain Model** | Mapping, Interpretation, Comparison, Temporal Evaluation, Derivation, Reconstruction | Significato, compatibilità, vincoli e criteri del dominio |
| **Identifier Schemes** | Mapping, Interpretation, Reconciliation | Schema, scope, normalizzazione e significato identificativo |
| **Mapping Definitions** | Mapping; Impact Assessment per le dipendenze | Applicabilità delle corrispondenze sorgente–significato |
| **Quality Model** | Produttori locali di assessment e loro consumatori | Target, dimensione, base e scopo; nuova valutazione sostenuta da nuova base, criterio o contesto materialmente pertinente |
| **Application Decision Policies** | Policy Evaluation | Comportamenti consentiti e prudenza applicativa |
| **Criteri dei casi d’uso** | Functions, Query, Reconstruction, Projection, Explanation | Scopo e condizioni di correttezza del risultato richiesto |
| **Regole di accesso e sicurezza** | Ingresso, Query, Verification, Application | Chi può accedere, contribuire o agire |

Versioni e ambiti di applicabilità vengono registrati quando hanno contribuito materialmente a un risultato o a una decisione.

Le risorse definiscono forme, significati, criteri e vincoli. Non sono componenti attivi che eseguono autonomamente le valutazioni.

## Responsabilità di conservazione

```text
RISORSE DI RIFERIMENTO
Core / Domain / Mapping / Quality / Policies / criteri d'uso
          ^
          │ CONSULTS
          │
ATTIVITÀ ─┼── READS / WRITES ──> MEMORIE INFORMATIVE
          │                      ├── Source e rappresentazioni
          │                      ├── Observation e locator
          │                      ├── proposte e Interpretation Result
          │                      ├── Knowledge governata
          │                      ├── contributi, basi originarie e supporti
          │                      ├── Quality Assessment
          │                      ├── Provenance e Lineage
          │                      ├── giustificazioni inferenziali
          │                      ├── relazioni storiche e impatti
          │                      └── scope di Query e ricostruzioni
          │
          └── READS / WRITES ──> MEMORIA OPERATIVA
                                 ├── Acquisition
                                 ├── Work
                                 ├── tentativi, attese ed esiti
                                 ├── Decision
                                 ├── Disposition
                                 └── Application
```

Knowledge è il corpo governato dei commitment, non un duplicato materiale obbligatorio di tutte le informazioni.

La base originaria del contributo umano rimane recuperabile insieme al contesto semanticamente pertinente e collegata alle interpretazioni successive. Questa responsabilità non impone un archivio separato né una classificazione universale di ogni intervento come Source.

Per le Decision, anche non-Policy, devono essere recuperabili origine dell’autorità, target, scope, contesto, Decision, Disposition e storia dell’eventuale Application. La memoria necessaria è stabilita; resta aperta l’ownership della formalizzazione nei percorsi non-Policy.

## Provenance, Lineage e storie

Provenance, Lineage, storia epistemica e audit operativo possono essere percorsi collegati della stessa storia conservata. Devono però mantenere il proprio significato:

- **Provenance:** origine e contesto di produzione.
- **Lineage:** trasformazioni e dipendenze informative.
- **Storia epistemica:** come sono cambiati supporti, valutazioni e commitment.
- **Audit operativo:** quali attività sono state autorizzate, tentate ed eseguite.

Il traversal è una capacità di accesso. Non produce retroattivamente le tracce mancanti.

La cattura locale deve rendere recuperabili anche le dipendenze e l’origine comune pertinenti. Contare più elementi conservati non basta a stabilire che rappresentino più attestazioni indipendenti.

Per esempio:

- due scansioni dello stesso documento possono migliorare la lettura, senza diventare automaticamente due attestazioni indipendenti;
- due conclusioni derivate dalle stesse premesse non sono automaticamente due conferme indipendenti;
- un nuovo tentativo tecnico non crea automaticamente una nuova fonte epistemica.

I contributi dipendenti non sono inutili: possono aumentare leggibilità, compatibilità, precisione o copertura. Non devono però essere contati automaticamente come corroborazione indipendente.

## Conservazione necessaria alla contestabilità della coreferenza

Una conclusione identitaria o un uso unitario non devono distruggere le rappresentazioni originarie, le loro differenze, le Provenance e la giustificazione necessaria a contestare la conclusione.

Il requisito di reversibilità è riferito all’informazione ancora legittimamente conservata. Non introduce un obbligo di conservazione indiscriminata e non definisce una funzione software di unmerge.

# H — Responsabilità autonome

Le schede descrivono **autonomia del problema**, non confini software. I meccanismi di ragionamento sono inclusi perché possiedono problemi distinti; le loro schede non li trasformano in componenti separati.

Le due capacità di adattamento del canale e registrazione dell’Acquisition sono raccolte nella ricezione tracciata, senza perderne la distinzione. Il coordinamento dei Work rimane trasversale e non riceve una scheda da controllore centrale.

Per tutte le schede valgono gli obblighi pertinenti:

- ogni produttore conserva la propria Provenance e Lineage;
- assessment e validazioni vengono prodotti localmente dove esiste la competenza;
- nessun risultato può diventare supporto epistemico di sé stesso attraverso un ciclo;
- molteplicità di elementi o percorsi non implica indipendenza epistemica;
- una nuova Quality Assessment richiede nuova base, nuovo criterio o nuovo contesto materialmente pertinente.

## H1 — Ricezione tracciata

- **Problema posseduto:** rendere disponibile una consegna preservando sia le peculiarità del canale sia l’identità della ricezione.
- **Input principali:** contenuto consegnato, metadati del canale, mittente, contesto autorizzativo.
- **Output principali:** consegna normalizzata, Acquisition, collegamento al contenuto ricevuto o riutilizzato.
- **Risorse consultate:** regole del canale, accesso e condizioni tecniche.
- **Memorie lette/scritte:** scrive storia dell’Acquisition; legge informazioni di consegna e precedenti pertinenti.
- **Coopera con:** validazione tecnica, deduplicazione, preservazione e proprietari dei Work eventualmente aperti.

Le due capacità interne rimangono distinguibili:

- adattare la consegna preserva il contesto del canale;
- registrare l’Acquisition conserva l’identità e la storia della ricezione.

## H2 — Validazione tecnica

- **Problema posseduto:** stabilire se e a quali condizioni il materiale possa essere elaborato tecnicamente.
- **Input principali:** contenuto, formato dichiarato, esiti tecnici disponibili.
- **Output principali:** diagnosi di processabilità, limitazioni, errori e condizioni tecniche.
- **Risorse consultate:** regole tecniche e di sicurezza.
- **Memorie lette/scritte:** legge materiale e Acquisition; scrive esiti dei controlli.
- **Coopera con:** ricezione, preservazione, estrazione e coordinamento operativo.

Non valuta la verità delle informazioni contenute.

## H3 — Identificazione e deduplicazione tecnica

- **Problema posseduto:** riconoscere ripetizioni tecniche senza moltiplicare impropriamente materiale ed effetti.
- **Input principali:** contenuto e caratteristiche tecniche; precedenti pertinenti.
- **Output principali:** corrispondenze tecniche e indicazioni di riuso.
- **Risorse consultate:** criteri tecnici di confronto e idempotenza.
- **Memorie lette/scritte:** legge identità tecniche conservate; scrive collegamenti fra ricezioni e contenuti.
- **Coopera con:** ricezione, preservazione e gestione dei tentativi.

Non conclude identità documentale o equivalenza fra Assertion.

L’assenza di duplicazione tecnica non dimostra indipendenza epistemica: rappresentazioni tecnicamente differenti possono avere origine comune.

## H4 — Preservazione delle Source

- **Problema posseduto:** mantenere recuperabile il materiale originario e distinguibile dalle trasformazioni successive.
- **Input principali:** contenuto o riferimento disponibile, Acquisition, condizioni tecniche.
- **Output principali:** Source preservata e rappresentazioni collegate.
- **Risorse consultate:** criteri di conservazione, accesso, sicurezza e sovranità.
- **Memorie lette/scritte:** scrive Source, metadati originali e collegamenti alle rappresentazioni.
- **Coopera con:** ricezione, estrazione, Query e responsabilità di conservazione/ripristino.

La preservazione non dipende dal successo dell’interpretazione.

## H5 — Estrazione e produzione delle Observation

- **Problema posseduto:** rendere indirizzabile ciò che è osservabile nel materiale.
- **Input principali:** Source e sue rappresentazioni tecnicamente utilizzabili.
- **Output principali:** Observation, strutture osservate, letture alternative, risultati parziali e assessment estrattivi.
- **Risorse consultate:** conoscenza dei formati e criteri di osservazione, parsing e qualità.
- **Memorie lette/scritte:** legge Source; scrive Observation, localizzazioni, assessment e Lineage.
- **Coopera con:** preservazione, Mapping, Interpretation e gestione dei tentativi.

Testo nativo, OCR, layout, struttura e parsing sono capacità interne distinte. Il grezzo non viene sostituito silenziosamente dalla normalizzazione.

Letture differenti della stessa origine possono migliorare leggibilità, precisione o copertura. Non costituiscono automaticamente attestazioni indipendenti del fatto successivamente interpretato.

## H6 — Valutazione ed esecuzione del Mapping

- **Problema posseduto:** applicare corrispondenze riutilizzabili senza confonderle con l’interpretazione già accettata.
- **Input principali:** Observation o campi strutturati, contesto classificatorio, Mapping candidati.
- **Output principali:** applicabilità valutata, ruoli semantici proposti, ambiguità e dipendenze dal Mapping.
- **Risorse consultate:** Mapping Definitions, Domain, schemi identificativi e forme Core.
- **Memorie lette/scritte:** legge materiale pertinente; scrive risultati del Mapping, assessment e Lineage.
- **Coopera con:** Interpretation, Query e Impact Assessment.

Non ammette Assertion né riconcilia definitivamente referenti.

## H7 — Interpretation

- **Problema posseduto:** comporre elementi disponibili in una proposta di significato coerente.
- **Input principali:** Source/Observation, risultati del Mapping, contributi strutturati con base originaria recuperabile, contesto recuperato.
- **Output principali:** Referent e Assertion proposti, Interpretation Result, alternative, attribuzioni e supporti pertinenti.
- **Risorse consultate:** Core, Domain, Mapping e Quality Model.
- **Memorie lette/scritte:** legge materiale, basi dei contributi, contesto e Knowledge; scrive proposte, supporti, assessment e dipendenze.
- **Coopera con:** Mapping, Reconciliation, Comparison, Verification, Query e User Contribution Intake.

Comprende classificazione contestuale e composizione documentale. Non decide Admission o automazione.

Il significato attribuito a un contributo umano rimane distinguibile dal contenuto effettivamente ricevuto.

Il riuso della Knowledge deve conservare le dipendenze pertinenti. Il risultato dell’Interpretation non può tornare attraverso il contesto come nuova giustificazione indipendente di sé stesso.

## H8 — Identity Reconciliation

- **Problema posseduto:** valutare se rappresentazioni differenti possano riferirsi allo stesso soggetto.
- **Input principali:** Referent proposti o esistenti, identificatori, assegnazioni, attributi e contributi.
- **Output principali:** proposte di coreferenza, alternative, indizi contrari e assessment referenziali.
- **Risorse consultate:** Domain, schemi identificativi, Core invariants e Quality Model.
- **Memorie lette/scritte:** legge contesto referenziale e supporti; scrive proposte e giustificazioni, mantenendo recuperabili le rappresentazioni originarie e le differenze pertinenti.
- **Coopera con:** Interpretation, Query, Comparison e Governance.

La coreferenza documentale è una specializzazione.

Un merge operativo non è la proposizione di identità. Una conclusione di coreferenza o un uso unitario non devono distruggere:

- le rappresentazioni originarie;
- le loro differenze;
- le relative Provenance;
- la giustificazione necessaria a contestare successivamente la conclusione.

Sulla base dell’informazione ancora legittimamente conservata, deve restare possibile contestare la coreferenza, revisionarla e tornare a distinguere le rappresentazioni quando una successiva evidenza mostra che riguardano soggetti differenti.

Questo è un vincolo di non distruttività e contestabilità, non il progetto di una funzione software di unmerge.

Una proposta di assegnazione o un risultato di riconciliazione non possono diventare prova indipendente della riconciliazione che li ha prodotti.

## H9 — Comparison

- **Problema posseduto:** confrontare contenuti semanticamente comparabili e riconoscerne le relazioni.
- **Input principali:** Assertion, qualificazioni temporali, contesto referenziale e contributi pertinenti.
- **Output principali:** equivalenza valutata, differenza, compatibilità, incompatibilità e relazioni di correzione riconosciute.
- **Risorse consultate:** Domain, Core invariants e criteri di confronto.
- **Memorie lette/scritte:** legge contenuti e giustificazioni; scrive relazioni e relative basi.
- **Coopera con:** Reconciliation, Temporal Evaluation, Interpretation, Impact Assessment e Admission.

Conflict Detection è una specializzazione; scegliere un comportamento di fronte al conflitto non appartiene al confronto.

Compatibilità fra contributi non implica indipendenza delle rispettive origini.

## H10 — Temporal Evaluation

- **Problema posseduto:** valutare relazioni temporali senza confondere tempo del contenuto e storia del sistema.
- **Input principali:** qualificazioni temporali, intervalli, reference time e contesto.
- **Output principali:** confronti temporali, sovrapposizioni, successioni e valutazioni pertinenti.
- **Risorse consultate:** semantica temporale Domain e invarianti Core.
- **Memorie lette/scritte:** legge tempi e storie; scrive valutazioni con il proprio contesto.
- **Coopera con:** Comparison, Derivation, Reconstruction, Impact Assessment e Governance.

L’arrivo tardivo non viene trattato come una modifica automatica del tempo del fatto.

## H11 — Derivation

- **Problema posseduto:** produrre conclusioni applicando criteri inferenziali pertinenti a premesse esplicite.
- **Input principali:** premesse, regola o metodo, condizioni di applicabilità e reference context.
- **Output principali:** conclusione derivata, giustificazione, dipendenze e assessment inferenziale.
- **Risorse consultate:** Core, Domain, criteri inferenziali e Quality Model.
- **Memorie lette/scritte:** legge premesse e risorse; scrive risultato e Lineage; può formulare una nuova Assertion proposta.
- **Coopera con:** Query, Temporal Evaluation, Reconstruction, Policy e Admission.

La Policy governa attivazione e usi, non la validità semantica della conclusione.

Una conclusione derivata non diventa supporto indipendente delle proprie premesse perché è stata materializzata o riutilizzata. Percorsi inferenziali differenti devono mantenere recuperabili le dipendenze e le basi comuni pertinenti.

## H12 — Current Reconstruction

- **Problema posseduto:** ricostruire ciò che Fold può sostenere per un aspetto, tempo e scopo determinati.
- **Input principali:** Knowledge disponibile, reference time, conflitti, correzioni, impatti e criteri d’uso.
- **Output principali:** ricostruzione qualificata, alternative e limiti.
- **Risorse consultate:** Domain, criteri del caso d’uso e vincoli di utilizzo applicabili.
- **Memorie lette/scritte:** legge commitment e giustificazioni; scrive, quando necessario, risultato, scope e dipendenze.
- **Coopera con:** Query, Comparison, Temporal Evaluation, Derivation, Projection e Explanation.

Non identifica il corrente con l’ultimo valore ricevuto. Proposte eventualmente considerate rimangono distinguibili dai commitment ammessi.

La ricostruzione non può trattare il riuso di risultati dipendenti come nuova corroborazione indipendente.

## H13 — Impact Assessment

- **Problema posseduto:** individuare e qualificare quali risultati o decisioni siano materialmente affetti da un cambiamento.
- **Input principali:** cambiamento, dipendenze conservate, risultati e versioni pertinenti.
- **Output principali:** qualificazioni d’impatto, bersagli coinvolti e basi della valutazione.
- **Risorse consultate:** significato delle risorse cambiate e criteri pertinenti al bersaglio.
- **Memorie lette/scritte:** legge Lineage, contenuti e storia decisionale; scrive impatti recuperabili.
- **Coopera con:** Query/traversal, Reconstruction, Policy, autorità competente e proprietari dei Work.

Non pianifica autonomamente ogni rivalutazione e non dichiara automaticamente falso ogni risultato dipendente.

## H14 — Valutazione delle Application Decision Policies

- **Problema posseduto:** scegliere un comportamento autorizzato fra quelli semanticamente ammissibili.
- **Input principali:** situazione, assessment, risultati, impatti, scopo dell’azione e autorità applicabile.
- **Output principali:** Decision e Disposition motivate, oppure assenza di una disposizione applicabile.
- **Risorse consultate:** Application Decision Policies, Core invariants e criteri applicativi.
- **Memorie lette/scritte:** legge contesto informativo e operativo; scrive base, versione e risultato decisionale.
- **Coopera con:** Verification, Admission, Functions e gestione dei Work.

Non è l’unica origine possibile delle Decision.

L’ownership della formalizzazione delle Decision nei percorsi non-Policy rimane una questione aperta; non viene assorbita automaticamente da questa responsabilità.

## H15 — Gestione della Verification

- **Problema posseduto:** ottenere una verifica mirata senza perdere che cosa è stato effettivamente chiesto e confermato.
- **Input principali:** richiesta autorizzata, target, alternative, materiale pertinente e attore coinvolto.
- **Output principali:** richiesta di verifica, contributi/esiti contestualizzati, assessment e stato operativo del lavoro.
- **Risorse consultate:** criteri di verifica, Domain, Quality Model e autorizzazioni.
- **Memorie lette/scritte:** legge proposte e giustificazioni; scrive verifica, contesto e storia del Work; mantiene il collegamento alla base del contributo ricevuto tramite Intake.
- **Coopera con:** Intake, Interpretation, Policy, Query e Admission.

Non ogni risposta è conferma informativa, autorizzazione o Admission.

Un eventuale nuovo assessment deve indicare la nuova base, il nuovo criterio o il nuovo contesto materialmente pertinente. Il solo completamento della verifica come lavoro non aumenta Quality.

## H16 — Admission e revisioni di governance

- **Problema posseduto:** applicare un commitment o una revisione autorizzata mantenendo contenuto e storia distinguibili.
- **Input principali:** Referent/Assertion proposti, Disposition, basi pertinenti e condizioni correnti.
- **Output principali:** commitment applicato o revisionato, storia dell’effetto, oppure motivo della mancata applicazione.
- **Risorse consultate:** Core invariants, vincoli pertinenti, autorità e disposizione applicabile.
- **Memorie lette/scritte:** legge proposte e decisioni; scrive governance della Knowledge e Application.
- **Coopera con:** Policy, Verification, Comparison, Impact Assessment e proprietari delle applicazioni.

Non aumenta Quality, non cambia il claim sorgente e non inventa una nuova disposizione.

L’ammissione di una conclusione identitaria non deve rendere distruttiva o non contestabile l’unificazione delle rappresentazioni. Restano applicabili gli obblighi di preservazione definiti per la Reconciliation.

## H17 — Query & Retrieval

- **Problema posseduto:** trovare materiale pertinente conservandone natura, scope e qualificazioni.
- **Input principali:** domanda, target, filtri semantici, tempo, corpus e autorizzazioni.
- **Output principali:** risultati recuperati o risultato negativo delimitato.
- **Risorse consultate:** Domain, criteri di Query e regole di accesso.
- **Memorie lette/scritte:** legge Source, Observation, proposte, Knowledge e storie; conserva scope e limiti quando necessari.
- **Coopera con:** Interpretation, ragionamento, Projection, Explanation e Functions.

Il traversal è una sua capacità di accesso. Recuperare non significa ammettere o concludere.

Il recupero delle giustificazioni deve consentire di risalire anche alle basi originarie dei contributi e alle dipendenze comuni pertinenti conservate.

## H18 — Composizione delle Projection

- **Problema posseduto:** organizzare risultati già semanticamente determinati per uno specifico utilizzo.
- **Input principali:** risultati di Query, ricostruzioni, conclusioni e qualificazioni.
- **Output principali:** rappresentazione applicativa selettiva.
- **Risorse consultate:** criteri del caso d’uso e vincoli di presentabilità.
- **Memorie lette/scritte:** legge risultati e loro qualificazioni; conserva la proiezione e le dipendenze solo quando necessario.
- **Coopera con:** Query, Reconstruction, Explanation, Functions e Presentation.

Se serve una nuova aggregazione o conclusione, la richiede al ragionamento anziché produrla implicitamente.

Una rappresentazione unitaria basata su coreferenza non deve distruggere le differenze informative necessarie a una successiva revisione della conclusione.

## H19 — Realizzazione dei casi d’uso e applicazione delle disposizioni

- **Problema posseduto:** ottenere il risultato applicativo richiesto rispettando autorizzazioni e significato dei dati.
- **Input principali:** richiesta dell’utente o Disposition, risultati disponibili e contesto del caso d’uso.
- **Output principali:** risultato utile, azione applicata o esito operativo motivato.
- **Risorse consultate:** criteri del caso d’uso, disposizioni e autorizzazioni pertinenti.
- **Memorie lette/scritte:** legge tramite responsabilità competenti; scrive esiti e Application.
- **Coopera con:** Query, ragionamento, Verification, Projection, Explanation, Presentation e Work.

È una famiglia di responsabilità per casi d’uso, non un controllore semantico universale.

Un uso unitario di rappresentazioni deve rispettare la non distruttività e la contestabilità della coreferenza. L’esecuzione di tale uso non rende vera la proposizione di identità né ne aumenta il supporto.

## H20 — Composizione delle Explanation

- **Problema posseduto:** rendere comprensibile la giustificazione reale di un risultato.
- **Input principali:** risultato da spiegare, domanda esplicativa, contributi, supporti, Lineage e decisioni.
- **Output principali:** spiegazione fedele, con limiti e alternative pertinenti.
- **Risorse consultate:** criteri esplicativi e significati Domain.
- **Memorie lette/scritte:** legge tracce e giustificazioni tramite Query; conserva la spiegazione se richiesto dal suo uso.
- **Coopera con:** Query, ragionamento, Governance, Projection e Presentation.

Non inventa un percorso plausibile dove manca la traccia reale.

La spiegazione deve rispettare la distinzione fra molteplicità e indipendenza dei contributi: più rappresentazioni o percorsi con origine comune non vengono presentati automaticamente come conferme indipendenti.

## H21 — Presentation

- **Problema posseduto:** rendere percepibili contenuto, qualificazioni ed esiti senza cambiarne il significato.
- **Input principali:** Projection, Explanation, risultati operativi e azioni disponibili.
- **Output principali:** rappresentazione comprensibile per l’utente.
- **Risorse consultate:** criteri di presentazione del caso d’uso e vincoli semantici pertinenti.
- **Memorie lette/scritte:** legge risultati pronti alla presentazione; non modifica direttamente Knowledge.
- **Coopera con:** Projection, Explanation, Functions e User Contribution Intake.

Semplificare il linguaggio non autorizza a trasformare “non confermato” in “non avvenuto”.

## H22 — User Contribution Intake

- **Problema posseduto:** acquisire un intervento dell’utente preservando il contenuto ricevuto e il contesto necessario a distinguerlo dal significato successivamente attribuito e dall’eventuale autorità della scelta.
- **Input principali:** risposta, dichiarazione o scelta; contenuto effettivamente ricevuto, autore/origine, target, tempo, contesto presentato e natura pertinente dell’interazione.
- **Output principali:** base originaria recuperabile; contributo contestualizzato e attribuito oppure scelta deliberata tracciata, instradati al percorso pertinente.
- **Risorse consultate:** contesto dell’interazione, significati pertinenti e autorità applicabile.
- **Memorie lette/scritte:** legge il contesto; scrive il contenuto effettivamente ricevuto e la storia pertinente dell’interazione, mantenendoli distinguibili dall’Interpretation successiva.
- **Coopera con:** Verification, Interpretation, Functions e percorsi di Governance; l’ownership della formalizzazione delle Decision non-Policy rimane da precisare.

Devono essere recuperabili, quando semanticamente pertinenti:

- contenuto effettivamente ricevuto;
- autore o origine;
- target;
- tempo;
- contesto;
- natura dell’interazione, come dichiarazione libera, risposta a una domanda, conferma circoscritta o scelta autorizzativa.

Non modifica direttamente Knowledge e non interpreta ogni intervento come conferma o autorizzazione.

Non richiede una Observation artificiale. Non impone che ogni intervento umano sia modellato come Source. Non implica conservare indiscriminatamente gli eventi dell’interfaccia.

La necessità della base originaria rimane indipendente dalla forma concreta con cui verrà rappresentata.

# I — Core / modello informativo

Le classificazioni indicano il sostegno concettuale, non autorità canonica:

- **FORTE:** distinzione necessaria e sufficientemente sostenuta.
- **CANDIDATO:** organizzazione o definizione adottata per questa v2.
- **APERTO NON BLOCCANTE:** forma esatta rinviata, con default che preserva l’informazione.

`FORTE` non significa automaticamente primitiva autonoma. `CANDIDATO` non rende facoltativa la responsabilità informativa che la forma proposta deve coprire.

## Elementi e famiglie

| Elemento | Stato | Ruolo nella candidata |
|---|---|---|
| **Referent** | FORTE | Locus referenziale interno per un soggetto proposto o riconosciuto |
| **Assertion** | FORTE | Elemento semantico indirizzabile che porta un contenuto proposizionale |
| **Value** | FORTE | Contenuto strutturato non referenziale |
| **Distinzione schema–valore–assegnazione dell’Identifier** | FORTE | Impedisce di equiparare stringa, identificatore e identità |
| **Forma ontologica definitiva di Identifier** | APERTO NON BLOCCANTE | Non necessaria per conservare le tre distinzioni |
| **Qualificazioni temporali** | FORTE | Ruoli temporali riferiti al bersaglio pertinente |
| **Source** | FORTE | Origine contenutistica disponibile a Fold, adiacente alla grammatica centrale |
| **Observation** | FORTE | Risultato di osservazione della Source, distinto dalla proposizione semantica |
| **Interpretation Result** | CANDIDATO | Conserva composizione, alternative e dipendenze delle proposte |
| **Locator / anchor** | CANDIDATO | Identifica la porzione pertinente senza richiedere una nuova primitiva di dominio |
| **Contributo attribuito** | FORTE | Collega contenuto, origine/contributore e contesto, con base originaria recuperabile |
| **Supporto qualificato** | FORTE | Rende recuperabile perché un contributo sostiene una proposizione |
| **Forma concreta del supporto indirizzabile** | APERTO NON BLOCCANTE | Autonomia e granularità della relazione possono essere precisate dopo |
| **Quality Assessment** | FORTE | Valutazione storica di target, dimensione, base e scopo pertinente |
| **Provenance** | FORTE | Origine e contesto di produzione |
| **Lineage** | FORTE | Dipendenze e trasformazioni informative |
| **Derivation record / justification** | FORTE | Premesse, regola/metodo, contesto e conclusione recuperabili |
| **Risultato negativo delimitato** | FORTE | Esito di osservazione o ricerca con perimetro, non negazione universale |
| **Qualificazione d’impatto** | FORTE | Informazione sul risultato materialmente affetto |
| **Ricostruzione contestualizzata** | CANDIDATO | Risultato riferito a tempo, scopo e basi informative |
| **Posizione proposta** | FORTE | Governance della proposta, non sostanza Candidate |
| **Knowledge come corpo governato** | CANDIDATO | Referent e Assertion ammessi, con giustificazioni e storie raggiungibili |
| **Decision / Disposition / Application** | FORTE | Scelta, trattamento autorizzato ed esecuzione distinti |
| **Work come unità durevole** | CANDIDATO | Supporta attese, tentativi, dipendenze e riprese |
| **Granularità concreta del Work** | APERTO NON BLOCCANTE | Non ogni attività richiede un Work autonomo |
| **Documento come possibile Referent** | CANDIDATO | Usato quando l’identità documentale deve essere indipendente dalle rappresentazioni |

## Referent, Assertion e commitment

Il Referent non è la cosa esterna né una prova della sua esistenza. Può rappresentare un soggetto attuale, passato, pianificato, ipotizzato o contestato.

L’Assertion porta il contenuto proposizionale. Contributore, supporto, Quality e commitment sono collegati, non automaticamente incorporati nella sua definizione.

La distinzione centrale è:

```text
contenuto proposizionale
    che cosa viene sostenuto

contributo attribuito
    chi o quale Source lo presenta e in quale contesto

commitment di Fold
    quale posizione Fold assume tramite Governance
```

Più contributi possono sostenere lo stesso contenuto; un contributo può sostenere contenuti differenti. La similitudine non autorizza la fusione automatica delle Assertion.

Nel caso umano, il contributo interpretato deve rimanere collegato al contenuto effettivamente ricevuto e al suo contesto pertinente. Attribuire una proposizione all’utente non sostituisce la base originaria con la sola formulazione ricavata da Fold.

## Value

`Value — FORTE` indica la necessità della distinzione di contenuto strutturato non referenziale.

Non significa che sia stata definitivamente acquisita una primitiva autonoma Value, dotata di identità propria o di una particolare rappresentazione tecnica.

## Identifier

```text
valore osservato
    ↓ parsing / interpretazione pertinente
compatibilità con uno schema
    ↓
valore identificativo normalizzato
    ↓
Assertion di assegnazione a un Referent
```

La freccia non garantisce successo: ogni passaggio può restare ambiguo.

L’assegnazione può essere temporale, contestata o corretta. La stringa originale rimane recuperabile.

Una proposta di assegnazione non costituisce, per il solo fatto di essere stata prodotta, supporto indipendente della riconciliazione che l’ha generata.

## Supporto, dipendenze e indipendenza

Il supporto deve rendere recuperabile perché un contributo sostiene una proposizione e sotto quale scope.

L’esistenza di più collegamenti di supporto non dimostra, da sola, indipendenza delle rispettive basi.

Sono quindi distinti:

- presenza di un contributo;
- attribuzione del contenuto;
- adeguatezza del supporto;
- compatibilità con altri contributi;
- indipendenza rispetto alle origini e alle dipendenze pertinenti.

Contributi dipendenti possono essere utili e migliorare leggibilità, precisione, compatibilità o copertura. Non vengono automaticamente contati come corroborazione indipendente.

Nessun ciclo di supporto, Interpretation, Reconciliation, Derivation o riuso della Knowledge può rendere un risultato supporto epistemico di sé stesso. La materializzazione di una conclusione non cancella le sue premesse né la rende una fonte indipendente rispetto a esse.

## Quality Assessment

Una Quality Assessment è riferita a un target, una dimensione, una base e uno scopo pertinente, e conserva la propria storia.

Una nuova Quality Assessment richiede:

- una nuova base;
- oppure un nuovo criterio;
- oppure un nuovo contesto materialmente pertinente.

Non costituiscono da soli nuova giustificazione:

- ripetere la stessa valutazione;
- ammettere il risultato;
- trovarlo già nella Knowledge;
- riutilizzarlo attraverso un nuovo percorso operativo.

Admission non aumenta Quality. La produzione delle valutazioni resta distribuita presso i produttori competenti.

## Tempo

| Natura temporale | Esempio di significato |
|---|---|
| Tempo del contenuto | Periodo al quale un importo, rapporto o evento si riferisce |
| Storia informativa/epistemica | Quando Fold ha osservato, interpretato, verificato o ammesso |
| Storia operativa | Quando un lavoro è stato aperto, tentato, sospeso o applicato |
| Reference time | Momento rispetto al quale si effettua una valutazione o ricostruzione |

Una data non migra automaticamente da un ruolo all’altro. Non esiste una `Validity` universale.

## Documenti e rappresentazioni

- Un **file** è una forma tecnica di contenuto.
- Una **Source** è un’origine contenutistica resa disponibile.
- Una **rappresentazione** può raffigurare o contenere uno o più documenti.
- Un **documento** può essere trattato come soggetto documentale.
- Un **Referent documentale** serve quando occorre conservarne identità indipendente.
- Un **locator** individua la porzione pertinente della rappresentazione.

Sono ammesse sia più Source per un documento sia una Source con più documenti.

Comporre porzioni non prova coreferenza; uguaglianza tecnica non prova identità documentale. Le regole specifiche di versione e correzione vengono dal Domain.

La coreferenza e l’eventuale uso unitario non devono distruggere le rappresentazioni originarie e le differenze necessarie a contestare la conclusione. Se l’informazione ancora legittimamente conservata permette di riconoscere soggetti differenti, deve rimanere possibile revisionare la conclusione e tornare a distinguerli.

## Informazione negativa e modalità

La candidata distingue:

1. negazione esplicita sostenuta;
2. assenza osservata in una porzione delimitata;
3. esito negativo di una ricerca;
4. Assertion negativa sul mondo.

Corpus, scope, tempo, copertura e limiti rimangono recuperabili quando necessari. Un risultato vuoto entro il corpus accessibile non dimostra assenza al di fuori di quel corpus.

Il contenuto proposizionale può inoltre essere descrittivo, normativo, intenzionale o predittivo. Questa modalità appartiene al significato, non alla Policy comportamentale di Fold.

# J — Relation map

## Grammatica fra responsabilità, informazioni e risorse

| Relazione | Direzione | Significato |
|---|---|---|
| `CALLS` | Attività → attività | Richiede una capacità competente |
| `PRODUCES` | Attività → risultato | Genera un elemento o una valutazione |
| `READS` | Attività → informazione/memoria | Consulta contenuto già disponibile |
| `WRITES` | Attività → memoria | Conserva il risultato di propria competenza |
| `CONSULTS` | Attività → risorsa | Usa definizioni o criteri |
| `CONSTRAINED_BY` | Attività/uso → invariante, autorità o qualificazione | Deve rispettare un vincolo |
| `REACTS_TO` | Attività → cambiamento pertinente | Può essere attivata dal cambiamento |
| `MAY_OPEN_WORK` | Attività → Work | Può avviare lavoro durevole nel contesto autorizzato |

`MAY_OPEN_WORK` non significa che ogni cambiamento produca automaticamente lavoro né che l’attività possieda autorità illimitata.

## Grammatica informativa

| Famiglia | Relazione necessaria | Distinzione preservata |
|---|---|---|
| Descrittiva/referenziale | Assertion `describes` Referent | Contenuto semantico sul soggetto |
| Descrittiva/referenziale | Assertion esprime assegnazione di Identifier | Identificatore distinto dal soggetto |
| Epistemica | Contributo `attributed_to` attore/origine | Provenienza della dichiarazione |
| Epistemica | Contributo `presents` contenuto di Assertion | Attribuzione distinta dall’accettazione |
| Epistemica | Contributo `supports` Assertion | Supporto distinto dalla sola presenza del contenuto |
| Epistemica | Contributo/Assertion `contests` altro contenuto | Obiezione recuperabile |
| Epistemica | Assertion `incompatible_with` altra Assertion, sotto scope | Conflitto contestualizzato |
| Epistemica | Contenuto/contributo `corrects` un precedente | Correzione direzionale, non successione generica |
| Rappresentazione | Source/rappresentazione `represents` documento | Materiale distinto dal soggetto documentale |
| Osservazione | Observation `extracted_from` Source | Lettura distinta dal contenuto semantico |
| Localizzazione | Observation/supporto `located_at` locator | Target preciso dell’evidenza |
| Provenance | Risultato `produced_by` attività | Origine del risultato |
| Inferenza | Assertion `premise_of` Derivation | Premessa distinta dalla conclusione |
| Inferenza | Conclusione `derived_via` Derivation | Giustificazione inferenziale recuperabile |
| Qualificazione | Assessment `assesses` target | Quality locale |
| Qualificazione | Impatto `affects` risultato/decisione | Effetto pertinente non cancellabile dalla Policy |
| Operativa | Work `waits_for` input/condizione | Attesa del lavoro, non stato della Knowledge |
| Operativa | Work `depends_on` altro esito operativo | Dipendenza di esecuzione |
| Governance | Disposition `authorizes` trattamento | Comportamento autorizzato |
| Operativa | Application `applies` Disposition | Effetto eseguito distinto dalla scelta |
| Governance | Admission `establishes/revises` commitment | Effetto sulla Knowledge |

Questa mappa non decide una struttura tecnica comune `Relation`.

Le relazioni di Provenance e Lineage devono consentire di risalire anche alla base originaria dei contributi umani, distinguendola dal significato attribuito, e alle origini comuni e dipendenze pertinenti.

Tre precisazioni:

- “Il documento D2 dichiara di correggere D1” può essere contenuto di un’Assertion documentale; l’effetto sul commitment di Fold è un’altra relazione di governance.
- Una dipendenza inferenziale e una dipendenza operativa possono avere nomi simili, ma non sono intercambiabili.
- La presenza di un percorso fra elementi non lo rende un percorso di supporto valido: un ciclo non autorizza auto-supporto e più percorsi non dimostrano indipendenza.

La proposizione di identità e l’eventuale applicazione di un uso unitario restano distinguibili. Tale applicazione non può distruggere le informazioni necessarie alla contestabilità della proposizione.

# K — Traceability delle 24 responsabilità

| # | Responsabilità | Destinazione v2 | Natura | Coperta? |
|---|---|---|---|---|
| 1 | Acquisizione dal canale | H1, adattamento della consegna | Capacità interna | SÌ |
| 2 | Registrazione e governo dell’acquisizione | H1, registrazione della ricezione e collegamento al risultato | Capacità interna | SÌ |
| 3 | Validazione tecnica | H2 | Responsabilità autonoma | SÌ |
| 4 | Identificazione e deduplicazione tecnica | H3 | Responsabilità autonoma | SÌ |
| 5 | Preservazione delle Source | H4 | Responsabilità autonoma | SÌ |
| 6 | Estrazione e produzione delle Observation | H5, con sottocapacità esplicite | Responsabilità autonoma | SÌ |
| 7 | Valutazione ed esecuzione del Mapping | H6 | Responsabilità autonoma | SÌ |
| 8 | Composizione semantica / Interpretation | H7 | Responsabilità autonoma | SÌ |
| 9 | Identity Reconciliation | H8 | Meccanismo | SÌ |
| 10 | Comparison e relazioni fra contenuti | H9; Conflict Detection specializzato | Meccanismo | SÌ |
| 11 | Temporal Evaluation | H10 | Meccanismo | SÌ |
| 12 | Derivation | H11 | Meccanismo | SÌ |
| 13 | Current Reconstruction | H12 | Meccanismo | SÌ |
| 14 | Impact Assessment | H13 | Meccanismo | SÌ |
| 15 | Valutazione delle Application Decision Policies | H14 | Governance | SÌ |
| 16 | Gestione del lavoro di verifica | H15 | Responsabilità autonoma | SÌ |
| 17 | Admission e revisioni di governance | H16 | Governance | SÌ |
| 18 | Query & Retrieval contestualizzato | H17, incluso traversal | Responsabilità autonoma | SÌ |
| 19 | Composizione delle Projection | H18 | Responsabilità autonoma | SÌ |
| 20 | Casi d’uso e applicazione delle disposizioni | H19 | Funzione | SÌ |
| 21 | Composizione delle spiegazioni | H20 | Responsabilità autonoma | SÌ |
| 22 | Presentazione fedele | H21 | Confine applicativo | SÌ |
| 23 | Acquisizione dei contributi utente | H22, inclusa recuperabilità della base originaria | Confine applicativo | SÌ |
| 24 | Coordinamento operativo dei Work | Piano operativo, presso i proprietari delle attività | Trasversale | SÌ |

Le 22 schede non sono 22 componenti definitivi: descrivono autonomia di problema. Le capacità interne, i meccanismi e le memorie restano riconoscibili senza imporne la separazione tecnica.

La copertura delle 24 responsabilità non risolve implicitamente l’ownership della formalizzazione delle Decision non-Policy, mantenuta aperta in O.

# L — Reverse check dei 34

**NESSUNA RESPONSABILITÀ NECESSARIA DELLA v1 RISULTA PERSA.**

Rimane la distribuzione fra responsabilità autonome, capacità interne, specializzazioni, memorie e obblighi trasversali. Non vengono ripristinati componenti separati dove il problema è già coperto da tale distribuzione.

# M — Anti-regression check

| Problema da evitare | Ricompare? | Come viene evitato nella v2 |
|---|---|---|
| Candidate universale | NO | Referent e Assertion proposti; Interpretation Result e alternative distinti |
| Knowledge State universale | NO | Commitment, assessment, contestazione, applicabilità e Work hanno bersagli differenti |
| Validity universale | NO | Ruoli temporali e reference time espliciti |
| Relation semanticamente universale | NO | Famiglie descrittive, epistemiche, rappresentative, inferenziali e operative |
| Evidence indifferenziata | NO | Attribuzione, supporto, localizzazione e giustificazione inferenziale distinti |
| Current State come ultimo dato | NO | Reconstruction usa tempo, commitment, conflitti, revisioni e impatti |
| Orchestratore semantico universale | NO | Responsabilità competenti e coordinamento dei Work privo di autorità semantica globale |
| Quality controller centrale | NO | Assessment locali con Quality Model condiviso |
| Provenance Recorder centrale | NO | Cattura presso produttori e applicatori; traversal separato |
| Candidate Validator universale | NO | Controlli locali e verifiche di applicabilità in Admission |
| Logical Document obbligatorio | NO | Documento come eventuale Referent; Source e rappresentazioni indipendenti |
| Policy unica origine della Disposition | NO | Decision da Policy o autorità deliberata prevista; ownership della formalizzazione non-Policy esplicitamente aperta |
| Dedup tecnica come identità documentale | NO | H3 distinto dalla coreferenza documentale di H8 |
| Admission sinonimo di verità | NO | Commitment governato senza incremento automatico di supporto o Quality |
| Work come stato della Knowledge | NO | Piano operativo distinto da contenuti e posizioni epistemiche |
| Contributo umano interpretato che sostituisce l’ingresso originario | NO | H22 conserva contenuto ricevuto e contesto; H7 mantiene distinta l’Interpretation |
| Auto-supporto attraverso cicli | NO | Invariante esplicito su Interpretation, Reconciliation, supporto, Derivation e riuso della Knowledge |
| Origine comune contata automaticamente come corroborazione indipendente | NO | Origini e dipendenze pertinenti recuperabili; molteplicità distinta da indipendenza |
| Nuova valutazione senza nuova giustificazione | NO | Nuova Quality Assessment vincolata a nuova base, criterio o contesto materialmente pertinente |
| Coreferenza applicata come fusione distruttiva | NO | Rappresentazioni, differenze, Provenance e giustificazioni preservate per consentire contestazione e revisione |

Sono inoltre vincoli della candidata:

- attribuzione ≠ supporto sufficiente ≠ commitment;
- Policy non cancella impatti determinati;
- Policy non rende valida o invalida una conclusione inferenziale;
- una risposta utente non equivale automaticamente a Verification, Authorization o Admission;
- una base originaria umana non richiede una Observation artificiale;
- i contributi dipendenti possono essere utili senza diventare attestazioni indipendenti;
- la preservazione necessaria alla reversibilità riguarda l’informazione ancora legittimamente conservata.

# N — Assembly gaps

**NESSUN ASSEMBLY GAP BLOCCANTE PER LA REVIEW DELLA CANDIDATA.**

Le garanzie integrate trovano collocazione nelle responsabilità, nelle memorie, nelle relazioni e nei vincoli già presenti.

In particolare:

- le proposte hanno una memoria anche senza Work;
- i Work hanno proprietari senza diventare stati della Knowledge;
- impatti e revisioni hanno rappresentazione informativa e seguito operativo distinto;
- le decisioni deliberate non devono attraversare artificialmente Policy Evaluation;
- la derivazione su richiesta può produrre un risultato senza Admission implicita;
- qualità, supporto e Provenance restano obblighi locali visibili;
- la base originaria del contributo umano rimane recuperabile senza una nuova primitiva;
- auto-supporto, falsa indipendenza e nuova valutazione priva di nuova giustificazione sono esplicitamente esclusi;
- l’uso unitario di rappresentazioni resta vincolato alla non distruttività e alla contestabilità.

Rimane **non assegnata definitivamente** l’ownership della formalizzazione delle Decision/Disposition nei percorsi non-Policy. La candidata rende esplicita tale apertura in O, senza eliminare gli obblighi informativi e di conservazione pertinenti.

Il carattere non bloccante riguarda la possibilità di sottoporre questa candidata concettuale a review indipendente, non la prontezza di ogni suo percorso per l’implementazione.

# O — Questioni volutamente aperte

| Questione | Perché non blocca la review della candidata |
|---|---|
| **Quando due contenuti condividano una sola Assertion** | Il default conservativo preserva Assertion distinte e relazioni esplicite di equivalenza, compatibilità o implicazione |
| **Granularità finale degli accorpamenti** | I problemi e i loro output sono distinguibili anche quando la futura realizzazione li raggrupperà diversamente |
| **Forma ontologica esatta di Identifier** | Schema, valore e assegnazione rimangono già separabili |
| **Forma concreta del supporto indirizzabile** | Target, attribuzione, base, qualificazioni e storia sono già richiesti |
| **Granularità concreta del Work** | È definito quando serve continuità operativa; non occorre ora decidere un Work per ogni attività |
| **Criteri specifici di identità e versione documentale** | Sono demandati al Domain; la candidata non equipara file, rappresentazione e documento |
| **Algoritmi di Reconciliation** | La candidata definisce input, risultati, alternative e vincoli, inclusa la non distruttività, senza assumere un algoritmo |
| **Formule e soglie di Quality** | Sono preservati target, dimensione, base e vincoli di giustificazione; non occorre un punteggio definitivo per esaminare la distinzione |
| **Forma software futura** | Le responsabilità concettuali non impongono servizi, classi o processi |
| **Storage concreto** | Le memorie definiscono ciò che deve essere recuperabile, non dove o come verrà memorizzato |
| **Ownership della formalizzazione delle Decision/Disposition non-Policy** | La pluralità delle autorità e gli obblighi di rappresentazione e conservazione sono stabiliti. Rimane aperta l’assegnazione della formalizzazione, senza rendere facoltative le informazioni necessarie |

## Apertura esplicita sui percorsi non-Policy

È stabilito che una Decision può derivare sia da Policy Evaluation sia da un’autorità esplicita.

Resta da precisare quale responsabilità possieda la formalizzazione della Decision/Disposition nei percorsi non-Policy e se tale ownership sia locale al contesto decisionale o richieda un confine di Governance comune.

Devono comunque rimanere recuperabili:

- origine dell’autorità;
- target;
- scope;
- contesto;
- Decision;
- Disposition;
- storia dell’eventuale Application.

Non viene introdotta una soluzione a questa apertura. In particolare, non viene creato un Decision Manager né attribuita implicitamente la responsabilità a uno dei produttori esistenti.

Nessuna delle questioni aperte viene risolta per rendere la candidata apparentemente più completa.

# P — Readiness finale della candidata

## Verifica meccanica dell’integrazione

| ID | Controllo | Esito |
|---|---|---|
| **D01** | È recuperabile la distinzione fra contenuto umano ricevuto e sua interpretazione? | **SÌ** — D, G, H7, H22 e I mantengono base originaria, contesto e significato attribuito distinguibili. |
| **D02** | È esplicito il divieto di auto-supporto? | **SÌ** — C, D, H e I lo applicano ai cicli pertinenti; M lo riporta fra i guardrail. |
| **D03** | È esplicito che origine comune non equivale a corroborazione indipendente? | **SÌ** — C, D, G, H, I e J preservano dipendenze e distinzione fra molteplicità e indipendenza. |
| **D04** | È esplicito che una nuova valutazione richiede nuova base, criterio o contesto? | **SÌ** — D, F, G, H e I esplicitano il requisito di pertinenza materiale e le condizioni che da sole non bastano. |
| **D05** | È esplicita la non distruttività/reversibilità della Reconciliation? | **SÌ** — E, G, H8, H16, H18–H19 e I preservano rappresentazioni e giustificazioni necessarie a contestazione, revisione e successiva distinzione. |
| **D06** | È visibile come aperto senza soluzione inventata? | **SÌ** — E, H14, H22, N e O distinguono l’ownership aperta dagli obblighi informativi già stabiliti. |

## `v2 CANDIDATA CORRETTA — PRONTA PER REVIEW INDIPENDENTE`

Le cinque correzioni sono integrate senza cambiare la struttura fondamentale, aggiungere componenti o introdurre nuove primitive.

La candidata resta:

- provvisoria e non canonica;
- distinta dal taglio dell’MVP;
- non ancora validata dal test domestico o dallo stress test cross-domain;
- esplicita sulle questioni ancora aperte.

Il passaggio successivo è la lettura interna del documento e la consegna a Claude per una review indipendente. La candidata può essere letta come oggetto autonomo, senza richiedere la conoscenza delle conclusioni dei Round precedenti.

Non vengono eseguiti ulteriori audit o stress test in questo passaggio. Nessun repository, file di progetto, documento Notion o elemento Linear è stato modificato.

# Delta applicato dopo il Regression Audit

| ID | Correzione applicata | Sezioni v2 interessate |
|---|---|---|
| **D01** | Resa esplicita la base originaria del contributo umano, distinta dal significato attribuito e dall’eventuale autorità; nessuna Observation artificiale o classificazione universale come Source. | C, D, F, G, H7, H15, H17, H22, I, J, K, M |
| **D02** | Ripristinato il divieto trasversale di auto-supporto attraverso Interpretation, Reconciliation, supporto, Derivation e riuso della Knowledge. | C, D, G, H, H7–H8, H11, I, J, M |
| **D03** | Ripristinata la distinzione fra molteplicità e indipendenza epistemica, con recuperabilità di origini comuni e dipendenze pertinenti. | C, D, F, G, H, H3, H5, H9, H11–H12, H17, H20, I, J, M |
| **D04** | Vincolata ogni nuova Quality Assessment a nuova base, criterio o contesto materialmente pertinente; esclusi Admission, mera ripetizione e riuso operativo come giustificazioni sufficienti. | D, E, F, G, H, H15–H16, I, M |
| **D05** | Esplicitata la Reconciliation non distruttiva e contestabile, preservando quanto necessario a revisionare la coreferenza e tornare a distinguere le rappresentazioni. | E, G, H8, H16, H18–H19, I, J, M, O |

**D06 — mantenuto esplicitamente aperto, nessuna soluzione introdotta.**
<!-- END ORIGINAL V2 BODY -->

