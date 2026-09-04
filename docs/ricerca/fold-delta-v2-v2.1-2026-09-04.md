---
title: "Fold — delta congelato dalla candidata v2 alla futura v2.1"
status: Draft
date: 2026-09-04
scope: "Registro del delta concettuale autorizzato; non anatomia v2.1"
baseline_commit: "20ba8f053d7c6c1ee44d5571ef3ec2206d79a444"
decision_basis: "Mandato esplicito dell'utente del 2026-09-04; Knowledge / Decision Ledger e Coverage v2"
---

# Fold — delta v2 → v2.1

## 0 — Scopo, autorità e limiti

Questo documento congela **la destinazione delle conoscenze e delle critiche**, non applica i ripristini alla candidata. Stabilisce esattamente nove ripristini per la futura v2.1, due gruppi di conoscenza da mantenere intenzionalmente nel Ledger, sette questioni da portare aperte al test domestico e dieci tesi da non reintrodurre.

Non è la v2.1, non sostituisce alcun artefatto precedente e non autorizza implementazione, nuovi componenti, servizi, primitive, tecnologie, modifiche a Notion/Linear o operazioni Git di pubblicazione.

Lo stato documentale `Draft` significa che questo è un artefatto preparatorio della futura anatomia. **Il perimetro del delta è fissato dal mandato dell'utente**: non è una proposta di esplorazione libera. Né lo stato documentale né la scelta di ripristinare un contenuto cambiano lo stato genealogico dei suoi K-ID. In particolare, K-080 e K-023 restano CANDIDATA.

### 0.1 — Gerarchia delle fonti

1. [Knowledge / Decision Ledger](fold-knowledge-decision-ledger-2026-09-04.md): autorità genealogica primaria su formulazione acquisita, stato, origine e superamenti delle conoscenze.
2. [Coverage v2](fold-coverage-ledger-v2-2026-09-04.md): evidenza della presenza, perdita, compressione o alterazione nella candidata; contiene T01–T10.
3. [Snapshot v2](fold-anatomia-v2-snapshot-2026-09-04.md): usato qui per localizzare i futuri interventi e verificare i confini delle schede, non per annullare conoscenza del Ledger.
4. Review Claude/Codex/Claude: evidenza di stress. Serve a distinguere critiche mantenute, riformulate, ridimensionate e ritirate; **non può superare una voce STABILE senza una nuova decisione esplicita e motivata**.

La baseline versionata è il commit `20ba8f053d7c6c1ee44d5571ef3ec2206d79a444`, `docs: preserve Fold v2 knowledge baseline`. Nessun K-ID viene dichiarato superato da questo delta.

### 0.2 — Identificazione delle evidenze di stress

Le sigle S1/S2/S3 indicano documenti distinti, non tre autorità concorrenti.

| Fonte | Identificazione recuperabile | Uso nel delta |
|---|---|---|
| S1 — review iniziale Claude | Allegato `C:/Users/giuseppe/.codex/attachments/c04690d1-dfaf-4e98-ab25-c3df3013e90e/pasted-text.txt`; titolo «Review indipendente — Fold, candidata v2» | Individuare le tesi originarie F1–F8 e I1–I4, senza confonderle con il verdetto successivo. |
| S2 — contro-esame Codex | Sessione `01a05d0a-e483-7793-a648-e46306e04177`; risposta finale del 2026-09-03 alle 21:49:35.520 UTC; riga JSONL 1271 | Recuperare obiezioni, richiami genealogici, parti già coperte e residui aperti. |
| S3 — auto-stress finale Claude | Testo integrale fornito dall'utente nella risposta asincrona del 2026-09-03 alle 23:30:08.354 UTC; stessa sessione, riga JSONL 1750; corpo da «# Auto-stress della review» | Fonte della classificazione finale dei rilievi, dei ritiri e dei cinque top issue sopravvissuti. |

Per S2/S3 il file locale di provenienza è `C:/Users/giuseppe/.codex/sessions/2026/09/01/rollout-2026-09-01T14-56-30-01a05d0a-e483-7793-a648-e46306e04177.jsonl`. Le righe sopra sono **numerate da 1**, non sono gli ordinali usati altrove nel Ledger.

Impronte SHA-256 per riconoscere le fonti consultate:

- S1, byte del file allegato: `bbe88c1440cd7aa40b24affcee37a6cb150131fba4d7877a2b7656ef60a203ff`.
- S2, testo della risposta in UTF-8: `9a7c4c427969bd907283278c9556354999661a3589989001705ac3cb00b61939`.
- S3, solo corpo dell'auto-stress in UTF-8, esclusa la cornice della risposta utente: `780cf6c8a9acdf6326bcf4f5f8d9867e9bab2956172c50f6d7566b99d4c1bd83`.

La sezione F conserva in questo documento il contenuto classificatorio necessario: la futura integrazione non deve dipendere dal ricordo della conversazione.

### 0.3 — Convenzioni di lettura

- **Δ01–Δ09** identificano solo i ripristini autorizzati; **C01–C07** solo le questioni del test; **R01–R10** le tesi respinte della sezione D.
- **D06** resta il nome storico dell'apertura sulla formalizzazione non-Policy. Non coincide con **Δ06**, che riguarda continuità temporale e identitaria.
- I riferimenti A–P e H1–H22 nelle schede indicano le sezioni dello **snapshot v2**. Sono localizzazioni probabili, non testo già modificato né nuovi componenti.
- I K-ID di una questione aperta sono ancoraggi genealogici o vincoli già acquisiti: non significa che tutte quelle voci del Ledger diventino APERTA.
- «Da non reintrodurre» respinge la necessità o l'universalità della soluzione indicata, non vieta una futura scelta locale giustificata con una nuova decisione.
- Un criterio già acquisito ma compresso nella v2 è un **ripristino/regressione di consolidamento**, anche quando la review lo presenta come novità. Un criterio non acquisito rimane aperto: la review non lo delibera.

## A — Ripristini obbligatori della futura v2.1

I nove ripristini sono prescrizioni per la futura redazione. **Non sono già applicati**. Le formulazioni sotto preservano il significato delle voci indicate; le spiegazioni dei confini non aggiungono primitive o responsabilità.

### Δ01 — Attenzione temporale e base dell'attesa

**K-ID e genealogia**

| K-ID | Stato nel Ledger | Origine registrata nel Ledger |
|---|---|---|
| K-079 | STABILE | R3 §R3.6 e Delta §B.7 |
| K-080 | CANDIDATA | R3 §R3.7, Soluzione candidata E |
| K-081 | STABILE | R3 §R3.6–R3.7 e Delta §A.10/B.10 |

**Problema che il ripristino evita.** Una funzione promette attenzione autonoma ma il modello descrive solo reazioni a nuovi ingressi; oppure il Work viene usato come prova dell'attesa informativa o del mancato arrivo.

**Principio da preservare.** Distinguere base informativa dell'attesa, condizioni e finestra pertinenti, risultato del riscontro entro il perimetro esaminato e comportamento applicativo. Temporal Evaluation usa un reference time. La Function distingue risposta su richiesta da attenzione autonoma; quando promette quest'ultima, il coordinamento del Work autorizzato riconosce la condizione temporale e prosegue. Il Work conserva l'impegno e la prosecuzione operativa, non sostituisce base predittiva, obbligo descritto o risultato negativo. Base, condizioni e finestra devono restare recuperabili quando l'attesa viene riusata.

**Sezioni v2 probabilmente interessate.** D — percorsi che riaprono elaborazioni; F — esecuzione/attesa/ripresa; H10, H11, H17, H19; I — tempo e modalità; M.

**Cosa NON deriva dal ripristino.** Nessuna Expectation, Temporal Controller, Expectation Manager o Event temporale Core universali; nessun scheduler o algoritmo scelto; nessun alert obbligatorio per ogni scadenza. Il passaggio del tempo non crea di per sé una Source. Non segue che una previsione sia un obbligo o che il Work in attesa provi un'assenza nel mondo. K-080 rimane CANDIDATA quanto alla forma compositiva: il ripristino non la promuove a ontologia definitiva.

**Tracciabilità della classificazione.** Coverage T01; S1 F2 → S2 F2 → S3 F2a/F2b, §F.4. K-079/K-080/K-081 precedono la review: conferma di perdita/compressione della v2, non nuova scoperta. Il confronto previsione/riscontro resta C02.

### Δ02 — Recuperabilità delle basi materialmente usate

**K-ID e genealogia**

| K-ID | Stato nel Ledger | Origine registrata nel Ledger |
|---|---|---|
| K-075 | STABILE | R3 §R3.4, Che cosa produrre e che cosa conservare?; R4 §R4.8 |
| K-093 | STABILE | R3 §R3.9; R4 §R4.8 |
| K-109 | STABILE | R4 §R4.8 |

**Problema che il ripristino evita.** Una Decision o spiegazione storica dipende da una ricostruzione, proiezione o risultato intermedio di cui restano soltanto l'esito finale o il nome della versione usata.

**Principio da preservare.** Se un risultato contribuisce materialmente a una Decision o a una spiegazione storica, devono restare recuperabili il risultato pertinente e le basi effettivamente usate: premesse, criterio, riferimento temporale, contesto e limiti necessari. Per le risorse, il riferimento di versione deve consentire di recuperare la definizione o parte semanticamente pertinente, non solo un'etichetta. Il test di materialità è se il cambiamento di quella dipendenza potrebbe alterare significato, giustificazione/esito o la spiegazione della scelta fra alternative.

**Sezioni v2 probabilmente interessate.** G — risorse e responsabilità di conservazione; H11–H12, H17–H18, H20; H14/H16/H22 per i collegamenti alla Decision e al contesto dell'interazione.

**Cosa NON deriva dal ripristino.** Nessuna conservazione indiscriminata di calcoli, risorse o interazioni; nessun archivio autonomo per ciascun risultato; nessuna Admission automatica o trasformazione del risultato in Assertion, Source o Decision. Cambia l'obbligo di recuperabilità, non la natura informativa. Recuperare fedelmente non equivale a garantire riesecuzione identica.

**Tracciabilità della classificazione.** Coverage T02; S1 F6/I2 → S2 F6/I2 → S3 F6/I2, §F.3. K-003, K-027 e K-108 sono vincoli collegati, non nuovi ripristini.

### Δ03 — Impatto oltre le premesse positive

**K-ID e genealogia**

| K-ID | Stato nel Ledger | Origine registrata nel Ledger |
|---|---|---|
| K-085 | STABILE | R3 §R3.8 |
| K-086 | STABILE | R3 §R3.8 |

**Problema che il ripristino evita.** Una nuova informazione modifica il risultato di una ricerca negativa o di un'aggregazione, ma non compare nelle dipendenze positive conservate; il sistema conclude erroneamente che non vi sia impatto.

**Principio da preservare.** La valutazione d'impatto considera anche referente, ruolo, tempi, perimetro esaminato e presupposti di assenza, completezza o continuità materialmente usati. Una nuova informazione o un nuovo membro può incidere pur non figurando fra le premesse lette in passato. Dipendenza non trovata non dimostra assenza d'impatto: con basi insufficienti occorre ampliare il controllo pertinente o dichiarare indeterminatezza, senza presentare il risultato come aggiornato per sola assenza di collegamenti.

**Sezioni v2 probabilmente interessate.** G — Lineage e scope delle ricerche; H11–H13, H17; J — dipendenze e qualificazioni d'impatto.

**Cosa NON deriva dal ripristino.** Nessun grafo completo del mondo, rilevatore onnisciente, ricomputazione globale automatica o nuovo controller. Non si dichiara falso ogni risultato potenzialmente coinvolto, né si inventano le dipendenze mancanti.

**Tracciabilità della classificazione.** Coverage T03. Si ripristina il criterio del Ledger; la review è stress complementare e non la sua origine.

### Δ04 — Potenziale impatto, tenuta delle basi e risultato rivalutato

**K-ID e genealogia**

| K-ID | Stato nel Ledger | Origine registrata nel Ledger |
|---|---|---|
| K-087 | STABILE | R3 §R3.9, apertura e Cinque passaggi; R6 §V.9 |

**Problema che il ripristino evita.** Dipendere da una risorsa cambiata viene equiparato a una conclusione già ricalcolata e corretta; oppure, per non ricalcolare subito, viene nascosto ciò che è già noto sull'inadeguatezza delle basi.

**Principio da preservare.** Mantenere distinguibili il risultato storico, il potenziale coinvolgimento nel cambiamento, ciò che è noto o messo in dubbio sulla tenuta delle basi per un uso, l'avvenuta o mancata rivalutazione e il risultato effettivamente accertato: confermato o corretto. Il dubbio o l'inadeguatezza accertata di una premessa non determinano da soli il nuovo valore della conclusione. Il ripristino precisa i livelli di conoscenza sull'impatto senza indebolire K-161: un impatto già determinato resta recuperabile e vincola gli usi pertinenti anche se la rivalutazione viene rinviata.

**Sezioni v2 probabilmente interessate.** D — cambiamenti e rivalutazione; E — impatto epistemico e Policy; H12–H13; I — qualificazioni d'impatto; M.

**Cosa NON deriva dal ripristino.** Nessun asse o stato globale STALE, enum obbligatorio o nuova responsabilità; nessuna falsità automatica; nessun obbligo di ricalcolare tutto prima di riconoscere un problema delle basi. Non vengono decisi i criteri di inclusione/esclusione per ciascun uso: restano C03.

**Tracciabilità della classificazione.** Coverage T04; S1 I4 → S2 I4 → S3 I4, §F.2. K-088 e K-161 delimitano il ripristino; i criteri applicativi residui sono C03.

### Δ05 — Indipendenza non stabilita

**K-ID e genealogia**

| K-ID | Stato nel Ledger | Origine registrata nel Ledger |
|---|---|---|
| K-102 | STABILE | R4 §R4.5, Quality Assessment |

**Problema che il ripristino evita.** La mancanza di una dipendenza conosciuta viene trasformata in attestazione di indipendenza, oppure l'incertezza viene nascosta dietro il numero dei contributi.

**Principio da preservare.** Quando l'indipendenza rispetto al bersaglio non è stabilita, non può essere presunta. L'assessment può dichiarare indipendenza non determinata e i consumatori devono rispettare questa qualificazione senza contare automaticamente i contributi come corroborazione indipendente. Ciò non equivale a dichiararli certamente dipendenti o inutili. Rimangono validi recuperabilità delle origini/dipendenze note e divieto di auto-supporto.

**Sezioni v2 probabilmente interessate.** G — Provenance, Lineage e origini comuni; H7–H8, H12, H20; I — supporto e Quality; M.

**Cosa NON deriva dal ripristino.** Nessun enum a tre valori, primitiva Independence o controllore centrale obbligatorio. Non si richiede certezza su ogni origine reale e non si attribuisce alla Quality la scelta applicativa di prudenza, che resta distinta.

**Tracciabilità della classificazione.** Coverage T05; S1 F5/I1 → S2 F5/I1 → S3 F5/I1, §F.1. K-102 risolve la verifica genealogica richiesta da Claude: la distinzione era già STABILE. K-097/K-101/K-152 restano vincoli collegati; K-118 conserva aperti i criteri empirici, senza trasformarli in requisito nuovo.

### Δ06 — Continuità temporale e identitaria non automatica

**K-ID e genealogia**

| K-ID | Stato nel Ledger | Origine registrata nel Ledger |
|---|---|---|
| K-071 | STABILE | R3 §R3.2–R3.3 |
| K-138 | STABILE | R5 Identità e tempo |

**Problema che il ripristino evita.** Un periodo documentato viene esteso indefinitamente, o il cambiamento di fornitore/nome/identificatore viene interpretato automaticamente come nuova identità o identità invariata.

**Principio da preservare.** Assenza di fine dichiarata non prova durata infinita; un periodo documentato non costituisce necessariamente decorrenza continuativa. La ricostruzione rende espliciti criterio di continuità e limiti. Per l'identità, Domain determina quale soggetto è rappresentato — per esempio punto, rapporto o contratto — e le condizioni della sua continuità. Mutamenti descrittivi e assegnazioni identificative temporali non decidono da soli l'identità.

**Sezioni v2 probabilmente interessate.** G — Domain; H8, H10, H12; I — Referent, Identifier e tempo.

**Cosa NON deriva dal ripristino.** Nessuna regola universale di continuità, fusione o separazione; nessun nuovo tipo di entità; nessuna imposizione che ogni cambio fornitore crei o preservi il medesimo Referent. I criteri specifici non vengono definiti qui.

**Tracciabilità della classificazione.** Coverage T06; origine nei Round registrata nel Ledger, non nuova conclusione della review.

### Δ07 — Effetto già applicato e scope delle conferme

**K-ID e genealogia**

| K-ID | Stato nel Ledger | Origine registrata nel Ledger |
|---|---|---|
| K-018 | STABILE | R1 §R6; R3 §R3.10; R6 §III.11; AUDIT §28 |
| K-038 | STABILE | R2 §R2.5 |
| K-039 | STABILE | R2 §R2.5 |

**Problema che il ripristino evita.** Una disposizione viene riapplicata ignorando un effetto già prodotto; una conferma tardiva viene estesa al target modificato; una conferma del collegamento diventa supporto di tutti i dati mostrati.

**Principio da preservare.** Admission verifica condizioni e target pertinenti, autorità, invarianti ed effetto già applicato; restituisce un esito appropriato o la mancata applicazione senza inventare una nuova Disposition. Una risposta tardiva resta riferita a oggetto, aspetto, contenuto presentato, portata e natura dell'atto originari: nuovi elementi non ereditano la conferma. Una conferma abilitante può consentire un uso, ma non diventa supporto diretto di tutte le premesse utilizzate.

**Sezioni v2 probabilmente interessate.** E — applicabilità; F — verifica/ripresa; H15–H16, H19, H22; I/J — supporti e dipendenze d'uso.

**Cosa NON deriva dal ripristino.** Nessuna equivalenza applicabilità = nuova Decision; nessun protocollo tecnico di exactly-once; nessuna soluzione al controllo uniforme nei rami diversi da Admission o all'ownership non-Policy. C01 e C07 restano aperti; il controllo di applicabilità già acquisito non viene riaperto.

**Tracciabilità della classificazione.** Coverage T08; S1 F1 → S2 F1 → S3 F1, §F.5. Il nucleo acquisito si ripristina; il contratto uniforme residuo è C01. K-094 ammette anche applicabilità non determinabile: non si recepisce una riduzione obbligatoria a controllo binario.

### Δ08 — Persona rappresentata, attore e autorità concreta

**K-ID e genealogia**

| K-ID | Stato nel Ledger | Origine registrata nel Ledger |
|---|---|---|
| K-179 | STABILE | AUDIT §G, trasversali |

**Problema che il ripristino evita.** Riconoscere una persona o un account viene trattato come autorizzazione a vedere, confermare o applicare qualsiasi operazione sui soggetti riconciliati.

**Principio da preservare.** Persona rappresentata, account/attore e autorità concreta rispetto a target e azione sono distinguibili. La coreferenza e l'attendibilità di una fonte non attribuiscono da sole permessi. L'origine e la portata dell'autorità pertinente rimangono recuperabili nel contesto dell'azione.

**Sezioni v2 probabilmente interessate.** C — trasversali; G — accesso e sicurezza; E — autorità; H1, H15, H19, H22; richiamo in H8.

**Cosa NON deriva dal ripristino.** Nessun modello tecnico di autenticazione o autorizzazione, ruolo universale o nuova primitiva Actor; nessuna equiparazione fra account e Referent personale; nessuna assegnazione anticipata dell'ownership di D06.

**Tracciabilità della classificazione.** Coverage T10, parte K-179. Separata da Δ09 per non fondere autorizzazioni e recuperabilità.

### Δ09 — Retention, cancellazione e recupero dei legami

**K-ID e genealogia**

| K-ID | Stato nel Ledger | Origine registrata nel Ledger |
|---|---|---|
| K-180 | STABILE | AUDIT §G, trasversali |

**Problema che il ripristino evita.** Dopo una cancellazione o un ripristino dei soli file, Fold continua a mostrare la stessa verificabilità benché basi o relazioni necessarie non siano più disponibili.

**Principio da preservare.** Retention e cancellazione autorizzata possono ridurre la verificabilità: la conseguenza sulla base dei risultati deve restare riconoscibile. Recovery deve preservare o ristabilire, entro il materiale ancora legittimamente conservato, anche le relazioni necessarie alla comprensione e verifica dei risultati, non soltanto i file. Restano distinti autorizzazione alla conservazione e attendibilità epistemica.

**Sezioni v2 probabilmente interessate.** C — conservazione e trasversali; G — memorie e Provenance/Lineage; H4, H12, H17, H20; O — separazione dal futuro storage.

**Cosa NON deriva dal ripristino.** Nessun piano tecnico di backup, replica o disaster recovery; nessuna garanzia di recupero di dati legittimamente cancellati; nessuna retention illimitata. Il requisito di tracciabilità non autorizza a trattenere dati oltre i vincoli pertinenti.

**Tracciabilità della classificazione.** Coverage T10, parte K-180. K-027/K-108/K-167 e i limiti di K-127 impediscono conservazione indiscriminata.

## B — Conoscenze attive intenzionalmente fuori dall'anatomia v2.1

«Ledger-only» è una **destinazione documentale motivata**, non cancellazione, superamento o perdita di efficacia. Queste conoscenze continuano a vincolare il lavoro quando se ne affronta il problema. Non vengono duplicate nell'anatomia corrente soltanto per far salire la coverage.

### B01 — Lifecycle, calcolo, effetti e parallelizzabilità

**K-ID:** K-022 — STABILE; K-023 — CANDIDATA. **Origine:** R1 §R2/R8. **Coverage:** T07, entrambe assenti nella v2.

La conoscenza da conservare è precisa: lavori contemporaneamente aperti, elaborazioni simultanee e applicazioni indipendenti sono tre cose diverse. Una verifica in attesa non sta necessariamente calcolando; due calcoli distinti possono contendere lo stesso effetto. Il test candidato K-023 richiede prerequisiti disponibili, assenza di dipendenze necessarie, contesto identificabile e adeguato, compatibilità di effetti e invarianti, dichiarando se la parallelizzabilità riguarda soltanto il calcolo.

**Perché resta nel Ledger.** È un criterio per valutare una futura organizzazione dell'esecuzione e dei suoi effetti, non una responsabilità informativa aggiuntiva da descrivere ora nell'anatomia. La descrizione di Work, dipendenze e Application non deve assorbirne un secondo trattato sulla concorrenza. Il mandato attuale sceglie intenzionalmente di non duplicarlo.

**Limite dell'esclusione.** Non è lecito dedurre che due Work aperti siano indipendenti né che l'assenza di frecce autorizzi effetti simultanei. K-018 e Δ07 restano pertinenti all'applicazione. Non si promuove K-023 a regola implementativa definitiva e non si decide come eseguire in parallelo.

**Destinazione:** Ledger, K-022/K-023, con rinvio esplicito quando sarà affrontata la parallelizzabilità; nessun ripristino aggiuntivo nella v2.1.

### B02 — Governance fondazionale del cambiamento dei Core invariants

**K-ID:** K-091 — STABILE. **Origine:** R3 §R3.9, «Cambia un Core invariant». **Coverage:** T09.

Cambiare un Core invariant richiede una decisione fondazionale esplicita: individuare l'assunzione superata, le rappresentazioni coinvolte e l'informazione ancora recuperabile. Un numero di versione non ricrea distinzioni già perdute.

**Perché resta nel Ledger.** Riguarda la governance della progettazione e dell'evoluzione delle fondamenta. Non è il normale comportamento di ragionamento, né una scelta affidata alle Application Decision Policies. La futura anatomia deve rispettare gli invarianti in vigore; non deve duplicare al proprio interno la procedura con cui il progetto può deliberare di cambiarli.

**Limite dell'esclusione.** Non autorizza modifiche silenziose agli invarianti, retroattività automatica o loro trattamento come configurazioni applicative. Non dichiara superato K-091 e non demanda alla Policy la revisione delle fondamenta.

**Destinazione:** Ledger, K-091; eventuale futura decisione fondazionale esplicita, fuori dal delta corrente.

## C — Questioni aperte da portare al test domestico

Le sette schede seguenti **non contengono una soluzione deliberata**. I casi servono a rendere falsificabile la domanda; non introducono soglie, workflow, nuovi proprietari o rappresentazioni obbligatorie.

Ogni scheda separa ciò che il test deve chiarire da ciò che non può essere rimesso in discussione implicitamente. Non si trasforma un vincolo STABILE in un'ipotesi soltanto perché esiste un contratto ancora da precisare.

### C01 — Controllo uniforme di applicabilità nei rami Verification/Work/Application

**Stato:** APERTO PER IL TEST, senza soluzione adottata.

**K-ID pertinenti:** K-018, K-015, K-016, K-062, K-094.

**Domanda non risolta.** Come vengono resi espliciti e coerenti, nei diversi rami, controllore competente, input della verifica, esiti di non applicabilità/indeterminatezza e proprietario del seguito autorizzato?

**Vincoli già acquisiti da non riaprire.** Admission può già controllare l'applicabilità senza scegliere una nuova disposizione. Δ07 ne ripristina i limiti; non si riapre quel principio.

**Caso da portare al test.** Una verifica resta in attesa; un documento rende superata la domanda; l'utente risponde due settimane dopo nel contesto dell'interazione originaria.

**Localizzazione per la futura verifica.** E; F; H15–H16; H19.

**Evidenza di stress / genealogia.** S1 F1 → S2 F1 → S3 F1, §F.5: residuo di contratto, non prova dell'assenza di un decisore.

### C02 — Base predittiva dell'attesa e successivo riscontro negativo

**Stato:** APERTO PER IL TEST, senza soluzione adottata.

**K-ID pertinenti:** K-080, K-076, K-077, K-078, K-149.

**Domanda non risolta.** Quale rapporto sussiste fra base predittiva dell'attesa e successivo riscontro negativo, e con quali condizioni la prima viene prodotta, eventualmente ammessa e confrontata con il secondo, senza presumere che il mancato riscontro sia già una smentita?

**Vincoli già acquisiti da non riaprire.** Δ01 separa base, finestra, riscontro e comportamento; Derivation può prevedere e Query verificare. Non sono decisi forma universale dell'attesa, Admission obbligatoria o conflitto automatico fra previsione e ricerca negativa.

**Caso da portare al test.** Una periodicità inferita non riceve conferma nella finestra considerata.

**Localizzazione per la futura verifica.** D; F; H10–H11; H17; H19; I.

**Evidenza di stress / genealogia.** S1 F2 → S2 F2/F8 → S3 F2b, §F.4; quesito esplicito del mandato. S3 ritira F2c e la necessità di Expectation.

### C03 — Uso di contenuti ammessi ma impattati

**Stato:** APERTO PER IL TEST, senza soluzione adottata.

**K-ID pertinenti:** K-087, K-088, K-073, K-161.

**Domanda non risolta.** Quali condizioni del caso d'uso consentono inclusione qualificata, esclusione o richiesta di rivalutazione, e come distinguere uso storico da uso corrente?

**Vincoli già acquisiti da non riaprire.** L'impatto determinato non può essere occultato; Admission e utilizzabilità non coincidono. Δ04 conserva la graduazione senza scegliere una Policy universale.

**Caso da portare al test.** Una Query o azione usa un'Assertion ammessa, con basi materialmente affette e rivalutazione rinviata.

**Localizzazione per la futura verifica.** E; H12–H14; H18–H21.

**Evidenza di stress / genealogia.** S1 F3/I4 → S2 F3/I4 → S3 F3/I4. Il residuo sui criteri è aperto; l'asserita assenza di ogni obbligo minimo non prevale su K-161.

### C04 — Visibilità degli esiti parziali interni di Interpretation

**Stato:** APERTO PER IL TEST, senza soluzione adottata.

**K-ID pertinenti:** K-010, K-042, K-043, K-044, K-045, K-053, K-183.

**Domanda non risolta.** Quali risultati, dipendenze mancanti e incertezze delle capacità interne devono essere distinguibili dai consumatori nel caso domestico?

**Vincoli già acquisiti da non riaprire.** Esiti parziali e proposte sono già rappresentabili; la loro forma non impone scissione di H7 né classificazione completa obbligatoria.

**Caso da portare al test.** Classificazione irrisolta con proposta identificativa utilizzabile per una verifica; localizzazione della Source precedente alla composizione documentale.

**Localizzazione per la futura verifica.** D; H5–H7; I; O.

**Evidenza di stress / genealogia.** S1 F4 → S2 F4 → S3 F4: ritirati irrappresentabilità, argomento sul locator, attraversamento obbligatorio delle capacità e scissione necessaria.

### C05 — Corpus richiesto, accessibile, esaminato e copertura

**Stato:** APERTO PER IL TEST, senza soluzione adottata.

**K-ID pertinenti:** K-034, K-077, K-149, K-175.

**Domanda non risolta.** Come specificare e rendere riconoscibili corpus richiesto, materiale accessibile, materiale effettivamente esaminato e copertura/limiti del risultato negativo per la promessa della funzione?

**Vincoli già acquisiti da non riaprire.** Query produce già risultati negativi delimitati; non occorre dimostrare completezza del mondo per produrre una conclusione locale corretta.

**Caso da portare al test.** Nessuna conferma nella Knowledge, ma Source non interpretate o materiale non accessibile.

**Localizzazione per la futura verifica.** H17; G — scope; I — informazione negativa; H11.

**Evidenza di stress / genealogia.** S1 F8 → S2 F8 → S3 F8: ritirata la tesi che manchi il produttore.

### C06 — Criteri con cui Reconstruction considera proposte non ammesse

**Stato:** APERTO PER IL TEST, senza soluzione adottata.

**K-ID pertinenti:** K-003, K-052, K-073, K-134, K-136.

**Domanda non risolta.** Per quali scopi e con quali qualificazioni una proposta viene considerata, esclusa o ripresentata nella Reconstruction, senza confondere durata, pertinenza e commitment?

**Vincoli già acquisiti da non riaprire.** Una proposta può esistere senza Work o Admission; mostrarla o conservarla non la ammette. Non è già deciso un termine obbligatorio per ogni proposta.

**Caso da portare al test.** Più proposte irrisolte restano disponibili quando viene richiesta una ricostruzione corrente.

**Localizzazione per la futura verifica.** D; G; H12; H17–H21; I.

**Evidenza di stress / genealogia.** S1 F3/I3 → S2 F3/I3 → S3 I3: ritirati previsione quantitativa e termine obbligatorio.

### C07 — D06 — ownership della formalizzazione Decision/Disposition non-Policy

**Stato:** APERTO PER IL TEST, senza soluzione adottata.

**K-ID pertinenti:** K-185; genealogia K-017 SUPERATA; K-015, K-016, K-178.

**Domanda non risolta.** Quale responsabilità formalizza e registra la scelta deliberata nei singoli percorsi non-Policy, e con quale confine comune o locale?

**Vincoli già acquisiti da non riaprire.** Autorità, target, scope, contesto, Decision, Disposition e storia dell'Application sono già obbligatori. Nessuna assegnazione a Intake, Verification o Functions viene inventata qui.

**Caso da portare al test.** Un intervento umano contiene informazione e scelta autorizzativa da mantenere distinte.

**Localizzazione per la futura verifica.** E; G; H14; H22; N/O.

**Evidenza di stress / genealogia.** D06 già aperto nel Ledger e nella Coverage; S1 §H e S2 §4. S3 non lo chiude né fornisce una nuova assegnazione autorizzata.

## D — Tesi respinte / da non reintrodurre

Le dieci righe registrano le tesi respinte e preservano separatamente il problema valido eventualmente sottostante. Le etichette R01–R10 sono identificatori di questo registro, non componenti di Fold.

| ID | Tesi respinta | Motivo e K-ID pertinenti | Residuo valido e riscontro nella review |
|---|---|---|---|
| R01 | Applicabilità = nuova Decision | K-018/K-094 distinguono verifica delle condizioni già stabilite e scelta di un nuovo trattamento; K-015/K-016 distinguono Decision, Disposition e applicazione. Anche l'indeterminatezza è possibile: non ogni esito valutativo è una Decision di governance. | S3 F1 ritira la tesi; Δ07 ripristina i limiti acquisiti, C01 lascia aperto il contratto uniforme. |
| R02 | Expectation universale | K-080/K-081 e K-047 non dimostrano una nuova primitiva per distinguere base dell'attesa, riscontro e comportamento. | S3 F2b ritira la primitiva; Δ01 ripristina la composizione candidata e C02 conserva il confronto predittivo aperto. |
| R03 | Temporal Controller universale | K-079/K-081 assegnano l'attenzione promessa al comportamento della Function e alla prosecuzione del Work autorizzato senza imporre un nuovo controller. | S3 F2a ritira il nuovo componente e il carattere bloccante; Δ01 recupera la responsabilità già acquisita. |
| R04 | Asse universale Admission/Usability | K-003/K-052/K-073/K-136 consentono usi qualificati di materiale non ammesso; K-161 vincola l'uso pertinente di quello impattato. Un nuovo asse universale non è dimostrato. | S3 F3 ritira l'equivalenza fra ammesso e utilizzabile e la presunta falsità della definizione di Knowledge; restano C03/C06. |
| R05 | Scissione obbligatoria di H7 | K-010/K-043/K-053 ammettono risultati parziali e alternative; K-183 lascia aperta la granularità finale. Non deriva l'obbligo di dividere Interpretation. | S3 F4 ritira scissione, irrappresentabilità e argomenti su locator/attraversamento obbligatorio; C04 conserva la visibilità dei sub-risultati come quesito. |
| R06 | Controllore centrale dell'auto-supporto | K-021/K-152 mantengono gli obblighi dei produttori e la tracciabilità delle dipendenze; un controllo pertinente può consultare contesto più ampio senza diventare un nuovo controllore centrale. K-173 non impone un validatore universale. | S3 F5 ritira l'assenza di verificatore per i cicli. Il problema distinto dell'indipendenza non stabilita resta Δ05. |
| R07 | Enum obbligatorio per l'indipendenza | K-102 ammette l'indipendenza non determinata; K-047 separa distinzione necessaria da primitiva. K-118 lascia aperti i criteri empirici. | S3 F5/I1 ritira l'enum: Δ05 ripristina il principio, non un tipo o algoritmo. |
| R08 | Candidate universale | K-052 supera l'involucro Candidate obbligatorio; K-053/K-134 conservano proposte e risultati eterogenei. Recuperare un insieme di non ammessi non lo rende un tipo fondamentale. | S3 F7 ritirato interamente. C06 riguarda l'uso delle proposte, non la creazione di un nuovo contenitore ontologico. |
| R09 | Un risultato intermedio cambia natura perché sostiene una Decision | K-075/K-093/K-109 stabiliscono l'obbligo materiale di recuperabilità; K-003/K-108 preservano natura e differenza fra recuperare, spiegare e rieseguire. | S3 F6/I2 ritira il cambiamento di natura. Δ02 resta obbligatorio senza Admission o conversione in Assertion. |
| R10 | Assenza di un produttore del risultato negativo | K-034/K-149/K-175 attribuiscono alla Query recupero e risultato negativo delimitato; H17 ne è la localizzazione nella v2. | S3 F2c è ritirato; S3 F8 riconosce l'errore fattuale. C05 riguarda corpus e copertura, non l'invenzione del produttore. |

Non si sostituiscono questi rigetti con divieti più forti di quelli acquisiti. Per esempio, R07 non vieta di rappresentare esplicitamente l'incertezza; nega che un particolare enum sia obbligatorio. R05 non congela H7 per sempre; nega che la review abbia dimostrato una scissione necessaria.

## E — Criterio di accettazione della futura v2.1

La v2.1 **non deve massimizzare la coverage numerica**. Per ogni K-ID attivo deve essere documentabile almeno una destinazione motivata:

1. `rappresentato nella v2.1`, con localizzazione e verifica di fedeltà;
2. `intenzionalmente fuori dalla funzione dell'anatomia e coperto dal Ledger`, con motivo esplicito, senza perdita del vincolo;
3. `esplicitamente ancora aperto`, delimitando la domanda rispetto a ciò che è già acquisito;
4. `esplicitamente superato da una nuova decisione motivata`, con genealogia e sostituzione identificabili.

**Nessuna conoscenza può semplicemente scomparire.**

### E.1 — Stato e collocazione non sono la stessa cosa

La baseline del Ledger distingue 146 STABILE, 15 CANDIDATA, 14 APERTA e 13 SUPERATA. Le 161 voci STABILE/CANDIDATA costituiscono la coverage forward della baseline: le CANDIDATA non diventano STABILE perché rappresentate, e le STABILE non diventano aperte per una formulazione più debole nella review.

Le 14 aperture e la genealogia delle 13 voci superate restano anch'esse recuperabili. Il criterio sulle voci attive non è un permesso di eliminarle. In particolare:

- K-080 rimane CANDIDATA anche dentro Δ01.
- K-023 rimane CANDIDATA e attiva anche fuori dall'anatomia.
- K-185 resta APERTA; K-017 resta SUPERATA da K-185. Non si cancella la proposta storica K-017 né la si presenta come assegnazione completa ancora vigente.
- K-161 resta STABILE: i criteri d'uso specifici possono essere aperti, il divieto di occultare un impatto determinato no.
- K-118 resta APERTA: Δ05 non inventa i criteri empirici dell'indipendenza.

### E.2 — Perimetro congelato e assenza di riscritture implicite

La futura integrazione deve applicare **solo i nove ripristini della sezione A**, rendere riconoscibile l'esclusione motivata della sezione B, conservare gli aperti e non reintrodurre le tesi della sezione D. Non è autorizzata una riscomposizione generale dell'anatomia.

I recuperi D01–D05 già presenti nella v2 — base umana, divieto di auto-supporto, origine comune, nuova base per gli assessment e reversibilità della coreferenza — vanno preservati, non riaperti o riscritti come nuove conquiste. D06 rimane aperto.

Questo delta **non riclassifica automaticamente tutti gli altri K-ID** e non costituisce una nuova Coverage Map. Le restanti righe della Coverage precedente conservano il proprio valore, comprese parzialità e scelte di assemblaggio già segnalate. Non menzionare una voce qui non la rende né scartabile né implicitamente risolta; l'audit per-K della futura v2.1 deve darle una destinazione secondo il criterio sopra.

Se quell'audit richiederà modifiche ulteriori ai nove ripristini, dovrà renderle esplicite e motivate prima di estendere il delta. Non è consentito trasformare ogni parzialità numerica in una nuova modifica obbligatoria.

### E.3 — Regole della successiva verifica

Per ciascun ripristino, la verifica futura dovrà dimostrare sia il recupero positivo del principio sia il rispetto del relativo «NON deriva». Non basterà aggiungere il nome di una distinzione.

Per ciascuna apertura dovranno restare visibili domanda, vincoli acquisiti ed eventuale nuova decisione successiva; per ciascuna esclusione, motivo e collocazione nel Ledger. Una critica ritirata non potrà tornare come requisito tramite una diversa etichetta.

Il completamento di questo documento **non dichiara eseguiti i ripristini, superato un nuovo gate o pronto il prototipo per l'implementazione**. Il perimetro e le promesse del test domestico non vengono decisi qui.

## F — Verifica di copertura del delta e dello stress

### F.1 — Destinazione completa di T01–T10

| Tema della Coverage | Destinazione | K-ID | Stato nel delta |
|---|---|---|---|
| T01 — Attenzione temporale e basi delle attese | A / Δ01; C02 per il rapporto predizione-riscontro ancora aperto | K-079, K-080, K-081 | Ripristino obbligatorio; K-080 resta CANDIDATA |
| T02 — Criterio della conservazione obbligatoria | A / Δ02 | K-075, K-093, K-109 | Ripristino obbligatorio |
| T03 — Impatto oltre le premesse positive | A / Δ03 | K-085, K-086 | Ripristino obbligatorio |
| T04 — Impatto potenziale e rivalutazione effettiva | A / Δ04; C03 per i criteri d'uso specifici | K-087; vincoli K-088, K-161 | Ripristino obbligatorio; criteri specifici aperti |
| T05 — Indipendenza non determinata | A / Δ05 | K-102 | Ripristino obbligatorio, non nuova scoperta |
| T06 — Continuità temporale e identitaria | A / Δ06 | K-071, K-138 | Ripristino obbligatorio |
| T07 — Lifecycle, calcolo, effetti e parallelizzabilità | B / B01 | K-022, K-023 | Ledger-only attivo; K-023 resta CANDIDATA |
| T08 — Limiti di applicazioni e conferme | A / Δ07; C01 per il contratto uniforme | K-018, K-038, K-039 | Ripristino obbligatorio; contratto residuo aperto |
| T09 — Governance del cambiamento dei Core invariants | B / B02 | K-091 | Ledger-only attivo, fuori dalla funzione dell'anatomia |
| T10 — Autorità e conservazione oltre i nomi delle trasversali | A / Δ08 e Δ09 | K-179, K-180 | Due ripristini obbligatori distinti |

**Esito: 10/10 temi hanno una destinazione esplicita.** Non sono dieci ripristini: T07/T09 restano nel Ledger; T10 si separa nei due problemi già distinti K-179/K-180.

### F.2 — Registro finale dei rilievi Claude

La colonna «Esito S3» riferisce la posizione finale del revisore, non cambia lo stato dei K-ID. La colonna successiva applica la gerarchia delle fonti e distingue un ripristino da una questione non ancora decisa.

| Rilievo | Esito S3: parte mantenuta e parte ritirata | Classificazione e destinazione del delta | Ancoraggi K-ID |
|---|---|---|---|
| F1 | Ridimensionato a contratto uniforme; ritirati seconda Decision, impossibilità di controllo per H16 e assenza generale di destinatario dell'esito negativo. | Il controllo Admission è già acquisito. Δ07 ripristina i limiti; C01 mantiene aperti i contratti degli altri rami; R01 respinge l'equivoco. Nessun nuovo proprietario deliberato. | K-018, K-038, K-039, K-094; K-015, K-016, K-062 |
| F2a | Mantenuto/riformulato come condizione temporale non esplicitata; ritirati nuovo componente e carattere bloccante. | Regressione di consolidamento verificata dal Ledger e da T01, non nuova responsabilità scoperta nella review. Δ01; R03. | K-079, K-080, K-081 |
| F2b | Mantenuto e ristretto al rapporto fra base predittiva e riscontro; ritirata la primitiva Expectation. | Due destinazioni: Δ01 recupera la separazione già candidata; C02 resta realmente aperto sul confronto e sul trattamento. Non si decide che ogni attesa sia un'Assertion ammessa né che ogni mancato riscontro sia un conflitto. R02. | K-080, K-076, K-077, K-078, K-149 |
| F2c | Ritirato interamente: risultato negativo delimitato e H17 già presenti. | Tesi già coperta/errore di lettura; R10. Nessun ripristino del produttore. | K-034, K-149, K-175 |
| F2d | Ridimensionato: resta non esplicitato chi rende disponibile un cambiamento di versione; ritirata la diagnosi di buco privo di soluzione. | **Residuo di contratto aperto, conservato in questa riga e nella nota F2d sotto.** Raccordo con le aperture sulle attivazioni e sui cambiamenti delle risorse; fuori dai nove ripristini. Non si adotta come decisione la soluzione suggerita in S2/S3. | K-006 CANDIDATA; K-090 STABILE; K-096 APERTA — ancoraggi, non assegnazione già decisa |
| F3 | Ritirato come failure strutturale; restano criteri d'uso di contenuti ammessi/impattati. Ritirate equivalenza ammesso-utilizzabile e falsa definizione di Knowledge. | C03 conserva il residuo specifico; R04 respinge l'asse universale; Δ04 recupera i livelli d'impatto. L'eventuale lettura «si può ignorare un impatto determinato» è già esclusa da K-161, non è un'alternativa da lasciare aperta. | K-003, K-073, K-087, K-088, K-136, K-161 |
| F4 | Ridimensionato alla visibilità di sub-risultati; ritirati irrappresentabilità, scissione di H7, obiezione sul locator e attraversamento obbligatorio delle capacità. | C04 resta aperto. R05 respinge la scissione necessaria; non si riapre la possibilità già acquisita di risultati parziali. | K-010, K-043, K-053, K-057, K-183 |
| F5 | Mantenuto/riformulato per indipendenza non stabilita; ritirati assenza di verificatore dei cicli, enum e unificazione di auto-supporto/falsa indipendenza. | Δ05 recupera K-102; R06/R07 preservano i rigetti. I criteri empirici restano aperti in K-118: non si confonde il divieto di presumere indipendenza con un algoritmo generale per provarla. | K-021, K-097, K-101, K-102, K-118, K-152 |
| F6 | Mantenuto il criterio di recuperabilità materiale; ritirato il cambiamento di natura. | Regressione della v2: Δ02. R09 respinge la promozione ontologica e la conservazione indiscriminata. | K-075, K-093, K-109; K-003, K-108 |
| F7 | Ritirato interamente. | R08: insieme recuperabile di non ammessi non implica Candidate universale. Nessun problema aggiuntivo di tipo fondamentale. | K-052, K-053, K-134 |
| F8 | Ridimensionato a corpus richiesto/accessibile/esaminato/copertura; ritirata l'assenza del produttore, riconosciuta come errore fattuale. | C05 mantiene il quesito di contratto; R10 conserva il rigetto. Il risultato negativo locale è già acquisito. | K-034, K-077, K-149, K-175 |
| I1 | Mantenuto il bisogno della distinzione; ritirata la pretesa di novità, subordinata a verifica storica. | Verifica genealogica conclusa: K-102 è STABILE da R4 §R4.5, T05 ne registra la perdita. Stessa destinazione di F5: Δ05, non una seconda scoperta o un decimo ripristino. | K-102; K-118 |
| I2 | Ritirata la formulazione «cambia natura»; la parte valida coincide con F6. | Δ02/R09, senza duplicare il rilievo né creare un risultato di nuova natura. | K-075, K-093, K-109 |
| I3 | Mantenuto/riformulato sui criteri per considerare proposte; ritirati previsione quantitativa e termine necessario. | C06 resta aperto. Recuperabilità e durata non sono né Admission né criterio sufficiente di inclusione in una Reconstruction. | K-003, K-052, K-073, K-134, K-136 |
| I4 | Mantenuta la distinzione dei livelli; ritirata la circolarità e la necessità di ricalcolare sempre per riconoscere impatto. | Regressione di consolidamento: Δ04; C03 conserva la scelta dei trattamenti per uso. Non si trasforma il problema in STALE globale. | K-087, K-088, K-161 |

**Nota F2d — destinazione senza soluzione implicita.** Questo residuo è tracciato qui come contratto da precisare nel lavoro futuro sulle attivazioni/cambiamenti di risorse, coerentemente con la scelta ancora aperta di eventi e comunicazioni in K-006 e con il contesto K-090/K-096. Non si afferma che questi K-ID assegnino già un produttore preciso: sono gli ancoraggi del problema, non la sua soluzione. La proposta «l'attività che modifica o rende applicabile la risorsa produce la traccia» resta una proposta emersa nello stress, **non adottata**. F2d non aggiunge una C08 ai sette quesiti richiesti, non viene occultato e non amplia i nove ripristini.

Altri ritiri di S3 non vengono conteggiati come nuovi problemi: l'assenza del Candidate Validator non aggrava automaticamente F1 (K-173); il Work che attende non asserisce un'assenza nel mondo (K-079/K-080); la segmentazione documentale non rende invalido un locator sulla rappresentazione (K-057). La sezione originaria «Responsibility gaps» ripeteva rilievi già contati: non moltiplica le destinazioni. Il criterio metodologico ritirato da Claude — «aggiunta locale ⇒ non strutturale» — non viene assunto come regola di Fold.

### F.3 — Tutti i top issue effettivamente sopravvissuti

L'elenco è quello di **S3 §F**, non quello della review iniziale.

| Top issue S3 | Destinazione | K-ID | Stato e confine |
|---|---|---|---|
| 1 — Indipendenza epistemica, F5/I1 | Δ05; R06/R07; apertura già conservata in K-118 | K-102; K-101, K-118, K-152 | Ripristino prima della futura integrazione; nessun enum o criterio empirico inventato |
| 2 — Potenziale impatto, basi in dubbio e risultato accertato, I4 | Δ04; C03 per i criteri d'uso | K-087; K-088, K-161 | Ripristino dei livelli; uso specifico ancora aperto, non il vincolo minimo |
| 3 — Recuperabilità dei risultati usati per decidere, F6 | Δ02; R09 | K-075, K-093, K-109 | Ripristino obbligatorio; nessuna mutazione di natura |
| 4 — Attivazione temporale F2a e previsione/riscontro F2b | Δ01 per base e attenzione; C02 per confronto; R02/R03 | K-079, K-080, K-081; K-076, K-077, K-078, K-149 | Ripristino del nucleo; residuo predittivo realmente aperto |
| 5 — Applicabilità uniforme nei rami, F1 | Δ07 per i limiti acquisiti; C01 per il contratto; R01 | K-018, K-038, K-039, K-094 | Nucleo da ripristinare; contratto da portare al test |

**Esito: 5/5 top issue hanno destinazione; F2a e F2b sono distinti, come F5 e il problema del ciclo di auto-supporto.** I3, F4, F8 e F2d, esplicitamente esterni ai primi cinque in S3, sono comunque tracciati in F.2.

### F.4 — Cautele di lettura del verdetto finale

S3 conclude «CANDIDATA COERENTE CON PROBLEMI NON BLOCCANTI», distingue gravità concettuale e gate e mantiene le etichette «strutturale» per F5/I1, I4 e F2b. Queste sono **classificazioni del revisore**: qui non diventano tre nuove decisioni progettuali. Le destinazioni derivano dal Ledger e dal mandato.

Due disallineamenti interni a S3 non vanno propagati:

- La matrice §A formula F1 anche come mancanza di proprietario non-Admission; la discussione §B/§D conclude invece per un contratto locale non uniforme. Il residuo registrato è C01: nessuna assenza generale di owner viene assunta come fatto acquisito.
- La matrice §A mette F2b fra i rilievi da chiudere prima del test; la successiva §F.4 precisa che il prerequisito minimo è F2a e che F2b può restare aperto se il prototipo non promette attenzione autonoma. Si registra la precisazione finale, senza decidere qui quali promesse farà il prototipo. Il mandato mantiene C02 aperto.

Due ulteriori confini dipendono dall'autorità genealogica, non da una scelta silenziosa fra revisori:

- **K-161:** il fatto che i criteri specifici siano aperti non autorizza a ignorare un impatto determinato. S3 F3 non può riaprire questo vincolo STABILE.
- **K-102/K-118:** è già acquisito non inventare indipendenza quando non è determinata; non è acquisito un algoritmo generale che la dimostri in tutti i casi. Il ripristino e l'apertura non si sostituiscono l'uno all'altra.

## G — Controlli conclusivi e integrità del perimetro

### G.1 — Checklist del documento

| Controllo | Riscontro |
|---|---|
| Tutti i T01–T10 hanno destinazione | F.1: dieci righe, nessun tema escluso tacitamente |
| Tutti i top issue di S3 hanno destinazione | F.3: cinque gruppi; scorporo F2a/F2b esplicito |
| Anche i rilievi sopravvissuti fuori dai top cinque sono tracciati | F.2: I3, F4, F8, F2d; nessuna soluzione promossa automaticamente |
| Ripristini esattamente quelli richiesti | A: Δ01–Δ09, con i K-ID del mandato; T07/T09 in B, non ulteriori ripristini |
| Aperture non trasformate in decisioni | C01–C07 restano domande; K-118 e F2d mantengono i propri residui; D06 non assegnato |
| Nessuna nuova primitiva o responsabilità | Le localizzazioni usano solo sezioni/ruoli esistenti; R01–R10 e i «NON deriva» impediscono le promozioni indebite |
| Gerarchia rispettata | K-080/K-023 non promossi; K-102/K-161 non indeboliti; K-185 non chiuso; nessun K-ID superato qui |
| Nessuna v2.1 anticipata | Documento di delta, non riscrittura dell'anatomia o dei contratti |
| Nessuna estensione tecnologica | Nessun servizio, database, API, policy engine, scheduler o backup tecnico progettato |

### G.2 — Baseline da mantenere invariata

Le impronte seguenti identificano i tre file precedenti, **byte per byte**; sono distinte dall'impronta del solo corpo storico presente nei metadati dello snapshot.

| File precedente | SHA-256 |
|---|---|
| `fold-anatomia-v2-snapshot-2026-09-04.md` | `3e517fee286bf727aa927e5d368863194c578d4746af3cb93a41afef9ab74f72` |
| `fold-knowledge-decision-ledger-2026-09-04.md` | `fff10fdb54ae444feef27d15a8fa876bdcfa8a1055aad95a2001d9782801b354f` |
| `fold-coverage-ledger-v2-2026-09-04.md` | `9bfb8afd4dfb09110c47f749d33a54d23782a3617bbf48fd058e255389331bda` |

L'unica aggiunta autorizzata da questo lavoro è `docs/ricerca/fold-delta-v2-v2.1-2026-09-04.md`. Snapshot, Ledger, Coverage, candidata v2 e altri file precedenti restano invariati; nessun aggiornamento a Notion o Linear e nessun commit, push o branch fanno parte di questa operazione.

**Conclusione:** è congelato il perimetro del delta da applicare in futuro, non sono chiuse le questioni che il documento mantiene aperte.
