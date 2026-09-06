---
title: "Fold — candidata v2.1 dell’anatomia concettuale"
status: Draft
date: 2026-09-04
candidate_version: "v2.1"
baseline_snapshot: "docs/ricerca/fold-anatomia-v2-snapshot-2026-09-04.md"
delta_source: "docs/ricerca/fold-delta-v2-v2.1-2026-09-04.md"
baseline_commit: "ef3b24f450e21173c07563aee02c96ef39babcf7"
knowledge_preservation_gate: "primo Gate non superato; patch controllata applicata; re-check mirato superato"
model_preservation_gate: "superato"
pre_freeze_anti_regression: "superato"
freeze_status: "frozen — baseline for falsification"
freeze_date: 2026-09-06
falsification_target: "FOL-37"
falsification_status: "non ancora eseguita sui casi domestici o cross-domain"
implementation_readiness: "non autorizzata"
---

# Fold — Candidata v2.1

**Stato:** candidata concettuale Draft, non canonica.
**Scopo:** descrivere in modo autonomo il funzionamento di Fold, mantenendo distinguibili informazione, attività, risorse, governance, operatività, memorie e funzioni.

Questa candidata deriva dallo snapshot storico v2 e applica esclusivamente il delta v2 → v2.1 congelato. Il primo Knowledge Preservation Gate non è stato superato; questa stessa candidata contiene la patch controllata dei finding approvati, verificata dal Knowledge Preservation re-check superato. Anche il successivo Model Preservation Gate e il pre-freeze anti-regression sono stati superati. Questa specifica versione è congelata dal 2026-09-06 come baseline concettuale per la falsificazione FOL-37, pur restando Draft e non canonica: non è ancora stata validata sui casi domestici o cross-domain e non autorizza implementazione. Il nome storico `candidate` del file è preservato per mantenere la tracciabilità dei Gate già prodotti.

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

# B — Principio organizzativo della candidata v2.1

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

# C — Anatomia v2.1 candidata completa

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
FOLD — CANDIDATA v2.1 PROVVISORIA
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
    ├── distinzione fra persona rappresentata, attore e autorità concreta
    ├── effetti di retention e cancellazione sulla verificabilità
    └── conservazione, ripristino dei contenuti e dei legami, versionamento e audit
```

La base originaria del contributo umano è una responsabilità di recuperabilità dell’ingresso, non una nuova primitiva. Il suo rapporto con il contributo interpretato è precisato nelle viste e nelle schede pertinenti.

Persona rappresentata, account o attore e autorità concreta rispetto a un target e a un’azione restano distinguibili: coreferenza e attendibilità non attribuiscono da sole permessi. Retention e cancellazione autorizzata possono ridurre la verificabilità; il ripristino, entro il materiale ancora legittimamente conservato, deve preservare o ristabilire anche i legami necessari a comprendere e verificare i risultati, non soltanto i file. Questi vincoli non introducono una primitiva Actor, un modello tecnico di autorizzazione, retention illimitata o un piano di backup.

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

Il produttore rende disponibile un risultato con caratteristiche e limiti propri; il consumatore stabilisce quale risultato o condizione gli occorra e se quanto disponibile sia sufficiente per il tratto successivo. L’esistenza dell’output del produttore non garantisce tale sufficienza. Quando serve continuità, il Work conserva il requisito non ancora soddisfatto e il seguito operativo, senza introdurre un’orchestrazione centrale.

Produrre un risultato, rendere osservabile ad altri un accadimento o segnale, reagire a tale cambiamento ed essere vincolati da una condizione o da un invariante restano significati differenti. La forma concreta del vocabolario di eventi e comunicazioni, inclusa l’eventuale relazione `EMITS`, resta **CANDIDATA (K-006)**: non viene canonizzata una nuova relazione e `PRODUCES`, `REACTS_TO` e `CONSTRAINED_BY` non assorbono gli altri significati.

`Correction / Supersession` non compare come unico componente: Interpretation e Comparison riconoscono le relazioni, Temporal Evaluation distingue la successione, Admission applica la revisione autorizzata e Impact Assessment ne valuta le dipendenze.

## Vincoli comuni ai collegamenti

I feedback fra responsabilità non autorizzano auto-supporto:

> Nessun risultato può diventare supporto epistemico di sé stesso attraverso un ciclo di Interpretation, Reconciliation, supporto, Derivation o riuso della Knowledge.

Un ciclo di elaborazione può esistere e produrre risultati utili. Non può far apparire il risultato iniziale come una nuova giustificazione indipendente di sé stesso.

Analogamente, molteplicità di rappresentazioni, contributi, letture, percorsi o derivazioni non implica indipendenza epistemica. Origine comune e dipendenze pertinenti devono rimanere recuperabili. Se l’indipendenza rispetto al bersaglio non è stabilita, non può essere presunta: può restare non determinata senza trasformarsi né in dipendenza certa né in inutilità del contributo.

Questi sono vincoli sui produttori e consumatori esistenti, non responsabilità affidate a nuovi controllori né a un enum o a una primitiva universale di indipendenza.

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

## Attenzione temporale e base dell’attesa

Una funzione deve distinguere la risposta su richiesta dall’attenzione autonoma che eventualmente promette. Quando è autorizzata e promessa attenzione autonoma, il coordinamento del Work riconosce una condizione temporale pertinente, usa Temporal Evaluation con un reference time e prosegue il lavoro; il passaggio del tempo non crea una Source.

Restano separati:

- la base informativa dell’attesa;
- le condizioni e la finestra pertinenti;
- il risultato del riscontro entro il perimetro esaminato;
- il comportamento applicativo autorizzato.

Se la base viene riusata, base, condizioni e finestra restano recuperabili. Il Work conserva impegno e prosecuzione operativa: non prova un obbligo, un mancato arrivo o un’assenza nel mondo.

Questa composizione resta **CANDIDATA (K-080)** e non introduce una primitiva Expectation, un Temporal Controller, uno scheduler o un alert universale. Il rapporto fra base predittiva e successivo riscontro negativo resta aperto.

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

La conformità o correttezza procedurale di una Decision o della sua applicazione e la correttezza fattuale del contenuto sul mondo sono valutazioni differenti: nessuna delle due prova automaticamente l’altra.

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

Una rettifica o correzione prevale quando è sostenuta la relazione pertinente con il bersaglio e il relativo contesto. Maggior numero di fonti, maggiore recenza, autorità globale o ranking generico della Source non sono sufficienti da soli e non costituiscono un truth score.

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
- l’effetto pertinente non risulti già applicato;
- impatti noti non rendano improprio l’effetto previsto.

Se queste condizioni non reggono, non viene inventata silenziosamente una disposizione alternativa. Rimangono recuperabili la Decision storica e il motivo della mancata applicazione.

Una conferma o risposta tardiva resta riferita a oggetto, aspetto, contenuto presentato, portata e natura dell’atto originari: elementi aggiunti o target modificati non la ereditano. Una conferma che abilita un uso non diventa per questo supporto diretto di tutte le premesse usate. Questo controllo non equivale a produrre una nuova Decision e non risolve il contratto uniforme di applicabilità nei rami Verification, Work e Application, che resta aperto.

## Impatto epistemico e Policy

```text
Cambiamento pertinente
       │
       ├── possibile coinvolgimento di risultati o decisioni
       ├── tenuta delle basi: non valutata / messa in dubbio / accertata per un uso
       ├── rivalutazione: non eseguita / eseguita
       └── risultato accertato: confermato / corretto
                 │
          qualificazione recuperabile
                 │
          scelta operativa distinta:
          rivalutare ora / dopo
          verificare / segnalare
          limitare un uso
```

Risultato storico, potenziale impatto, tenuta delle basi, avvenuta rivalutazione e risultato effettivamente accertato non sono intercambiabili. Una base dubbia o inadeguata non determina da sola il nuovo valore; riconoscere un problema delle basi non richiede di avere già ricalcolato tutto.

Un impatto determinato resta recuperabile e vincola gli usi pertinenti anche quando la rivalutazione è rinviata. La Policy può governare il seguito operativo, non cancellare l’impatto né presentare il vecchio risultato come pienamente aggiornato. Non viene introdotto uno stato globale STALE e i criteri specifici d’uso dei contenuti ammessi ma impattati restano aperti.

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
  attività concreta      input / evento /
       │                  condizione temporale pertinente
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

Attempt, attesa ed esito sono aspetti recuperabili della storia del Work; non vengono promossi automaticamente a primitive autonome. Una condizione temporale può rendere riprendibile il Work autorizzato quando la funzione promette attenzione autonoma; il Work non sostituisce la base informativa dell’attesa né il risultato del successivo riscontro.

I risultati utili prodotti da un tentativo interrotto possono sopravvivere come risultati identificabili di quel tentativo, con provenienza e tentativo recuperabili per ciascun risultato. Il successo di un retry non rende automaticamente preferibili o valide in blocco tutte le letture che esso produce e non richiede un selettore globale del tentativo migliore.

Un retry è un nuovo tentativo sotto presupposti materialmente equivalenti. Un mutamento materiale di premesse, risorse, criteri o contesto può richiedere una nuova valutazione, senza riscrivere gli esiti storici dei tentativi precedenti.

Un output vuoto resta qualificato distinguendo almeno esecuzione riuscita con zero risultati nel perimetro, esecuzione incompleta o parziale e materiale non processabile; copertura e tentativo pertinenti restano recuperabili. L’insieme vuoto dei risultati non determina da solo l’esito del Work né prova un’assenza nel mondo.

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

La ricezione della risposta può consentire una ripresa operativa senza essere sufficiente a confermare il contenuto. Prima del riuso devono restare valutabili pertinenza e applicabilità nel contesto corrente; la risposta resta legata alla domanda, al target, al contenuto presentato e allo scope originari.

La stessa interazione può contenere informazione e scelta autorizzativa, ma le due nature devono rimanere distinguibili. Identificare la persona rappresentata o l’account che contribuisce non stabilisce da solo l’autorità concreta rispetto al target e all’azione. L’Intake non acquisisce automaticamente, per questo, l’ownership della formalizzazione delle Decision non-Policy.

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
| **Regole di accesso e sicurezza** | Ingresso, Query, Verification, Application | Chi può accedere, contribuire o agire, distinguendo persona rappresentata, account/attore e autorità concreta per target e azione |

Versioni e ambiti di applicabilità vengono registrati quando hanno contribuito materialmente a un risultato o a una decisione. Se un risultato contribuisce materialmente a una Decision o a una spiegazione storica, devono restare recuperabili il risultato pertinente e le basi effettivamente usate: premesse, criterio, reference time, contesto, limiti e parte semanticamente pertinente delle risorse. Una dipendenza è materiale quando il suo cambiamento potrebbe alterare significato, giustificazione o esito, oppure la spiegazione della scelta fra alternative.

Le risorse definiscono forme, significati, criteri e vincoli. Non sono componenti attivi che eseguono autonomamente le valutazioni. Il requisito di recuperabilità non cambia la natura del risultato, non ne implica Admission, non impone di conservare ogni calcolo o ogni risorsa e non promette una riesecuzione identica.

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

L’osservabilità del funzionamento del sistema — metriche e diagnosi operative — ha uno scopo distinto dall’audit di azioni e Decision, dalla Provenance/Lineage e dalla storia epistemica. Questi percorsi possono condividere registrazioni pertinenti ma non si sostituiscono; non ne deriva uno stack di monitoring o logging.

Il traversal è una capacità di accesso. Non produce retroattivamente le tracce mancanti.

La cattura locale deve rendere recuperabili anche le dipendenze e l’origine comune pertinenti. Per risultati negativi, aggregazioni e continuità comprende, quando materialmente usati, referente, ruolo, tempo, perimetro esaminato e presupposti di assenza, completezza o continuità. Una dipendenza non trovata non dimostra assenza d’impatto: se le basi sono insufficienti, il controllo pertinente deve essere ampliato oppure l’esito deve restare indeterminato.

Per ciascun risultato utile provenienza e Lineage raggiungono il tentativo che lo ha prodotto, anche quando quel tentativo è stato interrotto o seguito da un retry. Per un’aggregazione semanticamente trattata come Derivation restano inoltre recuperabili membri inclusi, criterio d’inclusione, periodo o scope pertinente e metodo di aggregazione.

La granularità di Provenance, supporto e assessment deve poter raggiungere la più piccola unità sulla quale conferma, correzione, contestazione o derivazione possono avere effetto differente. Questo criterio non impone una segmentazione tecnica universale né un oggetto per parola.

Contare più elementi conservati non basta a stabilire che rappresentino più attestazioni indipendenti; l’assenza di una dipendenza conosciuta non prova indipendenza.

Per esempio:

- due scansioni dello stesso documento possono migliorare la lettura, senza diventare automaticamente due attestazioni indipendenti;
- due conclusioni derivate dalle stesse premesse non sono automaticamente due conferme indipendenti;
- un nuovo tentativo tecnico non crea automaticamente una nuova fonte epistemica.

I contributi dipendenti non sono inutili: possono aumentare leggibilità, compatibilità, precisione o copertura. Non devono però essere contati automaticamente come corroborazione indipendente.

## Conservazione necessaria alla contestabilità della coreferenza

Una conclusione identitaria o un uso unitario non devono distruggere le rappresentazioni originarie, le loro differenze, le Provenance e la giustificazione necessaria a contestare la conclusione.

Il requisito di reversibilità è riferito all’informazione ancora legittimamente conservata. Non introduce un obbligo di conservazione indiscriminata e non definisce una funzione software di unmerge.

Retention e cancellazione autorizzata possono rendere non più disponibili basi o relazioni e quindi ridurre la verificabilità: questa conseguenza deve qualificare recuperi, ricostruzioni e spiegazioni pertinenti. Il recovery ristabilisce, entro il materiale ancora legittimamente conservato, contenuti e collegamenti necessari alla comprensione; non garantisce il recupero di dati legittimamente cancellati e non definisce backup, replica o disaster recovery.

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

La preservazione non dipende dal successo dell’interpretazione. I criteri di retention e cancellazione restano distinti dalla qualità epistemica; quando riducono il materiale disponibile, l’effetto sulla verificabilità deve restare riconoscibile. Il ripristino concettualmente pertinente comprende anche i collegamenti necessari, non soltanto il contenuto della Source.

## H5 — Estrazione e produzione delle Observation

- **Problema posseduto:** rendere indirizzabile ciò che è osservabile nel materiale.
- **Input principali:** Source e sue rappresentazioni tecnicamente utilizzabili.
- **Output principali:** Observation, strutture osservate, letture alternative, risultati parziali e assessment estrattivi.
- **Risorse consultate:** conoscenza dei formati e criteri di osservazione, parsing e qualità.
- **Memorie lette/scritte:** legge Source; scrive Observation, localizzazioni, assessment e Lineage.
- **Coopera con:** preservazione, Mapping, Interpretation e gestione dei tentativi.

Testo nativo, OCR, layout, struttura e parsing sono capacità interne distinte. Il grezzo non viene sostituito silenziosamente dalla normalizzazione.

Il testo nativo incorporato e la rappresentazione visuale possono divergere. Testo nativo e OCR restano letture con origine e metodo propri: nessuna sostituisce silenziosamente l’altra, e Provenance e Quality pertinenti devono rendere distinguibile l’eventuale divergenza senza imporre ora un algoritmo di confronto visuale.

L’estrazione dichiara per ciascun risultato ciò che è disponibile, i relativi limiti e il tentativo che lo ha prodotto. Non decide che tale risultato sia sufficiente per un uso semantico successivo; un risultato utile può sopravvivere anche se il tentativo complessivo è stato interrotto.

Letture differenti della stessa origine possono migliorare leggibilità, precisione o copertura. Non costituiscono automaticamente attestazioni indipendenti del fatto successivamente interpretato.

## H6 — Valutazione ed esecuzione del Mapping

- **Problema posseduto:** applicare corrispondenze riutilizzabili senza confonderle con l’interpretazione già accettata.
- **Input principali:** Observation o campi strutturati, contesto classificatorio, Mapping candidati.
- **Output principali:** applicabilità valutata, ruoli semantici proposti, ambiguità e dipendenze dal Mapping.
- **Risorse consultate:** Mapping Definitions, Domain, schemi identificativi e forme Core.
- **Memorie lette/scritte:** legge materiale pertinente; scrive risultati del Mapping, assessment e Lineage.
- **Coopera con:** Interpretation, Query e Impact Assessment.

Non ammette Assertion né riconcilia definitivamente referenti.

La classificazione del contenitore o del documento complessivo può proporre contesto e Mapping pertinenti, ma non trasferisce automaticamente il proprio tipo alle porzioni interne, ai documenti contenuti o a contenuti semanticamente distinti.

## H7 — Interpretation

- **Problema posseduto:** comporre elementi disponibili in una proposta di significato coerente.
- **Input principali:** Source/Observation, risultati del Mapping, contributi strutturati con base originaria recuperabile, contesto recuperato.
- **Output principali:** Referent e Assertion proposti, Interpretation Result, alternative, attribuzioni e supporti pertinenti.
- **Risorse consultate:** Core, Domain, Mapping e Quality Model.
- **Memorie lette/scritte:** legge materiale, basi dei contributi, contesto e Knowledge; scrive proposte, supporti, assessment e dipendenze.
- **Coopera con:** Mapping, Reconciliation, Comparison, Verification, Query e User Contribution Intake.

Comprende classificazione contestuale e composizione documentale. Non decide Admission o automazione.

Interpretation valuta se gli output disponibili soddisfino i prerequisiti del risultato semantico richiesto; la sola disponibilità dichiarata dal produttore non ne garantisce la sufficienza. La classificazione contestuale del contenitore resta un input e non ammette automaticamente il tipo delle parti interne.

Le alternative riconosciute come mutuamente esclusive restano distinguibili e non possono essere trattate come commitment compatibili sul medesimo scope. Ridurne il numero tramite vincoli, eliminazione o incompatibilità non costituisce automaticamente nuovo supporto epistemico per l’alternativa rimasta.

Il significato attribuito a un contributo umano rimane distinguibile dal contenuto effettivamente ricevuto.

Il riuso della Knowledge deve conservare le dipendenze pertinenti. Il risultato dell’Interpretation non può tornare attraverso il contesto come nuova giustificazione indipendente di sé stesso.

## H8 — Identity Reconciliation

- **Problema posseduto:** valutare se rappresentazioni differenti possano riferirsi allo stesso soggetto.
- **Input principali:** Referent proposti o esistenti, identificatori, assegnazioni, attributi e contributi.
- **Output principali:** proposte di coreferenza, alternative, indizi contrari e assessment referenziali.
- **Risorse consultate:** Domain, schemi identificativi, Core invariants e Quality Model.
- **Memorie lette/scritte:** legge contesto referenziale e supporti; scrive proposte e giustificazioni, mantenendo recuperabili le rappresentazioni originarie e le differenze pertinenti.
- **Coopera con:** Interpretation, Query, Comparison e Governance.

La coreferenza documentale è una specializzazione. Il Domain determina quale soggetto debba continuare — per esempio punto, rapporto o contratto — e quali cambiamenti siano compatibili con tale continuità; nome, fornitore o Identifier non decidono da soli identità o separazione.

Riconciliare una persona rappresentata con un account o con un’altra rappresentazione non attribuisce all’attore autorità concreta sul target o sull’azione.

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

Comparison riconosce la relazione di rettifica rispetto al bersaglio e alle basi pertinenti: numero, recenza, autorità globale o ranking generico delle Source non la sostituiscono. Quando riconosce alternative mutuamente esclusive, la loro eliminazione o restrizione non produce da sola supporto indipendente per l’alternativa residua.

Compatibilità fra contributi non implica indipendenza delle rispettive origini.

## H10 — Temporal Evaluation

- **Problema posseduto:** valutare relazioni temporali senza confondere tempo del contenuto e storia del sistema.
- **Input principali:** qualificazioni temporali, intervalli, reference time e contesto.
- **Output principali:** confronti temporali, sovrapposizioni, successioni e valutazioni pertinenti.
- **Risorse consultate:** semantica temporale Domain e invarianti Core.
- **Memorie lette/scritte:** legge tempi e storie; scrive valutazioni con il proprio contesto.
- **Coopera con:** Comparison, Derivation, Reconstruction, Impact Assessment e Governance.

L’arrivo tardivo non viene trattato come una modifica automatica del tempo del fatto. Assenza di fine dichiarata non prova durata infinita e un periodo documentato non prova decorrenza continuativa: criterio e limiti della continuità devono essere espliciti.

Un tempo ignoto resta ignoto e un tempo impreciso conserva la propria precisione. Una data disponibile con un ruolo differente non completa silenziosamente un tempo mancante; un confronto temporale richiede compatibilità sufficiente di ruolo, precisione e contesto.

Restano distinti la cadenza o il tempo di produzione/emissione di un’informazione, il periodo o fenomeno descritto dal contenuto e il momento o la cadenza con cui l’informazione diventa disponibile a Fold. Pattern osservato, previsione, dichiarazione, obbligo e raccomandazione hanno basi e forza differenti: una ricorrenza osservata non acquisisce automaticamente forza predittiva o normativa.

Temporal Evaluation riceve un reference time e può valutare una condizione temporale usata dal Work; non si attiva autonomamente e non crea Source, obblighi, previsioni o alert.

## H11 — Derivation

- **Problema posseduto:** produrre conclusioni applicando criteri inferenziali pertinenti a premesse esplicite.
- **Input principali:** premesse, regola o metodo, condizioni di applicabilità e reference context.
- **Output principali:** conclusione derivata, giustificazione, dipendenze e assessment inferenziale.
- **Risorse consultate:** Core, Domain, criteri inferenziali e Quality Model.
- **Memorie lette/scritte:** legge premesse e risorse; scrive risultato e Lineage; può formulare una nuova Assertion proposta.
- **Coopera con:** Query, Temporal Evaluation, Reconstruction, Policy e Admission.

La Policy governa attivazione e usi, non la validità semantica della conclusione.

Quando una conclusione deriva da un’aggregazione, la sua giustificazione conserva almeno membri inclusi, criterio d’inclusione, periodo o scope pertinente e metodo di aggregazione. L’aggregazione resta un caso di Derivation quando semanticamente appropriato e non richiede un oggetto Aggregate universale.

Una conclusione derivata non diventa supporto indipendente delle proprie premesse perché è stata materializzata o riutilizzata. Percorsi inferenziali differenti devono mantenere recuperabili le dipendenze e le basi comuni pertinenti.

## H12 — Current Reconstruction

- **Problema posseduto:** ricostruire ciò che Fold può sostenere per un aspetto, tempo e scopo determinati.
- **Input principali:** Knowledge disponibile, reference time, conflitti, correzioni, qualificazioni progressive d’impatto e criteri d’uso.
- **Output principali:** ricostruzione qualificata, alternative e limiti.
- **Risorse consultate:** Domain, criteri di continuità, criteri del caso d’uso e vincoli di utilizzo applicabili.
- **Memorie lette/scritte:** legge commitment e giustificazioni; quando il risultato contribuisce materialmente a una Decision o spiegazione storica, rende recuperabili risultato, scope, reference time, basi e dipendenze effettivamente usate.
- **Coopera con:** Query, Comparison, Temporal Evaluation, Derivation, Projection e Explanation.

Non identifica il corrente con l’ultimo valore ricevuto. Non presume continuità oltre la semantica e la base disponibili. Proposte eventualmente considerate rimangono distinguibili dai commitment ammessi; i criteri del loro uso restano aperti.

Current Reconstruction distingue sia ciò che Fold sosteneva o conosceva in un momento storico, usando il patrimonio e i criteri allora disponibili, sia ciò che Fold oggi può ricostruire riguardo a quel momento passato. Entrambe le risposte mantengono recuperabili reference context e basi effettivamente usate; l’informazione acquisita tardi non retrodata la storia epistemica.

Un impatto determinato qualifica la ricostruzione pertinente anche quando la rivalutazione è rinviata; un potenziale impatto o una base dubbia non vengono presentati come risultato già corretto. La ricostruzione non può trattare il riuso di risultati dipendenti, o contributi la cui indipendenza non è stabilita, come nuova corroborazione indipendente.

## H13 — Impact Assessment

- **Problema posseduto:** individuare e qualificare quali risultati o decisioni possano essere materialmente coinvolti da un cambiamento e che cosa sia già accertato sulle loro basi.
- **Input principali:** cambiamento, dipendenze conservate, risultati e versioni pertinenti; referenti, ruoli, tempi, perimetri e presupposti materiali di assenza, completezza o continuità.
- **Output principali:** potenziale coinvolgimento, qualificazione della tenuta delle basi, stato della rivalutazione, eventuale risultato accertato, bersagli e basi della valutazione.
- **Risorse consultate:** significato delle risorse cambiate e criteri pertinenti al bersaglio.
- **Memorie lette/scritte:** legge Lineage, contenuti, scope e storia decisionale; scrive livelli d’impatto recuperabili, inclusa l’indeterminatezza quando le basi non bastano.
- **Coopera con:** Query/traversal, Reconstruction, Policy, autorità competente e proprietari dei Work.

Una nuova informazione o un nuovo membro può incidere su aggregazioni, risultati negativi e continuità anche senza comparire fra le premesse positive originarie. L’assenza di una dipendenza trovata non autorizza a dichiarare nessun impatto.

Non pianifica autonomamente ogni rivalutazione, non esegue ricomputazioni globali e non dichiara automaticamente falso ogni risultato coinvolto. Potenziale impatto, inadeguatezza delle basi e nuovo risultato non sono lo stesso esito.

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

Non ogni risposta è conferma informativa, autorizzazione o Admission. Una risposta tardiva conserva domanda, target, contenuto presentato, scope e natura dell’atto originari; non si estende automaticamente a elementi nuovi. Rimane aperto come uniformare il controllo di applicabilità alla ripresa del Work.

Un eventuale nuovo assessment deve indicare la nuova base, il nuovo criterio o il nuovo contesto materialmente pertinente. Il solo completamento della verifica come lavoro non aumenta Quality.

## H16 — Admission e revisioni di governance

- **Problema posseduto:** applicare un commitment o una revisione autorizzata mantenendo contenuto e storia distinguibili.
- **Input principali:** Referent/Assertion proposti, Disposition, basi pertinenti e condizioni correnti.
- **Output principali:** commitment applicato o revisionato, storia dell’effetto, oppure motivo della mancata applicazione.
- **Risorse consultate:** Core invariants, vincoli pertinenti, autorità e disposizione applicabile.
- **Memorie lette/scritte:** legge proposte, decisioni e storia degli effetti; scrive governance della Knowledge e Application, incluso il motivo di mancata applicazione.
- **Coopera con:** Policy, Verification, Comparison, Impact Assessment e proprietari delle applicazioni.

Prima dell’applicazione verifica anche se l’effetto pertinente sia già stato applicato. Non aumenta Quality, non cambia il claim sorgente e non inventa una nuova disposizione. Una conferma abilitante può consentire l’uso, ma non sostiene automaticamente tutte le premesse impiegate.

Alternative riconosciute come mutuamente esclusive non possono essere ammesse congiuntamente come commitment compatibili sul medesimo scope. L’Admission non trasforma la loro restrizione in nuovo supporto e non introduce un Candidate, solver o stato epistemico universale.

L’ammissione di una conclusione identitaria non deve rendere distruttiva o non contestabile l’unificazione delle rappresentazioni. Restano applicabili gli obblighi di preservazione definiti per la Reconciliation.

## H17 — Query & Retrieval

- **Problema posseduto:** trovare materiale pertinente conservandone natura, scope e qualificazioni.
- **Input principali:** domanda, target, filtri semantici, tempo, corpus e autorizzazioni.
- **Output principali:** risultati recuperati o risultato negativo delimitato.
- **Risorse consultate:** Domain, criteri di Query e regole di accesso.
- **Memorie lette/scritte:** legge Source, Observation, proposte, Knowledge e storie; conserva scope e limiti quando necessari.
- **Coopera con:** Interpretation, ragionamento, Projection, Explanation e Functions.

Il traversal è una sua capacità di accesso. Recuperare non significa ammettere o concludere. Un risultato negativo resta delimitato da corpus, tempo, criteri, copertura e limiti disponibili; non dimostra assenza nel mondo né che nessuna Source sia arrivata. La distinzione concreta fra corpus richiesto, accessibile, esaminato e copertura resta aperta.

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

È una famiglia di responsabilità per casi d’uso, non un controllore semantico universale. Ogni funzione dichiara se risponde soltanto su richiesta o promette attenzione autonoma; nel secondo caso può proseguire tramite Work autorizzato e condizioni temporali, senza introdurre un controller universale.

Riconoscere una persona o un account non autorizza da solo l’azione: l’autorità concreta resta riferita a target e comportamento. Il contratto uniforme di applicabilità delle Functions resta aperto.

Un uso unitario di rappresentazioni deve rispettare la non distruttività e la contestabilità della coreferenza. L’esecuzione di tale uso non rende vera la proposizione di identità né ne aumenta il supporto.

## H20 — Composizione delle Explanation

- **Problema posseduto:** rendere comprensibile la giustificazione reale di un risultato.
- **Input principali:** risultato da spiegare, domanda esplicativa, contributi, supporti, Lineage e decisioni.
- **Output principali:** spiegazione fedele, con limiti e alternative pertinenti.
- **Risorse consultate:** criteri esplicativi e significati Domain.
- **Memorie lette/scritte:** legge tracce e giustificazioni tramite Query; conserva la spiegazione se richiesto dal suo uso.
- **Coopera con:** Query, ragionamento, Governance, Projection e Presentation.

Non inventa un percorso plausibile dove manca la traccia reale. Se una spiegazione storica dipende materialmente da un risultato intermedio, recupera quel risultato, reference time, scope, basi e parti pertinenti delle risorse effettivamente usate, senza cambiarne la natura. Se retention o cancellazione hanno eliminato materiale necessario, rende visibile il limite di verificabilità invece di ricostruire la traccia.

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

Questa sezione rende visibili due assi non equivalenti:

- lo **stato genealogico** del Ledger — STABILE, CANDIDATA, APERTA o SUPERATA — qualifica la conoscenza acquisita nel percorso progettuale ed è determinato soltanto dal Ledger;
- la **forza o forma concettuale locale** — FORTE, CANDIDATO o APERTO NON BLOCCANTE — indica quanto una distinzione sia necessaria o quanto la forma adottata sia definitiva dentro questa candidata.

Le classificazioni locali indicano quindi il sostegno concettuale, non autorità canonica:

- **FORTE:** distinzione necessaria e sufficientemente sostenuta.
- **CANDIDATO:** organizzazione o definizione adottata per questa v2.1.
- **APERTO NON BLOCCANTE:** forma esatta rinviata, con default che preserva l’informazione.

`FORTE` non promuove una K-ID CANDIDATA a STABILE e non significa automaticamente primitiva autonoma. `CANDIDATO` non indebolisce una conoscenza STABILE né rende facoltativa la responsabilità informativa che la forma proposta deve coprire. Le etichette locali non sostituiscono lo stato del Ledger.

## Elementi e famiglie

| Elemento | Forza/forma locale e raccordo genealogico | Ruolo nella candidata |
|---|---|---|
| **Referent** | NECESSITÀ REFERENZIALE FORTE; DEFINIZIONE K-143 CANDIDATA | Il locus referenziale è necessario; la definizione corrente resta genealogicamente candidata |
| **Assertion** | FORTE | Elemento semantico indirizzabile che porta un contenuto proposizionale |
| **Value** | FORTE | Contenuto strutturato non referenziale |
| **Distinzione schema–valore–assegnazione dell’Identifier** | FORTE | Impedisce di equiparare stringa, identificatore e identità |
| **Forma ontologica definitiva di Identifier** | APERTO NON BLOCCANTE | Non necessaria per conservare le tre distinzioni |
| **Qualificazioni temporali** | FORTE | Ruoli temporali riferiti al bersaglio pertinente |
| **Source** | DEFINIZIONE K-049 STABILE; COLLOCAZIONE K-148 CANDIDATA | Origine contenutistica disponibile a Fold; la sua adiacenza alla grammatica centrale resta candidata |
| **Observation** | DEFINIZIONE K-050 STABILE; COLLOCAZIONE K-148 CANDIDATA | Risultato di osservazione distinto dalla proposizione; la sua adiacenza alla grammatica centrale resta candidata |
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
| **Ricostruzione contestualizzata** | RESPONSABILITÀ K-073 STABILE; FORMA CONCRETA DEL RISULTATO CANDIDATA | La necessità della Current Reconstruction è stabile; la materializzazione del risultato resta candidata |
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

Restano semanticamente distinguibili una relazione descrittiva fra Referent, una proprietà o assegnazione fra Referent e Value e le qualificazioni epistemiche, di Provenance o di supporto riferite alla proposizione o al contributo pertinente. Relazione fra soggetti, valore attribuito e qualificazione epistemica non sono la stessa cosa e non richiedono una struttura tecnica universale `Relation`.

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

L’assegnazione può essere temporale, contestata o corretta. La stringa originale rimane recuperabile. Il Domain stabilisce se l’identificatore riguarda, per esempio, un punto, un rapporto o un contratto e quali condizioni ne sostengano la continuità; uguaglianza o cambiamento del valore non decidono da soli identità o separazione.

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

Contributi dipendenti possono essere utili e migliorare leggibilità, precisione, compatibilità o copertura. Non vengono automaticamente contati come corroborazione indipendente. Quando l’indipendenza non è stabilita, l’assessment può mantenerla non determinata; non viene presunta dalla sola assenza di dipendenze note.

Una conferma abilitante resta una dipendenza d’uso entro il proprio scope e non diventa supporto diretto di tutte le premesse impiegate.

Nessun ciclo di supporto, Interpretation, Reconciliation, Derivation o riuso della Knowledge può rendere un risultato supporto epistemico di sé stesso. La materializzazione di una conclusione non cancella le sue premesse né la rende una fonte indipendente rispetto a esse.

## Quality Assessment

Una Quality Assessment è riferita a un target, una dimensione, una base e uno scopo pertinente, e conserva la propria storia.

Restano dimensioni non collassabili provenance/origine, integrità o fedeltà della rappresentazione, competenza o autorità relativa alla specifica proposizione, indipendenza e corroborazione. Non costituiscono una proprietà intrinseca unica della Source, un reliability score globale o un algoritmo obbligatorio.

Una nuova Quality Assessment richiede:

- una nuova base;
- oppure un nuovo criterio;
- oppure un nuovo contesto materialmente pertinente.

Non costituiscono da soli nuova giustificazione:

- ripetere la stessa valutazione;
- ammettere il risultato;
- trovarlo già nella Knowledge;
- riutilizzarlo attraverso un nuovo percorso operativo.

Admission non aumenta Quality. Un assessment può dichiarare indipendenza non determinata rispetto al proprio bersaglio; Quality non sceglie automaticamente il comportamento prudenziale e non richiede un enum universale. La produzione delle valutazioni resta distribuita presso i produttori competenti.

## Tempo

| Natura temporale | Esempio di significato |
|---|---|
| Tempo del contenuto | Periodo al quale un importo, rapporto o evento si riferisce |
| Storia informativa/epistemica | Quando Fold ha osservato, interpretato, verificato o ammesso |
| Storia operativa | Quando un lavoro è stato aperto, tentato, sospeso o applicato |
| Reference time | Momento rispetto al quale si effettua una valutazione o ricostruzione |

Una data non migra automaticamente da un ruolo all’altro. Assenza di fine dichiarata non prova durata infinita e un periodo documentato non prova automaticamente continuità; criterio, base e limiti della ricostruzione restano espliciti. Non esiste una `Validity` universale.

Un tempo ignoto non viene completato con un’altra data disponibile e un tempo impreciso conserva la propria precisione. I confronti richiedono compatibilità sufficiente di ruolo, precisione e contesto.

La cadenza o il tempo di produzione/emissione di un’informazione, il periodo o fenomeno descritto dal contenuto e il momento o la cadenza della sua disponibilità a Fold sono ruoli differenti. Pattern osservato, previsione, dichiarazione, obbligo e raccomandazione restano distinti; una ricorrenza osservata non conferisce da sola forza predittiva o normativa. Il rapporto fra base predittiva e successivo riscontro negativo resta aperto in C02.

Quando una funzione promette attenzione autonoma, base dell’attesa, condizioni/finestra, riscontro delimitato e comportamento restano distinti. La loro composizione è CANDIDATA (K-080): non costituisce una primitiva Expectation né un controller temporale.

## Documenti e rappresentazioni

- Un **file** è una forma tecnica di contenuto.
- Una **Source** è un’origine contenutistica resa disponibile.
- Una **rappresentazione** può raffigurare o contenere uno o più documenti.
- Un **documento** può essere trattato come soggetto documentale.
- Un **Referent documentale** serve quando occorre conservarne identità indipendente.
- Un **locator** individua la porzione pertinente della rappresentazione.

Sono ammesse sia più Source per un documento sia una Source con più documenti.

Locator e porzioni possono sovrapporsi, restare incompleti e avere confini incerti senza richiedere una segmentazione completa preventiva della Source. Un raggruppamento non dimostra automaticamente ordine, completezza o identità documentale.

Il testo nativo incorporato può divergere dalla rappresentazione visuale; testo nativo e OCR restano letture con origine, metodo, Provenance e Quality propri e nessuna sostituisce silenziosamente l’altra. Analogamente, la classificazione del contenitore complessivo può offrire contesto a Mapping e Interpretation, ma non trasferisce automaticamente il proprio tipo a porzioni, documenti contenuti o contenuti semanticamente distinti. I criteri documentali specifici restano aperti.

Comporre porzioni non prova coreferenza; uguaglianza tecnica non prova identità documentale. Le regole specifiche di versione e correzione vengono dal Domain.

La coreferenza e l’eventuale uso unitario non devono distruggere le rappresentazioni originarie e le differenze necessarie a contestare la conclusione. Se l’informazione ancora legittimamente conservata permette di riconoscere soggetti differenti, deve rimanere possibile revisionare la conclusione e tornare a distinguerli.

## Informazione negativa e modalità

La candidata distingue:

1. negazione esplicita sostenuta;
2. assenza osservata in una porzione delimitata;
3. esito negativo di una ricerca;
4. Assertion negativa sul mondo.

Corpus, scope, tempo, copertura e limiti rimangono recuperabili quando necessari. Un risultato vuoto entro il corpus accessibile non dimostra assenza al di fuori di quel corpus. Restano aperte sia la distinzione operativa fra corpus richiesto, accessibile, esaminato e relativa copertura, sia il rapporto fra una base predittiva e il successivo riscontro negativo: quest’ultimo non è automaticamente un conflitto o un fatto non avvenuto.

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
| Descrittiva/referenziale | Assertion esprime una relazione Referent→Referent | Relazione fra soggetti distinta da un valore attribuito |
| Predicativa | Assertion assegna o predica Value rispetto a Referent | Proprietà/valore distinto dal soggetto e dalle qualificazioni epistemiche |
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

| # | Responsabilità | Destinazione v2.1 | Natura | Coperta? |
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

| Problema da evitare | Ricompare? | Come viene evitato nella v2.1 |
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
| Applicabilità trattata come una nuova Decision | NO | Il controllo verifica condizioni già stabilite e non inventa una disposizione alternativa |
| Expectation o Temporal Controller universali | NO | Attesa, riscontro e comportamento restano composti attraverso responsabilità esistenti; K-080 resta CANDIDATA |
| Asse universale Admission/Usability | NO | Commitment e criteri d’uso restano distinti senza un nuovo asse comune |
| Scissione obbligatoria di H7 | NO | L’apertura riguarda la visibilità dei risultati parziali, non una nuova responsabilità |
| Controllore centrale dell’auto-supporto | NO | L’invariante resta distribuito presso produttori e consumatori |
| Enum obbligatorio dell’indipendenza | NO | L’indeterminatezza è ammessa senza imporre una rappresentazione universale |
| Risultato intermedio mutato di natura perché usato | NO | Cambia l’obbligo di recuperabilità materiale, non la natura informativa |
| Assenza del produttore del risultato negativo | NO | H17 produce già risultati negativi delimitati; resta aperta la precisione del corpus |

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

## Conoscenze intenzionalmente fuori dalla funzione dell’anatomia

| ID | K-ID | Disposizione preservata |
|---|---|---|
| **B01** | K-022 STABILE; K-023 CANDIDATA | Lifecycle, calcolo, effetti e test di parallelizzabilità restano nel Ledger. Non diventano una sezione di concorrenza o parallel execution della v2.1. |
| **B02** | K-091 STABILE | La governance fondazionale del cambiamento dei Core invariants resta nel Ledger. Non è Application Policy né comportamento runtime. |

Queste conoscenze restano attive e vincolanti quando verrà affrontato il relativo problema; la loro mancata duplicazione nell’anatomia non le supera. In particolare K-023 resta CANDIDATA.

## Aperture preservate per il test successivo

| ID | Questione ancora aperta | Vincolo già acquisito che non viene riaperto |
|---|---|---|
| **C01** | Controllo uniforme di applicabilità nei rami Verification, Work e Application | Admission può controllare l’applicabilità senza produrre una nuova Decision |
| **C02** | Rapporto fra base predittiva dell’attesa e successivo riscontro negativo | Base, finestra, riscontro e comportamento restano distinti |
| **C03** | Criteri d’uso di contenuti ammessi ma impattati | Un impatto determinato non può essere occultato; K-161 resta STABILE |
| **C04** | Visibilità degli esiti parziali interni di Interpretation | Esiti parziali e alternative sono rappresentabili; H7 non viene scissa |
| **C05** | Corpus richiesto, accessibile, esaminato e copertura | Query produce già il risultato negativo delimitato |
| **C06** | Criteri con cui Reconstruction considera proposte non ammesse | Conservazione o presentazione non equivalgono ad Admission |
| **C07 / D06** | Ownership della formalizzazione di Decision/Disposition non-Policy | Autorità, target, scope, contesto e storia restano obbligatori; K-185 resta APERTA |

Nessuna di queste righe sceglie una soluzione, un nuovo owner, una nuova primitiva o un nuovo stato globale.

**F2d — cambiamento di versione di una risorsa.** Resta aperto chi o quale responsabilità renda disponibile a Fold un cambiamento di versione affinché le responsabilità pertinenti possano reagire. K-006 resta CANDIDATA, K-090 STABILE e K-096 APERTA: non viene creato un C08, non viene assegnato un produttore e non sono scelti manager, event bus, polling, eventi o scheduler.

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

# P — Stato della candidata v2.1

## Controllo di preservazione dei recuperi preesistenti

| ID | Controllo | Esito |
|---|---|---|
| **D01** | È recuperabile la distinzione fra contenuto umano ricevuto e sua interpretazione? | **SÌ** — D, G, H7, H22 e I mantengono base originaria, contesto e significato attribuito distinguibili. |
| **D02** | È esplicito il divieto di auto-supporto? | **SÌ** — C, D, H e I lo applicano ai cicli pertinenti; M lo riporta fra i guardrail. |
| **D03** | È esplicito che origine comune non equivale a corroborazione indipendente? | **SÌ** — C, D, G, H, I e J preservano dipendenze e distinzione fra molteplicità e indipendenza. |
| **D04** | È esplicito che una nuova valutazione richiede nuova base, criterio o contesto? | **SÌ** — D, F, G, H e I esplicitano il requisito di pertinenza materiale e le condizioni che da sole non bastano. |
| **D05** | È esplicita la non distruttività/reversibilità della Reconciliation? | **SÌ** — E, G, H8, H16, H18–H19 e I preservano rappresentazioni e giustificazioni necessarie a contestazione, revisione e successiva distinzione. |
| **D06** | È visibile come aperto senza soluzione inventata? | **SÌ** — E, H14, H22, N e O distinguono l’ownership aperta dagli obblighi informativi già stabiliti. |

## `v2.1 DRAFT CONGELATA COME BASELINE PER LA FALSIFICAZIONE — GATE E PRE-FREEZE ANTI-REGRESSION SUPERATI`

I recuperi D01–D05 della baseline restano presenti e D06 resta aperto. I nove ripristini autorizzati e la patch controllata dei finding approvati sono integrati senza cambiare la struttura fondamentale, aggiungere componenti o introdurre nuove primitive. Il primo Knowledge Preservation Gate resta storicamente non superato; la patch è stata successivamente verificata dal Knowledge Preservation re-check superato e il percorso strutturale dal Model Preservation Gate superato. Dopo il pre-freeze anti-regression superato, questa specifica versione è congelata come baseline di FOL-37.

La candidata resta:

- Draft, provvisoria e non canonica;
- distinta dal taglio dell’MVP;
- corretta dopo il primo Knowledge Preservation Gate non superato, con Knowledge Preservation re-check, Model Preservation Gate e pre-freeze anti-regression successivamente superati;
- congelata dal 2026-09-06 come baseline concettuale per la falsificazione FOL-37, pur restando Draft e non canonica;
- non ancora falsificata dal test domestico o dallo stress test cross-domain;
- esplicita sulle questioni ancora aperte;
- non idonea ad autorizzare implementazione.

Il passaggio successivo autorizzato è la falsificazione domestica e cross-domain della baseline congelata in FOL-37. Eventuali modifiche future a questa baseline devono derivare da regressioni o problemi dimostrati dalla falsificazione, non da nuova esplorazione teorica. Il freeze non chiude FOL-36 e non autorizza implementazione, validazione sui casi reali, architettura tecnica o congelamento del perimetro MVP.

# Recuperi già presenti nella baseline v2

| ID | Correzione applicata | Sezioni v2 interessate |
|---|---|---|
| **D01** | Resa esplicita la base originaria del contributo umano, distinta dal significato attribuito e dall’eventuale autorità; nessuna Observation artificiale o classificazione universale come Source. | C, D, F, G, H7, H15, H17, H22, I, J, K, M |
| **D02** | Ripristinato il divieto trasversale di auto-supporto attraverso Interpretation, Reconciliation, supporto, Derivation e riuso della Knowledge. | C, D, G, H, H7–H8, H11, I, J, M |
| **D03** | Ripristinata la distinzione fra molteplicità e indipendenza epistemica, con recuperabilità di origini comuni e dipendenze pertinenti. | C, D, F, G, H, H3, H5, H9, H11–H12, H17, H20, I, J, M |
| **D04** | Vincolata ogni nuova Quality Assessment a nuova base, criterio o contesto materialmente pertinente; esclusi Admission, mera ripetizione e riuso operativo come giustificazioni sufficienti. | D, E, F, G, H, H15–H16, I, M |
| **D05** | Esplicitata la Reconciliation non distruttiva e contestabile, preservando quanto necessario a revisionare la coreferenza e tornare a distinguere le rappresentazioni. | E, G, H8, H16, H18–H19, I, J, M, O |

**D06 — mantenuto esplicitamente aperto, nessuna soluzione introdotta.**

## Delta integration record

| Delta | Sezioni v2.1 interessate | K-ID | Tipo di intervento | Verifica NON deriva |
|---|---|---|---|---|
| **Δ01** | C; D — Attenzione temporale; F — attesa/ripresa; H10, H17, H19; I — Tempo e informazione negativa; M, O | K-079, K-080, K-081 | Precisata la composizione fra base, finestra, riscontro e comportamento e la ripresa temporale del Work autorizzato | Nessuna Expectation o Temporal Controller universali; nessuno scheduler/alert; tempo ≠ Source; K-080 resta CANDIDATA |
| **Δ02** | G — Resources & Memories; H12, H20; M | K-075, K-093, K-109 | Reso esplicito il recupero del risultato e delle basi materialmente usate per Decision o spiegazioni storiche | Nessuna conservazione indiscriminata, Admission, mutazione di natura o promessa di riesecuzione identica |
| **Δ03** | E — Impatto; G — Lineage; H13 | K-085, K-086 | Esteso l’impatto a scope, assenze, completezza e continuità materialmente usati | Nessun grafo completo, rilevatore onnisciente, impatto negativo automatico o ricomputazione globale |
| **Δ04** | E — Impatto; H12–H13; M, O | K-087 | Separati potenziale coinvolgimento, tenuta delle basi, rivalutazione e risultato accertato | Nessuno stato globale STALE, enum obbligatorio, falsità automatica o criterio d’uso C03 risolto |
| **Δ05** | C — vincoli comuni; G — Lineage; H12; I — Supporto e Quality; M | K-102 | Vietata la presunzione d’indipendenza; ammessa l’indipendenza non determinata | Nessun enum/primitiva/controllore centrale; contributi non dichiarati certamente dipendenti o inutili |
| **Δ06** | H8, H10, H12; I — Identifier e Tempo | K-071, K-138 | Esplicitati base e limiti della continuità e il ruolo del Domain nel determinare il soggetto | Nessuna regola universale di continuità, fusione/separazione o nuovo tipo di entità |
| **Δ07** | E — Applicabilità; F — Verification; H15–H16; I — Supporto; M, O | K-018, K-038, K-039 | Aggiunti effetto già applicato, scope originario delle risposte tardive e limite del supporto abilitante | Applicabilità ≠ nuova Decision; nessun exactly-once tecnico; C01 e C07 restano aperti |
| **Δ08** | C — trasversali; G — accesso; H8, H19, H22 | K-179 | Distinte persona rappresentata, account/attore e autorità concreta per target/azione | Nessuna primitiva Actor, modello tecnico di autorizzazione, ruolo universale o soluzione D06 |
| **Δ09** | C — trasversali; G — conservazione/Lineage; H4, H20 | K-180 | Resi visibili gli effetti di retention/cancellazione sulla verificabilità e il recupero dei legami | Nessun piano di backup/replica/disaster recovery, recupero di dati cancellati o retention illimitata |

# Knowledge Preservation Patch Record

Questa tabella registra l’assemblaggio della patch autorizzata dopo il primo Gate non superato; non è autorità genealogica. Le sigle B01–B09 indicano qui i finding bloccanti del Gate e non le omonime disposizioni B01/B02 del delta.

| Finding | K-ID | localizzazione finale | intervento | apertura/guardrail preservato |
|---|---|---|---|---|
| **B01** | K-043 | F — Esecuzione; G — Lineage; H5 | Preservati risultati utili per tentativo e vietata la selezione in blocco del retry | Nessun Result/Attempt Core, merge o selettore globale |
| **B02** | K-068 | H10; I — Tempo | Conservati ignoranza, precisione, ruolo e condizioni di comparabilità temporale | Nessuna Validity, timestamp universale o data inferita automaticamente |
| **B03** | K-078 | H10; I — Tempo | Distinte produzione/emissione, fenomeno descritto, disponibilità e diverse forze modali | C02 resta aperta; nessun concetto domestico hardcoded nel Core |
| **B04** | K-117 | E — Correzione; H9 | Rettifica fondata sulla relazione pertinente al bersaglio, non su ranking generico | Nessun truth scorer |
| **B05** | K-132 | I — Value; J — grammatica | Distinti Referent→Referent, Referent→Value e qualificazioni epistemiche | Nessuna Relation tecnica universale o nuova primitiva |
| **B06** | K-150 | G — Lineage; H11 | Rese recuperabili base di inclusione, membri, periodo/scope e metodo dell’aggregazione | H18 resta Projection; nessun Aggregate universale |
| **B07** | K-151 | H7; H9; H16 | Vietata Admission congiunta di alternative mutuamente esclusive e falsa forza per eliminazione | Nessun Candidate, solver, stato o controller universale |
| **B08** | K-169 | H5; I — Documenti | Distinte letture native, OCR e rappresentazione visuale con Provenance/Quality proprie | Nessun algoritmo visuale deciso |
| **B09** | K-171 | H6; H7; I — Documenti | Vietato trasferire automaticamente il tipo del contenitore alle parti | K-142 e criteri documentali specifici restano aperti |
| **m01** | K-002 | C — Direzioni; H5; H7; F | Esplicitati output/limiti del produttore, requisito/sufficienza del consumatore e seguito del Work | Nessuna orchestrazione centrale |
| **m02** | K-006 | C — Direzioni | Distinti risultato, segnalazione osservabile, reazione e vincolo | K-006 resta CANDIDATA e il vocabolario resta candidato; `EMITS` non canonizzata |
| **m03** | K-013 | F — Esecuzione/Rivalutazione | Distinto retry su presupposti equivalenti da nuova valutazione; storia non riscritta | Nessuna nuova primitiva Attempt |
| **m04** | K-031 | I — Documenti e locator | Ammesse porzioni sovrapposte/incomplete senza segmentazione preventiva totale | Raggruppamento non prova ordine, completezza o identità |
| **m05** | K-042 | C — Direzioni; F; H5/H7 | Distinte disponibilità dichiarata, sufficienza valutata e continuità operativa | Nessun Result Validator universale |
| **m06** | K-063 | F — Esecuzione | Qualificato output vuoto per successo-zero, incompletezza o non processabilità, con copertura/tentativo | Output vuoto non prova assenza nel mondo |
| **m07** | K-074 | H12; I — Tempo | Distinte conoscenza storica allora disponibile e ricostruzione odierna del passato | Reference context e basi recuperabili; nessuna retrodatazione |
| **m08** | K-095 | E — Governance | Distinte correttezza procedurale e correttezza fattuale | Nessuna delle due prova l’altra |
| **m09** | K-100 | I — Quality | Distinte origine, fedeltà, competenza relativa, indipendenza e corroborazione | Nessuna reliability intrinseca o score globale |
| **m10** | K-107 | G — Provenance/Lineage | Definita granularità minima rispetto agli effetti differenti | Nessuna segmentazione tecnica universale |
| **m11** | K-181 | G — Provenance, Lineage e storie | Distinti audit, osservabilità operativa, Provenance/Lineage e storia epistemica | Nessuno stack di monitoring/logging deciso |
| **m12** | K-073 | I — assi ed Elementi | Resa STABILE la responsabilità e CANDIDATA soltanto la forma concreta del risultato | Nessun indebolimento genealogico della Reconstruction |
| **m13** | K-143 | I — assi ed Elementi | Distinte necessità referenziale forte e definizione K-143 CANDIDATA | Nessuna promozione genealogica del Referent |
| **m14** | K-049, K-050, K-148 | I — assi ed Elementi | Distinte definizioni STABILI e collocazione K-148 CANDIDATA | Source/Observation non indebolite né collocazione promossa |
| **m15** | K-006, K-090, K-096 | O — F2d | Resa visibile l’origine ancora non assegnata del cambiamento di versione | Nessun C08, produttore, manager o meccanismo tecnico scelto |
