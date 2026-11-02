# Architecture

**Status:** Canonical  
**Scope:** regole della cartella, non architettura definitiva

Questa cartella ospita il modello concettuale e l'architettura tecnica di Fold solo quando risultano sufficientemente verificati da poter guidare l'implementazione.

Il core informativo è attualmente oggetto di nuova progettazione e stress test. Per questo motivo **non esiste ancora qui un modello canonico del core da usare come contratto di implementazione**.

Quando il lavoro corrente sul core sarà chiuso, le conclusioni verificate verranno promosse qui distinguendo chiaramente:

- ciò che appartiene al Core generale;
- ciò che appartiene al Dominio;
- ciò che rappresenta dati reali;
- ciò che rimane ancora aperto o futuro.

Non tradurre anticipatamente concetti di lavoro in tabelle, classi, database o altri oggetti software prima che la progettazione li abbia consolidati.

## Scelte della prima slice locale — 2 novembre 2026

L'utente ha ora delegato le decisioni tecniche e autorizzato un primo risultato eseguibile. Il contratto della sola funzionalità realizzata, con prova e limiti, è nel [README principale](../../README.md); questa nota non consolida l'intera anatomia Draft.

- **Python 3.12+ e una sola dipendenza (`pypdf`)**: lettura locale dei PDF con testo; interfaccia HTML/CSS/JS senza build o dipendenze di rete. Il server della libreria standard è limitato all'anteprima su loopback, non a una distribuzione pubblica o domestica condivisa.
- **`core.py`** conserva fonti, osservazioni, soggetti, enunciati, contributi ricevuti e selezioni con riferimenti espliciti; non conosce POD, bollette o regole di pagamento. **`electricity.py`** contiene campi, mapping minimo e ricostruzione della situazione. **`extraction.py`** separa la lettura tecnica dall'interpretazione e limita il tempo del processo PDF. **`server.py`** applica il caso d'uso e i controlli HTTP.
- **SQLite per questa slice**: transazioni, vincoli referenziali, revisioni controllate e snapshot tramite API di backup. Gli originali sono BLOB nello stesso database: per il volume delimitato evita una transazione incompleta fra filesystem e database e permette di ripristinare contenuti e legami insieme. Non è una scelta definitiva del database del prodotto né un contratto universale di grafo/ontologia.
- Le letture automatiche e le correzioni umane sono enunciati distinti; una selezione corrente non cancella la storia. La base testuale del contributo umano rimane recuperabile e non viene falsamente attribuita al PDF.
- Le alternative differenti non vengono risolte a maggioranza; corrispondenze tecniche non diventano identità di utenza. Il pagamento dichiarato e la scadenza calcolata restano distinti. Ogni azione umana indica il campo e la revisione osservata; una risposta obsoleta è respinta senza scritture parziali.
- Dati d'istanza separati dal codice, nessuna telemetria o invio esterno. Backup include snapshot database, manifest e originali esportati. Nessuna cifratura applicativa, multiutenza o attenzione autonoma runtime è dichiarata realizzata.

Le migrazioni successive dovranno preservare originali, origine delle letture, contributi, collegamenti e storia. I documenti congelati rimangono fonti concettuali con il loro stato, non vengono riscritti per adeguarli al codice.
