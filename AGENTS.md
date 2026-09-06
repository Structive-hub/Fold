# Fold — istruzioni per gli agenti

**Status:** Canonical  
**Scope:** modalità di lavoro nel repository

Questo file definisce il comportamento richiesto agli agenti e indica gli entry point stabili da consultare. La mappa dettagliata e aggiornata degli artefatti, con il loro stato e la loro autorità, resta in `docs/README.md`; i documenti specifici conservano il contenuto effettivo.

## Regola fondamentale

Repository e Linear devono contenere insieme il contesto sufficiente perché Codex possa continuare Fold senza dipendere da Notion o da conversazioni precedenti.

- Il **repository** conserva la conoscenza versionata che deve guidare progettazione e implementazione.
- **Linear** conserva roadmap, issue, stato, dipendenze, checkpoint e avanzamento operativo.
- **Notion** è il luogo attualmente scelto per conservare ricerca estesa, intuizioni, percorso narrativo e materiale di case study; la sua indisponibilità non deve impedire a Fold di proseguire.

Non assumere di conoscere contenuti non ancora consultati e non ignorare le fonti collegate pertinenti: consulta esplicitamente il repository e, quando il lavoro appartiene a una issue o milestone, Linear secondo l'ordine di lettura seguente. Non presumere invece il contenuto di conversazioni o fonti non accessibili. Se un requisito necessario all'implementazione non è sufficientemente consolidato nel repository, non ricostruirlo per supposizione.

## Ordine di lettura

Prima di modificare Fold:

1. leggi `README.md` per l'orientamento generale e lo stato del progetto;
2. leggi `docs/README.md` per individuare il riferimento corrente dell'area, la mappa documentale e l'autorità degli artefatti;
3. leggi `docs/metodo-di-lavoro.md` quando devi avviare, riprendere o chiudere un lavoro significativo;
4. leggi i documenti canonici pertinenti alla task in `docs/product/`, `docs/decisions/` e `docs/specs/`; consulta `docs/architecture/` per il modello o l'architettura soltanto quando i documenti pertinenti risultano sufficientemente consolidati per l'uso richiesto;
5. usa `docs/ricerca/` per materiale `Research`, `Draft`, `Historical` o di supporto, mai come fonte automaticamente canonica; quando `docs/README.md` assegna esplicitamente a un artefatto di ricerca un ruolo corrente, consultalo entro quel ruolo e con l'autorità dichiarata;
6. se il lavoro appartiene a una issue o milestone, consulta in Linear descrizione, stato, dipendenze e checkpoint significativi. Se Linear non è accessibile, non inventare lo stato operativo mancante.

## AGENTS impact check

Ogni modifica significativa del repository deve includere un **AGENTS impact check**. Verifica se il cambiamento modifica il comportamento richiesto agli agenti, l'ordine di lettura, gli entry point, oppure l'autorità, lo stato o il ruolo delle fonti che gli agenti devono conoscere.

Se uno di questi aspetti cambia, `AGENTS.md` deve essere aggiornato nello stesso blocco coerente. Se non cambia, non modificare `AGENTS.md` per inerzia.

Il check è necessario almeno quando:

- nasce un nuovo entry point stabile;
- viene sostituito il riferimento corrente per un'area;
- cambia lo stato, l'autorità o il ruolo di una fonte che gli agenti devono conoscere;
- una fonte necessaria viene spostata;
- cambia l'ordine di lettura;
- cambia il metodo operativo;
- un riferimento presente in `AGENTS.md` diventa obsoleto.

Non richiede automaticamente una modifica di `AGENTS.md` la creazione di ogni file `Research`, di ogni Gate o di ogni documento aggiuntivo, né l'aggiunta di artefatti già correttamente raggiungibili attraverso `docs/README.md`.

## Stati della conoscenza

- **Canonical** — conoscenza sufficientemente consolidata per guidare direttamente il lavoro corrente;
- **Draft** — materiale in elaborazione che può sostenere esplorazione e progettazione in corso, ma non costituisce implicitamente un requisito implementativo;
- **Research** — evidenza o analisi; non è automaticamente una decisione di Fold;
- **Historical** — fotografia di una fase precedente;
- **Superseded** — sostituito da una decisione o documento più recente indicato esplicitamente.

Ciò che determina il comportamento da implementare deve essere sufficientemente consolidato nel repository. Non trasformare automaticamente Draft, ricerca, ipotesi o documenti storici in regole del prodotto.

## Persistenza dell'esplorazione

Non tutto ciò che emerge durante il lavoro deve diventare documentazione:

- un'esplorazione senza risultato persistente può restare nella conversazione;
- un'intuizione significativa va distillata nella memoria esplorativa attualmente adottata in Notion, chiaramente come ipotesi e senza modificare automaticamente roadmap o conoscenza canonica; se Notion non è disponibile, può essere differito soltanto il trasferimento in Notion: nel frattempo deve esistere nell'issue Linear pertinente il riferimento temporaneo definito in `docs/metodo-di-lavoro.md`, e il lavoro non deve bloccarsi;
- un cambiamento progettuale significativo richiede un checkpoint in Linear e una verifica d'impatto;
- una decisione o conoscenza necessaria a guidare Fold deve essere consolidata nel repository con lo stato appropriato.

Applica il ciclo completo definito in `docs/metodo-di-lavoro.md`.

## Quando le fonti sembrano divergere

Segui eventuali indicazioni esplicite `Supersedes` / `Superseded by` e le decisioni canoniche più recenti. Se una contraddizione non è risolta esplicitamente nel repository, non scegliere in silenzio una delle due interpretazioni: segnala il conflitto prima di basarvi l'implementazione.

## Regole di implementazione

- Implementa il perimetro corrente, non possibilità future non ancora acquisite dal progetto.
- Non introdurre tecnologie, componenti o astrazioni future solo per prepararle o escluderle.
- Non dedurre requisiti mancanti dalla struttura esistente del codice.
- Mantieni distinguibili decisioni di prodotto, decisioni architetturali e dettagli tecnici di implementazione.
- Prima di considerare una task conclusa, verifica i criteri di accettazione presenti nella relativa specifica.
- Non eseguire commit, push o creare branch salvo richiesta esplicita.

## Progettazione delle fondamenta

- In una normale task di implementazione segui soltanto il perimetro corrente e i requisiti consolidati; non introdurre pressioni future nel lavoro.
- Quando una task progetta esplicitamente fondamenta o contratti strutturali, distingui una futura funzione da una pressione fondazionale già autorizzata secondo la decisione pertinente.
- Usa una pressione fondazionale esclusivamente per falsificare assunzioni strutturali e individuare perdite semantiche concrete. Non implementare anticipatamente le capacità future analizzate e non ampliare implicitamente il perimetro corrente.

## Chiusura del lavoro

Non considerare conclusa una issue significativa soltanto perché la discussione o l'implementazione sono terminate. La chiusura deve rendere recuperabili in Linear almeno risultato, verifica, artefatti prodotti, fuori scope residuo, dipendenze aggiornate e lavoro sbloccato.

Alla chiusura di una milestone deve inoltre esistere in `docs/milestones/` una sintesi autosufficiente del percorso e del risultato, distinguendo le decisioni originarie dalle evoluzioni successive.

## Codex readiness gate

Una funzione è pronta per essere implementata quando il repository contiene abbastanza contesto per comprendere:

- cosa deve ottenere;
- perché esiste, quando questo influenza il comportamento;
- quali vincoli deve rispettare;
- cosa è fuori scope;
- come verificare che il risultato sia corretto.

Se queste informazioni mancano e sono necessarie per decidere il comportamento, il lavoro non è ancora pronto per l'implementazione.
