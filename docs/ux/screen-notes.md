# Schermate consolidate — v0.2

**Status: Draft · 3 novembre 2026.** Le immagini dei concept sono riferimenti; i JPG sono catture del prototipo. Tutti i dati del prototipo sono sintetici.

| Vista e obiettivo | Distribuzione dello spazio e motivazione | Visibile / contestuale / richiamabile | Comportamenti e limiti |
| --- | --- | --- | --- |
| Situazione: capire cosa fare adesso | Righe di attenzione e recenti al centro; accessi e prossima data nella colonna secondaria; piccola griglia per le aree | Attenzione e azioni visibili; dettaglio dopo il clic; aree configurabili da modale | Apri fonte, filtra pagamenti, cambia aree. La configurazione cambia visibilità, non documenti. Nessun ranking appreso, notifica o previsione realmente calcolata |
| Utenze: trovare e confrontare | Tabella per attributi ripetuti, filtri sopra, pannello più stretto per spiegare la selezione | Ricerca e ordine sempre visibili; filtri aggiuntivi apribili; anteprima chiudibile; vista memorizzabile | Filtri combinati, ordine, stato vuoto e ritorno al contesto. Su mobile il periodo è omesso e la sola tabella scorre; il pannello segue la lista. Nessuna promessa di persistenza delle viste |
| Documento: comprendere ed esaminare la base delle affermazioni | Sintesi e azioni nell'area principale; fonte e prova vicine in colonna; dati e storia in sezioni separate | Stato motivato subito; provenienza, collegamenti e cronologia richiamabili; dichiarazione in modale | Si apre la prova dell'importo, si dichiara con nota e si vede lo storico; si torna al punto di partenza. I quattro campi del runtime non diventano un nuovo schema universale. Il facsimile non è una prova reale |
| Acquisizione: confrontare ciò che entra con ciò che è compreso | Fonte a sinistra e letture a destra, poi singola colonna sullo stretto | Fonte e letture visibili; suggerimento in sezione dedicata; conferma del solo collegamento contestuale | Nessuna selezione/upload reale. Indirizzo demo compatibile spiega il suggerimento; conferma simulata e proseguimento senza verifica totale. Il pagamento non si deduce dal PDF |
| Bene: capire il contesto attraverso fonti condivise | Dati stabili in fascia laterale ridotta; situazione/documenti/relazioni nell'area ampia | Situazione iniziale; documenti e relazioni richiamabili; fonte accessibile da ogni prospettiva | Il documento mantiene la stessa identità tra archivio e Casa. Ritorno al bene conserva la sezione. Nessuna gerarchia aggiuntiva, causalità dedotta o dichiarazione «in regola» senza basi |

## Contraddizioni risolte

- Nei concept «confermato» e «in regola» possono sembrare giudizi complessivi. Nel prototipo una conferma riguarda solo il collegamento indicato; una dichiarazione di pagamento resta neutra e attribuita.
- Un contratto non è una bolletta e non ha un pagamento da verificare.
- Le percentuali nei suggerimenti dei concept non hanno misura e regola documentate: omesse in accordo alla decisione canonica 0002.
- «Riconosciuto» è distinto tra lettura e interpretazione, non una verità garantita dal colore verde.
- Le aree non sono un'ontologia completa del prodotto. Il repository non contiene una specifica canonica definitiva di tutta la navigazione: qui si consolidano scelte Draft esplicitamente richieste, senza attribuirle retroattivamente alla baseline.

## Comportamento comune

Ricerca e acquisizione hanno una posizione prevedibile. Le sezioni sono pulsanti nativi con stato premuto, utilizzabili con Tab e Invio, non widget ARIA incompleti. Le modali native contengono il focus e si chiudono con Esc. Il menu mobile chiuso non lascia link nascosti raggiungibili con Tab. Focus visibile, significato in testo e simboli, riduzione del movimento rispettata. La tabella ha pulsanti reali nelle celle invece di righe con ruolo di pulsante.
