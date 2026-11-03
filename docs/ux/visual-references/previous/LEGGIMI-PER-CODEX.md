# Fold — Riferimenti visivi dai layout discussi in chat

**Stato: Draft / supporto alla valutazione UX.** Materiale complementare a `Fold-UX-Reference-v0.1.zip`.

Queste immagini **non sono screenshot 1:1 dell'interfaccia di ChatGPT** e **non sono screenshot del runtime Fold**. Sono *ricostruzioni statiche* dei layout progettati in chat, renderizzate in browser per consentirne la consultazione a Codex. La forma è indicativa e non prevale sulle regole funzionali del primo pacchetto o sui documenti canonici del repository.

## Come usarle

Usare le immagini per individuare scelte compositive e valutarne i tradeoff: quale attività domina la schermata, quali informazioni si devono confrontare, quando le colonne sono più utili delle righe, quali dettagli sono disponibili su richiesta. **Non chiedere a Codex di replicare pixel per pixel ogni immagine** né di implementare funzionalità non supportate.

| Immagine | Funzione | Perché questa disposizione | Limite principale |
|---|---|---|---|
| 00-palette-semantica.png | Colore | Colori semantici piatti con testo; stessa palette del prototipo v0.1 | Il colore non può da solo codificare gli stati |
| 01-configurazione-adattiva.png | Configurazione iniziale | Scelta esigenze e anteprima in parallelo, con visibilità reversibile | Un onboarding lungo introdurrebbe attrito |
| 02-situazione.png | Home | Attività centrali in righe dense, contesto secondario laterale | Non sommergere con segnalazioni di bassa priorità |
| 03-utenze-tabella-e-anteprima.png | Consultazione | Tabella per confronto; anteprima accanto per interpretazione | Su viewport stretti la tabella richiede alternativa responsive |
| 04-documento-e-prova.png | Dettaglio | Importo/stato/contesto da una parte, PDF dall'altra | Una vista PDF complessa richiede espansione |
| 05-acquisizione-affiancata.png | Ingresso | Originale ed estrazione visti insieme per verificare | Non pretendere conferma di ogni valore |
| 06-scadenze-e-attese.png | Tempo | Colonne periodiche + elenco quando aumenta la densità | Una previsione non va spacciata per data certa |
| 07-immobile-prospettive.png | Vista per bene | Dati stabili secondari, situazione e relazioni centrali | Non scambiare correlazione temporale per causalità |
| 08-ricerca-trasversale.png | Ricerca | Risultati diversi nella stessa ricerca, spiegazione contestuale | Ordinamento e pertinenza devono essere comprensibili |
| 09-raggruppamenti-viste.png | Viste | Raggruppamento virtuale del medesimo insieme di file | Evitare un secondo archivio fatto di viste |

## Colori e vincoli condivisi con il primo pacchetto

- Fondo `#101317`, menu `#13171B`, superficie `#191E24`, superficie secondaria `#20262E`, divisori `#303842`.
- Testo `#E9EDF2`, secondario `#A4AFBB`.
- **Blu** `#96BBEB`: selezione, navigazione, link e prova richiamabile.
- **Ambra** `#DFB46E`: attenzione, attese o scadenze con qualificazione testuale.
- **Verde** `#8FC8AA`: conferma circoscritta, senza ampliare ciò che dimostra. **Pagamento dichiarato** rimane neutro finché non vi è una conferma idonea; dichiarazione non significa verifica bancaria.
- **Rosso** `#E6A0A0`: solo quando un vero errore/problema lo giustifica.
- Niente gradienti, glow, glassmorphism, ombre decorative, moltiplicazione inutile delle card.
- Ogni stato ha sempre **testo e/o simbolo**, non soltanto colore.

## Per Codex: ordine di autorità

1. `AGENTS.md`, `docs/README.md` e documenti canonici pertinenti del repository.
2. Requisiti e vincoli documentati in `Fold-UX-Reference-v0.1.zip` (ancora Draft e da validare).
3. Queste immagini come riferimento compositivo e di colore, **mai** come nuove specifiche di prodotto implicitamente approvate.

### Distinzione implementazione/prototipo

L'app attuale del branch `LABORATORIO` gestisce una prima slice locale relativa a bollette elettriche PDF con testo, correzioni ed evidenze. Nelle schermate sono rappresentati anche gas, veicoli, beni, attese, timeline, collegamenti estesi e ricerca trasversale: **sono solo scenari UI dimostrativi**, non capacità attualmente implementate né autorizzazione a costruirle tutte.

La prima integrazione UX dovrà conservare l'esistente e introdurre soltanto le parti necessarie e autorizzate, con dati demo isolati per la verifica.

## Suggerimento di confronto

Valutare prima 02, 03, 04, 05 come percorso principale, poi 01, 06, 07, 08, 09 come stress-test della grammatica UX. Annotare separatamente «riprodurre», «adattare», «posticipare» e «da verificare».
