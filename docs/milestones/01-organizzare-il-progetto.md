# Milestone 1 — Organizzare il progetto

**Status:** Historical  
**Completamento ricostruito:** 2026-08-21 — Linear non fornisce una data di completamento della milestone; la data è ricavata dalle issue concluse e dalla ricostruzione conversazionale.  
**Ricostruzione storica:** 2026-08-27  
**Scope:** ricostruzione autosufficiente della prima milestone di Fold — MVP domestico

**Nota metodologica:** questa sintesi combina le registrazioni disponibili in Linear con la ricostruzione delle conversazioni. FOL-5 → FOL-6 → FOL-7 descrive la sequenza logica **roadmap → metodo → configurazione operativa**, non una cronologia dettagliata dimostrata dai timestamp Linear.

## 1. Situazione iniziale

Fold esisteva già prima della creazione dell'attuale progetto **Fold — MVP domestico**. Nel tempo erano state accumulate conversazioni, ricerche, intuizioni, ipotesi, decisioni, vecchie formulazioni del prodotto e questioni ancora aperte.

Il problema non era partire da zero, ma governare materiale già abbondante e distribuito. Nelle conversazioni potevano emergere contemporaneamente ricerca, progettazione, funzionalità possibili, problemi tecnici, apprendimento e nuove direzioni. Era facile cambiare argomento, approfondire una possibilità soltanto perché interessante o perdere la distinzione tra ciò che era deciso, ipotizzato, realizzato o rimandato.

Fold doveva smettere di crescere come una grande conversazione continua e iniziare a essere trattato come un progetto di prodotto, pur restando personale e supportato dall'AI.

Esisteva anche un obiettivo complementare: conservare materiale sufficiente per un futuro case study professionale. Il prodotto doveva però restare prioritario e il portfolio doveva derivare dal lavoro reale, non generare attività artificiali.

## 2. Obiettivo e criterio di completamento

Lo scopo della milestone era:

> Mettere ordine in ciò che sappiamo, ciò che manca e ciò che è stato rimandato.

Il criterio di completamento era:

> Roadmap, dipendenze e sistema di lavoro sono abbastanza chiari da collocare ogni nuovo lavoro senza improvvisare.

Il risultato richiesto era organizzativo. La milestone non doveva ancora definire nel dettaglio prodotto, architettura o tecnologia.

## 3. FOL-5 — Definire la roadmap e le fasi del MVP

Prima di decidere il lavoro successivo è stato ricostruito lo stato del progetto distinguendo:

- ciò che era già stato fatto;
- ciò che restava aperto;
- ciò che era stato volutamente rimandato;
- ciò che richiedeva ancora verifica.

Il risultato è stato una roadmap di sette milestone:

1. Organizzare il progetto;
2. Definire il primo Fold domestico;
3. Progettare il MVP;
4. Costruire il primo sistema utilizzabile;
5. Completare le funzionalità del MVP;
6. Verificare Fold nell'uso reale;
7. Consolidare il MVP domestico.

La roadmap non era soltanto una lista: ogni fase dichiarava il risultato necessario per poter avanzare. Il ciclo stabilito era:

```text
obiettivo → milestone → task → risultato → verifica → chiusura → lavoro successivo
```

## 4. FOL-6 — Stabilire il metodo di lavoro e il ruolo degli strumenti

La roadmap richiedeva un metodo che impedisse di tornare alla conversazione indefinita. Sono state introdotte sei domande per ogni lavoro significativo:

1. cosa stiamo facendo;
2. perché;
3. cosa dobbiamo ottenere;
4. cosa resta fuori;
5. quando è finito;
6. cosa sblocca.

La regola generale era **lavorare per risultati, non per argomenti**.

Sono stati inoltre stabiliti:

- distinzione tra ricerca, ipotesi, decisioni, conoscenza canonica, lavoro futuro e risultato realizzato;
- regola block-vs-backlog per le deviazioni;
- registrazione del motivo e della condizione di ripresa del lavoro rimandato;
- preferenza per realtà osservata → comprensione → modello → soluzione;
- rifiuto della complessità prematura per il MVP;
- documentazione significativa durante il lavoro;
- prodotto prima del portfolio;
- trasparenza sul contributo umano e dell'AI;
- uso di Codex/AI come supporto al lavoro, non come memoria autonoma del progetto: il contesto necessario doveva essere fornito esplicitamente;
- necessità di non orientare Codex prematuramente con conoscenze future non ancora acquisite dal progetto;
- disciplina `lavoro → controllo → risultato coerente → commit → push`, con commit, push e creazione di branch soltanto su richiesta esplicita.

La responsabilità iniziale degli strumenti era:

- **Linear** — roadmap, milestone, issue, backlog, dipendenze e avanzamento;
- **Notion** — ricerca, intuizioni, spiegazioni estese e memoria progettuale;
- **Repository / GitHub** — codice, configurazione, documentazione canonica e risultati consolidati;
- **Codex / AI** — supporto al lavoro nel contesto fornito esplicitamente, non fonte autonoma di memoria persistente del progetto.

Questa era la decisione della milestone, non una configurazione immutabile degli strumenti.

## 5. FOL-7 — Configurare il progetto Fold — MVP domestico in Linear

Roadmap e metodo sono stati trasformati in una struttura operativa reale. In Linear sono stati creati:

- il progetto **Fold — MVP domestico**;
- obiettivo e principio operativo;
- le sette milestone;
- scopo e criterio di completamento di ciascuna fase.

La configurazione iniziale ha deliberatamente evitato scadenze, priorità, cycle, label e issue non ancora necessarie. La struttura doveva essere aggiunta quando risolveva un problema reale, non perché disponibile nello strumento.

L'obiettivo generale del progetto era progettare, costruire e verificare una prima versione domestica funzionante di Fold, documentandone il percorso come case study professionale. Il principio operativo stabiliva che ogni lavoro importante dovesse avere un motivo chiaro, un risultato osservabile e un criterio di completamento.

## 6. Risultato raggiunto

Alla chiusura esistevano concretamente:

- una roadmap ordinata;
- un criterio di completamento per ogni fase;
- un metodo orientato a risultati verificabili;
- una classificazione iniziale della conoscenza;
- una regola per gestire deviazioni e lavoro futuro;
- responsabilità distinte degli strumenti;
- un progetto Linear utilizzabile;
- una disciplina iniziale per lavorare con Codex e versionare i risultati.

La milestone poteva quindi essere considerata conclusa: un nuovo lavoro poteva essere collocato nel percorso e descritto in termini di motivo, risultato e completamento.

## 7. Cosa non era stato ancora definito

Non appartenevano alla milestone:

- utenti concreti del primo Fold domestico;
- situazioni e problemi domestici specifici;
- modello Core/Dominio;
- architettura tecnica;
- flussi dell'applicazione;
- tecnologia;
- interfaccia;
- implementazione.

Questi elementi appartenevano al lavoro successivo e non devono essere retrodatati; l'elenco non implica che siano già stati tutti completati.

## 8. Cosa ha sbloccato

La milestone ha reso possibile affrontare ordinatamente la definizione del primo Fold domestico e, successivamente, la progettazione del MVP. Non risultava una dipendenza tecnica formale tra le milestone, ma roadmap e metodo fornivano il prerequisito organizzativo per collocare e chiudere il lavoro successivo.

## 9. Evoluzioni successive

### FOL-8 — Rapporto operativo tra Notion e Linear

Dopo la chiusura è stata formalizzata la regola:

> Notion conserva il ragionamento completo. Linear conserva la parte necessaria per governare il lavoro.

FOL-8 dichiarava esplicitamente di non riaprire la milestone 1.

### Target date successiva

La configurazione originaria di FOL-7 evitava deliberatamente le scadenze. La target date presente nel progetto Linear al momento della ricostruzione storica del 27 agosto 2026 è stata introdotta successivamente e la sua provenienza non è stata ancora chiarita.

### Diario e memoria del percorso

Sono stati introdotti successivamente un Diario di progetto e un registro dei passaggi significativi. La regola della sintesi di chiusura delle milestone è quindi posteriore alla prima milestone.

### Governance del repository

È stata poi stabilita una struttura versionata per distinguere documentazione canonica, decisioni, specifiche, ricerca e materiale storico, riducendo la dipendenza dalle conversazioni.

### Codex come ambiente principale

La direzione successiva è che Codex sostenga sia esplorazione sia implementazione. Repository e Linear devono contenere insieme il contesto sufficiente per continuare, mentre Notion resta attivo senza diventare una dipendenza operativa.

## 10. Limite emerso nell'uso reale

L'audit ha mostrato che la milestone aveva definito correttamente le responsabilità concettuali, ma non ancora gli eventi di aggiornamento della conoscenza.

In particolare mancavano regole operative sufficienti per:

- distinguere un'esplorazione effimera da un'intuizione da preservare;
- registrare un cambiamento progettuale significativo;
- verificare l'impatto sulle diverse fonti;
- chiudere una issue con risultato, verifica e artefatti;
- produrre una sintesi autosufficiente di milestone;
- impedire che lo stato operativo duplicato diventasse obsoleto.

Questo limite non invalida la chiusura storica della milestone: descrive ciò che il metodo ha dovuto imparare durante l'uso.

## 11. Metodo corrente

Il metodo consolidato ed evoluto è definito in [`../metodo-di-lavoro.md`](../metodo-di-lavoro.md). Quel documento rappresenta la regola corrente; questa sintesi conserva invece il problema, le decisioni e il risultato della milestone originaria.

## 12. Fonti operative collegate

- [FOL-5 — Definire la roadmap e le fasi del MVP](https://linear.app/folderapp/issue/FOL-5/definire-la-roadmap-e-le-fasi-del-mvp)
- [FOL-6 — Stabilire il metodo di lavoro e il ruolo degli strumenti](https://linear.app/folderapp/issue/FOL-6/stabilire-il-metodo-di-lavoro-e-il-ruolo-degli-strumenti)
- [FOL-7 — Configurare il progetto Fold — MVP domestico in Linear](https://linear.app/folderapp/issue/FOL-7/configurare-il-progetto-fold-mvp-domestico-in-linear)
- [FOL-8 — Definire come trasferire contenuti operativi tra Notion e Linear](https://linear.app/folderapp/issue/FOL-8/definire-come-trasferire-contenuti-operativi-tra-notion-e-linear), evoluzione successiva
