# Fold

**Status:** Active project

Fold viene sviluppato prima di tutto come prodotto realmente utile e funzionante. La prima realizzazione e il perimetro di implementazione corrente sono **Fold — MVP domestico**. Il MVP non è però il limite concettuale contro cui vengono validate le fondamenta del progetto: la distinzione è definita nella decisione [`0001 — Distinguere perimetro di implementazione e perimetro di validazione fondazionale`](docs/decisions/0001-perimetro-implementazione-validazione-fondazionale.md).

Questo repository contiene la memoria ufficiale e versionata di ciò che Fold consolida e costruisce: documentazione canonica, decisioni, specifiche, configurazioni e codice.

## Stato attuale del repository

Fold è ancora nella fase di progettazione del MVP domestico. La baseline concettuale v2.1 dell'anatomia è stata congelata come `Draft` per la successiva falsificazione: non è `Canonical`, non è ancora validata sui casi domestici o cross-domain e non autorizza implementazione. Non sono ancora stati scelti un'architettura tecnica di implementazione o uno stack applicativo.

Il passaggio successivo è FOL-37, la falsificazione domestica e cross-domain della baseline congelata.

Per lo stato corrente del lavoro concettuale e la mappa degli artefatti, consultare [`docs/README.md`](docs/README.md).

## Come orientarsi

- `AGENTS.md` — regole operative per Codex e altri agenti;
- `docs/README.md` — indice e regole della documentazione;
- `docs/product/` — perimetro e comportamento del prodotto consolidati;
- `docs/architecture/` — architettura concettuale e tecnica consolidata;
- `docs/decisions/` — decisioni importanti e loro motivazione;
- `docs/specs/` — specifiche pronte a guidare l'implementazione;
- `docs/ricerca/` — ricerca ed evidenze, non automaticamente canoniche.

Il file storico `docs/fondamenti-fold.md` appartiene alla prima fase di formalizzazione del progetto. Va letto secondo le indicazioni presenti in `docs/README.md`, perché alcune sue parti sono attualmente oggetto di nuova verifica progettuale.
