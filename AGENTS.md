# Fold — istruzioni per gli agenti

**Status:** Canonical  
**Scope:** modalità di lavoro nel repository

## Regola fondamentale

Il repository è la fonte operativa e versionata per chi implementa Fold.

Non assumere di conoscere conversazioni avvenute in ChatGPT, Codex, Notion, Linear o altri strumenti. Se un requisito necessario all'implementazione non è presente nel repository, non ricostruirlo per supposizione.

## Ordine di lettura

Prima di modificare Fold:

1. leggi `README.md`;
2. leggi `docs/README.md` per capire stato e ruolo dei documenti;
3. leggi i documenti canonici pertinenti alla task in `docs/product/`, `docs/architecture/`, `docs/decisions/` e `docs/specs/`;
4. usa la ricerca in `docs/ricerca/` soltanto come evidenza o materiale di supporto, mai come requisito implicito.

## Stati della conoscenza

- **Canonical** — può guidare direttamente il lavoro corrente;
- **Draft** — materiale in elaborazione, non ancora vincolante;
- **Research** — evidenza o analisi; non è automaticamente una decisione di Fold;
- **Historical** — fotografia di una fase precedente;
- **Superseded** — sostituito da una decisione o documento più recente indicato esplicitamente.

Non trasformare automaticamente ricerca, ipotesi o documenti storici in regole del prodotto.

## Quando le fonti sembrano divergere

Segui eventuali indicazioni esplicite `Supersedes` / `Superseded by` e le decisioni canoniche più recenti. Se una contraddizione non è risolta esplicitamente nel repository, non scegliere in silenzio una delle due interpretazioni: segnala il conflitto prima di basarvi l'implementazione.

## Regole di implementazione

- Implementa il perimetro corrente, non possibilità future non ancora acquisite dal progetto.
- Non introdurre tecnologie, componenti o astrazioni future solo per prepararle o escluderle.
- Non dedurre requisiti mancanti dalla struttura esistente del codice.
- Mantieni distinguibili decisioni di prodotto, decisioni architetturali e dettagli tecnici di implementazione.
- Prima di considerare una task conclusa, verifica i criteri di accettazione presenti nella relativa specifica.
- Non eseguire commit, push o creare branch salvo richiesta esplicita.

## Codex readiness gate

Una funzione è pronta per essere implementata quando il repository contiene abbastanza contesto per comprendere:

- cosa deve ottenere;
- perché esiste, quando questo influenza il comportamento;
- quali vincoli deve rispettare;
- cosa è fuori scope;
- come verificare che il risultato sia corretto.

Se queste informazioni mancano e sono necessarie per decidere il comportamento, il lavoro non è ancora pronto per l'implementazione.