# Governare il confine Estrazione → Interpretazione senza anticipare strategie documentali

Status: Canonical
Date: 2026-09-07

## Contesto

Nel ragionamento sul mapping di documenti non strutturati sono emerse bollette di fornitori diversi, documenti antecedenti e successivi a discipline di standardizzazione del settore e cedolini con layout differenti.

La disponibilità di template reali rende possibile osservare differenze di lessico, impaginazione e struttura, ma non dimostra da sola quale strategia di estrazione o mapping debba adottare Fold.

Sono state considerate, come ipotesi, soluzioni quali:

- registry legati all'emittente;
- scelta del layout tramite P.IVA;
- profili documentali per famiglie di layout;
- mapping basato principalmente su etichette;
- uso di più segnali strutturali e normativi.

Nessuna di queste soluzioni viene adottata preventivamente.

## Decisione

Fold separa esplicitamente tre livelli di responsabilità:

1. **Estrazione:** osserva ciò che è presente nel documento e conserva la qualità tecnica della lettura.
2. **Interpretazione / Mapping:** stabilisce quale significato canonico possa essere attribuito alle osservazioni usando regole documentate e verificabili.
3. **Core:** rappresenta concetti trasversali come osservazioni, evidenze, provenienza, validità e stato epistemico senza conoscere regole specifiche di un settore o di un tipo documentale.

Da questa separazione seguono i principi seguenti.

### Autorevole non significa orizzontale

Una regola normativa o documentale può essere molto stabile, verificabile e autorevole senza appartenere al Core.

Conoscenze come pagina prescritta, sezione prevista, formato o struttura di un particolare tipo documentale appartengono al Domain e/o alle Mapping Definitions appropriate e devono poter essere versionate quando necessario.

Il Core non deve conoscere ARERA, cedolini, fornitori o altri dettagli specifici del dominio soltanto perché regolati da una norma.

### Extraction Quality ≠ semantic confidence

L'incertezza sulla lettura del segno e l'incertezza sul significato sono dimensioni differenti.

Un errore OCR, una stringa degradata o una relazione spaziale incerta descrivono la qualità dell'estrazione. La decisione che un'osservazione rappresenti, per esempio, un determinato campo canonico è invece una responsabilità di interpretazione.

Queste dimensioni non devono essere collassate in un unico punteggio globale dal quale derivi automaticamente una verità semantica.

### Accettazione semantica verificabile ed esplicabile

L'accettazione di un candidato semantico deve dipendere da regole verificabili ed esplicabili.

Non viene approvato un meccanismo del tipo:

```text
pagina 0.2
+ label 0.3
+ pattern 0.3
+ layout 0.2
= score 0.84
→ campo accettato
```

La qualità tecnica dei singoli segnali può essere misurata e conservata, ma la decisione semantica deve poter spiegare quali condizioni o alternative hanno giustificato l'accettazione.

Non viene fissata oggi una forma tecnica unica delle regole. Congiunzioni di predicati, alternative deterministiche o altre composizioni esplicite devono essere derivate dai casi reali e non assunte in anticipo.

### Nessun registry o profilo documentale approvato in anticipo

La presenza di layout differenti non dimostra che servano profili differenti.

Un registry per emittente o una scorciatoia P.IVA → layout non vengono adottati. La P.IVA identifica un soggetto quando pertinente; non è assunta come causa o identificatore stabile dell'impaginazione di un documento.

Anche il concetto di profilo documentale resta una possibile strategia futura, non una parte già approvata dell'architettura.

Prima bisogna osservare se layout differenti richiedano realmente strategie di mapping differenti.

### Saturazione osservata ≠ chiusura dimostrata

Un campione finito può mostrare che nuove varianti smettono temporaneamente di emergere, ma non dimostra che il vocabolario o la struttura possibili siano chiusi.

Le future misure devono quindi descrivere curve di nuove varianti osservate e stabilizzazione del campione, senza trasformarle in prova di completezza universale.

## Motivazione

Questa decisione preserva due obiettivi contemporaneamente:

- sfruttare struttura, lessico, vincoli normativi e pattern realmente utili dei documenti;
- evitare che Fold venga accoppiato prematuramente a layout, emittenti o strategie non dimostrate necessarie.

La separazione permette inoltre di distinguere chiaramente perché un dato è incerto: qualità tecnica dell'estrazione, insufficienza degli indizi semantici o entrambe, senza nasconderne l'origine dentro un unico score.

## Lavoro futuro approvato

Il lavoro futuro è registrato in Linear come **FOL-42 — Misurare la variabilità documentale al confine Estrazione → Interpretazione**.

Va ripreso dopo la definizione della slice finale del MVP, dentro il lavoro architetturale di FOL-39, soltanto se la slice richiede documenti non strutturati o capacità di mapping per cui la misura è necessaria.

La misura dovrà partire da documenti reali e distinguere almeno:

- invarianti del tipo documentale;
- vincoli normativi;
- variabilità lessicale;
- variabilità grafica;
- variabilità strutturale;
- casi non agganciabili con regole sufficientemente affidabili;
- eventuale necessità reale di strategie o profili specifici.

La raccolta deve preservare le osservazioni grezze prima della normalizzazione o categorizzazione.

## Cosa questa decisione non autorizza

Questa decisione non autorizza:

- analisi immediata dei template durante FOL-37;
- ampliamento del protocollo di falsificazione dell'anatomia;
- parser specifici per fornitore;
- registry per emittente;
- profili documentali automatici;
- mapping definitivo;
- soglie OCR definitive;
- un unico score di confidence usato come verità semantica;
- introduzione nel Core di conoscenza normativa o documentale specifica.

## Conseguenze

Da questo momento:

- Codex non deve assumere registry, profili o mapping per-emittente come architettura già decisa;
- le Mapping Definitions possono usare conoscenza di dominio autorevole senza trasformarla in invarianti del Core;
- qualità estrattiva e giudizio semantico devono restare distinguibili e tracciabili;
- l'eventuale strategia di mapping viene scelta dopo la misura della variabilità reale richiesta dalla slice;
- FOL-42 resta lavoro futuro e non devia FOL-37;
- i template disponibili sono materiale di osservazione futuro, non prova a favore di una soluzione già scelta.
