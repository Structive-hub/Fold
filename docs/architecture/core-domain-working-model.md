# Core e Dominio — working model esplorativo

**Status:** Draft  
**Data:** 2026-08-30  
**Scope:** modello di lavoro per guidare l'analisi di FOL-13 e il confronto con Codex; non è una specifica implementabile e non autorizza scelte tecnologiche

## Perché esiste questo documento

Durante il lavoro sul nucleo informativo di Fold è emersa una difficoltà concettuale: `Core` e `Domain` rischiavano di essere descritti come due versioni dello stesso problema.

La discussione ha progressivamente distinto almeno quattro responsabilità:

1. rappresentare in modo trasversale ciò di cui il sistema parla;
2. dare significato specifico a quella rappresentazione in un dominio;
3. rappresentare che cosa il sistema sostiene di sapere e perché;
4. operare sulla conoscenza risultante.

Le ricerche in `docs/ricerca/fondamenti-rappresentazione-conoscenza.md` e `docs/ricerca/esempio-operativo-core-dominio.md` sostengono la realtà di molti dei problemi coinvolti, ma non dimostrano che il raggruppamento proposto qui sia la struttura definitiva di Fold.

Questo documento conserva il percorso, le ipotesi e soprattutto le questioni da falsificare.

## Stato epistemico

### Sufficientemente supportato dalla ricerca

- dato, record o documento non coincidono automaticamente con la realtà rappresentata;
- realtà e affermazione sulla realtà possono dover restare distinguibili;
- identificatore e identità non coincidono in generale;
- validità nel mondo e momento della conoscenza possono divergere;
- conflitto, correzione e cambiamento reale sono fenomeni differenti;
- provenienza, evidenza e derivazione possono richiedere distinzioni separate;
- il significato di una relazione e i suoi vincoli possono dipendere dal dominio;
- un motore generico non può inventare la semantica di dominio necessaria a decidere che due valori siano incompatibili;
- mapping fra struttura sorgente e rappresentazione semantica è una responsabilità distinta dal contenuto della sorgente stessa;
- stato corrente, storia e conoscenza completa non devono essere considerati automaticamente equivalenti.

### Ipotesi ancora aperte

- che il Core possieda due famiglie distinte di primitive, una relativa alla realtà rappresentata e una relativa alla conoscenza del sistema;
- che le primitive candidate siano precisamente `Referent`, `Relation`, `Property`, `Value`, `Identifier`, `Assertion`, `Evidence`, `Validity`, `Verification`, `Derivation` o equivalenti;
- che tutti questi concetti appartengano al Core e non siano in parte strutture derivate;
- che `Core Model` e `Core Engine` siano i nomi o i confini corretti;
- dove vivano esattamente regole, mapping, politiche di selezione e criteri di autorità delle fonti;
- quali meccanismi siano realmente cross-domain;
- quando eventi, processi, stati o situazioni debbano diventare concetti espliciti;
- quale tecnologia o formalismo possa implementare il modello.

## Evoluzione del modello mentale

### Prima formulazione

La prima rappresentazione didattica era lineare:

```text
dato
↓
primitive della realtà + dominio
↓
primitive della conoscenza
↓
meccanismi
```

È utile per distinguere i problemi, ma rischia di suggerire un'architettura sequenziale non dimostrata.

### Correzione

La ricerca successiva su mapping, ontology-based data access e sistemi semantic-driven suggerisce di trattare questi elementi come responsabilità che collaborano:

```text
Source / Extraction
Mapping / Interpretation
Core Model
Domain Model
Knowledge
Core Engine
Views / Functions
```

Non sono necessariamente sette stadi runtime.

`Core Model` e `Domain Model` possono essere risorse semantiche consultate durante interpretazione e ragionamento. `Mapping / Interpretation` collega ciò che proviene dalle sorgenti al significato interno. `Core Engine` opera sulla conoscenza strutturata usando anche semantica e regole appropriate.

## Significato provvisorio delle responsabilità

### Source / Extraction

Conserva ciò che una sorgente effettivamente fornisce e ciò che viene estratto da essa.

Regola importante emersa dalla discussione:

> Non considerare mai un dato in ingresso come già collegato alla conoscenza interna soltanto perché il formato sorgente contiene etichette o struttura.

Per esempio un documento può contenere:

```text
ID: P-204
Vibrazione: 8,2 mm/s
Ora rilevazione: 10:30
```

La parola `Vibrazione` è un indizio semantico presente nella sorgente. Non significa ancora che Fold abbia stabilito canonicamente quale referente, proprietà o relazione rappresenti.

La sorgente deve restare recuperabile come evidenza dell'interpretazione effettuata.

### Mapping / Interpretation

Responsabilità candidata a collegare struttura e lessico della sorgente a significati utilizzabili internamente.

Domande ancora aperte:

- quali parti del mapping descrivono soltanto la sorgente?
- quali richiedono conoscenza del Domain?
- quali richiedono capacità del Core Model?
- chi decide che un valore si riferisce a un referente già conosciuto?
- come viene rappresentata l'incertezza del mapping?

Il mapping non deve essere confuso con il Domain: può cambiare quando cambia la sorgente mantenendo invariato il significato del dominio.

### Core Model

Ipotesi: grammatica trasversale minima con cui Fold può rappresentare conoscenza indipendentemente dal dominio specifico.

Non è ancora stabilito quali primitive contenga.

La discussione ha usato due famiglie puramente analitiche:

#### Candidati relativi alla realtà rappresentata

Strutture generali che permetterebbero di esprimere di che cosa si parla, per esempio:

```text
referente
identificatore
proprietà
valore
relazione
tempo
```

Questi nomi non sono approvati.

L'idea è che il Core offra una grammatica generale, mentre il Domain specifichi che cosa significa una particolare cosa o relazione.

#### Candidati relativi alla conoscenza del sistema

Distinzioni che permetterebbero di esprimere il rapporto di Fold con ciò che sostiene, per esempio:

```text
affermazione
evidenza
provenienza
validità temporale
momento di conoscenza
verifica
derivazione
```

Queste non sono primitive dell'azione. Rendono invece la conoscenza sufficientemente qualificata perché i meccanismi possano operarvi sopra in modo sensato.

La ricerca deve ancora verificare se questa divisione in due famiglie sia reale, utile o artificiale.

### Domain Model

Ipotesi: descrive il significato specifico della realtà trattata in un certo contesto.

Può dover fornire:

- tipi e concetti specifici;
- significato delle proprietà e relazioni;
- vincoli che dipendono dal dominio;
- semantica temporale specifica;
- criteri o regole necessari a interpretare correttamente certe informazioni.

Esempio industriale:

```text
Pompa
Vibrazione
Sensore

la vibrazione è una misura applicabile a una certa tipologia di pompa
per quel tipo di pompa > 7 mm/s può significare condizione anomala
```

Il Domain non deve essere usato come contenitore di tutto ciò che il Core non sa. Il suo confine è ancora da verificare.

### Knowledge

È la rappresentazione interna risultante dall'interpretazione delle sorgenti usando mapping e semantica appropriata.

Principio di lavoro:

> Il sistema non dovrebbe conservare soltanto il risultato dell'interpretazione, ma anche il collegamento necessario a risalire alla sorgente, all'evidenza e al processo che lo ha prodotto quando ciò è richiesto.

### Core Engine

Ipotesi: insieme dei meccanismi generali che operano sulla conoscenza strutturata.

Candidati emersi:

- riconciliare referenti;
- confrontare affermazioni;
- gestire validità temporale;
- distinguere correzione, conflitto e cambiamento quando la semantica lo consente;
- applicare regole;
- derivare conclusioni;
- ricostruire lo stato corrente;
- preservare o seguire la provenienza;
- spiegare da quali conoscenze deriva un risultato.

Un meccanismo è candidato a essere Core soltanto se comportamento e invarianti sopravvivono a domini differenti.

### Views / Functions

Usano la conoscenza per rispondere a domande o produrre comportamenti del prodotto.

Una vista non dovrebbe ridefinire silenziosamente il significato della conoscenza sottostante. Quando produce una nuova conclusione o aggregazione, questa trasformazione deve rimanere concettualmente distinguibile quando serve spiegabilità.

## Esempio di lavoro — Pompa industriale P-204

L'esempio non è un requisito di Fold. Serve a osservare le responsabilità fuori dal dominio domestico.

### 1. Arriva una sorgente

Supponiamo che una sorgente contenga o permetta di estrarre:

```text
P-204
8,2 mm/s
10:30
vibrazione
```

Oppure:

```text
ID: P-204
Vibrazione: 8,2 mm/s
Ora rilevazione: 10:30
```

Fold possiede per ora informazioni estratte dalla sorgente.

Domande:

- che cosa rappresenta `P-204`?
- identifica qualcosa già conosciuto?
- che cosa significa `vibrazione` in quel contesto?
- `8,2 mm/s` è il valore di quale proprietà?
- a che cosa si riferisce `10:30`?
- le informazioni riguardano lo stesso referente?

### 2. Interpretazione con Core Model + Domain Model

Usando il significato del dominio e le strutture generali disponibili, il sistema può arrivare a interpretare:

```text
P-204
→ identificatore di una Pompa

vibrazione
→ proprietà misurabile della Pompa

8,2 mm/s
→ valore della proprietà vibrazione

10:30
→ momento della misurazione
```

Una possibile rappresentazione del contenuto è:

```text
[P-204]
   │
   └── ha vibrazione → 8,2 mm/s
                         │
                         └── rilevata alle 10:30
```

La struttura precisa non è approvata.

### 3. Qualificazione della conoscenza

Il sistema non dovrebbe necessariamente ridurre tutto a:

```text
P-204 = vibrazione 8,2
```

Potrebbe dover conservare qualcosa concettualmente simile a:

```text
affermazione:
P-204 ha vibrazione 8,2 mm/s

validità:
10:30

origine:
sorgente X

evidenza:
contenuto estratto Y

metodo:
estrazione / interpretazione ...

verifica:
...
```

Domande:

- perché Fold sostiene questa cosa?
- da dove arriva?
- quando vale?
- quando Fold l'ha appresa?
- è osservata o derivata?
- è verificata o incerta?

### 4. Regola di dominio

Il Domain può conoscere, solo per l'esempio:

```text
Per questo tipo di pompa:
vibrazione > 7 mm/s
→ condizione anomala
```

Questa soglia non appartiene al Core.

### 5. Meccanismo generale

Il motore può usare conoscenza + semantica/regola di dominio:

```text
P-204
vibrazione = 8,2

+

regola di dominio
> 7 = anomalia

↓

meccanismo generale

↓

conclusione:
P-204 presenta una condizione anomala
```

La conclusione dovrebbe poter rimanere collegata alla misurazione e alla regola da cui deriva se la spiegabilità è un requisito.

### 6. Nuova informazione

Successivamente arriva:

```text
P-204
5,1 mm/s
11:30
vibrazione
```

Il sistema deve stabilire almeno:

- se riguarda la stessa pompa;
- se rappresenta un momento differente;
- se è cambiamento reale, correzione o conflitto;
- quale conoscenza è applicabile al momento corrente.

#### Nota di progettazione — riuso del percorso già conosciuto

Se la nuova informazione arriva dalla stessa tipologia di sorgente, con la stessa struttura e lo stesso significato dei campi, non è necessario riscoprire ogni volta il mapping.

La prima elaborazione può aver stabilito un percorso validato:

```text
campo identificativo
→ identifica il referente

"vibrazione"
→ proprietà Vibrazione

valore numerico
→ valore della proprietà

timestamp
→ momento della misurazione
```

Una nuova occorrenza può quindi seguire:

```text
nuovo input
↓
riconosco struttura già nota
↓
riutilizzo mapping validato
↓
riconosco P-204
↓
produco una nuova informazione/affermazione
↓
la confronto con la conoscenza precedente
↓
ricalcolo eventuali conclusioni
```

Principio:

> Riutilizzare il percorso di interpretazione non significa riutilizzare automaticamente il risultato precedente.

La pipeline logica rimane perché la nuova informazione deve essere riferita, qualificata e confrontata; le parti interpretative già validate possono però diventare deterministiche.

### 7. Stato risultante

L'esempio può produrre:

```text
10:30
vibrazione 8,2
→ condizione anomala

11:30
vibrazione 5,1
→ condizione normale
```

Una funzione può mostrare uno stato corrente e mantenere contemporaneamente storia e spiegazione sottostante.

## Correzione importante all'esempio

La struttura precedente sembrava suggerire:

```text
input
↓
primitive realtà + dominio
↓
primitive conoscenza
↓
meccanismi
```

Questa lettura è troppo rigida.

Il passaggio corretto da investigare è il momento in cui:

```text
P-204 / vibration / 8.2 / 10:30
```

diventa una rappresentazione interna strutturata.

In quel momento possono collaborare:

- informazioni estratte dalla sorgente;
- mapping già conosciuto o inferito;
- semantica del Domain;
- capacità espressive del Core Model;
- riconciliazione con conoscenza già esistente.

Il risultato può nascere direttamente come conoscenza qualificata, senza che esistano necessariamente due passaggi runtime separati chiamati "realtà" e "conoscenza".

## Prima mappa delle responsabilità da sottoporre a Codex

```text
                    DOMAIN MODEL
              significati specifici
              vincoli / relazioni
                     ▲       ▲
                     │       │
SORGENTE → ESTRAZIONE → MAPPING / INTERPRETAZIONE
                         │
                         │ usa
                         ▼
                    CORE MODEL
              grammatica trasversale
                         │
                         ▼
                CONOSCENZA DI FOLD
                         │
                         ▼
                    CORE ENGINE
              confronta / riconcilia
              deriva / revisiona / ecc.
                         │
                         ▼
                  VISTE / FUNZIONI
```

Il diagramma esprime dipendenze e responsabilità, non un flusso runtime definitivo.

## Domande aperte prioritarie

1. Nel momento in cui una sorgente diventa conoscenza strutturata, quale responsabilità appartiene al mapping, quale al Domain e quale al Core Model?
2. Il Core Model necessita davvero di primitive distinte per realtà e conoscenza, oppure una struttura più compatta preserva le stesse differenze?
3. Che cosa rende una distinzione sufficientemente trasversale da appartenere al Core?
4. Come evitare che il Domain diventi il contenitore di ogni regola specifica non collocata altrove?
5. Quali regole sono semantica di dominio, quali policy applicative e quali meccanismi generali?
6. Come distinguere mapping riutilizzabile, interpretazione probabilistica e conoscenza già accettata?
7. Qual è il minimo necessario per preservare identità, tempo, provenienza, correzioni e derivazioni nel MVP?
8. Quanto della dimensione longitudinale deve essere dimostrato adesso per non chiudere evoluzioni future, senza introdurre un event engine generale?
9. Quali casi cross-domain possono falsificare meglio le presunte invarianti?
10. Quali proprietà deve avere una futura rappresentazione tecnica prima di confrontare tecnologie?

## Criterio di avanzamento

Questo Draft non diventa Canonical perché appare coerente.

Può avanzare soltanto dopo:

- critica indipendente di Codex;
- stress test su casi reali e almeno un caso non domestico realmente dinamico;
- separazione esplicita fra ciò che è necessario al MVP e ciò che serve soltanto a non chiudere evoluzioni future;
- individuazione delle distinzioni che sopravvivono ai test senza cambiare significato;
- consolidamento esplicito delle decisioni risultanti.

## Fonti collegate

- [`../ricerca/fondamenti-rappresentazione-conoscenza.md`](../ricerca/fondamenti-rappresentazione-conoscenza.md)
- [`../ricerca/esempio-operativo-core-dominio.md`](../ricerca/esempio-operativo-core-dominio.md)

Queste fonti sono `Research`; non prevalgono automaticamente su documenti canonici del progetto.