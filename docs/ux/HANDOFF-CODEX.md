# Continuità del laboratorio UX

**Status: Draft · aggiornato il 3 novembre 2026.**

Il pacchetto v0.1 è stato importato e consolidato nel prototipo v0.2. Leggere `README.md`, `screen-notes.md`, `ux-principles.md`, `user-flows.md` e `acceptance.md` di questa cartella insieme alle istruzioni del repository.

- Entrypoint: `reference/index.html`; nessuna dipendenza o connessione alle API Fold.
- Il runtime è ancora la prima slice locale elettrica. Non estenderne il modello o le capacità sulla sola base dei mockup.
- I tre concept recenti sono in `visual-references/`; le tavole precedenti e i wireframe restano riferimenti storici di design.
- Le catture JPG in `screenshots/` sono reali, desktop 1440×900 e mobile 390×844; i vecchi PNG/SVG denominati wireframe non lo sono.
- Per il prossimo passo seguire la proposta incrementale nel README UX e ottenere l'autorizzazione all'integrazione nel runtime.
- Non eseguire commit, push, merge o modifiche a backend/API/dati per questa task UX.
- AGENTS impact check eseguito: aggiunto l'entry point UX Draft in `AGENTS.md` e negli indici; nessuna promozione delle fonti o chiusura di issue/milestone.

Lo script `tools/capture_reference.py` è facoltativo, richiede Playwright installato a parte e non è stato usato in questa verifica. Le catture consegnate sono state prodotte con il browser integrato. Non installare Playwright solo per aprire il prototipo.
