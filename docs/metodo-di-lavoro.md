# Metodo di lavoro di Fold

**Status:** Canonical  
**Date:** 2026-08-27  
**Last updated:** 2026-08-30

**Scope:** esplorazione, progettazione, documentazione, realizzazione e verifica del progetto

## 1. Origine ed evoluzione

Questo metodo consolida ed evolve la disciplina introdotta nella milestone **Organizzare il progetto**. Fold aveva già prodotto conversazioni, ricerca, intuizioni, ipotesi, decisioni e questioni aperte, ma mancava un sistema sufficientemente chiaro per trasformare quel materiale in un percorso verificabile.

La milestone ha introdotto roadmap, lavoro per risultati, distinzione della natura della conoscenza e responsabilità iniziali degli strumenti. L'uso successivo ha mostrato un limite: erano definiti i principi, ma non ancora un ciclo abbastanza esplicito per decidere che cosa preservare, quando registrare un cambiamento e come aggiornare coerentemente le fonti.

Il metodo corrente mantiene quindi la disciplina originaria e integra il ciclo della conoscenza emerso dall'audit del 27 agosto 2026.

## 2. Lavorare per risultati

Fold non viene affrontato come una sequenza indefinita di argomenti interessanti. Ogni lavoro significativo deve produrre un risultato osservabile e verificabile.

Prima di iniziare dobbiamo poter rispondere a sei domande:

1. **Cosa stiamo facendo?**
2. **Perché lo stiamo facendo?**
3. **Cosa dobbiamo ottenere alla fine?**
4. **Cosa non stiamo facendo adesso?**
5. **Quando possiamo dire “finito”?**
6. **Cosa sblocca dopo?**

Prima comprensione, poi terminologia. Prima risultato, poi formalizzazione.

Formulazioni come “pensare al database”, “studiare la UX” o “approfondire gli identificatori” descrivono temi, non necessariamente lavori. Una issue deve indicare quale cambiamento o artefatto permetterà di verificarne il completamento.

## 3. Deviazioni: blocco o backlog

Durante l'esplorazione emergono continuamente domande e possibilità nuove.

- Se una questione **blocca il risultato corrente**, va affrontata o resa una dipendenza esplicita.
- Se non lo blocca, non va inseguita automaticamente: può essere registrata come intuizione oppure trasformata in lavoro futuro quando possiede un risultato definibile.

Quando un lavoro viene rimandato, dobbiamo possibilmente sapere:

- perché è importante;
- perché non appartiene al lavoro corrente;
- quando o a quale condizione avrebbe senso riprenderlo.

La roadmap può cambiare quando emergono nuove evidenze. Il cambiamento deve però essere consapevole e tracciabile, non il risultato implicito di una deviazione conversazionale.

## 4. Natura della conoscenza

Gli elementi emersi nel progetto non hanno tutti la stessa autorità. Manteniamo distinti almeno:

- **Ricerca / evidenza** — qualcosa osservato, studiato o verificato;
- **Ipotesi / intuizione** — qualcosa che potrebbe essere importante, ma non è ancora una decisione;
- **Decisione progettuale** — una scelta deliberata per Fold;
- **Conoscenza canonica** — ciò che deve guidare il lavoro corrente;
- **Lavoro futuro** — qualcosa riconosciuto come necessario o utile, ma non appartenente al lavoro attuale;
- **Risultato realizzato** — qualcosa effettivamente costruito e verificato.

Queste nature descrivono il significato dell'informazione. Gli stati documentali `Canonical`, `Draft`, `Research`, `Historical` e `Superseded` definiti in `docs/README.md` descrivono invece l'autorità del documento che la conserva.

Scrivere qualcosa nel repository non lo rende automaticamente `Canonical`. Una conoscenza diventa `Canonical` quando, dopo la verifica appropriata, viene deliberatamente consolidata come riferimento corrente.

- Un documento `Draft` può sostenere esplorazione e progettazione mentre una questione è ancora aperta, ma non diventa implicitamente un requisito implementativo.
- Decisioni di prodotto, metodo o architettura che modificano materialmente Fold richiedono l'approvazione esplicita dell'utente prima di diventare riferimento canonico, salvo che l'utente abbia delegato esplicitamente quella specifica decisione a Codex.
- Questa regola non si applica allo stesso modo ai normali dettagli tecnici che applicano decisioni già consolidate: possono essere canonizzati come risultato di una task verificata, senza trasformare ogni dettaglio in una nuova decisione strategica.

Ricerca, intuizioni e materiale storico non diventano automaticamente requisiti o decisioni correnti.

## 5. Partire dalla realtà osservata

Quando possibile, Fold segue:

```text
realtà osservata → comprensione → modello → soluzione
```

e non:

```text
modello astratto → tentativo di adattarvi la realtà
```

Problemi, documenti, comportamenti, casi d'uso e situazioni reali devono mettere alla prova il modello. Il futuro va considerato soprattutto per non chiudere inutilmente possibilità importanti, non per introdurre ora tecnologie, astrazioni o funzioni che il MVP non richiede.

Durante la progettazione di fondamenta o contratti strutturali, complessità future già consolidate nella direzione di Fold possono essere usate come pressioni di falsificazione quando servono a distinguere una buona semplificazione da un collasso semantico. Le pressioni devono essere deliberate, limitate e pertinenti alla fondazione esaminata. Il loro uso non amplia il perimetro implementativo, non genera automaticamente backlog, non rende un sistema futuro requisito del MVP e non autorizza progettazione speculativa general-purpose.

La distinzione completa fra perimetro di implementazione e perimetro di validazione fondazionale è definita nella decisione [`0001 — Distinguere perimetro di implementazione e perimetro di validazione fondazionale`](decisions/0001-perimetro-implementazione-validazione-fondazionale.md).

## 6. Documentare ciò che è significativo

Fold deve conservare il percorso mentre nasce, senza trasformare la documentazione in burocrazia.

Quando un lavoro produce qualcosa di significativo, valutiamo se preservare:

- problema e contesto;
- ricerca, fonti ed evidenze;
- conclusione;
- decisione e alternative scartate;
- diagramma, user flow, wireframe, UI, screenshot o confronto, quando utili;
- errore significativo;
- realizzazione e risultati ottenuti;
- test, feedback e verifica.

La sequenza che il progetto dovrebbe poter ricostruire è:

```text
Problema → Ricerca → Conclusione → Decisione → Realizzazione → Verifica
```

Fold cresce contemporaneamente come prodotto reale, percorso di apprendimento e progetto professionale documentato, mantenendo il prodotto come priorità. La documentazione resta subordinata al prodotto: non si introducono attività o funzionalità soltanto perché sarebbero utili al portfolio.

Quando il lavoro coinvolge competenze professionalmente rilevanti per l'utente, va organizzato perché possa comprenderle, esercitarle realmente e conservarne evidenza. Non vanno attribuite all'utente competenze che non ha realmente esercitato.

Per trasparenza sul contributo umano e dell'AI, nel materiale professionale deve restare distinguibile ciò che la persona ha ideato, progettato, realizzato, diretto o verificato e ciò che è stato delegato o prodotto con l'AI.

## 7. Ruolo corrente degli strumenti

### Repository / GitHub

Conserva ciò che deve guidare concretamente progettazione e implementazione: conoscenza canonica, decisioni, specifiche, ricerca necessaria, configurazione, codice e sintesi delle milestone. Una regola o decisione che deve guidare stabilmente Fold oltre la issue corrente va consolidata qui prima di essere trattata come conoscenza persistente del prodotto.

### Linear

Conserva il sistema operativo del progetto: roadmap, milestone, issue, stato, dipendenze, checkpoint di cambiamento, avanzamento e chiusura del lavoro. Può contenere il contratto operativo corrente di una issue, senza diventare da solo la memoria canonica delle regole che devono valere stabilmente oltre quella issue.

### Codex

È l'ambiente principale nel quale Fold viene esplorato, progettato, implementato e verificato. La conversazione corrente non è però memoria persistente: prima della chiusura, ciò che deve sopravvivere va trasferito nella fonte appropriata.

### Notion

È la memoria esplorativa attualmente adottata per ricerca estesa, intuizioni, percorso narrativo e materiale di case study. Non deve contenere requisiti, decisioni correnti o stato operativo indispensabili e assenti da repository e Linear, e la sua indisponibilità non deve impedire a Fold di proseguire.

### Conversazioni esterne

Possono produrre ragionamenti utili, ma non sono memoria canonica. Quando generano qualcosa che deve guidare Fold, occorre trasferirlo nel ciclo descritto di seguito.

## 8. Ciclo della conoscenza

### 8.1 Esplorazione effimera

Un'esplorazione senza risultato persistente può restare nella conversazione. Non va documentata soltanto perché è avvenuta.

### 8.2 Intuizione significativa

Un'ipotesi o possibilità che merita di non essere persa va distillata nella memoria esplorativa attualmente adottata nel database **Intuizioni** di Notion, senza modificare automaticamente roadmap, issue o conoscenza canonica.

Deve conservare almeno:

- problema o osservazione da cui nasce;
- cosa suggerisce;
- perché potrebbe essere importante;
- stato attuale;
- quando o a quale condizione avrebbe senso riprenderla.

Può essere collegata a una milestone o issue per contesto. Diventa lavoro operativo soltanto quando viene deliberatamente trasformata in una issue con risultato e criterio di completamento.

Se Notion non è disponibile, il lavoro non deve bloccarsi, ma l'intuizione non può restare soltanto nella conversazione: va registrato temporaneamente nell'issue Linear pertinente un riferimento chiaramente marcato **Intuizione da trasferire in Notion**, conservando il minimo necessario a recuperarne origine, significato e motivo d'importanza. Quando Notion torna disponibile, l'intuizione viene trasferita nella memoria esplorativa appropriata; la registrazione temporanea non la trasforma in issue, decisione o conoscenza canonica. Prima della chiusura di un lavoro significativo va verificato se esistono intuizioni rilevanti ancora presenti soltanto nella conversazione e, quando possibile, vanno preservate. Più intuizioni strettamente correlate possono essere distillate insieme se ne restano riconoscibili origine e significato.

### 8.3 Cambiamento progettuale significativo

Un cambiamento attiva un checkpoint quando produce conseguenze sul lavoro futuro, per esempio perché:

- modifica una decisione;
- modifica perimetro o fuori scope;
- modifica roadmap o dipendenze;
- modifica qualcosa che una specifica o implementazione dovrà rispettare;
- rende precedente conoscenza `Historical` o `Superseded`.

Una normale evoluzione del ragionamento interna al lavoro corrente, senza conseguenze a valle, non richiede checkpoint. Più cambiamenti correlati possono essere raccolti in un solo checkpoint.

Il checkpoint viene registrato nell'issue Linear pertinente e contiene:

1. situazione precedente;
2. nuova evidenza o problema;
3. cosa cambia;
4. perché il cambiamento è significativo;
5. conseguenze;
6. cosa resta da verificare;
7. fonti e attività interessate.

Il checkpoint non rende automaticamente canonica una conclusione. Se il cambiamento deve guidare Fold, la relativa decisione o conoscenza viene consolidata nel repository con lo stato appropriato.

### 8.4 Verifica d'impatto

Ogni checkpoint controlla esplicitamente:

- **Linear** — stato, perimetro, dipendenze, roadmap o lavoro successivo devono cambiare?
- **Repository** — documenti di prodotto, architettura, decisioni, ricerca o specifiche devono essere creati, aggiornati o superati?
- **Notion** — esiste ricerca, un'intuizione o un passaggio narrativo che vale la pena conservare?
- **Fonti precedenti** — qualcosa deve essere marcato `Historical` o `Superseded`?

Non tutte le fonti devono essere modificate ogni volta. La verifica serve a rendere consapevole anche la conclusione “nessun aggiornamento necessario”.

## 9. Ciclo operativo di una issue

### 9.1 Apertura

Una issue significativa deve rendere comprensibili:

- problema;
- motivo;
- risultato richiesto;
- fuori scope;
- criterio di completamento;
- dipendenze;
- artefatti attesi, quando già conoscibili.

### 9.2 Lavoro

Durante il lavoro si applicano block-vs-backlog e il ciclo della conoscenza. I checkpoint significativi vengono preservati; le esplorazioni senza conseguenze possono restare nella conversazione.

### 9.3 Chiusura

Prima di impostare una issue significativa come conclusa, Linear deve rendere recuperabili almeno:

- **Risultato** — cosa esiste ora;
- **Verifica** — come è stato controllato;
- **Artefatti** — documenti, decisioni, specifiche, codice o test prodotti;
- **Fuori scope residuo** — cosa non è stato risolto;
- **Dipendenze** — cosa è stato aggiornato, risolto o introdotto;
- **Lavoro sbloccato** — quale passo può iniziare dopo.

Una issue non è conclusa soltanto perché se ne è parlato abbastanza o perché l'implementazione sembra terminata.

## 10. Chiusura di una milestone

Alla chiusura di ogni milestone viene creato in `docs/milestones/` un documento autosufficiente con stato `Historical` che conserva:

- situazione iniziale;
- problema e obiettivo;
- issue affrontate;
- lavoro realmente svolto;
- decisioni prese in quella fase;
- risultato e relativa verifica;
- ciò che è rimasto volutamente fuori;
- artefatti prodotti;
- cosa è stato consegnato alla milestone successiva;
- per le milestone ricostruite a posteriori, eventuali evoluzioni successive già note al momento della ricostruzione, raccolte in una sezione chiaramente separata e senza retrodatazione.

La sintesi collega e riassume il lavoro, senza ricopiare integralmente issue e checkpoint, e conserva la fotografia storica della fase. Dopo il consolidamento non viene aggiornata continuamente con ogni evoluzione futura: le nuove evoluzioni vengono documentate nel lavoro successivo pertinente.

Linear mantiene stato e roadmap; il documento nel repository conserva il risultato storico necessario a comprendere il percorso senza consultare Notion.

## 11. Regole per Codex

- Definisci positivamente il perimetro corrente e non assumere contesto esterno.
- Consulta esplicitamente il repository e Linear pertinenti invece di presumere o ignorare il loro contenuto.
- Fornisci a Codex soltanto il contesto necessario al risultato richiesto, senza orientarlo prematuramente con conoscenze future non ancora acquisite dal progetto.
- Non introdurre prematuramente tecnologie o concetti futuri soltanto per prepararli o escluderli.
- Quando il lavoro progetta fondamenta o contratti strutturali, distingui le future feature dalle pressioni strutturali già consolidate: queste ultime possono falsificare una semplificazione senza ampliare il perimetro da implementare.
- Linear può definire il contratto operativo della issue corrente; se una regola o decisione sostanziale deve guidare Fold oltre quella issue e non è consolidata nel repository, segnala il vuoto invece di trattarla come conoscenza canonica o colmarla per supposizione.
- Distingui sempre ricerca, intuizione, decisione, conoscenza canonica e risultato realizzato.
- Non trasformare una vecchia decisione in regola corrente senza verificarne stato e provenienza.
- Quando spieghi un concetto a un utente non sviluppatore, presenta prima il concetto concreto, poi il motivo per cui serve e soltanto dopo il termine tecnico.
- Non eseguire commit, push o creare branch senza richiesta esplicita.

## 12. Versionamento

Il versionamento segue:

```text
lavoro → controllo → risultato coerente → commit → push
```

Commit e push avvengono solo quando richiesti. I commit devono descrivere risultati comprensibili anche mesi dopo e non raggruppare cambiamenti indipendenti senza motivo.

Prima del versionamento, verificare che documentazione, stato operativo e artefatti rappresentino coerentemente il risultato raggiunto.
