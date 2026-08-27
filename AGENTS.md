# Fold — istruzioni per gli agenti

**Status:** Canonical  
**Scope:** modalità di lavoro nel repository

## Regola fondamentale

Repository e Linear devono contenere insieme il contesto sufficiente perché Codex possa continuare Fold senza dipendere da Notion o da conversazioni precedenti.

- Il **repository** conserva la conoscenza versionata che deve guidare progettazione e implementazione.
- **Linear** conserva roadmap, issue, stato, dipendenze, checkpoint e avanzamento operativo.
- **Notion** è il luogo attualmente scelto per conservare ricerca estesa, intuizioni, percorso narrativo e materiale di case study; la sua indisponibilità non deve impedire a Fold di proseguire.

Non assumere di conoscere contenuti non ancora consultati e non ignorare le fonti collegate pertinenti: consulta esplicitamente il repository e, quando il lavoro appartiene a una issue o milestone, Linear secondo l'ordine di lettura seguente. Non presumere invece il contenuto di conversazioni o fonti non accessibili. Se un requisito necessario all'implementazione non è sufficientemente consolidato nel repository, non ricostruirlo per supposizione.

## Ordine di lettura

Prima di modificare Fold:

1. leggi `README.md`;
2. leggi `docs/README.md` per capire stato e ruolo dei documenti;
3. leggi `docs/metodo-di-lavoro.md` quando devi avviare, riprendere o chiudere un lavoro significativo;
4. leggi i documenti canonici pertinenti alla task in `docs/product/`, `docs/architecture/`, `docs/decisions/` e `docs/specs/`;
5. usa la ricerca in `docs/ricerca/` soltanto come evidenza o materiale di supporto, mai come requisito implicito;
6. se il lavoro appartiene a una issue o milestone, consulta in Linear descrizione, stato, dipendenze e checkpoint significativi. Se Linear non è accessibile, non inventare lo stato operativo mancante.

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
