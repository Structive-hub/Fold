# Fold — Laboratorio UX v0.2

**Status: Draft — direzione UX proposta e verificata sul prototipo, 3 novembre 2026.**

Questo riferimento consolida i due pacchetti v0.1 forniti dall'utente e i tre concept successivi. Questi ultimi hanno priorità visiva, entro i vincoli espliciti della richiesta: superfici scure piatte, blu desaturato, stati qualificati e composizioni diverse secondo il compito. Non è una specifica tecnica del backend né una promozione della baseline v2.1.

## Prima integrazione nel runtime

Il 3 novembre 2026 l'utente ha autorizzato la prima integrazione limitata alle bollette elettriche realmente archiviate. Il risultato, le verifiche e i limiti sono nel README principale; le nuove catture `screenshots/runtime-*` riguardano l'app reale. La v0.2 resta invariata come riferimento comportamentale Draft. La direzione grafite della richiesta di integrazione prevale sui colori di questo prototipo. Non sono state integrate persone, beni, altre famiglie o funzioni simulate.

## Aprire e provare

Aprire con doppio clic **`reference/index.html`** in Edge, Chrome o Firefox. Non servono installazioni, Python, internet, build o account. Tutto funziona anche come file locale. Se si preferisce un server statico:

```powershell
python -m http.server 8767 --bind 127.0.0.1 --directory docs/ux/reference
```

Aprire `http://127.0.0.1:8767/`. È un prototipo separato dall'app sulla porta 8765. I dati sono fittizi e gli interventi si azzerano al ricaricamento.

Percorso consigliato:

1. Situazione → bolletta da chiarire → prova dell'importo.
2. Esplora → ricerca Enel → Da chiarire → Ordina Documento → Apri documento → Torna a Utenze. Ricerca, filtro, ordine, selezione e posizione vengono conservati nella sessione.
3. Chiudi l'anteprima e riaprila selezionando una riga. Memorizza una vista, modifica i filtri e richiamala: è solo memoria della prova.
4. Nel documento, simula una dichiarazione con una nota e controlla Cronologia. Il PDF non diventa prova di pagamento.
5. Acquisisci → confronta facsimile e letture → Collegamenti suggeriti → simula conferma oppure prosegui senza confermare.
6. Vista per bene → Casa di famiglia → Documenti → apri una bolletta → ritorna al bene. È la stessa fonte, non una copia in una nuova cartella.
7. Personalizza aree, prova ricerca globale (`/`), chiudi con `Esc`, ripeti dal telefono o restringendo la finestra. Ricarica per ripartire.

## Fonti e autorità

- `visual-references/concept-01..03.png`: tre concept recenti forniti dall'utente, prioritari per composizione e tono visivo; non sono screenshot del software.
- `visual-references/previous/`: dieci tavole del secondo ZIP, con il relativo LEGGIMI; riferimenti precedenti, ancora utili per comportamenti e motivazioni.
- `screenshots/*-wireframe.*`: wireframe del primo ZIP, mantenuti come materiale v0.1; non sono catture browser.
- `screenshots/*-desktop.jpg` e `*-mobile.jpg`: catture reali del prototipo v0.2. Le istruzioni, le differenze e i limiti sono qui e in `screen-notes.md`.
- `ux-principles.md`, `screen-notes.md`, `user-flows.md`, `acceptance.md`: decisioni di design, percorsi e verifica del solo riferimento Draft.

## Cosa abbiamo trovato e cosa cambia

Il runtime presenta una lista di bollette elettriche e il dettaglio con quattro schede di evidenza, correzione, dichiarazione e storico; la UI è chiara/verde. La vista attuale non contiene Situazione generale, tabella Utenze, gestione dei beni o collegamenti tra documenti.

Il pacchetto v0.1 offreva quattro viste scure e interazioni in memoria. Mancavano la quinta vista per bene, un ordinamento effettivo, viste richiamabili e la chiusura dell'anteprima. Alcuni comandi producevano solo messaggi. La qualifica verde «pagamento confermato manualmente» era ambigua rispetto alla natura della dichiarazione.

La v0.2 completa le cinque esperienze, aggiunge le interazioni sopra e distingue letture, interpretazioni, conferma del collegamento, situazione derivata e dichiarazione umana. Il pagamento dichiarato usa un tono neutro. Il verde rimane circoscritto alla conferma di un collegamento nella prova.

## Decisioni e differenze dai concept

| Riferimento | Scelta della v0.2 | Motivo |
| --- | --- | --- |
| Home ricca di contatori e notifiche | Situazioni in righe; accessi frequenti e prossima data come contesto | Orientare l'azione senza KPI o automazioni inventate |
| Blu intenso, gradienti e luci nei concept | Blu desaturato e superfici piatte, bordi sottili | La richiesta testuale prevale sugli effetti decorativi delle immagini |
| «Confermato», «in regola», «Verifica pagamento» | Qualifiche esplicite: letto, interpretato, dichiarato, non verificato | Una scadenza o un clic non attestano un pagamento né una regolarità complessiva |
| Suggerimenti 98% / 96% | Motivazione del collegamento (indirizzo demo compatibile), senza percentuale | Nessuna misura di confidenza è disponibile; decisione canonica 0002 |
| Numerose destinazioni sempre visibili | Cassettoni/schede scelti; ricerca e acquisizione stabili; bene come prospettiva | Contenere gerarchia e rumore senza spostare documenti |
| Acquisizione a quattro passi obbligati | Fonte e letture affiancate, verifica mirata, continuazione libera | Non richiedere una conferma di routine di tutti i dati |
| Tabella completa su ogni schermo | Tabella desktop; su mobile scorrimento locale, periodo omesso e anteprima sotto | Conservare confrontabilità senza allargare la pagina |
| PDF realistico | Facsimile dichiarato e frammento dimostrativo | Il prototipo non carica documenti né fornisce prove reali |

Componenti riutilizzabili: barra e navigazione, intestazione con ritorno contestuale, righe di situazione, toolbar filtri/ordinamento, tabella con pulsanti nativi, anteprima richiudibile, badge con testo e simbolo, dati con origine, fonte richiamabile, pulsanti di sezione, modali, messaggi e stato vuoto. Le cinque composizioni sono descritte in `screen-notes.md`.

## Supporto reale e simulazioni

| Capacità | Runtime attuale | Prototipo |
| --- | --- | --- |
| PDF elettrico con testo, conservazione originale, numero/POD/importo/scadenza, frammento/pagina | Implementato e testato | Facsimili e dati predisposti; nessuna estrazione |
| Correzione mirata e alternative, dichiarazione, storico, persistenza, duplicati, backup | Implementato e testato | Dichiarazione con nota in memoria; correzione non simulata; nessun salvataggio/backup |
| Situazione limitata alla bolletta | Implementata su richiesta della scheda | Home dimostrativa; nessuno scheduler |
| Filtri, ordinamento, viste, anteprima e ricerca globale | Da integrare | Funzionanti sul piccolo insieme fittizio, solo in memoria |
| Altre utenze, servizi/fornitori/periodi strutturati, cassettoni configurabili | Non implementati | Dati dimostrativi, senza classificazione |
| Beni, collegamenti suggeriti e confermati, attese, adattamento avanzato | Non implementati | Esempio Casa, attesa statica e visibilità configurabile; nessun algoritmo di priorità |

## Integrazione incrementale proposta

Solo dopo autorizzazione all'integrazione:

1. Portare palette, tipografia e componenti di base nella UI reale. Conservare caricamento, backup, token e API; eseguire i 19 test e la prova browser esistenti.
2. Ricomporre il dettaglio reale in sintesi, dati/provenienza e storico. Usare esclusivamente i quattro campi disponibili, includendo mancanti, alternative e correzioni; collegare alla vera fonte PDF, senza dipingere il facsimile sopra dati reali.
3. Aggiungere la lista operativa delle sole bollette elettriche, con filtro e ordine calcolati da dati realmente disponibili e ritorno al contesto. Non mostrare fornitore, servizio o periodo come estratti finché non lo sono.
4. Introdurre una Situazione fondata sulle regole già esistenti. Una home multi-area, attese e priorità autonome richiedono dati e regole ulteriori.
5. Valutare beni e collegamenti con una piccola implementazione dedicata; questa demo non autorizza nuove API, modello a grafo o mapping automatico.

## Verifica e limiti

Al successivo ricontrollo sono stati corretti il dettaglio del contratto (niente etichette di importo non pertinente), lo storico delle dichiarazioni iniziali e successive e la distinzione tra nuovo esempio gas acquisito e bolletta già archiviata. Il dettaglio è in `acceptance.md`.

Il resoconto puntuale è in `acceptance.md`. Il 3 novembre 2026 sono stati percorsi i flussi nel browser, verificate le cinque viste a 1440×900 e 390×844 e una larghezza intermedia di 1024px. Catture reali in `screenshots/`. Sono controllati filtri combinati, zero risultati, selezione via tastiera, chiusura pannelli/modali, ritorno al contesto, dichiarazione e reset al reload. I rapporti di contrasto delle dieci coppie testuali controllate sono almeno 6,12:1; non è una certificazione completa WCAG.

```powershell
node docs/ux/tools/smoke.mjs
node docs/ux/tools/check-contrast.mjs
```

Nessuna dipendenza nuova. Restano da verificare con utenti: densità con centinaia di documenti, nomi molto lunghi, zoom 200%, lettore di schermo e dispositivi fisici. L'iconografia è provvisoria; il prototipo non misura accuratezza estrattiva né validità dei collegamenti. Backend, API e modello dati sono invariati; nessun commit, push o merge per questo lavoro UX.
