# Fold

**Status:** Active project

Fold viene sviluppato prima di tutto come prodotto realmente utile e funzionante. La prima realizzazione e il perimetro di implementazione corrente sono **Fold — MVP domestico**. Il MVP non è però il limite concettuale contro cui vengono validate le fondamenta del progetto: la distinzione è definita nella decisione [`0001 — Distinguere perimetro di implementazione e perimetro di validazione fondazionale`](docs/decisions/0001-perimetro-implementazione-validazione-fondazionale.md).

Questo repository contiene la memoria ufficiale e versionata di ciò che Fold consolida e costruisce: documentazione canonica, decisioni, specifiche, configurazioni e codice.

## Stato attuale del repository

Dal **2 novembre 2026** esiste una prima slice locale eseguibile: **bolletta elettrica PDF con testo → dati con evidenze → correzioni storicizzate → situazione di scadenza/pagamento spiegabile**. L'utente ha autorizzato esplicitamente l'avvio dell'implementazione e delegato le scelte tecniche necessarie a questa funzionalità.

Il codice è in `fold_app/`; le verifiche ripetibili sono in `tests/`. Sono realizzati caricamento, conservazione dei byte originali, lettura per pagina, proposte di quattro campi, gestione di alternative, verifica/correzione mirata, dichiarazione di pagamento, persistenza e copia esportabile/ripristinabile.

La baseline concettuale v2.1 resta **Draft** e congelata: questa implementazione limitata non la promuove, non conclude FOL-37 e non fissa l'architettura definitiva di Fold. Nessun documento reale è stato usato come dato di prova. La scelta dell'intero perimetro MVP e la falsificazione complessiva restano distinte dal risultato software qui disponibile.

## Riferimento UX separato

Dal 3 novembre 2026, [`docs/ux/README.md`](docs/ux/README.md) raccoglie la direzione UX/UI **Draft**, con cinque viste navigabili e dati fittizi. Aprire `docs/ux/reference/index.html` con un browser, senza installazioni. È un prototipo isolato: non modifica l'app funzionante, non importa documenti e non salva dati. Screenshot reali desktop/mobile e proposta di integrazione progressiva sono nella stessa cartella. L'integrazione nel runtime richiede una successiva autorizzazione.

## Prima integrazione UX nel runtime — 3 novembre 2026

L'app reale ora apre la lista delle **bollette elettriche archiviate**. Tema grafite piatto; righe per confrontare numero/file, POD, importo, scadenza, situazione e provenienza dei dati. Ricerca per numero, file, POD o importo; filtro per dati da chiarire, scadenza entro 30 giorni, scadenza superata e dichiarazioni di pagamento; ordinamento per acquisizione, scadenza, importo o numero.

Il dettaglio mostra subito importo, scadenza e situazione motivata. Ogni dato conserva origine, evidenza apribile, pagina/frammento e correzione mirata; dichiarazioni e cronologia rimangono distinte. **Torna alle bollette** e Indietro del browser ripristinano ricerca, filtro, ordine, selezione e posizione, recuperando i dati aggiornati. I criteri di consultazione restano anche al ricaricamento nella stessa sessione del browser; non sono viste salvate permanenti.

Sono usate esclusivamente le API già presenti. Nessuna migrazione o modifica a Core, regole elettriche, parser, salvataggi o protezioni HTTP. Nessun fornitore, periodo, persona o bene dedotto; nessuna demo inserita dalla UI. Eventuali esempi già archiviati dal backend sono etichettati come tali. La v0.2 in `docs/ux/` resta Draft e riferimento comportamentale: la sua palette e le funzioni simulate non sono il contratto del runtime.

**Prova personale:** avvia come sotto, cerca una bolletta, combina filtro e ordine, aprila, espandi un'evidenza e torna alla lista. **Dati da chiarire** riguarda campi mancanti o con alternative, non tutte le letture automatiche. **Scadenza superata** filtra la data, anche su una bolletta dichiarata pagata: non significa pagamento non eseguito. **Scadenza entro 30 giorni** include oggi e il giorno 30, esclude date mancanti/ambigue.

**Verifica:** 19 test Python superati; `node --check fold_app/static/app.js`; controlli della logica UI con `node tests/test_ui.mjs`. Prove browser sul runtime a 1440×900 e 390×844: lista, ricerca/filtro/ordine, zero risultati, dettaglio, evidenze, cronologia, ritorno con focus/selezione/scorrimento (anche Avanti/Indietro), nessun overflow orizzontale. Upload PDF, correzione, dichiarazione e persistenza al reload verificati nel medesimo runtime su database temporaneo. Archivio personale consultato senza scritture: conteneva un solo esempio già salvato, nessun corpus di PDF personali. Catture reali in `docs/ux/screenshots/runtime-*`.

**Limiti:** la lista carica i dettagli attraverso l'API esistente, quattro richieste concorrenti per volta; non è validata su centinaia di documenti. Nessun OCR, verifica bancaria o validazione dell'accuratezza su un corpus reale. Mobile verificato con viewport browser, non su dispositivo fisico; nessuna conformità WCAG complessiva dichiarata. Resta valida la conservazione di originali e storia. Nessun commit, push o merge eseguito.

## Avvio su Windows

Da PowerShell, nella cartella del repository:

```powershell
.\Start-Fold.ps1
```

Apri **http://127.0.0.1:8765**. Lascia aperto il terminale; `Ctrl+C` ferma il server. Il launcher cerca un ambiente `.venv`, poi Python del PC, poi l'eventuale runtime già incluso con Codex; non installa né modifica pacchetti globali.

Se l'esecuzione di script è bloccata, il solo processo può essere avviato con:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\Start-Fold.ps1
```

Su un PC senza Python compatibile con `pypdf`, prepara una volta un ambiente isolato (Python 3.12 o successivo):

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\Start-Fold.ps1
```

Avvio diretto, anche su altre piattaforme con la dipendenza installata:

```text
python -m fold_app --port 8765 --data-dir /percorso/archivio-fold
```

Su Windows i dati predefiniti sono in `%LOCALAPPDATA%\Fold\local-preview\fold.sqlite3`, separati dal codice. Per una prova separata usa una cartella **nuova**:

```powershell
.\Start-Fold.ps1 -Port 8766 -DataDir "$env:TEMP\Fold-prova"
```

## Prova guidata (senza documenti personali)

1. Per questa prova usa una **cartella dati temporanea**, separata dall'archivio personale. Scarica il PDF sintetico da `http://127.0.0.1:8765/api/example.pdf` (adatta la porta se diversa) e caricalo con **Aggiungi PDF**. Numero `DEMO-001`, importo `84,72 EUR`, POD e scadenza trascorsa sono dati fittizi della prova. La UI reale non inserisce più un esempio tramite pulsante.
2. Controlla le quattro schede: ogni lettura riporta pagina e frammento. Scarica l'originale per confrontarlo. **La scadenza trascorsa non viene mostrata come prova di mancato pagamento.**
3. Su **Totale da pagare**, scegli **Verifica o correggi**, inserisci `34,72` e un motivo. Il valore corrente cambia; gli `84,72` letti dal PDF restano nella **Cronologia**. La correzione ha una base umana distinta dalla lettura originale.
4. Premi **Dichiara il pagamento**, aggiungi una dichiarazione di esempio e salva. Lo stato diventa **Pagamento dichiarato**, senza fingere una verifica bancaria.
5. Ricarica la pagina, oppure ferma e riavvia usando la stessa cartella dati: scheda e storico rimangono.
6. **Esporta una copia** scarica un archivio con database coerente, manifest leggibile e originali. Per il ripristino ferma Fold, estrai `fold.sqlite3` in una cartella **nuova** e avvia con `-DataDir` su quella cartella. Non sovrascrivere archivi esistenti.

Puoi anche caricare un PDF con testo tramite **Aggiungi PDF**. Il canale è deliberatamente dedicato alle bollette elettriche; non è un classificatore documentale generale.

## Perimetro e limiti attuali

- Dati proposti: numero bolletta, POD riportato, totale da pagare in EUR, scadenza. Le regole cercano etichette esplicite e non sono parser per fornitore. Campi assenti o con valori differenti rimangono da chiarire; una mancata corrispondenza non prova assenza nel documento.
- L'importazione conserva anche i PDF senza testo, ma non esegue OCR. Limiti: 10 MB, 50 pagine, 25 secondi per la lettura. Il parser gira in un processo separato con controlli di dimensione, non in una sandbox di sicurezza completa.
- Le letture sono proposte ispezionabili. Non è richiesta la conferma di tutti i campi. La risposta sulla scadenza è qualificata dai dati mostrati; il pagamento è una dichiarazione esplicita e circoscritta.
- Una doppia acquisizione degli stessi byte registra un nuovo ingresso senza duplicare scheda e letture. Non è riconciliazione semantica di PDF diversi né prova di indipendenza delle fonti.
- Uso locale su un solo PC/utente fidato. Il server ascolta esclusivamente su `127.0.0.1`, controlla Host/Origin e un token per le scritture. Nessun servizio cloud o invio esterno dei documenti. Non esporre questa anteprima in rete: autenticazione, account e permessi non sono implementati.
- Nessun collegamento tra utenze, riconciliazione tra bollette, ricevute automatiche, OCR, scheduler, notifiche o servizi AI. Il passaggio del tempo viene rivalutato quando la scheda è richiesta; non c'è una promessa di attenzione autonoma.
- La persistenza della slice usa SQLite con relazioni esplicite tra fonti, osservazioni, referenti, enunciati, contributi e selezioni. Non rappresenta una scelta definitiva contro un DB a grafo; Core e regole elettriche restano separati.

## Verifica e prossimo passo

```text
python -m unittest discover -s tests -v
```

Prima verifica automatica: **19 test superati** con Python 3.12.14 e `pypdf` 6.10.0 su Windows. Copertura: PDF reale sintetico e PDF vuoto/cifrato/danneggiato; ambiguità; importi e date; distinzione pagamento/scadenza; duplicati; revisioni concorrenti; riapertura; backup/ripristino e integrità dei collegamenti; percorso HTTP; protezioni delle scritture e del percorso file.

Prova nel browser completata il 2 novembre 2026 sul codice in GITFOLD: caricamento dell'esempio, evidenze visibili, correzione da 84,72 a 34,72 con lettura originale conservata, dichiarazione fittizia di pagamento, cronologia e persistenza dopo il ricaricamento. Verificato anche l'avvio tramite `Start-Fold.ps1`, con selezione automatica del runtime Codex già presente e archivio temporaneo dedicato. L'installazione Python principale di questo PC non è stata modificata.

Non è misurata l'accuratezza su un corpus di bollette reali: il repository non include gli originali. La prossima implementazione consigliata è **associare una seconda evidenza alla stessa bolletta e ricostruire lo stato senza cancellare le basi precedenti**, dopo aver verificato i campi su un piccolo corpus autorizzato. Nessuna nuova roadmap è introdotta.

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
