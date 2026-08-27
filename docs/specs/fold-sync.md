# `fold-sync` — specifica funzionale

**Status:** Canonical
**Date:** 2026-08-27
**Scope:** comportamento della skill a comando per preservare la memoria emersa dalle conversazioni di Fold

## 1. Obiettivo

`fold-sync` impedisce che risultati significativi del lavoro su Fold rimangano soltanto nella conversazione.

La skill viene richiamata esplicitamente dall'utente su un tratto delimitato della conversazione. Identifica ciò che ha valore persistente, ne distingue la natura, consulta le fonti pertinenti, determina la disposizione corretta, propone le scritture necessarie, le applica soltanto dopo conferma e verifica infine la copertura del tratto acquisito.

La skill non è un riassuntore della conversazione e non conserva tutto ciò che è stato discusso.

## 2. Fonti e autorità

La skill applica il metodo definito in [`docs/metodo-di-lavoro.md`](../metodo-di-lavoro.md) e rispetta le istruzioni di `AGENTS.md` e il governo documentale di [`docs/README.md`](../README.md).

Le fonti hanno responsabilità differenti:

- il **repository** conserva la conoscenza versionata che deve guidare progettazione e implementazione;
- **Linear** conserva roadmap, milestone, issue, stato, dipendenze, checkpoint, chiusure e avanzamento operativo;
- **Notion** conserva ricerca estesa, intuizioni e percorso narrativo, senza essere necessario per continuare Fold;
- la **conversazione** è il luogo di acquisizione, non una memoria persistente del progetto.

Repository e Linear devono restare insieme sufficienti a continuare Fold. La skill non usa la disponibilità contingente di uno strumento per assegnargli una responsabilità che non possiede.

`Canonical` non è una natura primaria dell'informazione. È uno stato o una disposizione successiva, applicabile soltanto dopo aver verificato rilevanza, consolidamento e autorità.

## 3. Vincoli fondamentali

La skill:

- si attiva soltanto tramite invocazione esplicita `$fold-sync`;
- analizza soltanto il perimetro richiesto;
- consulta progressivamente soltanto le fonti pertinenti ai candidati emersi;
- non crea un audit generale del progetto;
- non duplica automaticamente la stessa informazione in più strumenti;
- non rende autonomamente Canonical una decisione materiale di prodotto, metodo o architettura;
- non trasforma ipotesi, Draft, ricerca o ricostruzioni storiche in requisiti implementativi;
- non risolve silenziosamente divergenze irrisolte;
- non esegue scritture prima dell'anteprima e della conferma;
- non esegue commit, push, creazione di branch o altre operazioni protette senza richiesta esplicita;
- non considera il proprio report una forma di persistenza.

## 4. Concetti operativi

### 4.1 Perimetro di acquisizione

È il tratto di conversazione determinato dal parametro numerico dell'invocazione. Soltanto da questo perimetro possono nascere nuovi candidati.

### 4.2 Contesto minimo di interpretazione

È il contenuto precedente alla finestra che può essere consultato esclusivamente quando è indispensabile per comprendere un riferimento presente nel primo messaggio utente selezionato.

Il contesto minimo non amplia il perimetro di acquisizione e non può produrre candidati autonomi.

### 4.3 Candidato

È un elemento emerso nel perimetro che supera la soglia di significatività e deve quindi ricevere una disposizione, anche quando risulta già rappresentato e non richiede nuove scritture.

### 4.4 Aspetto persistente

È una componente semanticamente distinta di un candidato, per esempio:

- evidenza;
- intuizione;
- decisione;
- lavoro futuro;
- risultato operativo;
- conseguenza sul lavoro successivo.

Un singolo passaggio conversazionale può produrre più aspetti persistenti. La skill assegna ogni aspetto alla fonte responsabile del relativo significato, senza cercare una collocazione primaria unica per l'intero candidato.

### 4.5 Disposizione

È l'esito assegnato a un aspetto:

- nessuna persistenza necessaria;
- già rappresentato correttamente;
- aggiornamento di una registrazione esistente;
- creazione di una nuova registrazione;
- approvazione necessaria;
- sospensione recuperabile;
- divergenza da preservare;
- non completato.

## 5. Interfaccia

### 5.1 Avvio

L'uso ordinario è:

```text
$fold-sync 30
```

Il numero è obbligatorio, deve essere un intero positivo e indica gli ultimi `N` messaggi dell'utente precedenti all'invocazione.

Se il parametro è assente, zero, negativo o non interpretabile univocamente, la skill non acquisisce la conversazione, non consulta fonti progettuali e richiede un valore valido.

### 5.2 Anteprima e risposte

Quando sono necessarie scritture, la skill mostra un'anteprima e propone direttamente le risposte applicabili, pronte da copiare:

```text
$fold-sync applica tutto
$fold-sync applica W1 W2
$fold-sync rivedi: ...
$fold-sync annulla
```

Se esistono decisioni materiali, propone anche formulazioni esplicite come:

```text
$fold-sync applica W1 W3 e approvo M1
```

Per impostazione predefinita, questi comandi si riferiscono all'ultima anteprima valida e ancora pendente della conversazione corrente.

Un identificatore del piano viene richiesto soltanto quando esistono più anteprime recuperabili o un'ambiguità reale. La skill non sceglie silenziosamente fra più piani.

La revisione invalida l'anteprima precedente e ne produce una nuova. Può chiarire o correggere candidati già acquisiti, ma non introdurre silenziosamente un candidato autonomo esterno alla finestra originaria.

L'annullamento non equivale a persistenza: se restano elementi significativi soltanto nella conversazione, l'esecuzione resta incompleta.

## 6. Delimitazione della conversazione

### 6.1 Semantica di `N`

`N` indica gli ultimi `N` messaggi dell'utente precedenti al comando di avvio.

La finestra:

- inizia dal più vecchio di questi messaggi;
- termina immediatamente prima dell'invocazione;
- comprende tutto il lavoro cronologico intermedio: risposte dell'assistente, commentary, chiamate e output degli strumenti, allegati e ulteriori messaggi dell'utente;
- non comprende il messaggio di invocazione.

Messaggi di sistema, istruzioni developer e `AGENTS.md` governano il comportamento, ma non vengono contati e non diventano automaticamente candidati.

Se `N` supera il numero di messaggi utente disponibili, la skill non riduce silenziosamente il perimetro: segnala il problema prima di qualsiasi scrittura e richiede una nuova scelta.

Se compattazione, troncamento o indisponibilità della cronologia impediscono di ricostruire esattamente la finestra, un riepilogo non sostituisce i messaggi originali. La skill non applica scritture basate su una ricostruzione presunta e richiede un perimetro accessibile o il materiale mancante.

### 6.2 Primo messaggio contestuale

Se il primo messaggio selezionato dipende da ciò che lo precede, la skill consulta il minimo contesto indispensabile per interpretarlo.

Esempio:

```text
Assistente: propone una decisione
Utente: "Sì, approvo."
```

Con `N = 1`, la proposta precedente può essere letta soltanto per identificare l'oggetto dell'approvazione. Non può generare altri candidati.

Se il riferimento resta ambiguo, l'aspetto dipendente viene sospeso senza ricostruirlo per supposizione.

### 6.3 Allegati, output, citazioni e collegamenti

- Un allegato appartiene al messaggio che lo contiene. Se non è accessibile, vengono sospesi soltanto gli aspetti che ne dipendono.
- Un output di strumento può sostenere o originare un candidato quando rappresenta il risultato diretto del lavoro nella finestra, verifica o contraddice un'affermazione della finestra, oppure è richiamato esplicitamente nel lavoro corrente.
- Campi incidentali incontrati in output ampi non diventano candidati.
- Un contenuto citato o incollato mantiene la propria provenienza e non diventa automaticamente una decisione corrente.
- La destinazione di un collegamento è esterna al perimetro di acquisizione. Può essere aperta per interpretazione, verifica, autorità o riconoscimento di registrazioni esistenti, ma non può generare candidati indipendenti.

## 7. Soglia di significatività

La skill non parte da una lista astratta di categorie, ma dal costo della perdita.

Un elemento supera la soglia quando perderlo comprometterebbe almeno uno fra:

- continuità del lavoro su Fold;
- governo del progetto;
- verifica dei risultati;
- ricostruzione di un passaggio progettuale significativo.

Il valore narrativo da solo non è sufficiente.

L'elemento deve inoltre conservare un contenuto minimo identificabile:

- problema, soggetto o osservazione da cui nasce;
- ciò che è emerso;
- almeno una fra conseguenza, importanza, evidenza o condizione di ripresa.

Un tema ancora vago può essere significativo se produce già una conseguenza concreta, per esempio:

- blocca una issue;
- modifica un criterio di completamento;
- introduce un rischio reale;
- cambia una dipendenza o il lavoro successivo.

Significatività, certezza e autorità sono valutazioni distinte. Un elemento può essere significativo ma incerto o non approvato.

La significatività è distinta dalla necessità di nuova persistenza. Un aspetto già recuperabile da una fonte autorevole per quello specifico significato resta un candidato significativo, ma può ricevere la disposizione `già rappresentato correttamente`.

Il codice può dimostrare comportamento implementato e risultati tecnici, ma non sostituisce automaticamente la persistenza dell'intenzione o di una decisione di prodotto, metodo o architettura.

## 8. Classificazione e scomposizione

La skill distingue almeno queste nature:

- **evidenza / ricerca** — osservazione, analisi o verifica;
- **intuizione / ipotesi** — possibilità significativa non ancora decisa;
- **decisione** — scelta deliberata, con autorità da verificare;
- **lavoro futuro** — risultato ancora da ottenere;
- **risultato realizzato** — esito effettivamente costruito e verificato;
- **conseguenza** — effetto su perimetro, stato, dipendenze, criteri o lavoro successivo.

La classificazione riguarda il significato dell'aspetto. `Canonical`, `Draft`, `Research`, `Historical` e `Superseded` riguardano invece lo stato dell'artefatto che lo conserva.

Prima di scegliere le scritture, la skill scompone il candidato nei suoi aspetti persistenti distinti. Più azioni sono ammesse quando svolgono funzioni differenti; non sono ammesse copie equivalenti dello stesso significato.

L'evoluzione è trattata come una catena di trasformazioni collegate:

```text
intuizione → lavoro → eventuale decisione → eventuale consolidamento
```

La registrazione precedente non viene trasferita né riscritta retroattivamente. Conserva il significato che aveva nella propria fase e può essere aggiornata soltanto con stato e collegamenti compatibili con il proprio ruolo.

## 9. Consultazione progressiva delle fonti

Per ogni candidato la skill parte dalla fonte più pertinente alla natura provvisoria dell'aspetto:

- stato, lavoro, dipendenze, checkpoint o chiusure → Linear;
- decisioni di prodotto, metodo o architettura → repository, poi Linear per le conseguenze operative;
- intuizioni → Notion / Intuizioni, poi issue collegata quando necessaria al contesto;
- risultati → issue, artefatto e relativa verifica;
- conoscenza di implementazione → repository e specifica pertinente;
- ricostruzione storica → artefatto storico e issue originarie;
- ricerca → fonte o memoria esplorativa pertinente;
- divergenza → fonti direttamente coinvolte.

Per ogni aspetto verifica:

- se esiste già una registrazione;
- se è completa e nella fonte responsabile;
- se è corrente, Draft, Research, Historical o Superseded;
- quale autorità possiede;
- se contraddice altre fonti pertinenti;
- se il risultato dichiarato è verificato;
- se occorre non intervenire, aggiornare, creare, sospendere o chiedere approvazione.

La consultazione si arresta quando esistono elementi sufficienti per determinare natura, certezza, autorità, stato temporale o documentale, registrazione pertinente, destinazione e disposizione.

`AGENTS.md`, `docs/README.md` e `docs/metodo-di-lavoro.md` governano la skill ma non diventano automaticamente oggetto dell'audit. Gli elementi non pertinenti trovati al loro interno restano fuori perimetro.

Informazioni significative ma indipendenti incontrate incidentalmente nelle fonti non vengono acquisite né seguite. Possono essere segnalate sinteticamente soltanto quando servono a rendere esplicito un limite o un fatto materialmente rilevante per la verifica.

## 10. Destinazione degli aspetti

La disposizione concettuale attesa è:

```text
esplorazione senza risultato persistente
→ nessun aggiornamento

intuizione significativa
→ memoria esplorativa in Notion

lavoro futuro realmente definito
→ Linear

cambiamento con conseguenze sul lavoro futuro
→ checkpoint Linear

decisione o conoscenza necessaria a guidare Fold
→ eventuale consolidamento nel repository

risultato realizzato e verificato
→ chiusura del lavoro e artefatti pertinenti
```

Una nuova issue Linear è giustificata soltanto quando il lavoro futuro possiede almeno un risultato richiesto e un criterio di completamento sufficientemente definiti.

Una voce di Diario Notion è giustificata soltanto quando esiste un valore narrativo o di case study distinto. Non viene creata per duplicare un risultato già recuperabile in Linear o nel repository.

Una decisione già approvata ma non ancora consolidata va direttamente nel documento repository pertinente quando il repository è disponibile. Linear viene aggiornato soltanto per una conseguenza operativa distinta o come fallback previsto.

## 11. Riconoscimento dell'esistente e idempotenza

Il confronto avviene per aspetto persistente, non per intero passaggio conversazionale.

La skill cerca corrispondenze secondo tre livelli:

1. **Identità esplicita** — ID Linear, URL Notion, percorso e sezione repository, milestone, artefatto o task indicati direttamente.
2. **Identità strutturale** — stesso progetto, problema, scope, risultato richiesto, significato, fase della catena, stato o condizione di ripresa.
3. **Somiglianza semantica probabile** — richiede ulteriore ricerca o conferma; non autorizza da sola un'unione.

Gli esiti possibili sono:

- stessa registrazione già completa → nessuna modifica;
- stessa registrazione incompleta o divenuta obsoleta nel proprio ruolo → aggiornamento mirato;
- registrazioni correlate ma semanticamente distinte → conservazione separata e collegamento;
- nessuna registrazione adeguata → nuova registrazione;
- corrispondenza ambigua → sospensione o conferma;
- contraddizione → gestione come divergenza, non fusione.

### 11.1 Aggiornare

La skill aggiorna quando:

- identità e scope dell'aspetto coincidono con sufficiente certezza;
- la nuova informazione completa stato, evidenza, collegamenti, risultato o condizione di ripresa;
- l'aggiornamento non falsifica il significato originario;
- il ruolo dell'artefatto ammette quell'evoluzione.

### 11.2 Creare

La skill crea quando:

- non esiste una corrispondenza sufficientemente certa;
- l'aspetto ha scope, risultato, stato o fase autonomi;
- una decisione nuova sostituisce una precedente senza autorizzare la riscrittura retroattiva;
- la registrazione esistente è soltanto collegata, non equivalente.

L'ambiguità non autorizza la creazione preventiva di un duplicato.

### 11.3 Protezione degli artefatti storici

Lo stato `Historical` non autorizza aggiornamenti indiscriminati. La skill rispetta il ruolo specifico dell'artefatto.

Una sintesi di milestone consolidata resta una fotografia storica. Le evoluzioni successive appartengono al lavoro successivo, salvo:

- correzioni storiche dimostrabili;
- collegamenti espressamente previsti dal metodo.

### 11.4 Controllo prima della scrittura

Prima di scrivere, la skill rilegge la registrazione bersaglio e verifica che il delta sia ancora assente.

Se la fonte è cambiata, può procedere senza nuova conferma soltanto quando restano invariati:

- effetto approvato;
- identità della registrazione bersaglio;
- sicurezza del delta.

Non deve sovrascrivere o invalidare contenuto nuovo.

In ogni altro caso invalida la decisione di scrittura, rivaluta l'aspetto e presenta una nuova anteprima.

Una nuova esecuzione sulla stessa finestra e sulle stesse fonti immutate deve produrre zero nuove modifiche semantiche. Un'esecuzione successiva a un tentativo parziale applica soltanto i delta ancora mancanti.

## 12. Autorità e decisioni materiali

Decisioni di prodotto, metodo o architettura che modificano materialmente Fold richiedono:

- approvazione esplicita dell'utente con oggetto identificabile; oppure
- delega esplicita di quella specifica decisione a Codex.

Non costituiscono approvazione sufficiente:

- silenzio o semplice prosecuzione della conversazione;
- proposta dell'assistente;
- stato `Done` di una issue;
- presenza di un'implementazione;
- commit o merge privi di una decisione ricostruibile;
- contenuto Draft, Research o Historical;
- approvazione contestuale che non può essere interpretata con sufficiente certezza.

I normali dettagli tecnici che applicano decisioni già consolidate possono essere consolidati come risultato verificato di una task.

La conferma di una scrittura non equivale automaticamente all'approvazione sostanziale dell'informazione registrata. Registrare un'intuizione, creare un lavoro di verifica o preservare un conflitto non approva la soluzione.

Se la conferma deve approvare anche una decisione materiale, l'anteprima contiene una sezione esplicita:

```text
Decisioni materiali che questa conferma approverà
```

Soltanto le decisioni esposte inequivocabilmente in questa sezione possono essere approvate mediante la relativa conferma generale o mediante una formula esplicita come `e approvo M1`.

Una decisione materiale non approvata viene disposta secondo il proprio stato:

- proposta esplorativa senza conseguenza operativa → intuizione Notion;
- proposta che blocca o modifica lavoro corrente → registrazione nella issue Linear pertinente;
- decisione necessaria ma aperta → checkpoint `Decisione in sospeso` nella registrazione pertinente;
- lavoro di decisione o verifica già definito → issue Linear;
- decisione approvata da consolidare → repository, oppure fallback Linear se il repository non è disponibile.

## 13. Anteprima e conferma

L'invocazione iniziale autorizza tutte le operazioni in sola lettura necessarie all'analisi, ma non le scritture.

Se non occorre alcuna scrittura, la skill può concludere direttamente con un esito verificato.

Se occorrono scritture, l'anteprima indica per ogni azione `W`:

- aspetto persistente;
- natura;
- fonte e registrazione bersaglio;
- creazione o aggiornamento;
- contenuto o delta essenziale;
- motivo;
- autorità disponibile;
- eventuale fallback prevedibile.

L'anteprima è completa sulle azioni di scrittura ma sintetica sugli elementi senza persistenza necessaria o già rappresentati, che possono essere raggruppati.

L'utente può approvare tutto, approvare un sottoinsieme, rivedere o annullare. La skill applica esclusivamente ciò che è stato approvato e non estende silenziosamente il piano.

Un'azione nuova o materialmente diversa richiede una nuova anteprima.

La conferma continua a riferirsi alla finestra originaria. Anteprima, conferma e messaggi di controllo non ampliano l'acquisizione.

## 14. Disponibilità delle fonti e fallback

La disponibilità di tutte le fonti non è un prerequisito assoluto. La skill verifica le fonti necessarie per ciascun aspetto e può continuare con operazioni indipendenti.

Se non riesce a consultare le regole canoniche del repository che governano il proprio comportamento, può svolgere un'analisi preliminare ma non applica scritture.

Un fallback:

- è ammesso soltanto se previsto dal metodo o da questa specifica;
- deve essere mostrato nell'anteprima;
- non cambia la natura dell'elemento;
- è una sistemazione temporanea;
- deve essere riconoscibile come riconciliazione pendente;
- conserva destinazione finale, contenuto residuo e condizione di ripresa.

Una successiva esecuzione deve riconoscere il fallback come lavoro ancora da riconciliare, non come stato definitivo già corretto.

### 14.1 Notion indisponibile

Un'intuizione significativa viene registrata temporaneamente nell'issue Linear realmente pertinente con la marcatura:

```text
Intuizione da trasferire in Notion
```

Il riferimento conserva almeno origine o osservazione, significato, motivo d'importanza, destinazione prevista e condizione di ripresa. Non trasforma l'intuizione in issue, decisione o conoscenza Canonical.

Quando Notion torna disponibile, la skill:

1. verifica se l'intuizione esiste già;
2. crea o aggiorna la memoria esplorativa appropriata;
3. collega la registrazione Notion al riferimento Linear;
4. marca il fallback come trasferito.

Se non esiste una issue Linear pertinente, la skill non ne crea una soltanto per ospitare il fallback. L'aspetto resta incompleto finché l'utente non indica una collocazione pertinente o Notion torna disponibile.

### 14.2 Repository indisponibile o non scrivibile

Quando una decisione già approvata deve essere consolidata nel repository e la scrittura non è possibile, la skill può proporre un checkpoint nella issue Linear pertinente:

```text
Consolidamento nel repository in sospeso
```

Il checkpoint conserva decisione o conoscenza da consolidare, autorità acquisita, conseguenza sul lavoro, artefatto previsto e condizione di ripresa.

Il checkpoint non rende la decisione Canonical. Se la conoscenza è necessaria all'implementazione, il readiness gate resta non superato fino al consolidamento.

### 14.3 Linear indisponibile

La skill non trasferisce automaticamente in Notion roadmap, issue, checkpoint o chiusure.

Le operazioni Linear restano non completate; quelle indipendenti destinate ad altre fonti possono proseguire. Se l'elemento operativo non è recuperabile fuori dalla conversazione secondo una regola prevista, l'esecuzione è incompleta.

### 14.4 Indisponibilità successiva all'anteprima

Se una fonte diventa indisponibile dopo la conferma, la skill applica il fallback soltanto se è già stato mostrato e autorizzato. Se il fallback cambia le scritture approvate, presenta una nuova anteprima.

## 15. Fallimenti parziali e riconciliazione

La skill ordina le azioni secondo dipendenze esplicite:

```text
creare o aggiornare la registrazione responsabile
→ verificarla
→ aggiungere collegamenti o aggiornamenti secondari
```

Un'operazione dipendente non parte se il prerequisito fallisce.

Se una scrittura riesce e una successiva fallisce, la skill:

- non cancella automaticamente quanto è già stato scritto;
- rilegge lo stato effettivo;
- non ripete una creazione già riuscita;
- registra in una traccia persistente ciò che resta da fare, quando possibile;
- alla ripresa applica soltanto il delta mancante.

Rollback o correzioni compensative sono ammessi soltanto se sicuri, compatibili con il ruolo dell'artefatto e compresi nell'autorizzazione.

Uno stato `parzialmente applicato` è recuperabile soltanto se anche le operazioni mancanti sono ricostruibili da una traccia persistente fuori dalla conversazione. In caso contrario l'esecuzione è `incompleta`.

## 16. Divergenze

Per ogni divergenza la skill identifica:

- affermazioni coinvolte;
- fonti e registrazioni;
- natura e stato documentale;
- periodo e scope;
- responsabilità della fonte;
- autorità ed evidenze;
- conseguenze sul lavoro corrente.

La recenza è un elemento di valutazione, non una regola di precedenza sufficiente.

### 16.1 Tipi

**Divergenza apparente** — le fonti descrivono tempi, scope o aspetti diversi. La skill conserva entrambe senza correggere retroattivamente la storia.

**Evoluzione esplicita** — esistono `Superseded by`, decisione approvata, checkpoint o aggiornamento della fonte responsabile. La skill segue la catena senza riscrivere il passato.

**Informazione operativa obsoleta** — una fonte che pretende di descrivere lo stato corrente è superata da un normale avanzamento chiaramente documentato nella fonte responsabile. La skill può proporre un aggiornamento mirato o una marcatura storica, preservando il percorso valido.

**Conflitto irrisolto** — le fonti descrivono lo stesso aspetto nello stesso ambito in modo incompatibile e manca una relazione esplicita che permetta di risolverlo. La skill non sceglie.

### 16.2 Persistenza del conflitto

Un conflitto con conseguenze operative viene registrato nella issue, milestone o altra registrazione Linear realmente pertinente. La registrazione conserva fonti, ragione dell'incertezza, conseguenza, decisione o verifica necessaria e condizione di ripresa.

L'assenza di una registrazione pertinente non autorizza da sola una nuova issue. La skill propone una nuova issue soltanto quando il lavoro necessario possiede risultato richiesto e criterio di completamento sufficientemente definiti.

Un conflitto rilevante soltanto per la ricostruzione storica o progettuale può essere preservato nella memoria storica o esplorativa appropriata come ricostruzione incerta, senza diventare backlog.

Una divergenza persistita con fonti, conseguenza e condizione di ripresa può chiudere correttamente l'esecuzione della skill anche quando la decisione progettuale resta aperta.

## 17. Verifica finale

### 17.1 Copertura della finestra

Dopo le scritture, la skill esegue una seconda lettura della stessa finestra immutata.

Per ogni candidato significativo verifica che tutti gli aspetti persistenti abbiano una disposizione e che nessuno sia rimasto soltanto nella conversazione.

Un aspetto significativo può non richiedere una nuova scrittura quando:

- è già rappresentato correttamente;
- un altro aspetto ne conserva già il significato necessario;
- è evidenza usata per verificare un risultato già registrato;
- una nuova registrazione sarebbe una duplicazione senza funzione distinta.

La disposizione deve indicare dove il significato è recuperabile oppure perché non richiede una registrazione autonoma.

### 17.2 Verifica delle scritture

La risposta positiva dello strumento non è sufficiente. La skill rilegge ogni bersaglio e verifica:

- identità;
- contenuto o delta;
- stato e classificazione;
- collegamenti necessari;
- assenza di sovrascritture non autorizzate;
- elementi necessari alla riconciliazione;
- coerenza con l'effetto approvato.

Per il repository verifica file e diff locale, senza versionare automaticamente. Per Linear e Notion rilegge la registrazione tramite il relativo identificatore.

Una scrittura riuscita ma non rileggibile non viene classificata come verificata e rende l'esecuzione incompleta finché la verifica non viene recuperata.

### 17.3 Duplicazioni e idempotenza

La verifica di duplicati ed equivalenti resta vincolata alle registrazioni e alle fonti pertinenti all'aspetto analizzato. Non diventa un audit generale del progetto.

La skill verifica in modo non mutativo che, sullo stato corrente delle stesse fonti, una nuova esecuzione non richiederebbe modifiche semantiche. Non riesegue materialmente tutte le scritture.

## 18. Stati dell'esecuzione

Per ogni aspetto sono ammessi almeno:

- `applicato e verificato`;
- `già rappresentato correttamente`;
- `nessuna persistenza necessaria`;
- `sospeso e recuperabile`, con riferimento persistente;
- `parzialmente applicato e recuperabile`, con operazioni residue persistite;
- `non completato`, quando contenuto o lavoro residuo esistono soltanto nella conversazione.

L'esito complessivo è:

- **completata** — tutti gli aspetti significativi sono coperti e verificati;
- **completata con riconciliazioni pendenti** — ogni sospensione o stato parziale è recuperabile fuori dalla conversazione e riconoscibile come temporaneo;
- **incompleta** — almeno un aspetto significativo, un'operazione residua o una verifica resta soltanto nella conversazione.

## 19. Report finale

Il report è sintetico ma verificabile e non sostituisce le fonti persistenti.

Contiene:

### Perimetro

- valore di `N`;
- estremi riconoscibili della finestra;
- eventuale uso del contesto minimo;
- allegati o contenuti inaccessibili.

### Fonti

- fonti consultate;
- disponibilità rilevanti;
- limiti incontrati.

### Scritture

Per ogni azione:

- aspetto;
- creazione o aggiornamento;
- destinazione esatta;
- effetto applicato;
- esito della rilettura;
- collegamenti prodotti.

### Decisioni materiali

- approvate e consolidate;
- soltanto registrate o sospese;
- approvate ma ancora da consolidare.

### Elementi senza nuove scritture

Possono essere raggruppati distinguendo:

- già rappresentati;
- nessuna persistenza ulteriore necessaria;
- sotto soglia.

### Fallback e riconciliazioni

Per ciascuno:

- registrazione temporanea;
- destinazione finale;
- contenuto residuo;
- condizione di ripresa;
- stato della riconciliazione.

### Elementi incompleti

Vengono esposti singolarmente con causa, fonte o autorizzazione mancante e azione necessaria.

## 20. Comportamento end-to-end

L'esecuzione completa segue questo ordine:

1. validare l'invocazione e `N`;
2. consultare, nell'ordine previsto, `AGENTS.md`, `docs/README.md` e `docs/metodo-di-lavoro.md` per acquisire le regole correnti che governano la skill; questi documenti restano istruzioni e non diventano oggetti automatici dell'audit;
3. delimitare e congelare il perimetro di acquisizione;
4. recuperare, se necessario, il solo contesto minimo di interpretazione;
5. individuare i candidati mediante la soglia di significatività;
6. scomporli in aspetti persistenti distinti;
7. classificare natura, certezza e autorità;
8. consultare progressivamente le fonti pertinenti;
9. riconoscere registrazioni esistenti, divergenze e fallback pendenti;
10. assegnare a ogni aspetto una disposizione;
11. produrre un'anteprima completa delle scritture;
12. attendere la conferma esplicita;
13. rileggere i bersagli e rivalutare azioni invalidate da cambiamenti concorrenti;
14. applicare soltanto le azioni approvate, rispettando dipendenze e fallback;
15. rileggere e verificare ogni scrittura;
16. riesaminare la finestra per verificarne la copertura;
17. verificare duplicazioni pertinenti e idempotenza in modo non mutativo;
18. restituire esito e report verificabile.

## 21. Fuori scope

Questa specifica non autorizza:

- implementazione della skill;
- elaborazione di conversazioni non delimitate;
- riassunto generale della conversazione;
- audit completo di repository, Linear o Notion;
- persistenza indiscriminata di ogni idea;
- creazione automatica di issue da temi vaghi;
- riscrittura retrospettiva di documenti storici;
- modifica dei criteri con cui una decisione diventa Canonical;
- risoluzione autonoma di decisioni materiali o divergenze;
- commit, push o creazione di branch.

## 22. Criteri di accettazione della futura implementazione

La skill sarà implementata correttamente quando saranno verificati almeno questi scenari:

1. `N` valido delimita esattamente gli ultimi `N` messaggi utente e tutto il lavoro intermedio.
2. `N` mancante, invalido o superiore alla cronologia disponibile non produce scritture.
3. Il contesto precedente interpreta il primo messaggio senza generare candidati autonomi.
4. Una finestra priva di elementi significativi termina senza scritture.
5. Un elemento significativo già rappresentato produce un riferimento verificato e zero modifiche.
6. Un passaggio con più aspetti produce azioni distinte nelle fonti responsabili senza duplicazioni equivalenti.
7. Un'intuizione nuova viene proposta per Notion senza diventare issue o decisione.
8. Un lavoro futuro genera una proposta di issue soltanto se possiede risultato e criterio di completamento.
9. Un cambiamento con conseguenze operative produce un checkpoint pertinente senza rendere automaticamente Canonical la decisione.
10. Una decisione materiale non approvata non viene consolidata nel repository.
11. Una decisione materiale approvata è esposta inequivocabilmente nell'anteprima e consolidata soltanto dopo conferma.
12. Una seconda esecuzione equivalente non richiede nuove modifiche semantiche.
13. Due elementi simili ma distinti non vengono fusi.
14. Un artefatto Historical, in particolare una sintesi di milestone, non viene aggiornato con evoluzioni successive non ammesse.
15. Una modifica concorrente rilevante invalida l'azione e produce una nuova anteprima.
16. L'anteprima non applica scritture e propone comandi di conferma semplici e contestuali.
17. Un'approvazione parziale applica soltanto le azioni e decisioni esplicitamente autorizzate.
18. Il fallback Notion → Linear conserva destinazione, contenuto residuo e condizione di ripresa ed è successivamente riconciliabile.
19. L'indisponibilità di Linear non sposta automaticamente lo stato operativo in Notion.
20. Un fallimento parziale è considerato recuperabile soltanto quando le operazioni residue sono persistite fuori dalla conversazione.
21. Una divergenza apparente viene distinta da un conflitto reale.
22. Un conflitto reale viene preservato senza soluzione arbitraria e senza creare una issue priva di risultato definito.
23. Ogni scrittura viene riletta; una scrittura non verificabile non produce esito `completata`.
24. La verifica di equivalenti resta limitata alle fonti pertinenti al candidato.
25. Il test d'idempotenza finale non ripete materialmente le scritture.
26. Il report distingue modificato, invariato, sospeso, riconciliazione pendente e incompleto.
27. L'esecuzione non può dirsi completata se un elemento significativo resta soltanto nel report della conversazione.
28. Un prompt che non invoca esplicitamente `$fold-sync` non attiva la skill.
29. Se `AGENTS.md`, `docs/README.md` o `docs/metodo-di-lavoro.md` non sono consultabili, la skill non esegue alcuna scrittura.
30. Una revisione produce una nuova anteprima e invalida realmente quella precedente, che non può più autorizzare scritture.
31. La skill non esegue commit, push o creazione di branch senza una richiesta esplicita dell'utente.

## 23. Readiness

Questa specifica resta `Draft` durante la revisione. Diventerà `Canonical` soltanto dopo l'approvazione esplicita dell'utente.

L'implementazione di `fold-sync` non deve iniziare finché il documento non è Canonical e non sono disponibili gli strumenti necessari a verificare realisticamente i criteri di accettazione pertinenti.

## 24. Fonti collegate

- [`docs/metodo-di-lavoro.md`](../metodo-di-lavoro.md)
- [`docs/README.md`](../README.md)
- [FOL-23 — Progettare la skill a comando per mantenere la memoria di Fold](https://linear.app/folderapp/issue/FOL-23/progettare-la-skill-a-comando-per-mantenere-la-memoria-di-fold)
- [FOL-22 — Allineare Linear e Notion al metodo di lavoro corrente](https://linear.app/folderapp/issue/FOL-22/allineare-linear-e-notion-al-metodo-di-lavoro-corrente)
