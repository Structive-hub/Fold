# Fold — Principi UX e sistema compositivo

**Stato: Draft · Evidenza di design per la valutazione**

**Aggiornamento v0.2, 3 novembre 2026:** i principi di seguito restano validi. Il consolidamento e l'ordine delle fonti sono nel README UX; i tre concept recenti prevalgono visivamente sui vecchi wireframe, entro la richiesta testuale. Nessun gradiente o glow, anche se compare nei concept. `refinements.css` aumenta la leggibilità dei metadati e dei controlli, mantiene il pagamento dichiarato neutro e adatta le cinque composizioni; i colori testuali controllati superano 4,5:1. Il colore del testo secondario resta `#A4AFBB` anche nei metadati prima più deboli. Le icone tipografiche sono provvisorie e vanno sostituite con un unico set coerente durante l'integrazione autorizzata, senza aggiungere dipendenze per questa demo.

## Principio guida

**Contenuti adattivi, comportamenti prevedibili, profondità progressiva.**

Il sistema non ha un layout unico. Mantiene interazioni riconoscibili e seleziona la composizione in base all'attività: confrontare, esplorare, leggere, verificare, acquisire, ricostruire una situazione.

## Regole da conservare

1. **Configurazione pertinente**: gli ambiti e le schede visibili dipendono dai bisogni dell'utente; cambiare visibilità non sposta o cancella documenti. L'onboarding non deve essere una configurazione amministrativa estesa.
2. **Due livelli organizzativi**: cassettoni → schede → vista di consultazione, non un nuovo livello di cartelle; fornitori, periodi, beni e stati sono tag, filtri, riferimenti o prospettive.
3. **Coerenza delle azioni**: ricerca, acquisizione, orientamento, ritorno e accesso alle evidenze restano riconoscibili; non devono necessariamente occupare la stessa quantità di spazio su ogni viewport.
4. **Spazio secondo compito**: righe per elementi confrontabili, tabella per attributi ripetuti, colonne per originale + interpretazione, griglie per elementi di pari ruolo, pannelli per dettagli brevi, lettura estesa per documenti complessi. Non trasformare tutto in card grandi.
5. **Grado di attenzione proporzionato**: la Home privilegia situazioni concrete, non contatori astratti. Segnalazioni non importanti non devono affollare la parte centrale.
6. **Stati qualificati**: scadenza trascorsa ≠ mancato pagamento; dichiarazione utente ≠ verifica bancaria; assenza di fonte ≠ prova che l'evento non sia avvenuto. Lo stato deve essere spiegabile.
7. **Approfondimento fino alla prova**: per dati importanti si deve poter raggiungere fonte, pagina e frammento, distinguendo osservato, interpretato e confermato.
8. **Continuità**: ritorno alla lista con ricerca, filtri, ordinamento, selezione e posizione conservati, almeno all'interno dell'uso corrente. Il prototipo conserva alcuni stati in memoria.
9. **Accessibilità e leggibilità**: etichette e simboli oltre al colore; focus visibile, testo leggibile, tabella con alternative responsive e tastiera.
10. **Onestà del prototipo**: simulazioni evidenti, nessun salvataggio reale, nessuna apparenza di funzionalità backend non implementate.

## Palette scura candidata

| Ruolo | HEX | Uso |
| --- | --- | --- |
| Fondo | `#101317` | Superficie predominante |
| Navigazione | `#13171B` | Barra e menu |
| Superficie | `#191E24` | Contenitori occasionali |
| Superficie secondaria | `#20262E` | Selezioni e pannelli secondari |
| Bordo | `#303842` | Separazione senza ombre |
| Testo | `#E9EDF2` | Contenuto primario |
| Testo secondario | `#A4AFBB` | Metadati |
| Blu `#96BBEB` | Interazione, selezione, navigabilità e fonte richiamabile |
| Ambra `#DFB46E` | Attesa, scadenza o attenzione, con testo che specifica la natura |
| Verde `#8FC8AA` | Conferma circoscritta, senza estenderla ad altri fatti |
| Rosso `#E6A0A0` | Solo errori o condizioni che davvero lo giustificano |

**Da validare:** contrasto WCAG nelle coppie di testo, focus, differenziazione non cromatica e leggibilità con riduzione della vista.

## Anti-pattern da evitare

- Una sidebar con tutte le aree possibili accese sempre.
- Pagine costruite soltanto impilando card di uguale dimensione.
- Numeri di dashboard senza domanda operativa.
- Grandi vuoti decorativi o padding che moltiplica lo scroll.
- Pannelli di dettaglio permanenti quando non c'è selezione utile.
- Una tabella universale con gli stessi campi per sanità, beni e utenze.
- Pannelli collassati che occultano funzioni usate di frequente.
- Icone/colori privi di etichetta semantica per gli stati.
- Nodi relazionali trasformati in ulteriori cartelle gerarchiche.
- Copiare una disposizione dei wireframe senza comprendere la sua responsabilità.

## Criterio per scegliere la disposizione

1. Identificare la domanda a cui la schermata deve rispondere.
2. Determinare quali dati devono essere visti insieme.
3. Assegnare più superficie al compito dominante, meno ai metadati.
4. Presentare subito ciò che serve per agire; spostare gli approfondimenti nel contesto.
5. Verificare il comportamento quando il contenuto cresce e quando lo schermo si restringe.
6. Osservare errori reali invece di inferire il successo dalla sola estetica.
