# Verifica UX v0.2

**Status: Draft · evidenza di verifica del prototipo, 3 novembre 2026.**

## Controlli eseguiti

- [x] Cinque viste raggiungibili: Situazione, Utenze, Documento, Acquisizione e Casa di famiglia.
- [x] Runtime osservato nel browser sulla porta 8765 e confrontato con il prototipo isolato.
- [x] Utenze: ricerca + filtro, ordinamento, zero risultati spiegato, apertura e chiusura dell'anteprima.
- [x] Dettaglio → ritorno alla lista: ricerca Enel, filtro Da chiarire, ordine Documento e selezione conservati.
- [x] Vista salvata solo in memoria, richiamabile; nessuna persistenza dichiarata.
- [x] Evidenza apribile/chiudibile, frammento e pagina coerenti con il facsimile; nessuna prova di pagamento implicita.
- [x] Dichiarazione simulata con nota; qualifica neutra e evento in cronologia; originale ancora visibile.
- [x] Acquisizione con dati/collegamenti, conferma mirata, conclusione senza upload reale.
- [x] Bene → documento → ritorno al bene con sezione conservata.
- [x] Configurazione aree reversibile, ricerca globale e stato vuoto, chiusura modali con Esc, reset al reload.
- [x] Pulsante di selezione tabella attivato con Invio; controlli nativi etichettati e focus visibile.
- [x] Cinque viste a 1440×900 e 390×844, controllo intermedio 1024×768. Nessun overflow dell'intera pagina; tabella mobile con scorrimento locale.
- [x] Catture JPG reali desktop/mobile per tutte le viste, distinte dai vecchi wireframe.
- [x] Dieci coppie testo/fondo controllate da `check-contrast.mjs`: minimo 6,12:1, sopra 4,5:1. Controllo DOM dei colori effettivi su campioni di vista.
- [x] Sintassi JS e smoke delle cinque composizioni, filtri combinati, ordinamento, dichiarazione/storia, facsimile e assenza di chiamate API/storage.
- [x] Backend, API e modello dati invariati; nessun dato reale, commit/push/merge eseguito per questa task.

## Ricontrollo del 3 novembre 2026

Corrette e verificate in browser le etichette di contratto (riferimento, pagamento non applicabile), la presenza delle dichiarazioni iniziali nella cronologia e la conservazione di più dichiarazioni successive. L'acquisizione ora usa un nuovo esempio `DEMO-GAS-002`, distinto dalla bolletta gas archiviata. Rimossa la duplicazione «Casa e immobili» nella navigazione e mantenuto il focus sul comando di evidenza effettivamente premuto. Lo smoke include regressioni per contratto, cronologia multipla ed esempio di acquisizione.

## Ancora da verificare

Le dieci catture già consegnate documentano il primo passaggio visivo v0.2. Nel ricontrollo successivo il browser ha consentito navigazione e verifiche DOM ma ha restituito «Unable to capture screenshot» alle nuove catture, anche usando l'API alternativa. Le immagini precedenti non sono state presentate come nuove prove delle correzioni; il prototipo aggiornato è stato lasciato aperto nel browser della chat.

- [ ] Test con persone e corpus documentale autorizzato.
- [ ] Uso esteso con screen reader, zoom 200%, contrasto non testuale completo e tutti gli stati di hover/focus.
- [ ] Scala a centinaia di righe, testi lunghi, lingue diverse e dispositivi fisici.
- [ ] Nuova verifica completa dopo l'integrazione autorizzata nel runtime.

Non si dichiara conformità WCAG complessiva. Lo smoke con DOM simulato non è un test end-to-end: la prova browser sopra è separata.

## Gate per un'integrazione successiva

Non sono ancora approvati dall'esistenza della demo: email, OCR, scheduler, attese calcolate, suggerimenti automatici, riconciliazione bancaria, account/permessi, classificazione completa, persistenza per beni o persone. Prima dell'integrazione servono autorizzazione e scelta del piccolo passo. Conservare PDF originali, alternative, revisioni, contributi umani, controllo concorrenza, export/ripristino e protezioni HTTP; ripetere test Python e prova browser con dati sintetici.
