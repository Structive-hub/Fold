# Fold — Coverage Map: Ledger ↔ candidata v2 congelata

**Status:** Research  
**Data:** 2026-09-04  
**Scope:** verifica documentale della conservazione delle conoscenze; non nuova anatomia, non v2.1, non risposta alla review indipendente.

## Baseline e sequenza della verifica

1. Salvato lo [snapshot storico v2](fold-anatomia-v2-snapshot-2026-09-04.md), senza modifiche al corpo originale dopo il Regression Audit.
2. Ricostruito e salvato il [Knowledge / Decision Ledger](fold-knowledge-decision-ledger-2026-09-04.md) dai Round in ordine cronologico, dal chiarimento R2 e dai gate pertinenti: **188 voci**. La v2 non ha fornito l'indice del Ledger.
3. Solo dopo la chiusura del Ledger, confrontate le **161 voci attive** con lo snapshot.
4. Eseguito il controllo inverso delle **87 affermazioni strutturali o gruppi di affermazioni omogenee**, senza integrare conoscenze nuove nel Ledger.

SHA-256 del corpo originale dello snapshot: `fad314962da4e44968824c213d44fcd0ac4eef8c02856cfd386d5f2d8dbc2567`.  
SHA-256 del file Ledger al passaggio alla coverage: `fff10fdb54ae444fef27d15a8fa876bdcfa8a1055aad95a2001d9782801b354f`.

Il Ledger non è stato modificato a partire da quel passaggio. I riferimenti A–P e H1–H22 indicano le sezioni dello snapshot, non quelle del Ledger. Le origini genealogiche e le motivazioni delle conoscenze sono nel Ledger: qui non vengono duplicate.

## Criteri di classificazione

- **ESPLICITA:** la v2 formula direttamente almeno il nucleo della conoscenza.
- **IMPLICITA:** la conclusione si ricava combinando impegni effettivamente presenti; la nota spiega il passaggio. La sola esistenza di un nome o contenitore non basta.
- **ASSENTE:** manca la garanzia o il criterio specifico. Non significa che la futura implementazione sia necessariamente incapace di rispettarlo.
- **COMPLETA:** il significato e i limiti necessari sono preservati, anche con lessico o esempi diversi.
- **PARZIALE:** parte della conoscenza è preservata, ma manca uno specifico obbligo o confine: la nota identifica quale.
- **ALTERATA:** la v2 adotta una formulazione differente; non implica automaticamente un errore semantico.
- **NON APPLICABILE:** non c'è contenuto corrispondente di cui misurare la fedeltà.

Una conoscenza non è giudicata persa solo perché manca lo stesso esempio. È invece parziale quando l'esempio storico aveva conquistato un vincolo che la nuova formulazione non garantisce.

Il controllo inverso verifica la genealogia delle affermazioni, non dimostra che lo snapshot preservi l'intero Ledger. **SUPPORTED BY LEDGER** può coesistere con copertura forward parziale: un componente può essere giustificato ma non riprendere tutti i propri vincoli.

## Report sintetico

### Ledger

| Misura | Totale |
|---|---:|
| Voci complessive | 188 |
| Conoscenze attive | 161 |
| Di cui STABILE nel percorso | 146 |
| Di cui CANDIDATA | 15 |
| Posizioni SUPERATA | 13 |
| Aperture | 14 |
| Voci di natura DECISIONE NEGATIVA | 37 |

Le decisioni negative sono una natura trasversale, non uno stato aggiuntivo: 36 sono attive e una appartiene a una questione aperta. Non si sommano ai 188 elementi.

### Copertura delle 161 conoscenze attive

| Misura | Totale |
|---|---:|
| Fedeltà COMPLETA | 108 |
| Fedeltà PARZIALE | 45 |
| Presenza IMPLICITA | 16 |
| ASSENTE / fedeltà NON APPLICABILE | 7 |
| Fedeltà ALTERATA | 1 |

**Le dimensioni si sovrappongono:** le 16 implicite comprendono 12 complete e 4 parziali. La partizione per fedeltà è 108 + 45 + 1 + 7 = 161. Per presenza: 138 esplicite, 16 implicite, 7 assenti.

L'unica alterazione rilevata è **K-004, CONSULTS/READS**, una variazione organizzativa rispetto alla proposta R1, non una regressione semantica dimostrata. Le 45 parziali non sono 45 problemi indipendenti: più voci possono condividere la stessa compressione documentale.

### Reverse coverage

| Classificazione | Totale |
|---|---:|
| SUPPORTED BY LEDGER | 79 |
| ASSEMBLY CHOICE | 8 |
| UNTRACED | 0 |
| Totale affermazioni/gruppi verificati | 87 |

**Nessun UNTRACED dimostrato nella lettura contestuale dello snapshot.** V-012 richiede una cautela: «non esiste un produttore universale delle Decision» va letto come pluralità delle origini dell'autorità, non come divieto definitivo di formalizzazione comune. E/O mantengono esplicitamente D06 aperto. Non classifico come nuova regola una lettura più forte che il contesto non impone.

### Dieci perdite o compressioni materialmente importanti

| ID | Ledger | Tema | Perdita o indebolimento |
|---|---|---|---|
| T01 | K-079, K-080, K-081 | Attenzione temporale e basi delle attese | Reference time e Work restano, ma non il legame fra comportamento promesso, attivazione senza nuovo ingresso e base/finestra/riscontro dell'attesa; perso anche il motivo per non introdurre Expectation universale. |
| T02 | K-075, K-093, K-109 | Quando la conservazione diventa obbligatoria | «Quando necessario» non conserva il criterio materiale Decision/spiegazione storica, né garantisce la parte della definizione usata oltre il nome della versione. |
| T03 | K-085, K-086 | Impatto oltre le premesse positive | Persi i presupposti di assenza/perimetro/continuità e il guardrail che dipendenza non trovata non prova irrilevanza. |
| T04 | K-087 | Impatto potenziale distinto da rivalutazione effettiva | La v2 vieta la falsità automatica, ma comprime potenzialmente affetto, rivalutato/confermato, rivalutato/corretto e non verificato per l'uso. |
| T05 | K-102 | Indipendenza non determinata | Origine comune e non doppio conteggio recuperati da D03, ma manca l'esito esplicito di indipendenza non determinata. |
| T06 | K-071, K-138 | Continuità temporale e identitaria non automatica | Mancano il divieto di estendere indefinitamente un periodo senza base e la dipendenza della continuità dal soggetto Domain effettivo. |
| T07 | K-022, K-023 | Parallelizzabilità non equivale a lavori contemporaneamente aperti | Assenti distinzione lifecycle/calcolo/effetti e test conservativo sulle condizioni e sulla compatibilità degli effetti. |
| T08 | K-018, K-038, K-039 | Limiti delle applicazioni e delle conferme | Non esplicitati effetto già applicato, non propagazione della conferma a target ampliati e distinzione fra conferma abilitante e supporto di tutte le premesse. |
| T09 | K-091 | Cambiamento degli invarianti Core | Manca il criterio che richiede decisione fondazionale esplicita e verifica delle distinzioni già perse; versionamento generico non basta. |
| T10 | K-179, K-180 | Autorizzazioni e conservazione non ridotte ai nomi delle trasversali | Non espliciti persona/account/autorità distinti, effetto della cancellazione sulla verificabilità e ripristino dei collegamenti oltre ai file. |

D01–D05 risultano recuperati nello snapshot: base umana, no auto-supporto, origine comune, nuova base degli assessment e reversibilità della coreferenza sono presenti. Questi recuperi non esauriscono tutte le conoscenze anteriori.

Non è dimostrata una promozione indebita da distinzione forte a primitiva autonoma. Sono invece omesse o poco visibili alcune aperture e alcune decisioni negative; i controlli supplementari le mantengono distinguibili da aperture realmente chiuse.

## 1. Coverage forward — Ledger → v2

Una riga per ciascuna voce STABILE o CANDIDATA ancora attiva. Le 13 SUPERATA restano nella genealogia e non sono requisiti da ripristinare.

| K-ID | Presenza nella v2 | Dove | Fedeltà | Nota |
|---|---|---|---|---|
| K-001 | ESPLICITA | B; C; D | COMPLETA | Le viste non sono una sequenza universale e gli accessi laterali sono espliciti. |
| K-002 | ESPLICITA | F — Esecuzione; J | PARZIALE | Chiamate, letture, produzioni e dipendenze distinte; meno esplicito il contratto sul risultato richiesto e sul tratto abilitato, diverso dalla conclusione del produttore. |
| K-003 | ESPLICITA | D; E; G | COMPLETA | Source, Observation, proposte e conclusioni possono essere conservate/usate senza Admission. |
| K-004 | ESPLICITA | C — Direzioni principali; J | ALTERATA | CONSULTS è nuovamente una voce distinta da READS: cambia la proposta terminologica R1. Non è dimostrato un cambiamento semantico; possibile scelta organizzativa, non divieto violato. |
| K-005 | IMPLICITA | C — Direzioni principali; J | COMPLETA | Relazioni tipate al posto della freccia generica FEEDS; il suo rigetto è ricavabile dal vocabolario, non dichiarato. |
| K-006 | ESPLICITA | J; F | PARZIALE | REACTS_TO e CONSTRAINED_BY presenti; emissione di un accadimento non distinta esplicitamente dalla produzione di un risultato, né vincolo da consultazione a ogni esecuzione. |
| K-007 | ESPLICITA | F — Esecuzione; H19 | COMPLETA | Il proprietario del lavoro governa dipendenze, attese e seguito autorizzato. |
| K-008 | ESPLICITA | F — Acquisition; H1 | COMPLETA | La ricezione non è la regia delle elaborazioni successive. |
| K-009 | ESPLICITA | H7; F; M | COMPLETA | Composizione semantica distinta dal coordinamento operativo. |
| K-010 | ESPLICITA | D; H7; I — Interpretation Result | COMPLETA | Alternative, dipendenze mancanti e proposte non ammesse sono lecite. |
| K-011 | ESPLICITA | F; E — Quattro significati | COMPLETA | Acquisition, Work, Attempt, risultato informativo ed Application non collassano. |
| K-012 | ESPLICITA | F; I; O | COMPLETA | Work durevole non universale, con proprietario, obiettivo, dipendenze e tentativi; granularità aperta. |
| K-013 | ESPLICITA | F — Rivalutazione | PARZIALE | Riuso di materiale e nuova storia espliciti; manca una definizione netta di retry sugli stessi presupposti rispetto a nuova valutazione su presupposti mutati. |
| K-014 | IMPLICITA | G — Policies; H14 | COMPLETA | Il criterio è scegliere comportamento/prudenza fra esiti ammissibili: include regole deterministiche, ma questo caso non è detto. |
| K-015 | ESPLICITA | E — Quattro significati; F | COMPLETA | Scelta, trattamento autorizzato ed esecuzione riuscita/tentata distinti. |
| K-016 | ESPLICITA | E; H14; O | COMPLETA | Percorso da autorità esplicita distinto dalla valutazione delle Policy. |
| K-018 | ESPLICITA | E — Applicabilità; H16 | PARZIALE | Controlli e divieto di disposizione alternativa espliciti; non esplicitato il controllo sull'effetto già applicato. Idempotenza tecnica H3 non basta per Admission. |
| K-019 | ESPLICITA | D — Ingresso umano; H15; H22 | COMPLETA | Natura della risposta e autorità non equiparate a conferma o Admission. |
| K-020 | ESPLICITA | D; G; H — obblighi comuni | COMPLETA | Assessment locali e rivalutabili, non passaggio unico. |
| K-021 | ESPLICITA | C — Vincoli; D; I; M | COMPLETA | D02 e D04 ripristinano il divieto di autoconferma. |
| K-022 | ASSENTE | —; solo riferimenti generali in F | NON APPLICABILE | Non ricostruita la triplice distinzione fra lavori aperti contemporaneamente, calcoli simultanei ed effetti indipendenti. |
| K-023 | ASSENTE | —; F tratta dipendenze, non il test | NON APPLICABILE | Non compare il test conservativo su prerequisiti, contesto e compatibilità degli effetti; l'assenza di frecce non è discussa. |
| K-024 | ESPLICITA | F; I; M | COMPLETA | Attempt/esiti restano aspetti operativi, non nuove primitive del mondo. |
| K-025 | ESPLICITA | E — Applicabilità; F; H13 | COMPLETA | Decision storica e nuovo controllo di condizioni sono distinti. |
| K-027 | IMPLICITA | G — Conservazione; O; P | COMPLETA | Nessuna conservazione indiscriminata né forma software/MVP già decisa; la non-obbligatorietà del parallelismo è solo conseguenza del fuori scope, non discussa. |
| K-028 | ESPLICITA | I — Documenti e rappresentazioni | COMPLETA | Cardinalità multiple e identità documentale distinta da forma tecnica. |
| K-029 | ESPLICITA | I — Elementi; I — Documenti | COMPLETA | Referent documentale facoltativo quando serve identità indipendente. |
| K-030 | ESPLICITA | M — Logical Document | COMPLETA | Escluso Logical Document obbligatorio. |
| K-031 | ESPLICITA | I — Locator; H5; H7 | PARZIALE | Localizzazione e composizione presenti; non esplicitato che porzioni indirizzabili non richiedono segmentazione automatica completa. |
| K-033 | ESPLICITA | D; H17 | COMPLETA | Accesso a Source, Observation e proposte senza Knowledge artificiale. |
| K-034 | ESPLICITA | H17; I — Informazione negativa | COMPLETA | Risultato negativo circoscritto a corpus, scope e limiti. |
| K-035 | ESPLICITA | D — Ingresso umano; H22; G | COMPLETA | D01 conserva base ricevuta, interpretazione ed autorità separabili. |
| K-036 | ESPLICITA | D; H22; M | COMPLETA | Nessuna Observation umana artificiale o classificazione universale come Source; nessuna nuova primitiva richiesta. |
| K-037 | IMPLICITA | D — Ingresso umano; H15; H22 | COMPLETA | Target e natura circoscritti implicano che correggere una lettura non confermi ruolo, soggetto o pagamento; il caso non è sviluppato. |
| K-038 | ESPLICITA | D; E — Applicabilità; H15 | PARZIALE | Scope/contesto conservati; non esplicitati risposta tardiva sul target originale e divieto di estensione a nuovi membri del bundle. |
| K-039 | IMPLICITA | D; I — Supporto; J | PARZIALE | Supporto circoscritto e dipendenze distinte consentono la lettura corretta; manca il caso/guardrail esplicito della conferma abilitante che non sostiene tutte le premesse. |
| K-040 | ESPLICITA | F; I | COMPLETA | Attempt ed esito non promossi a primitive; memorie eterogenee senza Result universale. |
| K-041 | ESPLICITA | H2; H4; F | COMPLETA | Processabilità e storia dell'acquisizione distinte da preservazione e verità. |
| K-042 | ESPLICITA | H5; H7; F — Esecuzione | PARZIALE | Produttore, consumatore e proprietario Work riconoscibili, ma non espresso chi decide sufficienza del risultato parziale per il singolo uso. |
| K-043 | ESPLICITA | H5; F — Esecuzione/Rivalutazione | PARZIALE | Risultati parziali e nuova storia presenti; non esplicita la conservazione selettiva dei risultati del tentativo interrotto né il divieto di preferire in blocco tutte le letture del retry riuscito. |
| K-044 | ESPLICITA | D; E; I — Interpretation Result; M | PARZIALE | Proposte e dipendenze locali evitano un Candidate globale; manca il criterio esplicito per l'ammissione parziale senza gate atomico del bundle. |
| K-045 | IMPLICITA | H5–H7; I — Observation/Assertion | COMPLETA | Distinzione estrazione/semantica e dipendenze irrisolte rendono ricavabile che un token chiaro non basti per una proposizione completa. |
| K-047 | ESPLICITA | C — Anti-bloat; I — Legenda; O | COMPLETA | Distinzione necessaria non impone primitiva, archivio o componente. |
| K-049 | ESPLICITA | I — Source; H4; D | COMPLETA | Origine contenutistica referenziabile, non evento di ricezione né esito. |
| K-050 | ESPLICITA | I — Observation; D; H5 | COMPLETA | Osservazione della Source distinta da Assertion e non obbligatoria per ogni ingresso. |
| K-052 | ESPLICITA | E — Proposta; I; M | COMPLETA | Proposed è posizione, non Candidate universale. |
| K-053 | ESPLICITA | D; H7; I | COMPLETA | Interpretation Result candidato conserva composizione, alternative e dipendenze. |
| K-054 | ESPLICITA | I — Supporto; J; O | COMPLETA | Supporto qualificato necessario, forma concreta aperta senza Evidence universale. |
| K-055 | ESPLICITA | I; J; M | COMPLETA | Informazioni adiacenti, relazioni epistemiche, operative e inferenziali non ridotte ad Assertion. |
| K-056 | IMPLICITA | I — Referent; I — Elementi | COMPLETA | Locator e risultati indirizzabili distinti dal locus referenziale; il criterio generale indirizzabilità non sufficiente è ricavabile, non formulato. |
| K-057 | ESPLICITA | I — Documenti; H5–H7; J | COMPLETA | Localizzazione, composizione e ruolo semantico hanno produttori e nature distinti. |
| K-058 | ESPLICITA | I — Value | COMPLETA | Necessario contenuto strutturato non referenziale, non primitiva autonoma. |
| K-059 | ESPLICITA | J; G — Storie | COMPLETA | Famiglie semanticamente non intercambiabili. |
| K-061 | ESPLICITA | E; F; I; M | COMPLETA | Commitment, Quality, conflitto, applicabilità e attesa hanno target distinti. |
| K-062 | ESPLICITA | G — Memoria operativa; F | COMPLETA | Work, tentativi e storia decisionale non sostituiti dalla Provenance informativa. |
| K-063 | ESPLICITA | F; H17; I — Informazione negativa | PARZIALE | Esiti operativi e risultato di ricerca sono distinti; non sviluppata la differenza fra output vuoto per successo, insufficienza o fallimento. |
| K-064 | ESPLICITA | G; B; C — Anti-bloat | COMPLETA | Risorse riutilizzabili non sono processi attivi né memorie dei casi. |
| K-067 | ESPLICITA | I — Tempo; H10; F | COMPLETA | Content time, storia epistemica, operativa e reference time espliciti. |
| K-068 | ESPLICITA | I — Tempo; H10 | PARZIALE | Non trasferire date fra ruoli è esplicito; precisione incompleta, anno ignoto e condizioni per confronto determinabile non sono precisati. |
| K-070 | ESPLICITA | I — Tempo; E — Applicabilità; H12 | COMPLETA | Tempo del contenuto, pertinenza per scopo e condizioni della disposizione separati, senza Validity universale. |
| K-071 | ASSENTE | —; G rinvia genericamente al Domain | NON APPLICABILE | Non compare il divieto di estendere automaticamente continuità/durata quando manca la fine; nome Domain non conserva il criterio. |
| K-073 | ESPLICITA | H12; I — Ricostruzione; M | COMPLETA | Ricostruzione per aspetto, tempo, scopo, alternative e limiti; non ultimo valore. |
| K-074 | ESPLICITA | I — Tempo; G — Storie; H12 | PARZIALE | Storie e riferimento temporale presenti; non distinte esplicitamente le due domande sul passato: ciò che sostenevamo allora e ciò che oggi ricostruiamo di allora. |
| K-075 | ESPLICITA | H11–H12; H18; H20; G | PARZIALE | Giustificazioni e conservazione quando necessario presenti; manca il criterio vincolante che l'uso materiale per Decision/spiegazione storica renda recuperabili le basi. |
| K-076 | ESPLICITA | H11; I — Derivation e negativo; J | PARZIALE | Regola, contesto e premesse sono più ampi di sole Assertion in H11; assenze/perimetri come dipendenze inferenziali non esplicitati, mentre J mostra solo Assertion premise_of. |
| K-077 | IMPLICITA | D — accesso a grezzo; I — Informazione negativa | PARZIALE | Natura dei risultati è distinta; non esplicito che nessun riscontro semanticamente riconosciuto possa coesistere con una Source arrivata ma non interpretata. |
| K-078 | ESPLICITA | I — Modalità; H11 | PARZIALE | Normativo e predittivo distinti; manca la separazione operativa fra periodicità osservata, previsione, obbligo e desiderio nella formazione di un'attesa. |
| K-079 | ESPLICITA | H10; F; H19 | PARZIALE | Reference time e Work con condizioni presenti; non assegnata esplicitamente l'attenzione temporale in assenza di nuovi ingressi quando promessa dalla Function. |
| K-080 | ASSENTE | —; F tratta attese operative | NON APPLICABILE | Manca la composizione base dell'attesa–riscontro nel perimetro–comportamento, incluse condizioni e finestra recuperabili per riuso. Work waits_for non la sostituisce. |
| K-081 | ASSENTE | —; C/I/M non trattano Expectation | NON APPLICABILE | Non è riportata la decisione negativa su Expectation e controller temporale universali. La loro sola assenza dall'inventario non conserva il motivo del rifiuto. |
| K-082 | ESPLICITA | D — Riaperture; E — Correzione; H9–H10; J | COMPLETA | Arrivo tardivo, correzione, successione e incompatibilità restano distinti. |
| K-083 | ESPLICITA | H9; J — incompatibilità sotto scope | COMPLETA | Comparabilità semantica preliminare e scelta applicativa separata. |
| K-084 | ESPLICITA | E — Correzione; C — Correction/Supersession; J | COMPLETA | Dichiarazione, riconoscimento e revisione governata distinti. |
| K-085 | ESPLICITA | H13; G — Lineage | PARZIALE | Impatto da dipendenze noto; mancano assenze, perimetri, completezza/continuità e nuovi membri come cause non ricavabili dalle sole premesse positive già collegate. |
| K-086 | ASSENTE | —; H13 | NON APPLICABILE | Non dichiarato che assenza di dipendenza trovata non provi assenza d'impatto, soprattutto con tracce incomplete. |
| K-087 | ESPLICITA | H13; D — Riaperture; E — Impatto | PARZIALE | Esclusa falsità automatica e separato il lavoro, ma il lessico passa da cambiamento a qualificazione del materialmente affetto senza mantenere esplicitamente potenziale / rivalutato-confermato / rivalutato-corretto / non verificato per l'uso. |
| K-088 | ESPLICITA | H13; E; M — Knowledge State | COMPLETA | Non tutto ciò che dipende dal cambiamento è falso; nessun asse globale dello stato. Il nome STALE non è necessario per preservare il confine. |
| K-089 | ESPLICITA | D — Riaperture; E — Impatto; F | COMPLETA | Impatto informativo, scelta operativa e nuova esecuzione distinti. |
| K-090 | ESPLICITA | E — Impatto; G; H13 | PARZIALE | Distinta modifica Mapping da Policy comportamentale; non sviluppati gli effetti diversi di Domain e Core, rinviati genericamente al significato della risorsa. |
| K-091 | ASSENTE | —; G cita Core invariants | NON APPLICABILE | Assente il requisito di una decisione fondazionale esplicita per cambiare un Core invariant e di identificare distinzioni già irrimediabilmente perse. |
| K-092 | ESPLICITA | E — Applicabilità/Impatto; F — Rivalutazione; G | COMPLETA | Decision storica conservata e Policy cambia applicabilità senza riscrivere automaticamente il contenuto. |
| K-093 | ESPLICITA | G — Risorse; H6; H13 | PARZIALE | Versioni e dipendenze materiali registrate; non obbliga esplicitamente a recuperare definizione/parte effettivamente usata oltre l'etichetta di versione. |
| K-094 | ESPLICITA | E — Applicabilità; H16 | COMPLETA | Condizioni correnti, autorità, target e impatti oltre il solo numero di versione; mancata applicazione motivata. |
| K-095 | ESPLICITA | E; F; G — Storie | PARZIALE | Atto, commitment e uso corrente distinti; correttezza procedurale dell'atto e correttezza fattuale non esplicitate come valutazioni indipendenti. |
| K-097 | ESPLICITA | I — Quality; G | COMPLETA | Target, dimensione, base, scopo e storia dell'assessment espliciti. |
| K-098 | ESPLICITA | H5–H8; H11; I — Quality; O | PARZIALE | Assessment estrattivo/referenziale/inferenziale e forma locale presenti; cinque famiglie e relativi confini non ricostruiti interamente. Nessuna promozione dimostrata della tassonomia a definitiva. |
| K-099 | IMPLICITA | E — Impatto/Policy; H14; I — Quality | COMPLETA | Policy sceglie comportamento, Quality resta fondata sulla propria base; prudenza non cambia il giudizio per sola decisione. |
| K-100 | ESPLICITA | H1–H2; I — Supporto; G | PARZIALE | Source/attendibilità tecnica e supporto distinti; non ricostruita la separazione sistematica fra provenienza, integrità/fedeltà e competenza relativa al contenuto. |
| K-101 | ESPLICITA | G — Provenance; I — Supporto; H5; H20 | COMPLETA | D03 generalizzato: copie e derivati utili ma non attestazioni indipendenti per numero. |
| K-102 | ESPLICITA | I — Supporto; O — Quality | PARZIALE | Indipendenza distinta dalla molteplicità, ma non espresso l'esito legittimo indipendenza non determinata. L'apertura di formule/soglie non lo sostituisce. |
| K-103 | ESPLICITA | I — Supporto; O; J | COMPLETA | Target/scope/storia e supporto indirizzabile mantenuti; autonomia/granularità restano aperte. |
| K-104 | ESPLICITA | D; H — obblighi comuni; H7–H8; H15 | COMPLETA | Supporti locali e pertinenti, non costruttore Evidence universale. |
| K-105 | ESPLICITA | G — Provenance, Lineage e storie | COMPLETA | Quattro significati distinti, pur potendo percorrere la stessa storia conservata. |
| K-106 | ESPLICITA | C — Direzioni; G; H — obblighi comuni | COMPLETA | Ogni produttore registra localmente tracce e dipendenze pertinenti. |
| K-107 | ESPLICITA | I — Supporto; H15; J — locator e target | PARZIALE | Target locali presenti; non formulato il criterio minimo dell'unità su cui correzione/conferma/contestazione hanno effetti diversi. |
| K-108 | ESPLICITA | G — Storie; H17; H20; F | PARZIALE | Traversal, spiegazione e rivalutazione separati; non esplicita la possibilità di spiegare senza poter rieseguire né i diversi requisiti di recuperabilità. |
| K-109 | ESPLICITA | G — Risorse; H13 | PARZIALE | Si richiede rilevanza materiale, ma manca il test controfattuale: cosa cambierebbe in significato, giustificazione o scelta fra alternative se la dipendenza cambiasse. |
| K-110 | ESPLICITA | H20; G — traversal | COMPLETA | Nessuna narrazione inventata per supplire a tracce mancanti. |
| K-111 | ESPLICITA | D; F; G; H; I; M | COMPLETA | D04 ripristina nuova base/criterio/contesto materialmente pertinente. |
| K-112 | IMPLICITA | G; H10–H16 | PARZIALE | Confini separati permettono di scomporre regole composite; non esposto il test da applicare prima di assegnare una frase a Domain/Policy. |
| K-113 | ESPLICITA | G — Risorse; H6–H16 | COMPLETA | Ruoli di Core, Domain, Mapping, Quality, meccanismi, Policy ed esecuzione preservati. |
| K-115 | IMPLICITA | D — Proposte; I — Assertion/Supporto; H16 | COMPLETA | Supporto collegato e non incorporato, proposte prima del commitment, Admission non aumenta Quality; possibilità di ipotesi non sostenuta è ricavabile, non illustrata. |
| K-116 | IMPLICITA | D — Riaperture; F — Rivalutazione; I — Supporto | COMPLETA | Stessa origine riusata non diventa nuova fonte; applicato implicitamente al Mapping aggiornato. |
| K-117 | ESPLICITA | E — Correzione; H9; H12 | PARZIALE | Relazione correttiva distinta dalla scelta; manca il divieto specifico di sostituirla con ranking globale, numero delle fonti o recenza. |
| K-121 | ESPLICITA | I — Identifier; G — Schemi | COMPLETA | Schema, valore e assegnazione distinti e correggibili. |
| K-122 | ESPLICITA | I — Identifier; H5–H7 | COMPLETA | Valore osservato e compatibilità di schema precedono l'assegnazione proposta. |
| K-123 | ESPLICITA | H5; I — Identifier | COMPLETA | Originale conservato e nessuna normalizzazione silenziosa; vietato inferire correzione certa dal solo match per i medesimi vincoli, senza esempio specifico. |
| K-124 | ESPLICITA | H6; H8; E; I — Identifier | COMPLETA | Assegnazione e proposta non provano né autorizzano autonomamente coreferenza. |
| K-125 | ESPLICITA | H8; E — Coreferenza | COMPLETA | Alternative, indizi contrari, assessment e Admission distinti dall'identità infallibile. |
| K-126 | ESPLICITA | H8; E — Coreferenza; H19 | COMPLETA | Proposizione identitaria, supporto, uso unitario ed effetti non coincidono. |
| K-127 | ESPLICITA | E; G; H8/H16/H18/H19; I | COMPLETA | D05 preserva differenze e giustificazioni per contestare e separare, entro informazione legittimamente conservata. |
| K-128 | IMPLICITA | E — Coreferenza; I; J | COMPLETA | Proposizione identitaria con posizioni diverse consente incertezza senza predicato nuovo; non nominato il rifiuto di possibly_same_as. |
| K-129 | IMPLICITA | H8; I — Referent/Identifier | COMPLETA | Più indizi e alternative non equiparano stringa e soggetto; il caso omonimia è ricavabile, non esplicito. |
| K-130 | ESPLICITA | I; J; M | PARZIALE | Famiglie e adiacenze impediscono di ridurre tutto ad Assertion; non discusso il caso meta-Assertion che descrive una struttura senza sostituirla. |
| K-131 | ESPLICITA | J; M | COMPLETA | Famiglie non intercambiabili e nessuna struttura tecnica Relation decisa. |
| K-132 | ESPLICITA | I — Value/Referent; J | PARZIALE | Value e Referent distinti; la grammatica J non esplicita relazioni fra due Referent rispetto a Referent–Value e qualificazioni del contenuto completo. |
| K-133 | ESPLICITA | H3; H7–H10; H16; I | COMPLETA | Dedup, composizione, coreferenza documentale e gestione versioni/correzioni distribuite. |
| K-134 | ESPLICITA | D; F; G; N | COMPLETA | Proposte in memoria indipendenti da Work attivo e Admission. |
| K-136 | ESPLICITA | G; I | COMPLETA | Knowledge come corpo governato, con storie raggiungibili e senza duplicazione fisica obbligatoria. |
| K-138 | ESPLICITA | G — Domain; H8/H10; I — Identifier | PARZIALE | Assegnazione temporale esplicita; assente la regola che continuità dipenda dal tipo di soggetto, distinguendo punto, rapporto e contratto o mutamenti descrittivi. |
| K-139 | ESPLICITA | H8; G; I — Supporto | PARZIALE | Attributi, indizi contrari, alternative e assessment presenti; mancano esplicitazione del dato discriminante mancante e indipendenza non determinata. |
| K-140 | ESPLICITA | H18; H19; I — Documenti | COMPLETA | Projection non crea semantica o certezza e non distrugge differenze referenziali. |
| K-143 | ESPLICITA | I — Referent | COMPLETA | Locus interno anche ipotetico/pianificato, non prova di esistenza; FORTE qualifica distinzione, non ontologia definitiva. |
| K-144 | ESPLICITA | D; F; I; N | COMPLETA | Proposte informative prima del commitment e indipendenti da Work. |
| K-146 | ESPLICITA | I — Knowledge; H16; G | COMPLETA | Target Referent/Assertion e memorie adiacenti non ammesse come fatti per sola conservazione. |
| K-147 | ESPLICITA | I — Informazione negativa e modalità | COMPLETA | Descrittivo/normativo/intenzionale/predittivo appartengono al significato, non alla Policy. |
| K-148 | ESPLICITA | C; I — Source/Observation; D | COMPLETA | Adiacenze al Core e nessuna Observation fittizia per ingresso strutturato. |
| K-149 | ESPLICITA | I — Informazione negativa; H17; J | PARZIALE | Quattro forme distinte e ricerca delimitata; non esplicitate le condizioni Domain/supporto necessarie al passaggio dalla ricerca negativa alla negazione sul mondo. |
| K-150 | ESPLICITA | H18; H11; G — giustificazioni | PARZIALE | Aggregazione affidata al ragionamento, con premesse/metodo; non esplicitata conservazione di membership, criteri di inclusione e periodo dell'aggregato. |
| K-151 | IMPLICITA | D; H7; H12; I; O | PARZIALE | Alternative e non fusione presenti; divieto di ammettere congiuntamente alternative mutuamente esclusive non enunciato, solo implicato da coerenza e Comparison. |
| K-152 | ESPLICITA | C; D — Contesto; H8; I; M | COMPLETA | Cicli senza auto-supporto, contesto e dipendenze recuperabili, origine comune e nuova base valutativa. |
| K-156 | ESPLICITA | C — Anti-bloat; H — intro; M; O | COMPLETA | Memorie/obblighi locali non impongono controllori o archivi separati. |
| K-157 | ESPLICITA | Introduzione; N; P | COMPLETA | Provvisorietà, non canonizzazione, fuori MVP e necessità di ulteriori test espliciti. |
| K-158 | ESPLICITA | I — Assertion e commitment; E | COMPLETA | Contenuto, contributo attribuito e commitment distinti senza tre primitive imposte. |
| K-159 | ESPLICITA | I — Supporto; E — Correzione; J | PARZIALE | Attribuzione/supporto/commitment e contributi distinti; non esplicita la regola che rettificare un contributo non rettifichi automaticamente gli altri e l'Assertion ammessa. |
| K-161 | ESPLICITA | D — Riaperture; E — Impatto; H12–H14; M | COMPLETA | Impatto determinato recuperabile e vincolante sull'uso anche senza immediata rivalutazione. |
| K-162 | ESPLICITA | H11; H14; D — Derivazione; M | COMPLETA | Policy governa attivazione/usi, non correttezza inferenziale. |
| K-163 | ESPLICITA | H1; F; K | COMPLETA | Due capacità di ricezione preservate dentro lo stesso raggruppamento. |
| K-164 | ESPLICITA | H2; F — Separazioni | COMPLETA | Ammissibilità tecnica distinta da verità del contenuto. |
| K-165 | ESPLICITA | H3; F — Rivalutazione; D | COMPLETA | Uguaglianza tecnica non equivale a identità; diversa risorsa può generare nuova elaborazione sul materiale conservato. |
| K-166 | ESPLICITA | F; G; M | COMPLETA | Condizioni tecniche e Work separati da proposte/commitment; nessuno staging universale. |
| K-167 | ESPLICITA | H4; D; G | COMPLETA | Preservazione autonoma dal successo semantico, con rappresentazioni e criteri autorizzativi. |
| K-168 | ESPLICITA | C — Estrazione; H5; H — obblighi comuni | COMPLETA | Sottocapacità distinte, grezzo, localizzazione, risultati parziali, assessment e Lineage. |
| K-169 | ESPLICITA | H5; F; G | PARZIALE | Testo nativo/OCR distinti e letture storiche; omesso il limite per cui il testo incorporato può non corrispondere alla rappresentazione visuale. |
| K-170 | ESPLICITA | H5–H7; I — Documenti | PARZIALE | Layout/struttura/parsing conservati e separati dal significato; non dettagliato il passaggio di un'ambiguità non solo sintattica all'Interpretation. |
| K-171 | ESPLICITA | H6–H7; I — Documenti | PARZIALE | Classificazione contestuale e Source multi-documento presenti; non esplicito che il tipo del contenitore non si trasferisca alle porzioni. |
| K-172 | ESPLICITA | H6–H7; G | COMPLETA | Applicabilità/versione Mapping e composizione semantica con confini distinti. |
| K-173 | ESPLICITA | H — obblighi comuni; H9; H16; M | COMPLETA | Validazioni locali, confronto e applicabilità, senza validatore universale. |
| K-174 | ESPLICITA | C — Anti-bloat; H8–H13; M | COMPLETA | Core Engine solo nome di famiglia, non autorità aggiuntiva. |
| K-175 | ESPLICITA | D — Contesto; H17; G | COMPLETA | Query di tutte le nature, scope, autorizzazioni e traversal; contesto usato recuperabile. |
| K-176 | ESPLICITA | H15; F — Verifica; H22 | COMPLETA | Domanda, target, risposta, attesa e ruolo della verifica distinti da Admission. |
| K-177 | ESPLICITA | H18–H21; D; F | COMPLETA | Problemi di organizzazione, spiegazione, uso ed espressione distinti, senza nuova semantica implicita. |
| K-178 | ESPLICITA | H22; D; E — Ownership | COMPLETA | Intake preserva e instrada senza sovrascrittura o proprietà automatica della Decision. |
| K-179 | ESPLICITA | G — Accesso; H1/H15/H22 | PARZIALE | Autorizzazioni presenti; non esplicita la distinzione fra account/attore e persona rappresentata né il divieto di inferire permessi dalla coreferenza. |
| K-180 | ESPLICITA | C — Trasversali; G; H4; O | PARZIALE | Accesso, sicurezza, privacy, conservazione/ripristino nominati; non esplicitati effetti della cancellazione sulla verificabilità e ripristino dei collegamenti oltre i file. |
| K-181 | ESPLICITA | G — Audit operativo; F | PARZIALE | Storia operativa distinta da epistemica; manca la distinzione audit/indicatori di osservabilità del funzionamento. |
| K-182 | ESPLICITA | A; H — intro; K; L; O | COMPLETA | Checklist 24 non è inventario software; capacità locali e responsabilità preservate. Non prova però copertura di ogni guardrail del Ledger. |
| K-184 | IMPLICITA | P; M; Delta finale | COMPLETA | D01–D05 verificati puntualmente; il criterio generale che nominare una risorsa non preservi tutti i suoi vincoli è applicato ma non enunciato. |
| K-186 | ESPLICITA | I — Legenda; I — Value; O | COMPLETA | FORTE distinto da primitiva autonoma; CANDIDATO non rende opzionale la responsabilità. |
| K-187 | ESPLICITA | H1; K; A | COMPLETA | Due capacità interne con output/storie distinti: accorpamento organizzativo legittimo. |
| K-188 | ESPLICITA | P; Delta finale; E/O | COMPLETA | Cinque recuperi integrati e D06 ancora aperto; gate limitato alla review e non canonizzazione. |

## 2. Controllo inverso — v2 → Ledger

Le ricorrenze dello stesso vincolo in più viste sono raggruppate, non contate come nuove conoscenze. L'indice copre principio organizzativo, percorsi, 22 schede, elementi informativi, risorse, memorie, relazioni, anti-regressione e gate.

| ID | Affermazione strutturale v2 | Dove | Classificazione | Ledger | Motivazione / limite |
|---|---|---|---|---|---|
| V-001 | Opzione 3: mappa per nature e viste separate | A–C | ASSEMBLY CHOICE | K-001, K-047, K-064, K-182 | Scelta di esposizione fra tre opzioni; non nuova responsabilità o semantica. |
| V-002 | Sette gruppi nell'albero, non componenti aggiuntivi | C | ASSEMBLY CHOICE | K-047, K-156, K-182 | Conteggio e posizione organizzano nature già distinte. |
| V-003 | Viste non runtime obbligatorio e accessi laterali | B; D | SUPPORTED BY LEDGER | K-001, K-003, K-033, K-134 | Non trasforma l'ingresso in pipeline universale. |
| V-004 | Separazione informazione/attività/risorse/governance/operatività/uso | B; C | SUPPORTED BY LEDGER | K-003, K-011, K-015, K-059, K-061–K-064, K-177 | Memorie non rendono equivalenti le nature. |
| V-005 | Core Engine solo famiglia; correzione distribuita | C; H; M | SUPPORTED BY LEDGER | K-082–K-084, K-133, K-174 | Non un proprietario semantico universale. |
| V-006 | Base umana ricevuta distinta da interpretazione e autorità | D; H22; I | SUPPORTED BY LEDGER | K-035–K-039, K-158–K-159, K-178 | Recupero D01, nessuna Observation/Source universale imposta. |
| V-007 | Riuso del contesto non genera auto-supporto | C; D; H7; I | SUPPORTED BY LEDGER | K-021, K-101, K-111, K-152 | Cicli ammessi, falsa indipendenza esclusa. |
| V-008 | Conclusione derivata su richiesta senza Admission implicita | D; H11; N | SUPPORTED BY LEDGER | K-003, K-033, K-075–K-076, K-162 | Uso qualificato distinto da commitment. |
| V-009 | Riapertura da nuove informazioni, ritardi, rettifiche o risorse | D | SUPPORTED BY LEDGER | K-082, K-085–K-094, K-161 | Non implica nuova acquisizione né ricalcolo già avvenuto. |
| V-010 | Decision, Disposition, Admission e Application distinte | E | SUPPORTED BY LEDGER | K-015–K-019, K-146, K-158 | Admission applicata ha effetto governato e storia operativa. |
| V-011 | Decision da Policy oppure autorità esplicita | E; H14 | SUPPORTED BY LEDGER | K-016, K-185 | Pluralità delle origini autorizzative acquisita. |
| V-012 | Assenza di un'origine decisionale obbligatoria unica, nel contesto di E | E — Origine della Decision | SUPPORTED BY LEDGER | K-016, K-017, K-185 | «Non esiste un produttore universale» è letto nel contesto dei due percorsi di autorità, non come divieto definitivo di formalizzazione comune. E/O mantengono D06 aperto: la lettura più forte non è una conclusione acquisita. |
| V-013 | Non-Policy ownership esplicitamente aperta | E; H14; H22; O | SUPPORTED BY LEDGER | K-185 | La memoria è obbligatoria; non si inventa Decision Manager. |
| V-014 | Proposta, supporto, contestazione e commitment non equivalenti | E; I | SUPPORTED BY LEDGER | K-052, K-061, K-084, K-158–K-159 | Uso autorizzato non elimina la contestazione. |
| V-015 | Coreferenza non distruttiva, revisionabile e separabile | E; G; H8; I | SUPPORTED BY LEDGER | K-126–K-127, K-180 | D05; limiti di conservazione non sono funzione software unmerge. |
| V-016 | Applicabilità corrente prima dell'effetto, senza disposizione inventata | E; H16 | SUPPORTED BY LEDGER | K-018, K-025, K-094 | Copertura del principio; limite sul già applicato nella forward K-018. |
| V-017 | Impatto noto vincola usi anche se Policy rinvia il lavoro | E; H12–H14 | SUPPORTED BY LEDGER | K-161 | Distinto dalla diagnosi del contenuto già rivalutato, compressa rispetto a K-087. |
| V-018 | Acquisition può concludersi senza Work o alimentarne uno esistente | F | SUPPORTED BY LEDGER | K-008, K-011–K-012, K-041 | Ricezione e durata del lavoro indipendenti. |
| V-019 | Work con owner, dipendenze, Attempt, attesa e ripresa | F | SUPPORTED BY LEDGER | K-007, K-011–K-013, K-062, K-166 | Non primitive autonome né stato epistemico. |
| V-020 | Domanda/risposta possono sbloccare il lavoro senza confermare il contenuto | F | SUPPORTED BY LEDGER | K-019, K-035–K-039, K-063, K-176 | Seguito operativo non verità. |
| V-021 | Rivalutazione produce nuovi risultati senza riscrivere esiti storici | F | SUPPORTED BY LEDGER | K-013, K-025, K-087, K-092, K-111 | Il tentativo non genera nuova forza epistemica. |
| V-022 | Nove righe di risorse di riferimento | G | SUPPORTED BY LEDGER | K-064, K-090–K-094, K-113, K-172, K-179–K-180 | Core/invariants, Domain/schemi, Mapping, Quality, Policy, criteri d'uso/accesso sono già acquisiti. |
| V-023 | Partizione grafica fra memorie informative e operative | G | ASSEMBLY CHOICE | K-003, K-062, K-105, K-134, K-136, K-156 | Layout organizza responsabilità; non archivi tecnici separati. |
| V-024 | Contributi, supporti, assessment, proposte e giustificazioni conservabili | G | SUPPORTED BY LEDGER | K-054, K-075–K-076, K-097, K-103–K-109, K-134, K-159 | Il bisogno esiste, ma alcuni criteri di conservazione sono compressi nella forward. |
| V-025 | Provenance, Lineage, storia epistemica e audit operativo | G | SUPPORTED BY LEDGER | K-105–K-106, K-181 | Stessa storia percorribile con significati differenti. |
| V-026 | Dipendenza non implica inutilità del contributo | G; I | SUPPORTED BY LEDGER | K-101–K-102, K-159 | Leggibilità/precisione possono migliorare senza indipendenza. |
| V-027 | H1 Ricezione tracciata con due capacità interne | H1; K | ASSEMBLY CHOICE | K-163, K-187 | Il raggruppamento è organizzativo; output e responsabilità erano già distinti. |
| V-028 | H2 Validazione tecnica | H2 | SUPPORTED BY LEDGER | K-041, K-164 | Controlli tecnici non verità. |
| V-029 | H3 Deduplicazione tecnica | H3 | SUPPORTED BY LEDGER | K-028, K-165 | Non identità documentale o equivalenza delle Assertion. |
| V-030 | H4 Preservazione delle Source | H4 | SUPPORTED BY LEDGER | K-041, K-049, K-167, K-180 | Originale e rappresentazioni indipendenti dall'interpretazione. |
| V-031 | H5 Estrazione con sottocapacità e risultati locali | H5 | SUPPORTED BY LEDGER | K-050, K-097, K-106, K-168–K-170 | Accorpamento già candidato nell'Audit. |
| V-032 | H6 Mapping applicabile con risorse e Lineage | H6 | SUPPORTED BY LEDGER | K-090, K-113, K-172 | Corrispondenza non ammissione o identità. |
| V-033 | H7 Composizione semantica e classificazione/document composition | H7 | SUPPORTED BY LEDGER | K-009–K-010, K-053, K-057, K-133, K-144, K-171–K-172 | Output proposto, alternative e attribuzioni. |
| V-034 | H8 Identity Reconciliation | H8 | SUPPORTED BY LEDGER | K-121–K-129, K-139 | Proposte e giustificazioni, non merge distruttivo. |
| V-035 | H9 Comparison, conflitto come specializzazione | H9 | SUPPORTED BY LEDGER | K-082–K-084, K-117, K-174 | Comparabilità e comportamento distinti. |
| V-036 | H10 Temporal Evaluation | H10 | SUPPORTED BY LEDGER | K-067–K-071, K-082 | Ruoli e riferimento temporale; non aggiunge trigger autonomo. |
| V-037 | H11 Derivation | H11 | SUPPORTED BY LEDGER | K-075–K-076, K-150, K-162 | Conclusione e giustificazione senza Policy semantica. |
| V-038 | H12 Current Reconstruction | H12 | SUPPORTED BY LEDGER | K-073–K-075, K-161 | Uso contestualizzato, non ultimo valore. |
| V-039 | H13 Impact Assessment | H13 | SUPPORTED BY LEDGER | K-085–K-089, K-161 | Responsabilità sostenuta; formulazione compressa nel grado d'impatto. |
| V-040 | H14 Policy Evaluation | H14 | SUPPORTED BY LEDGER | K-014–K-016, K-113, K-162 | Decision motivata, non unica autorità. |
| V-041 | H15 Verification | H15 | SUPPORTED BY LEDGER | K-019, K-035–K-039, K-111, K-176 | Target e contesto, non Admission. |
| V-042 | H16 Admission/revisione | H16 | SUPPORTED BY LEDGER | K-018, K-094, K-127, K-146, K-158 | Applica commitment autorizzato e registra effetto. |
| V-043 | H17 Query con traversal | H17 | SUPPORTED BY LEDGER | K-033–K-034, K-108, K-149, K-175 | Accesso a tutte le nature, scope e risultati negativi. |
| V-044 | H18 Projection | H18 | SUPPORTED BY LEDGER | K-140, K-150, K-177 | Organizzazione senza aggregazione semantica implicita. |
| V-045 | H19 Functions | H19 | SUPPORTED BY LEDGER | K-007, K-015, K-079, K-127, K-177 | Realizzano casi d'uso, non controllore universale. |
| V-046 | H20 Explanation | H20 | SUPPORTED BY LEDGER | K-101, K-108, K-110, K-177 | Spiegazione sulla storia reale. |
| V-047 | H21 Presentation | H21 | SUPPORTED BY LEDGER | K-140, K-161, K-177 | Espressione fedele a contenuti e qualificazioni. |
| V-048 | H22 Intake utente | H22 | SUPPORTED BY LEDGER | K-035–K-039, K-178, K-185 | Base originaria preservata e instradamento contestualizzato. |
| V-049 | H: assessment, validazione, supporto e Provenance distribuiti | H — premessa; M | SUPPORTED BY LEDGER | K-020, K-104, K-106, K-156, K-173 | Obblighi locali, nessun nuovo controllore. |
| V-050 | 22 schede e 24 responsabilità tracciate | K | ASSEMBLY CHOICE | K-182–K-183, K-187 | Conteggio di esposizione dopo raggruppamenti, non nuova ontologia. |
| V-051 | Referent locus interno, non prova di esistenza | I — Referent | SUPPORTED BY LEDGER | K-143 | Include proposto, ipotizzato e pianificato. |
| V-052 | Assertion portatrice di contenuto, non commitment incorporato | I — Assertion | SUPPORTED BY LEDGER | K-055, K-158 | Raffinamento del controllo finale. |
| V-053 | Value strutturato non referenziale, autonomia non acquisita | I — Value | SUPPORTED BY LEDGER | K-058, K-186 | FORTE qualifica la distinzione. |
| V-054 | Identifier schema/valore/assegnazione, ontologia aperta | I — Identifier; O | SUPPORTED BY LEDGER | K-121–K-124, K-141 | Originale recuperabile e assegnazione temporale. |
| V-055 | Temporalità qualificata e nessuna Validity universale | I — Tempo | SUPPORTED BY LEDGER | K-067–K-070 | Distinzione forte; altre regole temporali omesse nella forward. |
| V-056 | Source adiacente, non solo file né evento | I — Source/Documenti | SUPPORTED BY LEDGER | K-028, K-049, K-148 | Origine contenutistica e ricezione separabili. |
| V-057 | Observation da osservazione, non Assertion | I — Observation | SUPPORTED BY LEDGER | K-050, K-148 | Non pedaggio universale degli ingressi. |
| V-058 | Interpretation Result candidato | I — Elementi | SUPPORTED BY LEDGER | K-053 | Forma candidata, alternative necessarie. |
| V-059 | Locator/anchor candidato | I — Elementi/Documenti | SUPPORTED BY LEDGER | K-031–K-032, K-057 | Porzione recuperabile senza primitiva documentale imposta. |
| V-060 | Contributo attribuito e supporto qualificato distinti | I — Supporto | SUPPORTED BY LEDGER | K-054, K-103, K-158–K-159 | Forma autonoma supporto ancora aperta K-065. |
| V-061 | Quality locale storica e nuova giustificazione | I — Quality | SUPPORTED BY LEDGER | K-097–K-099, K-111 | Non score globale né aumento tramite Admission. |
| V-062 | Provenance/Lineage forti ma non controllore centrale | I; G | SUPPORTED BY LEDGER | K-105–K-109, K-156 | Forza della distinzione, non separazione software. |
| V-063 | Derivation record/justification | I — Elementi | SUPPORTED BY LEDGER | K-075–K-076, K-162 | Premesse, metodo, contesto e conclusione. |
| V-064 | Risultato negativo delimitato e quattro nature negative | I — Negativo | SUPPORTED BY LEDGER | K-034, K-077, K-149 | Nessuna negazione globale dal solo vuoto. |
| V-065 | Qualificazione d'impatto forte | I — Elementi | SUPPORTED BY LEDGER | K-161 | Non cancellabile tramite Policy. |
| V-066 | Ricostruzione contestualizzata candidata | I — Elementi | SUPPORTED BY LEDGER | K-073–K-075, K-186 | Responsabilità necessaria, forma candidata. |
| V-067 | Proposed e Knowledge governata | I; E | SUPPORTED BY LEDGER | K-052, K-134, K-136, K-144, K-146 | Memoria informativa più ampia della Knowledge. |
| V-068 | Work durevole candidato, granularità aperta | I; O | SUPPORTED BY LEDGER | K-012, K-026, K-166 | Nessun Work obbligatorio per ogni attività. |
| V-069 | Documento eventuale Referent, Source/documenti molti-a-molti | I — Documenti | SUPPORTED BY LEDGER | K-028–K-032, K-133 | Non Logical Document universale. |
| V-070 | Modalità descrittiva/normativa/intenzionale/predittiva | I — Modalità | SUPPORTED BY LEDGER | K-147 | Non diventa ordine applicativo. |
| V-071 | CALLS, READS, WRITES, PRODUCES | J — Grammatica attività | SUPPORTED BY LEDGER | K-002, K-005 | Relazioni distinte acquisite nel R1. |
| V-072 | CONSULTS separato in tabella da READS | J — Grammatica attività | ASSEMBLY CHOICE | K-004, K-064 | Etichetta organizzativa per risorse; diverge dalla preferenza R1, senza nuova semantica dimostrata. |
| V-073 | REACTS_TO e CONSTRAINED_BY | J — Grammatica attività | SUPPORTED BY LEDGER | K-006 | Attivazione possibile e vincolo distinti; EMITS non recuperato. |
| V-074 | MAY_OPEN_WORK come etichetta propria | J — Grammatica attività | ASSEMBLY CHOICE | K-007, K-012, K-016, K-089 | Nome di assemblaggio per apertura condizionata già ammessa; non nuova autorità. |
| V-075 | Famiglie descrittive, epistemiche, rappresentative, inferenziali, operative | J — Grammatica informativa | SUPPORTED BY LEDGER | K-059, K-131, K-158–K-159 | Nessuna forma tecnica universale decisa. |
| V-076 | Localizzazione, assessment e impatto come relazioni qualificate | J | SUPPORTED BY LEDGER | K-057, K-097, K-103, K-161 | Non una nuova famiglia software. |
| V-077 | Correzione dichiarata distinta dall'effetto di governance | J; E | SUPPORTED BY LEDGER | K-084, K-117, K-159 | Correzione non successione né uso implicito. |
| V-078 | Nessuna responsabilità necessaria v1 persa, nel perimetro dell'audit 34 | L | SUPPORTED BY LEDGER | K-182 | È l'esito storico dell'audit delle responsabilità, non prova della copertura di tutte le 188 conoscenze. |
| V-079 | No Candidate/Knowledge State/Validity/Relation/Evidence universali | M | SUPPORTED BY LEDGER | K-047, K-052, K-054, K-059, K-061, K-070 | Decisioni negative acquisite. |
| V-080 | No orchestratore, Quality controller, Provenance Recorder o Candidate Validator universali | M | SUPPORTED BY LEDGER | K-009, K-020, K-104, K-106, K-173–K-174 | Distribuzione delle responsabilità non loro cancellazione. |
| V-081 | No Logical Document obbligatorio, dedup-identità, Admission-verità o Work-epistemica | M | SUPPORTED BY LEDGER | K-011, K-030, K-061, K-124, K-158, K-165 | Guardrail storici. |
| V-082 | D01–D05 presenti nel check anti-regressione | M; P; Delta | SUPPORTED BY LEDGER | K-035, K-021, K-101, K-111, K-127, K-184, K-188 | Recuperi giustificati; la verifica odierna conferma il contenuto, non tutta la coverage. |
| V-083 | Aperti di equivalenza, accorpamenti, Identifier, supporto e Work | O | SUPPORTED BY LEDGER | K-026, K-065, K-141, K-160, K-183 | Default conservativi; non chiusi per comodità. |
| V-084 | Aperti su identità/versione, algoritmi, Quality, software/storage | O | SUPPORTED BY LEDGER | K-032, K-046, K-096, K-118–K-119, K-141–K-142, K-156 | Non ogni apertura storica è elencata; controllo supplementare sotto. |
| V-085 | D06 aperto senza soluzione introdotta | O; P | SUPPORTED BY LEDGER | K-185, K-188 | Non si assegna per supposizione l'ownership. |
| V-086 | Gate di review non implica readiness implementativa | N; P | SUPPORTED BY LEDGER | K-157, K-188 | Il gate dell'assemblaggio è riportato come storico, non nuovo esito dell'audit attuale. |
| V-087 | V2 leggibile autonomamente come anatomia | P | ASSEMBLY CHOICE | K-182, K-188 | Obiettivo editoriale; non equivale a memoria esaustiva delle conoscenze conquistate. |

## 3. Aperture: non confondere omissione e risoluzione

Le 14 voci APERTA non entrano nel conteggio forward. La tabella verifica se la v2 le rende visibili o se la loro chiusura rischia di essere presunta. **Non ribadita** non significa automaticamente **chiusa**.

| K-ID | Dove nella v2 | Esito | Nota |
|---|---|---|---|
| K-026 | F; O; P | PARZIALMENTE RIBADITA | Granularità Work/software aperte; contratti per risultati parziali, retry e percorsi MVP non riepilogati in dettaglio. Non risultano chiusi. |
| K-032 | I; O | PARZIALMENTE RIBADITA | Locator candidato e criteri documentali aperti; forma della composizione non interamente ripresa. |
| K-046 | H1/H15; O | NON RIBADITA SPECIFICAMENTE | Contratti acquisizione/verifica/domande multiple non definiti; fuori scope tecnico non equivale a chiusura concettuale. |
| K-065 | I; O | ESPLICITAMENTE APERTA | Forma concreta del supporto indirizzabile rinviata. |
| K-066 | I — Assertion; O | CHIUSURA NON DIMOSTRATA | La meta-Assertion su interpretazioni non è discussa esplicitamente; non considerarla risolta solo dalla definizione generale. Dubbio genealogico dichiarato nel Ledger. |
| K-096 | O; H10–H13 | PARZIALMENTE RIBADITA | Regole temporali specifiche, retention ulteriore e rivalutazione non tutte nominate come aperte; nessuna soluzione completa esplicita. |
| K-118 | O — Quality | PARZIALMENTE RIBADITA | Formule/soglie aperte; criteri empirici di indipendenza e articolazione delle dimensioni non interamente riassunti. |
| K-119 | D; G; O | PARZIALMENTE RIBADITA | Memoria delle proposte chiarita; storage aperto. Forma della conferma di Observation non ripresa. |
| K-141 | I; O | ESPLICITAMENTE APERTA | Ontologia Identifier aperta; criteri specifici rimangono Domain/algoritmi, non universalmente decisi. |
| K-142 | I; J; O | ESPLICITAMENTE APERTA | Criteri documentali aperti; J non decide struttura tecnica comune Relation. |
| K-145 | H16; I; O | CHIUSURA NON DIMOSTRATA | Target Referent nominato, ma nessun criterio completo per ammissione senza Assertion già ammessa. Non confondere naming del target con risoluzione. |
| K-160 | I; O | ESPLICITAMENTE APERTA | Equivalenza e condivisione di Assertion rinviate, con default non-fusione. |
| K-183 | A; H; O | ESPLICITAMENTE APERTA | Granularità dei raggruppamenti non congelata. |
| K-185 | E; H14; H22; N; O; P | ESPLICITAMENTE APERTA | D06 riconoscibile, senza proprietario inventato. |

## 4. Candidate: verifica delle promozioni implicite

FORTE nello snapshot significa forza della distinzione, non Canonical né primitiva autonoma. Lo status del Ledger registra il grado raggiunto nel percorso; l'adozione di una forma per la candidata non ne prova l'universalità.

| K-ID | Dove nella v2 | Esito | Nota |
|---|---|---|---|
| K-004 | J | FORMULAZIONE CAMBIATA | CONSULTS distinto da READS; variazione organizzativa, non promozione ontologica. |
| K-006 | J | PARZIALMENTE RIPRESA | Reazione/vincolo sì, emissione non distinta. |
| K-012 | I; O | STATUS PRESERVATO | Work CANDIDATO, granularità aperta. |
| K-023 | — | OMESSA | Test di parallelizzabilità non conservato; non dichiarato superato. |
| K-029 | I | STATUS PRESERVATO | Documento come Referent CANDIDATO. |
| K-053 | I | STATUS PRESERVATO | Interpretation Result CANDIDATO. |
| K-080 | — | OMESSA | Composizione dell'attesa non conservata; nessuna decisione contraria. |
| K-098 | G; H; I; O | TASSONOMIA NON CONGELATA | Località forte, numero/confini delle cinque famiglie non resi definitivi. |
| K-136 | I | STATUS PRESERVATO | Knowledge come corpo governato CANDIDATO. |
| K-143 | I | NESSUN UPGRADE ONTOLOGICO DIMOSTRATO | Referent FORTE per distinzione; definizione adottata nella candidata non equivale a Core canonico. |
| K-146 | H16; I | DEFINIZIONE ADOTTATA, NON CANONICA | Target espliciti dentro anatomia candidata; criteri del caso residuo K-145 non risolti. |
| K-148 | C; I | NESSUN UPGRADE ONTOLOGICO DIMOSTRATO | Source/Observation FORTE per distinzione; adiacenza non impone primitive o moduli. |
| K-168 | H5; H premessa; O | STATUS PRESERVATO | Autonomia del problema, raggruppamento ancora provvisorio. |
| K-182 | A; K; O | STATUS PRESERVATO | 24 come checklist, non numero finale di componenti. |
| K-187 | A; H1; K | SCELTA ADOTTATA SOLO PER LA CANDIDATA | Accorpamento di esposizione non chiude la granularità futura. |

## 5. Posizioni superate: verifica di non reintroduzione

| Posizione storica | Sostituita / circoscritta da | Riscontro nello snapshot |
|---|---|---|
| K-017 — Formalizzazione non-Policy assegnata al responsabile del flusso | K-185 | E/O mantengono D06 aperto; non reintroducono assegnazione completa a Function/Verification. |
| K-048 — Source definita come materiale ricevuto/preservato/utilizzabile | K-049 | I distingue origine contenutistica da esiti della ricezione. |
| K-051 — Candidate come natura unica per proposte, incompletezza e bundle | K-052 | E/I/M: Proposed non è natura universale. |
| K-060 — Knowledge State come stato globale unitario | K-061 | E/F/I/M: qualificazioni su bersagli distinti. |
| K-069 — Validity come contenitore di verità, periodo e utilizzabilità | K-070 | I/M: nessuna Validity universale. |
| K-072 — Current-State Derivation come nome sempre derivativo | K-073 | H12/I/M: Current Reconstruction contestualizzata. |
| K-114 — Regola assoluta: ogni Assertion deve già avere supporto | K-115 | D/I: proposte e supporto non coincidono; nessuna evidenza fabbricata da Admission. |
| K-120 — Referent come soggetto della realtà/documentale con identità indipendente | K-143 | I: locus interno, anche ipotizzato o pianificato. |
| K-135 — Knowledge intesa come solo insieme di Assertion ammesse | K-136 | I/G: Referent e Assertion ammessi nel corpo governato. |
| K-137 — Ammissione di Referent e proposte referenziali: apertura R5 | K-144 | D/I conservano proposta pre-Admission; il residuo K-145 non è dichiarato risolto. |
| K-153 — Formula R6: Policy può ignorare l'impatto | K-161 | E/H13/M: impatto determinato non cancellabile dalla Policy. |
| K-154 — Formula R6: Policy decide se applicare una derivazione | K-162 | H11/M: Policy non governa validità inferenziale. |
| K-155 — Assertion R6 ancora sovrapposta a claim e commitment | K-158 | I/E: contenuto, contributo e commitment distinti. |

## 6. Dubbi storici e limiti del risultato

1. **D06 / K-017 → K-185:** R1 conteneva una proposta generale di ownership del flusso. Il Regression Audit dichiara incompleta l'assegnazione concreta, soprattutto dalla baseline R6/Audit. Il Ledger conserva entrambe le posizioni e non trasforma l'indeterminatezza finale in un'assenza di ragionamento precedente.
2. **K-066 e K-145:** non è verificata una chiusura esplicita dei due casi specifici. Le definizioni generali successive non bastano a dimostrarla. Le aperture sono mantenute con questa riserva, non elevate a nuovi bloccanti.
3. Le fonti primarie dei Round sono messaggi originali recuperati dalla sessione locale, con ordinal e hash nel Ledger. Gli allegati di richiesta, da soli, non sarebbero stati sufficienti a ricostruire le risposte: non sono stati usati come sostituti delle conclusioni.
4. Nessuna ricerca o critica successiva al perimetro stabilito ha introdotto nuove conoscenze nel Ledger. Le classificazioni di questa Coverage Map sono esiti dell'attuale verifica documentale, non nuove regole del prodotto.
5. Non sono stati eseguiti test di comportamento del software: nessun comportamento è stato implementato. La copertura misura quanto il documento conserva, non la qualità empirica di un futuro sistema.

## 7. Controlli finali e perimetro delle modifiche

- Corpo dello snapshot confrontato con il messaggio originale mediante SHA-256; wrapper e metadati sono esterni al corpo.
- Ledger costruito dalle dieci fonti cronologiche indicate nel proprio registro, con 188 ID unici, campi richiesti, origini, vincoli e rinvii di superamento.
- Decisioni negative presenti: 37; posizioni superate conservate: 13. Tutti i rinvii a K-ID verificati.
- Ledger completato e salvato prima della coverage; hash al confine di fase riportato sopra.
- Forward: 161 ID attivi, ciascuno una sola volta; nessuna voce aperta o superata inserita per errore.
- Reverse: 87 unità verificate; 14 aperture e 15 candidate controllate separatamente.
- Nessuna discrepanza ha modificato lo snapshot o generato una v2.1.
- Solo i tre artefatti di questa richiesta sono stati creati in `docs/ricerca/`; nessun documento preesistente modificato.
- Nessuna modifica a Linear o Notion; nessun commit, push o branch.

Lo snapshot resta storico; il Ledger è la memoria genealogica; questa mappa è la verifica fra i due. Una futura revisione deve trattare le discrepanze esplicitamente, non dedurre che ciò che manca nella v2 sia stato abbandonato.
