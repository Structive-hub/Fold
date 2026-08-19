# Ricerca sulla funzione semantica degli identificatori nelle bollette

> **Stato del documento:** materiale di ricerca. Questo testo non modifica i fondamenti canonici di Fold e non definisce un modello generale delle utenze. Conserva esclusivamente le conclusioni raggiunte nel ciclo di analisi degli identificatori presenti nelle bollette luce e gas.

## 1. Scopo e perimetro

La ricerca parte dal confronto documentale conservato in [bollette-luce-gas-arera.md](bollette-luce-gas-arera.md) e considera soltanto gli identificatori effettivamente analizzati:

- numero della bolletta;
- codice cliente;
- numero di fornitura assegnato dal venditore;
- POD;
- PDR;
- codice offerta;
- matricola del misuratore.

Codice cliente e numero di fornitura sono mantenuti distinti nell'elenco perché potrebbero riconoscere cose diverse, anche se la documentazione disponibile non ne chiarisce completamente la separazione.

## 2. Funzioni semantiche emerse

| Funzione semantica | Che cosa viene riconosciuto | Identificatori che la svolgono | Continuità resa osservabile | Limiti e ambiguità |
| --- | --- | --- | --- | --- |
| Identificazione documentale | Una specifica bolletta o emissione documentale relativa a un determinato periodo | Numero della bolletta | Distingue una bolletta dalle precedenti e dalle successive anche quando la fornitura rimane invariata | La bolletta sintetica e la fattura elettronica sono collegate, ma non necessariamente coincidono; anche i rispettivi numeri possono coincidere oppure essere distinti |
| Identificazione amministrativa presso il venditore | Una posizione riconosciuta nel sistema del venditore: il cliente, la fornitura amministrata o il rapporto gestito | Codice cliente; numero di fornitura del venditore | Collega documenti successivi all'interno dello stesso ambito commerciale o amministrativo | Non è stato stabilito se ciascun codice riconosca la persona, il rapporto contrattuale, la fornitura amministrata o una combinazione di questi elementi; la continuità può interrompersi cambiando venditore |
| Identificazione del punto tecnico | Il punto della rete presso il quale avviene il prelievo dell'energia elettrica o la riconsegna del gas | POD; PDR | Rende osservabile la continuità del punto anche mentre cambiano aspetti commerciali, contrattuali o tecnici | La stabilità rispetto al cambio di venditore è esplicitamente sostenuta per il POD; per il PDR il corpus non ha verificato direttamente tutti i casi. Non sono stati analizzati gli eventi tecnici che possono determinare cessazione o sostituzione del punto |
| Identificazione commerciale | Una determinata offerta e la configurazione economica che essa rappresenta | Codice offerta | Permette di riconoscere quale offerta è applicata alla fornitura in un certo periodo e di osservare un eventuale cambiamento dell'offerta senza confonderlo con il cambiamento del punto | Non identifica il contratto, il cliente o il punto. La ricerca non ha stabilito tutte le regole secondo cui una variazione delle condizioni comporta il mantenimento o la sostituzione del codice |
| Identificazione dell'apparato fisico | Uno specifico dispositivo utilizzato per misurare i prelievi | Matricola del misuratore | Permette di seguire la permanenza dello stesso apparecchio e di rilevarne la sostituzione, mentre il punto tecnico può rimanere invariato | La continuità riguarda il dispositivo, non il punto o la fornitura. I documenti non offrivano una sequenza completa delle matricole precedente e successiva a una sostituzione |

## 3. Differenze di continuità

Gli identificatori analizzati rendono osservabili continuità differenti:

- il numero della bolletta distingue singole emissioni e cambia normalmente a ogni nuovo documento;
- codice cliente e numero di fornitura sostengono una continuità interna al sistema del venditore, ma non necessariamente oltre il cambio di venditore;
- POD e PDR sostengono la continuità del punto tecnico, distinta dalle configurazioni commerciali e dagli apparati di misura;
- il codice offerta sostiene la continuità di una configurazione commerciale applicata in un certo periodo;
- la matricola sostiene la continuità del singolo misuratore e cambia quando l'apparato viene sostituito.

Queste continuità possono sovrapporsi temporalmente, ma non sono equivalenti. Una di esse può interrompersi mentre le altre proseguono.

## 4. Ambiguità ancora aperte

Restano aperte le seguenti questioni, senza svilupparle ulteriormente:

- distinzione precisa tra numero della bolletta e numero della fattura elettronica;
- oggetto esatto riconosciuto dal codice cliente e dal numero di fornitura nei diversi sistemi dei venditori;
- condizioni complete nelle quali un POD o un PDR viene cessato, sostituito o ricreato;
- regole con cui una variazione commerciale determina il mantenimento o il cambiamento del codice offerta;
- ricostruzione documentale completa della successione delle matricole in caso di sostituzione del misuratore.

## 5. Conclusione della ricerca

Nei documenti analizzati, **identificare non significa sempre riconoscere lo stesso tipo di cosa**. Gli identificatori considerati possono riconoscere un documento, una posizione amministrativa interna a un venditore, un punto tecnico, un'offerta commerciale oppure un apparato fisico.

Di conseguenza, gli identificatori analizzati non identificano tutti la stessa cosa e nessuno di essi, preso da solo, può essere assunto come identificatore dell'“utenza” nel suo complesso.
