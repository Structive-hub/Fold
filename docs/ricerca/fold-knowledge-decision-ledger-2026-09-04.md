# Fold — Knowledge / Decision Ledger del percorso Round 1–6 e gate

**Status:** Draft  
**Data di ricostruzione:** 2026-09-04  
**Scope:** memoria genealogica del percorso concettuale; non nuova anatomia, non specifica implementativa e non canonizzazione.

## Come leggere il Ledger

Il Ledger è costruito dai Round in ordine storico, compreso il chiarimento strutturale del Round 2, poi readiness check finale, audit dei 34/Coverage Gate e recuperi del Regression Audit. La candidata v2 non è l'indice né la fonte delle voci. La review di Claude e le risposte successive sono escluse come fonti di nuove conclusioni.

- **STABILE:** distinzione o vincolo mantenuto come base del percorso e sostenuto dai casi/gate; non significa Canonical nel repository.
- **CANDIDATA:** formulazione o accorpamento preferito ma non definitivamente dimostrato.
- **APERTA:** problema reale lasciato irrisolto al termine del perimetro storico.
- **SUPERATA:** posizione sostituita, con rinvio esplicito alla formulazione successiva; non cancellata.

Una voce può avere più nature. Gli ID sono stabili: non rinumerare le voci in revisioni future. I campi Supera/Superata da conservano la genealogia; una diversa formulazione senza sostituzione dimostrata non viene risolta per semplice recenza. Le alternative soltanto esaminate e respinte non sono rappresentate come decisioni prima adottate.

Questo documento distilla conclusioni e motivazioni, non duplica integralmente le conversazioni. Le ripetizioni dei Round convergono nella voce originaria; una sostituzione effettiva conserva invece entrambe le posizioni.

Artefatti distinti: [snapshot v2 immutabile](fold-anatomia-v2-snapshot-2026-09-04.md) e [Coverage Map](fold-coverage-ledger-v2-2026-09-04.md). Il secondo confronto viene eseguito soltanto dopo la chiusura della ricostruzione del Ledger.

## Registro delle fonti primarie

Testi finali originali della sessione `01a05d0a-e483-7793-a648-e46306e04177`, consultati direttamente. Il percorso locale della fonte è `C:\Users\giuseppe\.codex\sessions\2026\09\01\rollout-2026-09-01T14-56-30-01a05d0a-e483-7793-a648-e46306e04177.jsonl`. Gli ordinal identificano messaggi, non righe di questo Ledger. SHA-256 sul corpo originale UTF-8, non sul wrapper JSON.

I riferimenti come R3 §R3.6 sono sezioni del testo indicato sotto. In R1 le sezioni originali si chiamano R1–R8; non sono otto Round separati. R2C è il chiarimento richiesto prima di passare al Round 3. AUDIT comprende il Coverage Gate nella propria chiusura.

| Sigla | Fonte | Ordinal | Data UTC del messaggio | SHA-256 del corpo |
|---|---|---:|---|---|
| R1 | Round 1 | 287 | 2026-09-03T15:43:17.415Z | `5fb8ce0254c4f05eab269401dfa6a6047a0b8573423e3962d0ee73b068031921` |
| R2 | Round 2 | 346 | 2026-09-03T16:18:55.599Z | `ecec0a90a41adea38c0cf2279e82d3531924d7e0fc39f5660e0ce01cde57098e` |
| R2C | Delta strutturale / chiarimento Round 2 | 428 | 2026-09-03T16:48:33.734Z | `1da70e3482e80224ce5680b2b6aec5805ec5fa887c64729dd34519d470874ca6` |
| R3 | Round 3 | 491 | 2026-09-03T17:17:26.933Z | `79ad61ee3422d868164cf361977cc634fd204504abf219a5dc1419a0fba6dec7` |
| R4 | Round 4 | 561 | 2026-09-03T17:53:00.474Z | `e8fba153785d436c414839f6a4eb162ecaf3755e0695564a0bbbfdb4ac68783e` |
| R5 | Round 5 | 618 | 2026-09-03T18:09:20.674Z | `68c1bc51f8627545407b2a5dfafc3c38f4b0b0ce2c8fa937e7a271c42cbdd2a3` |
| R6 | Round 6 | 661 | 2026-09-03T18:26:24.962Z | `1246773134d196608c00c55053dd108b11dd92cafb9d5d94f3bb05746a53e088` |
| GATE | Controllo finale dei tre problemi del Readiness Gate | 692 | 2026-09-03T18:33:11.566Z | `1892741375aab1c342751afd852507423604754ae49c975962246df3e81babf2` |
| AUDIT | Audit dei 34 e Coverage Gate | 822 | 2026-09-03T18:56:39.427Z | `504d4177ea8997f8c4b1b4cd1bc5e941cf3c0bd305356f7d918b12e2fb726be4` |
| REG | Regression & Change-Justification Audit (solo recuperi/chiarimenti) | 1070 | 2026-09-03T21:09:51.828Z | `f756ac83259a7d1b99aba157d93a0aa3a0d3766d84eb2a066fa33f9ead3600d1` |

Le fonti primarie originarie restano esterne al repository; il Ledger ne conserva il contenuto progettuale distillato e riferimenti verificabili, non un archivio integrale. Lo snapshot v2 è invece incluso integralmente nell'artefatto dedicato. Nessuna dipendenza da Notion è necessaria per leggere le conclusioni qui registrate.

## Voci in ordine di emersione

## Round 1 — aree, attività, autorità e operatività

### K-001 — Aree funzionali, non stadi runtime obbligatori

- **ID:** K-001
- **Conoscenza:** Aree funzionali, non stadi runtime obbligatori
- **Natura:** DISTINZIONE; DECISIONE NEGATIVA
- **Stato:** STABILE
- **Origine:** R1 §R1; R6 §III.2 e VI.B
- **Problema che risolve:** La numerazione delle fasi imponeva passaggi non necessari.
- **Ultima formulazione giustificata:** Le aree classificano problemi; un percorso concreto può iniziare da Query, funzione o rivalutazione. Nessuna conclusione universale sulla sequenza deriva dalla numerazione.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** —

### K-002 — Relazioni tipate e prerequisiti riferiti a risultati

- **ID:** K-002
- **Conoscenza:** Relazioni tipate e prerequisiti riferiti a risultati
- **Natura:** GUARDRAIL / INVARIANTE
- **Stato:** STABILE
- **Origine:** R1 §R2
- **Problema che risolve:** Una freccia confondeva chiamata, lettura e dipendenza.
- **Ultima formulazione giustificata:** Distinguere CALLS, DEPENDS_ON, READS, WRITES e PRODUCES; specificare risultato/condizione richiesto e tratto di attività abilitato. Conclusione dell'OCR non garantisce dati sufficienti al consumatore.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** —

### K-003 — Produrre, conservare e ammettere non coincidono

- **ID:** K-003
- **Conoscenza:** Produrre, conservare e ammettere non coincidono
- **Natura:** DISTINZIONE
- **Stato:** STABILE
- **Origine:** R1 §R2; R2C §T3; R6 §VI.C
- **Problema che risolve:** Un output veniva trattato come automaticamente persistito e accettato.
- **Ultima formulazione giustificata:** PRODUCES non implica WRITES, Admission o uso immediato; un risultato può essere conservato senza commitment e senza lavoro ancora attivo.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-002

### K-004 — CONSULTS come lettura qualificata: proposta originaria

- **ID:** K-004
- **Conoscenza:** CONSULTS come lettura qualificata: proposta originaria
- **Natura:** RICLASSIFICAZIONE
- **Stato:** CANDIDATA
- **Origine:** R1 §R2, Cosa eliminerei o ridurrei
- **Problema che risolve:** CONSULTS duplicava READS nella grammatica rigorosa.
- **Ultima formulazione giustificata:** Nel Round 1 si propone di non renderla relazione autonoma: lettura con ruolo semantico, normativo o decisionale. Verificare le formulazioni successive senza dichiarare una sostituzione non esplicita.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-002
- **Note:** Proposta terminologica, non divieto canonico. Eventuale reintroduzione nell'assemblaggio va verificata nella Coverage Map.

### K-005 — FEEDS e frecce generiche non spiegano la cooperazione

- **ID:** K-005
- **Conoscenza:** FEEDS e frecce generiche non spiegano la cooperazione
- **Natura:** DECISIONE NEGATIVA
- **Stato:** STABILE
- **Origine:** R1 §R2
- **Problema che risolve:** Una relazione generica nascondeva chi produce e chi usa.
- **Ultima formulazione giustificata:** Esplicitare produttore, risultato, lettore e prerequisito pertinente; non dedurre una chiamata diretta da una dipendenza.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** —

### K-006 — Emissione, reazione e vincolo sono relazioni diverse

- **ID:** K-006
- **Conoscenza:** Emissione, reazione e vincolo sono relazioni diverse
- **Natura:** DISTINZIONE
- **Stato:** CANDIDATA
- **Origine:** R1 §R2
- **Problema che risolve:** Segnalazione di un accadimento e avvio del lavoro erano confusi.
- **Ultima formulazione giustificata:** EMITS rende noto un evento; REACTS_TO indica possibile attivazione condizionata; CONSTRAINED_BY non impone una consultazione a ogni esecuzione. Eventi e comunicazioni effettivi restano da scegliere.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** —

### K-007 — Il proprietario funzionale possiede la continuazione

- **ID:** K-007
- **Conoscenza:** Il proprietario funzionale possiede la continuazione
- **Natura:** RESPONSABILITÀ NECESSARIA; REGOLA OPERATIVA
- **Stato:** STABILE
- **Origine:** R1 §R3 e R5; R6 §V.9
- **Problema che risolve:** Controller e orchestrazione duplicavano il governo del lavoro.
- **Ultima formulazione giustificata:** Il titolare dell'attività interpreta gli esiti rispetto al contratto e possiede la continuazione autorizzata. La gestione esecutiva registra tentativi/attese e realizza riprese, senza inventare semantica o prudenza.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** —

### K-008 — Acquisition non governa tutto il futuro della Source

- **ID:** K-008
- **Conoscenza:** Acquisition non governa tutto il futuro della Source
- **Natura:** DECISIONE NEGATIVA; REGOLA OPERATIVA
- **Stato:** STABILE
- **Origine:** R1 §R3; R2 §R2.1
- **Problema che risolve:** Un errore OCR successivo rendeva ambiguamente fallita l'acquisizione.
- **Ultima formulazione giustificata:** Ricezione riuscita ed estrazione interrotta possono coesistere; il coordinamento dell'acquisizione termina sul proprio risultato, non sul completo futuro semantico della Source.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-007

### K-009 — Interpretation è composizione semantica, non regia universale

- **ID:** K-009
- **Conoscenza:** Interpretation è composizione semantica, non regia universale
- **Natura:** RICLASSIFICAZIONE; RESPONSABILITÀ NECESSARIA
- **Stato:** STABILE
- **Origine:** R1 §R4; AUDIT §21
- **Problema che risolve:** Il nome Coordinator prometteva governo dei lifecycle altrui.
- **Ultima formulazione giustificata:** Comporre significato da osservazioni, mapping e contesto; produrre proposte, alternative, ambiguità e input mancanti. Non implica attivare né possedere ogni attività a monte.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-007

### K-010 — Interpretazione parziale e riferimento irrisolto sono legittimi

- **ID:** K-010
- **Conoscenza:** Interpretazione parziale e riferimento irrisolto sono legittimi
- **Natura:** GUARDRAIL / INVARIANTE
- **Stato:** STABILE
- **Origine:** R1 §R4; R2C §3; R6 §IV
- **Problema che risolve:** Interpretation e Reconciliation si richiedevano reciprocamente un risultato definitivo.
- **Ultima formulazione giustificata:** Una proposta può esistere con alternative e dipendenze irrisolte. Classificazione o riconciliazione completa non sono prerequisiti universali; gli esiti insufficienti vanno riconoscibili.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-009

### K-011 — Accadimento, Work, Attempt e risultato hanno storie distinte

- **ID:** K-011
- **Conoscenza:** Accadimento, Work, Attempt e risultato hanno storie distinte
- **Natura:** DISTINZIONE; REGOLA OPERATIVA
- **Stato:** STABILE
- **Origine:** R1 §R5; R2 §R2.1; R6 §V.9
- **Problema che risolve:** Lo stato del documento sostituiva l'identità del lavoro.
- **Ultima formulazione giustificata:** Distinguere ricezione avvenuta, lavoro con obiettivo/presupposti/proprietario, tentativo ed esito. Il risultato può sopravvivere al lavoro; esito operativo e posizione epistemica non coincidono.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** —

### K-012 — Work durevole quando serve continuità, non per ogni trasformazione

- **ID:** K-012
- **Conoscenza:** Work durevole quando serve continuità, non per ogni trasformazione
- **Natura:** DEFINIZIONE; DECISIONE NEGATIVA
- **Stato:** CANDIDATA
- **Origine:** R1 §R5; R6 §V.9
- **Problema che risolve:** Un unico Processing Case o un lifecycle per ogni nome producevano granularità artificiale.
- **Ultima formulazione giustificata:** Riconoscere lavoro autonomo quando ha obiettivo, input, presupposti, proprietario e conclusione distinguibili e può attendere/fallire/riprendere. Attempt e attesa possono restarne aspetti; nessun Case universale uno-a-uno con Source.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-011

### K-013 — Retry e rivalutazione non sono sinonimi

- **ID:** K-013
- **Conoscenza:** Retry e rivalutazione non sono sinonimi
- **Natura:** DISTINZIONE; REGOLA OPERATIVA
- **Stato:** STABILE
- **Origine:** R1 §R5; R3 §R3.9
- **Problema che risolve:** Nuovi presupposti venivano nascosti come semplice ripartenza.
- **Ultima formulazione giustificata:** Sugli stessi presupposti può esistere un altro tentativo; input, mapping o contesto materialmente cambiati richiedono distinguere la nuova valutazione. Non riscrivere il precedente esito riuscito come fallimento.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-011

### K-014 — Determinismo non esclude una Policy

- **ID:** K-014
- **Conoscenza:** Determinismo non esclude una Policy
- **Natura:** GUARDRAIL / INVARIANTE; REGOLA DI GOVERNANCE
- **Stato:** STABILE
- **Origine:** R1 §R6; R4 §R4.10
- **Problema che risolve:** Una soglia deterministica di accettazione sembrava logica non-Policy.
- **Ultima formulazione giustificata:** Se una regola sceglie prudenza, fiducia o automazione è una Policy anche quando l'esecuzione è deterministica. Non rinominarla contratto per nasconderne la natura.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** —

### K-015 — Decision, Disposition e Application sono distinte

- **ID:** K-015
- **Conoscenza:** Decision, Disposition e Application sono distinte
- **Natura:** DISTINZIONE; REGOLA DI GOVERNANCE
- **Stato:** STABILE
- **Origine:** R1 §R6; R3 §R3.10; R6 §III.11
- **Problema che risolve:** Scelta, autorizzazione e applicazione venivano fuse.
- **Ultima formulazione giustificata:** La decisione motiva una scelta, la disposizione esprime trattamento autorizzato e condizioni, l'applicazione conserva ciò che è stato tentato/eseguito. Un'interruzione può lasciare una disposizione pendente.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** —

### K-016 — Policy Evaluation non è l'unica origine dell'autorità

- **ID:** K-016
- **Conoscenza:** Policy Evaluation non è l'unica origine dell'autorità
- **Natura:** DECISIONE NEGATIVA; REGOLA DI GOVERNANCE
- **Stato:** STABILE
- **Origine:** R1 §R6; R6 §III.11
- **Problema che risolve:** Ogni transizione attraversava una nuova scelta Policy anche quando già autorizzata.
- **Ultima formulazione giustificata:** Una decisione esplicita autorizzata o una disposizione ancora applicabile possono consentire la transizione. Valutazione strutturale favorevole, da sola, non autorizza Admission.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-014, K-015

### K-017 — Formalizzazione non-Policy assegnata al responsabile del flusso

- **ID:** K-017
- **Conoscenza:** Formalizzazione non-Policy assegnata al responsabile del flusso
- **Natura:** REGOLA DI GOVERNANCE
- **Stato:** SUPERATA
- **Origine:** R1 §R6, Chi produce concretamente la Disposition senza Policy Evaluation?
- **Problema che risolve:** Mancava chi esprimesse la scelta umana nel contratto di Admission.
- **Ultima formulazione giustificata:** La proposta di R1 assegna al responsabile del flusso, ad esempio Function o Verification, la traduzione della scelta autorizzata in Disposition; nessuna Disposition Factory. Conservare questa posizione finché ne sia verificata l'evoluzione.
- **Supera:** —
- **Superata da:** K-185
- **Vincoli collegati:** K-016

### K-018 — Admission controlla applicabilità senza scegliere un'alternativa

- **ID:** K-018
- **Conoscenza:** Admission controlla applicabilità senza scegliere un'alternativa
- **Natura:** RESPONSABILITÀ NECESSARIA; REGOLA DI GOVERNANCE
- **Stato:** STABILE
- **Origine:** R1 §R6; R3 §R3.10; R6 §III.11; AUDIT §28
- **Problema che risolve:** Non scegliere nuove policy era interpretato come applicare ciecamente.
- **Ultima formulazione giustificata:** Verificare target, revisione/condizioni pertinenti, autorità, invarianti ed effetto già applicato. Restituire mancata applicazione o esito appropriato senza inventare una nuova disposizione.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-015, K-016

### K-019 — Conferma informativa non equivale ad autorizzazione generale

- **ID:** K-019
- **Conoscenza:** Conferma informativa non equivale ad autorizzazione generale
- **Natura:** GUARDRAIL / INVARIANTE; REGOLA DI GOVERNANCE
- **Stato:** STABILE
- **Origine:** R1 §R6 e Contraddizioni §5; R3 §R3.10
- **Problema che risolve:** Confermare un importo estendeva indebitamente la portata all'intero documento.
- **Ultima formulazione giustificata:** Distinguere lettura/contenuto confermato, collegamento verificato e transizione autorizzata. Target e scope della scelta devono essere espliciti.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-015

### K-020 — Qualità locale incrementale, non passaggio monolitico

- **ID:** K-020
- **Conoscenza:** Qualità locale incrementale, non passaggio monolitico
- **Natura:** RICLASSIFICAZIONE; RESPONSABILITÀ NECESSARIA
- **Stato:** STABILE
- **Origine:** R1 §R7; R4 §R4.9
- **Problema che risolve:** Tutta la qualità doveva precedere tutto il ragionamento.
- **Ultima formulazione giustificata:** Produttori competenti valutano target specifici e consumano valutazioni pertinenti. Ragionamento e Reconciliation possono produrne di nuove senza un valutatore centrale né uno score globale.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** —

### K-021 — Niente autoconferma attraverso contesto e qualità

- **ID:** K-021
- **Conoscenza:** Niente autoconferma attraverso contesto e qualità
- **Natura:** GUARDRAIL / INVARIANTE; DECISIONE NEGATIVA
- **Stato:** STABILE
- **Origine:** R1 §R7; R4 §R4.9; REG D02–D04
- **Problema che risolve:** La stessa aspettativa risolveva l'OCR e poi figurava come conferma indipendente.
- **Ultima formulazione giustificata:** Conservare dipendenze. Un ciclo non aumenta supporto da solo; ulteriore valutazione richiede una base/criterio/contesto pertinente identificabile. Incertezza o sospensione sono esiti legittimi, senza ciclo fino a soglia.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-020

### K-022 — Sovrapposizione dei lifecycle, calcolo ed effetti non coincidono

- **ID:** K-022
- **Conoscenza:** Sovrapposizione dei lifecycle, calcolo ed effetti non coincidono
- **Natura:** DISTINZIONE; REGOLA OPERATIVA
- **Stato:** STABILE
- **Origine:** R1 §R2 e R8
- **Problema che risolve:** Attività aperte contemporaneamente erano considerate indipendenti.
- **Ultima formulazione giustificata:** Distinguere lavori aperti, elaborazioni simultanee e applicazioni indipendenti. Una verifica pendente non sta necessariamente elaborando; calcoli separati possono contendere lo stesso effetto.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** —

### K-023 — Test conservativo di parallelizzabilità

- **ID:** K-023
- **Conoscenza:** Test conservativo di parallelizzabilità
- **Natura:** GUARDRAIL / INVARIANTE
- **Stato:** CANDIDATA
- **Origine:** R1 §R8
- **Problema che risolve:** Assenza di frecce o input differenti erano assunti sufficienti.
- **Ultima formulazione giustificata:** Richiedere prerequisiti disponibili, nessuna dipendenza necessaria, contesto identificabile/adeguato, compatibilità degli effetti e delle invarianti. Dichiarare se vale solo per il calcolo; due proposte sulla stessa persona possono richiedere controllo all'Admission.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-022, K-018

### K-024 — Operatività interna non prova primitive Core del mondo

- **ID:** K-024
- **Conoscenza:** Operatività interna non prova primitive Core del mondo
- **Natura:** DECISIONE NEGATIVA
- **Stato:** STABILE
- **Origine:** R1 Contraddizioni §1; R6 §V.9
- **Problema che risolve:** Work, eventi e attese interni venivano proiettati nell'ontologia dell'utente.
- **Ultima formulazione giustificata:** Servono distinzioni operative, non ne consegue una primitiva Activity, Process o Event informativa né un orchestratore centrale o process engine.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** —

### K-025 — Risultato storico riuscito non garantisce applicabilità corrente

- **ID:** K-025
- **Conoscenza:** Risultato storico riuscito non garantisce applicabilità corrente
- **Natura:** DISTINZIONE; REGOLA TEMPORALE
- **Stato:** STABILE
- **Origine:** R1 Contraddizioni §2 e §4; R3 §R3.10
- **Problema che risolve:** Un cambiamento successivo confondeva esecuzione passata e uso attuale.
- **Ultima formulazione giustificata:** Separare storia dell'attività, posizione epistemica e applicabilità. Una disposizione può essere nata correttamente e non essere più applicabile senza cancellarne la storia.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-013, K-018

### K-026 — Aperture operative e funzionali del primo Round

- **ID:** K-026
- **Conoscenza:** Aperture operative e funzionali del primo Round
- **Natura:** APERTURA
- **Stato:** APERTA
- **Origine:** R1 §R1–R8, Cosa resta volutamente aperto
- **Problema che risolve:** Il catalogo non determina tutti i contratti applicativi.
- **Ultima formulazione giustificata:** Restano da specificare percorsi MVP, input obbligatori per ciascun risultato, stati/granularità dei Work, retry, condizioni di riapertura e quali risultati parziali ogni funzione possa usare.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-010, K-012, K-013

### K-027 — Conservazione indefinita e parallelismo MVP non sono conseguenze

- **ID:** K-027
- **Conoscenza:** Conservazione indefinita e parallelismo MVP non sono conseguenze
- **Natura:** DECISIONE NEGATIVA
- **Stato:** STABILE
- **Origine:** R1 Ipotesi che non devono diventare canoniche
- **Problema che risolve:** Distinzioni concettuali diventavano requisiti esecutivi o archivistici indiscriminati.
- **Ultima formulazione giustificata:** Né ogni intermedio/tentativo va conservato indefinitamente né ogni parallelizzabilità va implementata. Quantità della memoria e forma software richiedono criteri separati.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-003, K-023

## Round 2 — materiale, documenti, contributi e risultati parziali

### K-028 — Identità documentale distinta da file e rappresentazioni

- **ID:** K-028
- **Conoscenza:** Identità documentale distinta da file e rappresentazioni
- **Natura:** DISTINZIONE
- **Stato:** STABILE
- **Origine:** R2 §R2.1–R2.2; R5 §R5.2 e R5.9
- **Problema che risolve:** Il numero dei file veniva usato per contare i documenti.
- **Ultima formulazione giustificata:** Più Source possono rappresentare un documento e una Source più documenti; caricamento congiunto, stessa pagina o file differente non provano identità, completezza, versione o correzione.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** —

### K-029 — Documento come Referent facoltativo

- **ID:** K-029
- **Conoscenza:** Documento come Referent facoltativo
- **Natura:** DEFINIZIONE
- **Stato:** CANDIDATA
- **Origine:** R2 §R2.1; R5 §R5.2 e R5.9; R6 §III.9
- **Problema che risolve:** Serviva parlare del documento indipendentemente dai file.
- **Ultima formulazione giustificata:** Usare Referent documentale quando identità e storia indipendenti sono necessarie; può essere menzionato senza rappresentazione diretta, ma non inventato senza base.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-028

### K-030 — Nessuna primitiva universale Logical Document

- **ID:** K-030
- **Conoscenza:** Nessuna primitiva universale Logical Document
- **Natura:** DECISIONE NEGATIVA
- **Stato:** STABILE
- **Origine:** R2 §R2.1; R6 §III.9
- **Problema che risolve:** Il vecchio nome di un componente forzava un nuovo oggetto.
- **Ultima formulazione giustificata:** Il bisogno d'identità documentale non dimostra una primitiva autonoma né un documento per file/pagina. Il raggruppamento operativo di input non afferma un'identità documentale.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-028, K-029

### K-031 — Porzioni indirizzabili senza segmentazione automatica completa

- **ID:** K-031
- **Conoscenza:** Porzioni indirizzabili senza segmentazione automatica completa
- **Natura:** RESPONSABILITÀ NECESSARIA; DECISIONE NEGATIVA
- **Stato:** STABILE
- **Origine:** R2 §R2.2; R4 §R4.7
- **Problema che risolve:** Totale e intestazione di ricevute diverse venivano collegati per co-presenza.
- **Ultima formulazione giustificata:** Indicare intera Source o parte pertinente, anche sovrapposta/incompleta e con confini incerti. Nessun obbligo di ritaglio o segmentazione completa preventiva; ordine e completezza non sono dedotti dal raggruppamento.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-028

### K-032 — Forma del locator e composizione documentale restano candidate

- **ID:** K-032
- **Conoscenza:** Forma del locator e composizione documentale restano candidate
- **Natura:** APERTURA
- **Stato:** APERTA
- **Origine:** R2 §R2.1–R2.2; R6 §VII.2
- **Problema che risolve:** L'indirizzabilità necessaria non determina la forma dei riferimenti.
- **Ultima formulazione giustificata:** Restano aperti individuazione manuale/automatica delle porzioni, rappresentazione dei confini incerti e criteri di completezza/ordine; nessun nuovo oggetto Core obbligatorio.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-031

### K-033 — Query può recuperare materiale senza Knowledge artificiale

- **ID:** K-033
- **Conoscenza:** Query può recuperare materiale senza Knowledge artificiale
- **Natura:** RESPONSABILITÀ NECESSARIA; DECISIONE NEGATIVA
- **Stato:** STABILE
- **Origine:** R2 §R2.3; R6 §III.5; AUDIT §29
- **Problema che risolve:** Una Source non interpretata scompariva dalle funzioni.
- **Ultima formulazione giustificata:** Recuperare Source, metadati, porzioni e Observation oltre a proposte e Knowledge. Mostrare il livello informativo effettivo e i limiti di copertura; non creare commitment solo per rendere materiale apribile.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** —

### K-034 — Esito negativo di ricerca non è assenza nel documento o nel mondo

- **ID:** K-034
- **Conoscenza:** Esito negativo di ricerca non è assenza nel documento o nel mondo
- **Natura:** GUARDRAIL / INVARIANTE
- **Stato:** STABILE
- **Origine:** R2 §R2.3; R3 §R3.4; R6 §V.7
- **Problema che risolve:** OCR incompleto faceva inferire assenza fattuale.
- **Ultima formulazione giustificata:** Non trovato nel testo esaminato non implica non presente nella pagina non letta né assente nel mondo. Scope, corpus e copertura delimitano la conclusione.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-033

### K-035 — Base umana ricevuta, significato attribuito e autorità sono distinti

- **ID:** K-035
- **Conoscenza:** Base umana ricevuta, significato attribuito e autorità sono distinti
- **Natura:** DISTINZIONE; CRITERIO DI CONSERVAZIONE / PROVENANCE
- **Stato:** STABILE
- **Origine:** R2 §R2.4; R4 §R4.6–R4.8; REG D01
- **Problema che risolve:** Un sì o un comando veniva trasformato in fatto verificato senza conservarne il contesto.
- **Ultima formulazione giustificata:** Preservare contributo significativo, autore/origine, domanda/target, tempo, contesto e natura dell'interazione; tenere collegata ma distinta l'interpretazione e l'eventuale autorizzazione. Non conservare indiscriminatamente tutte le interazioni.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-019

### K-036 — Nessuna Human Evidence universale né Observation umana artificiale

- **ID:** K-036
- **Conoscenza:** Nessuna Human Evidence universale né Observation umana artificiale
- **Natura:** DECISIONE NEGATIVA
- **Stato:** STABILE
- **Origine:** R2 §R2.4; R2C §T2; R6 §V.5; REG D01
- **Problema che risolve:** Per includere la persona si introduceva una seconda famiglia epistemica.
- **Ultima formulazione giustificata:** Una dichiarazione può fungere da origine non documentale; non ogni comando è Source o evidenza fattuale. Input strutturato può alimentare interpretazione/verifica senza OCR o Observation artificiale; umano non significa infallibile.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-035

### K-037 — Correggere una lettura non conferma ruolo, soggetto o pagamento

- **ID:** K-037
- **Conoscenza:** Correggere una lettura non conferma ruolo, soggetto o pagamento
- **Natura:** GUARDRAIL / INVARIANTE
- **Stato:** STABILE
- **Origine:** R2 §R2.4, Tipi 1–5; R4 §R4.1–R4.2
- **Problema che risolve:** La verifica di 34,72 sostituiva la verifica del suo significato.
- **Ultima formulazione giustificata:** Distinguere correzione estrattiva, conferma semantica, associazione, fatto nuovo e autorizzazione. Una correzione della trascrizione conserva l'OCR storico e non stabilisce automaticamente che l'importo sia dovuto o pagato.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-035, K-019

### K-038 — Scope di supporto e scope d'autorizzazione sono separati

- **ID:** K-038
- **Conoscenza:** Scope di supporto e scope d'autorizzazione sono separati
- **Natura:** REGOLA DI GOVERNANCE; CRITERIO DI CONSERVAZIONE / PROVENANCE
- **Stato:** STABILE
- **Origine:** R2 §R2.5
- **Problema che risolve:** Conferme del bundle diventavano contagiose e si estendevano ai contenuti futuri.
- **Ultima formulazione giustificata:** Rendere recuperabili oggetto, aspetto, contenuto presentato, portata e natura dell'atto. Una risposta tardiva resta riferita al target originale; nuovi elementi aggiunti al bundle non ereditano la conferma.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-019, K-035

### K-039 — Una conferma abilitante non sostiene tutte le premesse usate

- **ID:** K-039
- **Conoscenza:** Una conferma abilitante non sostiene tutte le premesse usate
- **Natura:** GUARDRAIL / INVARIANTE
- **Stato:** STABILE
- **Origine:** R2 §R2.5
- **Problema che risolve:** Confermare l'utenza sembrava fornire nuova evidenza anche all'importo.
- **Ultima formulazione giustificata:** Il link verificato può consentire una vista dell'utenza, ma l'importo mantiene la propria base documentale. Distinguere dipendenza d'uso e supporto diretto.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-038

### K-040 — Nessun involucro universale Result o Attempt/Event autonomi necessari

- **ID:** K-040
- **Conoscenza:** Nessun involucro universale Result o Attempt/Event autonomi necessari
- **Natura:** DECISIONE NEGATIVA
- **Stato:** STABILE
- **Origine:** R2 §R2.6; R6 §V.9
- **Problema che risolve:** Le distinzioni operative generavano un oggetto fondamentale ciascuna.
- **Ultima formulazione giustificata:** Observation, proposte e decisioni sono già risultati. Un tentativo deve essere distinguibile/indirizzabile quando necessario nella storia del Work, non automaticamente gestito come entità autonoma.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-011, K-012, K-024

### K-041 — Preservazione, processabilità ed esito dell'acquisizione sono distinti

- **ID:** K-041
- **Conoscenza:** Preservazione, processabilità ed esito dell'acquisizione sono distinti
- **Natura:** DISTINZIONE
- **Stato:** STABILE
- **Origine:** R2 §R2.7; R2C §K1
- **Problema che risolve:** File conservato ma illeggibile poteva soltanto esistere pienamente o non esistere.
- **Ultima formulazione giustificata:** Distinguere ricezione avvenuta, lavoro ed esito; materiale può essere trattenuto, incompleto, riutilizzato o non autorizzato alla normale elaborazione. OCR successivo non riscrive acquisizione.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-008, K-011

### K-042 — Produttore dichiara disponibilità, consumatore sufficienza

- **ID:** K-042
- **Conoscenza:** Produttore dichiara disponibilità, consumatore sufficienza
- **Natura:** RESPONSABILITÀ NECESSARIA
- **Stato:** STABILE
- **Origine:** R2 §R2.8
- **Problema che risolve:** 22 pagine lette venivano considerate sufficienti a qualunque significato.
- **Ultima formulazione giustificata:** Extraction dichiara Observation e limiti; Interpretation valuta i prerequisiti del risultato richiesto; coordinamento mantiene il lavoro; Policy/autorità autorizzano ulteriore tentativo quando il contratto non basta.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-002, K-007, K-010

### K-043 — Risultati parziali sopravvivono al tentativo interrotto

- **ID:** K-043
- **Conoscenza:** Risultati parziali sopravvivono al tentativo interrotto
- **Natura:** REGOLA OPERATIVA; CRITERIO DI CONSERVAZIONE / PROVENANCE
- **Stato:** STABILE
- **Origine:** R2 §R2.6–R2.8
- **Problema che risolve:** Un tentativo fallito annullava risultati già consegnati o un retry li sovrascriveva tutti.
- **Ultima formulazione giustificata:** Distinguere quali esecuzioni producono quali letture e quali parti restano mancanti. Il successo di un secondo tentativo non seleziona tacitamente tutte le sue letture.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-011, K-013

### K-044 — Bundle come contesto, non gate atomico di accettazione

- **ID:** K-044
- **Conoscenza:** Bundle come contesto, non gate atomico di accettazione
- **Natura:** DEFINIZIONE; DECISIONE NEGATIVA
- **Stato:** STABILE
- **Origine:** R2 §R2.9; R2C §T3
- **Problema che risolve:** READY unico bloccava tutto o accettava tutto.
- **Ultima formulazione giustificata:** Le proposte semanticamente valutabili sono indirizzabili con dipendenze e alternative; niente qualità/decisione/lifecycle unico del contenitore. L'ammissione parziale richiede le dipendenze pertinenti, non alta confidenza di un token.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-010, K-038

### K-045 — Leggibilità del valore non è completezza proposizionale

- **ID:** K-045
- **Conoscenza:** Leggibilità del valore non è completezza proposizionale
- **Natura:** GUARDRAIL / INVARIANTE
- **Stato:** STABILE
- **Origine:** R2 §R2.9; R2C §3
- **Problema che risolve:** Un importo senza ruolo o referente certo diventava Assertion completa.
- **Ultima formulazione giustificata:** 84,72 ben letto può restare Observation o lettura candidata se mancano soggetto/ruolo. Alternative collegate non sono affermazioni indipendentemente confermate.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-044

### K-046 — Contratti acquisizione, verifiche e domanda multipla ancora aperti

- **ID:** K-046
- **Conoscenza:** Contratti acquisizione, verifiche e domanda multipla ancora aperti
- **Natura:** APERTURA
- **Stato:** APERTA
- **Origine:** R2 §R2.4–R2.9, Cosa resta aperto
- **Problema che risolve:** I casi dimostrano separazioni, non tutte le regole del prodotto.
- **Ultima formulazione giustificata:** Restano da definire criteri di acquisizione riuscita, gestione rifiuti/incompletezza, domande multiple, qualificatori dello scope, input deliberati MVP e regole specifiche di ammissione parziale.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-026, K-038, K-041

## Chiarimento del Round 2 — delta strutturale e correzioni

### K-047 — Distinzione necessaria non implica primitiva autonoma

- **ID:** K-047
- **Conoscenza:** Distinzione necessaria non implica primitiva autonoma
- **Natura:** GUARDRAIL / INVARIANTE; DECISIONE NEGATIVA
- **Stato:** STABILE
- **Origine:** R2C Introduzione e §2; R6 §I e VII
- **Problema che risolve:** Ogni problema sembrava giustificare un nuovo oggetto Core.
- **Ultima formulazione giustificata:** Distinguere necessità del significato, necessità d'indirizzabilità e appartenenza alla grammatica Core. Una forma elementare può essere necessaria senza identità propria; non promuovere ogni distinzione a primitiva.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** —

### K-048 — Source definita come materiale ricevuto/preservato/utilizzabile

- **ID:** K-048
- **Conoscenza:** Source definita come materiale ricevuto/preservato/utilizzabile
- **Natura:** DEFINIZIONE; SUPERAMENTO
- **Stato:** SUPERATA
- **Origine:** R2 §A; R2C §T1 e §13.C.1
- **Problema che risolve:** La prima risposta usava criteri d'esistenza incompatibili.
- **Ultima formulazione giustificata:** Posizione diagnosticata in R2C: ricezione, conservazione e processabilità non possono definire insieme l'esistenza della Source.
- **Supera:** —
- **Superata da:** K-049
- **Vincoli collegati:** K-041
- **Note:** Si conserva l'imprecisione storica, non la si propone come definizione corrente.

### K-049 — Source come contenuto d'origine determinato e referenziabile

- **ID:** K-049
- **Conoscenza:** Source come contenuto d'origine determinato e referenziabile
- **Natura:** DEFINIZIONE
- **Stato:** STABILE
- **Origine:** R2C §T1; R6 §V.5
- **Problema che risolve:** PDF conservato non processabile e dichiarazione umana rompevano la definizione precedente.
- **Ultima formulazione giustificata:** Base per ricostruire ciò che fu fornito/dichiarato, distinta da estrazione, interpretazione e derivazione. Autore, canale, ricezione, autorizzazioni e affidabilità sono distinti; il solo log di ricezione non è una Source consultabile.
- **Supera:** K-048
- **Superata da:** —
- **Vincoli collegati:** K-035, K-041

### K-050 — Observation è risultato di osservazione, non pedaggio universale

- **ID:** K-050
- **Conoscenza:** Observation è risultato di osservazione, non pedaggio universale
- **Natura:** DEFINIZIONE; DECISIONE NEGATIVA
- **Stato:** STABILE
- **Origine:** R2C §T2; R6 §V.5
- **Problema che risolve:** Uniformare i percorsi duplicava il contributo strutturato senza differenza utile.
- **Ultima formulazione giustificata:** Observation rende indirizzabile quanto rilevato nel contenuto d'origine e il riferimento pertinente; non è né Source né Assertion. Alcuni ingressi preservano ricevuto/concluso senza una Observation distinta.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-036, K-049

### K-051 — Candidate come natura unica per proposte, incompletezza e bundle

- **ID:** K-051
- **Conoscenza:** Candidate come natura unica per proposte, incompletezza e bundle
- **Natura:** DEFINIZIONE; SUPERAMENTO
- **Stato:** SUPERATA
- **Origine:** R2 §A e R2.9; R2C §T3 e §13.C.2
- **Problema che risolve:** La stessa parola mescolava proposizione determinata, lavoro incompleto e contenitore.
- **Ultima formulazione giustificata:** Il Candidate unitario della formulazione precedente non ha una giustificazione comune; una proposizione può restare la stessa unità semantica prima/dopo Admission.
- **Supera:** —
- **Superata da:** K-052
- **Vincoli collegati:** K-044

### K-052 — Proposed qualifica la posizione, non una sostanza universale

- **ID:** K-052
- **Conoscenza:** Proposed qualifica la posizione, non una sostanza universale
- **Natura:** RICLASSIFICAZIONE; DECISIONE NEGATIVA
- **Stato:** STABILE
- **Origine:** R2C §T3; R6 §III.3 e VI.C
- **Problema che risolve:** L'ammissione sembrava trasformare un oggetto Candidate in un altro oggetto Assertion.
- **Ultima formulazione giustificata:** Contenuto determinato può esistere come Assertion proposta; alternative/incompletezza restano risultati interpretativi. Proposed non equivale a bassa credibilità; nessun involucro Candidate obbligatorio.
- **Supera:** K-051
- **Superata da:** —
- **Vincoli collegati:** K-003, K-044, K-047

### K-053 — Interpretation Result per composizioni e alternative

- **ID:** K-053
- **Conoscenza:** Interpretation Result per composizioni e alternative
- **Natura:** DEFINIZIONE
- **Stato:** CANDIDATA
- **Origine:** R2C §T3 e §10.2; R6 §V.1 e VII.2
- **Problema che risolve:** Conservare solo Assertion determinate perde risultati ancora utili.
- **Ultima formulazione giustificata:** Mantenere proposte incomplete, alternative, referenze irrisolte, supporti e dipendenze; la loro recuperabilità non dipende da Admission. Non è dimostrato un oggetto o archivio universale separato.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-010, K-052

### K-054 — Supporto qualificato necessario, Evidence-oggetto non dimostrato

- **ID:** K-054
- **Conoscenza:** Supporto qualificato necessario, Evidence-oggetto non dimostrato
- **Natura:** RICLASSIFICAZIONE; DECISIONE NEGATIVA
- **Stato:** STABILE
- **Origine:** R2C §T4; R4 §R4.4
- **Problema che risolve:** Evidence ripeteva la Source e limitava il target alle Assertion di dominio.
- **Ultima formulazione giustificata:** Rappresentare che cosa sostiene quale contenuto/aspetto, con base e scope; può sostenere una lettura o un link. Indirizzabilità autonoma quando necessaria a verifica/contestazione; forma esatta aperta.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-038, K-047

### K-055 — Assertion non è la forma universale di ogni informazione

- **ID:** K-055
- **Conoscenza:** Assertion non è la forma universale di ogni informazione
- **Natura:** DEFINIZIONE; DECISIONE NEGATIVA
- **Stato:** STABILE
- **Origine:** R2C §3; R6 §V.3; GATE §1
- **Problema che risolve:** Un modello solo Assertion doveva inventare soggetto/ruolo o scartare una lettura.
- **Ultima formulazione giustificata:** Unità semantica indirizzabile con contenuto proposizionale valutabile, non verità né commitment implicito. Materiale grezzo, alternative, lavori e disposizioni non diventano automaticamente Assertion.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-045, K-050, K-052

### K-056 — Essere indirizzabile non basta per essere Referent

- **ID:** K-056
- **Conoscenza:** Essere indirizzabile non basta per essere Referent
- **Natura:** GUARDRAIL / INVARIANTE; DECISIONE NEGATIVA
- **Stato:** STABILE
- **Origine:** R2C §T5; R5 §R5.1; R6 §V.1
- **Problema che risolve:** Work, locator e gruppi interni venivano promossi a cose del mondo.
- **Ultima formulazione giustificata:** Separare identità di un soggetto rappresentato e possibilità di richiamare un elemento interno. Documento-Referent richiede un soggetto documentale, non solo un raggruppamento di elaborazione.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-029, K-030, K-047

### K-057 — Localizzazione, rappresentazione documentale e ruolo semantico distinti

- **ID:** K-057
- **Conoscenza:** Localizzazione, rappresentazione documentale e ruolo semantico distinti
- **Natura:** DISTINZIONE; CRITERIO DI CONSERVAZIONE / PROVENANCE
- **Stato:** STABILE
- **Origine:** R2C §T6
- **Problema che risolve:** Una regione geometricamente precisa sembrava già semanticamente attribuita.
- **Ultima formulazione giustificata:** Regione della foto, parte rappresentata del documento e totale dovuto sono livelli distinti. Per materiale trasformato, locator e Lineage devono consentire di ricondurre la lettura alla rappresentazione pertinente.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-031

### K-058 — Value strutturato non implica entità autonoma

- **ID:** K-058
- **Conoscenza:** Value strutturato non implica entità autonoma
- **Natura:** DEFINIZIONE; DECISIONE NEGATIVA
- **Stato:** STABILE
- **Origine:** R2C §5; R5 §R5.8; R6 §V.3
- **Problema che risolve:** Il numero astratto veniva dotato di identità, evidenza e lifecycle della sua occorrenza.
- **Ultima formulazione giustificata:** Distinguere forma letta, quantità, unità/valuta, precisione e ruolo contestuale. Due occorrenze uguali non sono la stessa informazione; tempo e supporto riguardano lettura/proposizione. Value può essere forma Core senza identità referenziale.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-045, K-047

### K-059 — Relazioni informative, provenienziali, operative e inferenziali distinte

- **ID:** K-059
- **Conoscenza:** Relazioni informative, provenienziali, operative e inferenziali distinte
- **Natura:** DISTINZIONE; RICLASSIFICAZIONE
- **Stato:** STABILE
- **Origine:** R2C §4 e §11; R6 §V.3
- **Problema che risolve:** Un'unica freccia o Relation uniforme confondeva significato e lavoro.
- **Ultima formulazione giustificata:** Una relazione di dominio può essere Assertion; provenienza/rappresentazione, dipendenza giustificativa e attesa operativa non sono intercambiabili. Rappresenta-parte non significa parte-fisica; richiede-risultato non significa giustificato-da.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-002, K-054

### K-060 — Knowledge State come stato globale unitario

- **ID:** K-060
- **Conoscenza:** Knowledge State come stato globale unitario
- **Natura:** DEFINIZIONE; SUPERAMENTO
- **Stato:** SUPERATA
- **Origine:** R2 §A; R2C §6 e §13.C.6
- **Problema che risolve:** Pending, ambiguo, autorizzato e ammesso erano allineati sullo stesso asse.
- **Ultima formulazione giustificata:** La formulazione unitaria è messa in crisi perché mescola disponibilità, determinazione, qualità, governo e lifecycle operativo.
- **Supera:** —
- **Superata da:** K-061
- **Vincoli collegati:** —

### K-061 — Qualificazioni su bersagli e assi distinti

- **ID:** K-061
- **Conoscenza:** Qualificazioni su bersagli e assi distinti
- **Natura:** DISTINZIONE; RICLASSIFICAZIONE
- **Stato:** STABILE
- **Origine:** R2C §6; R4 §R4.2; R6 §I.H
- **Problema che risolve:** L'incertezza del link si trasferiva all'importo e il lavoro pendente alla conoscenza.
- **Ultima formulazione giustificata:** Distinguere disponibilità, completezza/ambiguità semantica, qualità/supporto, posizione di Admission, autorizzazione ed esecuzione. Un contenuto ammesso mantiene attribuzione, incertezza e limiti.
- **Supera:** K-060
- **Superata da:** —
- **Vincoli collegati:** K-020, K-025, K-052

### K-062 — Memoria operativa necessaria, non sostituita dalla sola Provenance

- **ID:** K-062
- **Conoscenza:** Memoria operativa necessaria, non sostituita dalla sola Provenance
- **Natura:** RESPONSABILITÀ NECESSARIA; CRITERIO DI CONSERVAZIONE / PROVENANCE
- **Stato:** STABILE
- **Origine:** R2C §9–§10.3
- **Problema che risolve:** Domanda inviata nel log non diceva se qualcuno dovesse ancora attenderne la risposta.
- **Ultima formulazione giustificata:** Recuperare obiettivo, target, scope, copertura, risultati/esiti, dipendenze mancanti, domanda/contenuto presentato, decisioni, effetti e proprietario della prosecuzione. Nessun nuovo archivio fisico o workflow engine imposto.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-007, K-011, K-038

### K-063 — Output vuoto non determina l'esito del lavoro

- **ID:** K-063
- **Conoscenza:** Output vuoto non determina l'esito del lavoro
- **Natura:** DISTINZIONE; REGOLA OPERATIVA
- **Stato:** STABILE
- **Origine:** R2C §9, Un limite ulteriore
- **Problema che risolve:** Nessuna Observation significava indifferentemente assenza di testo o errore.
- **Ultima formulazione giustificata:** Distinguere nessun testo rilevato, elaborazione incompleta e formato non processabile. Outcome deve restare recuperabile con copertura e tentativo, non dedotto dal solo insieme dei risultati.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-034, K-043, K-062

### K-064 — Risorse di riferimento non sono memorie dei casi né attori

- **ID:** K-064
- **Conoscenza:** Risorse di riferimento non sono memorie dei casi né attori
- **Natura:** DISTINZIONE
- **Stato:** STABILE
- **Origine:** R2C §10.1; R3 §R3.9; AUDIT §C
- **Problema che risolve:** Modello, decisione e Work sembravano lo stesso posto dove vive una regola.
- **Ultima formulazione giustificata:** Core, Domain, Mapping, Quality e Policies forniscono forme/criteri; la Decision conserva l'esito per un caso, Work il seguito e Knowledge il commitment. La risorsa non prende iniziative da sola.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** —

### K-065 — Forma del supporto indirizzabile ancora aperta

- **ID:** K-065
- **Conoscenza:** Forma del supporto indirizzabile ancora aperta
- **Natura:** APERTURA
- **Stato:** APERTA
- **Origine:** R2C §T4 e §13.D; R4 §R4.4
- **Problema che risolve:** Necessità di supporto veniva scambiata per decisione sulla sua ontologia.
- **Ultima formulazione giustificata:** Non è deciso se sempre relazione, registrazione indirizzabile o altra forma; devono restare target, base, scope, qualificazioni e storia. Non risolvere per uniformità.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-054, K-047

### K-066 — Confine di Assertion verso proposizioni su interpretazioni: apertura R2

- **ID:** K-066
- **Conoscenza:** Confine di Assertion verso proposizioni su interpretazioni: apertura R2
- **Natura:** APERTURA
- **Stato:** APERTA
- **Origine:** R2C §3 e §13.D
- **Problema che risolve:** Il ruolo attribuito alla data non era una proprietà diretta dell'utenza.
- **Ultima formulazione giustificata:** R2 lascia aperta la rappresentazione di proposizioni su letture/interpretazioni interne. R6 distingue Assertion da Interpretation Result e il Gate ne amplia/precisa la definizione proposizionale, ma non risolve esplicitamente ogni caso di meta-Assertion interna. Non promuovere il caso specifico a chiuso per sola generalità della definizione.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-055
- **Note:** Apertura non ribadita nominalmente nell'elenco finale: chiusura non dimostrata dalle fonti consultate.

## Round 3 — tempo, derivazioni, attese e applicabilità

### K-067 — Content time, storia epistemica, operativa e reference time distinti

- **ID:** K-067
- **Conoscenza:** Content time, storia epistemica, operativa e reference time distinti
- **Natura:** DISTINZIONE; REGOLA TEMPORALE
- **Stato:** STABILE
- **Origine:** R3 §R3.1; R6 §V.6
- **Problema che risolve:** Ricezione veniva usata come decorrenza o momento della conoscenza.
- **Ultima formulazione giustificata:** Conservare ruoli temporali pertinenti: tempo descritto, produzione/acquisizione, osservazione/interpretazione, decisione/verifica, ammissione/applicazione e riferimento della valutazione. Possono coincidere, non sono equivalenti; nessun set di timestamp obbligatorio per ogni elemento.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-025

### K-068 — Un tempo ignoto non si completa con una data disponibile

- **ID:** K-068
- **Conoscenza:** Un tempo ignoto non si completa con una data disponibile
- **Natura:** GUARDRAIL / INVARIANTE; REGOLA TEMPORALE
- **Stato:** STABILE
- **Origine:** R3 §R3.1 e R3.4
- **Problema che risolve:** Ricezione riempiva emissione/decorrenza, 30/09 riceveva un anno arbitrario.
- **Ultima formulazione giustificata:** Mantenere precisione, ruolo e incertezza; confrontare solo quando il contesto consente il risultato. Emissione, periodo fatturato e scadenza non sono un unico tempo della Source.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-067

### K-069 — Validity come contenitore di verità, periodo e utilizzabilità

- **ID:** K-069
- **Conoscenza:** Validity come contenitore di verità, periodo e utilizzabilità
- **Natura:** DEFINIZIONE; SUPERAMENTO
- **Stato:** SUPERATA
- **Origine:** R3 §R3.2 e Delta §F.3
- **Problema che risolve:** La stessa etichetta creava una falsa storia temporale.
- **Ultima formulazione giustificata:** Posizione storica criticata: intervallo di verità, periodo sorgente e intervallo d'uso erano sovrapposti.
- **Supera:** —
- **Superata da:** K-070
- **Vincoli collegati:** —

### K-070 — Temporalità del contenuto, pertinenza d'uso e applicabilità distinti

- **ID:** K-070
- **Conoscenza:** Temporalità del contenuto, pertinenza d'uso e applicabilità distinti
- **Natura:** DISTINZIONE; RICLASSIFICAZIONE
- **Stato:** STABILE
- **Origine:** R3 §R3.2; R4 §R4.2
- **Problema che risolve:** Documento scaduto sembrava rendere falsa tutta la conoscenza ricavata.
- **Ultima formulazione giustificata:** Tempo del contenuto, posizione epistemica, pertinenza per una domanda e applicabilità dell'autorizzazione sono domande differenti. Un pagamento al 10 settembre non è vero soltanto quel giorno; una Source scaduta può restare utile storicamente.
- **Supera:** K-069
- **Superata da:** —
- **Vincoli collegati:** K-061, K-067

### K-071 — Continuità temporale richiede semantica e base esplicite

- **ID:** K-071
- **Conoscenza:** Continuità temporale richiede semantica e base esplicite
- **Natura:** REGOLA TEMPORALE; GUARDRAIL / INVARIANTE
- **Stato:** STABILE
- **Origine:** R3 §R3.2–R3.3
- **Problema che risolve:** C documentato a marzo veniva esteso automaticamente ad aprile.
- **Ultima formulazione giustificata:** Assenza di fine dichiarata non prova durata infinita; un periodo documentato non è necessariamente una decorrenza continuativa. La ricostruzione dichiara criterio di continuità e limiti.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-068

### K-072 — Current-State Derivation come nome sempre derivativo

- **ID:** K-072
- **Conoscenza:** Current-State Derivation come nome sempre derivativo
- **Natura:** RICLASSIFICAZIONE; SUPERAMENTO
- **Stato:** SUPERATA
- **Origine:** R3 §R3.3, Componenti interessati; AUDIT §B 25h
- **Problema che risolve:** Il nome assumeva una nuova derivazione per ogni stato corrente.
- **Ultima formulazione giustificata:** Formulazione precedente troppo vincolante: una ricostruzione può comporre recupero, selezione e ragionamento senza produrre sempre una nuova Assertion.
- **Supera:** —
- **Superata da:** K-073
- **Vincoli collegati:** —

### K-073 — Current Reconstruction contestualizzata

- **ID:** K-073
- **Conoscenza:** Current Reconstruction contestualizzata
- **Natura:** RESPONSABILITÀ NECESSARIA; DEFINIZIONE
- **Stato:** STABILE
- **Origine:** R3 §R3.3; AUDIT §B 25h
- **Problema che risolve:** Ultimo arrivo e valore corrente erano equiparati.
- **Ultima formulazione giustificata:** Sintetizzare ciò che Fold può sostenere su referente/aspetto per un tempo e scopo, con basi, conflitti, correzioni, assunzioni e limiti. Può essere incompleta/non univoca; non è necessariamente nuovo fatto o nuova derivazione.
- **Supera:** K-072
- **Superata da:** —
- **Vincoli collegati:** K-070, K-071

### K-074 — Passato ricostruito oggi distinto da ciò che Fold sosteneva allora

- **ID:** K-074
- **Conoscenza:** Passato ricostruito oggi distinto da ciò che Fold sosteneva allora
- **Natura:** REGOLA TEMPORALE; CRITERIO DI CONSERVAZIONE / PROVENANCE
- **Stato:** STABILE
- **Origine:** R3 §R3.3 e Delta §C.7; R4 §R4.8
- **Problema che risolve:** Rielaborare vecchie Source con regole nuove veniva chiamato ricostruzione del pensiero storico.
- **Ultima formulazione giustificata:** Distinguere reference time del contenuto, patrimonio allora disponibile e risultati/criteri realmente usati. La scoperta tardiva non retrodata acquisizione, interpretazione o commitment.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-067, K-073

### K-075 — Risultati materiali per decisioni o spiegazioni: basi recuperabili

- **ID:** K-075
- **Conoscenza:** Risultati materiali per decisioni o spiegazioni: basi recuperabili
- **Natura:** CRITERIO DI CONSERVAZIONE / PROVENANCE
- **Stato:** STABILE
- **Origine:** R3 §R3.4, Che cosa produrre e che cosa conservare?; R4 §R4.8
- **Problema che risolve:** Una conclusione usata poteva sparire lasciando l'effetto senza giustificazione.
- **Ultima formulazione giustificata:** Se un risultato sostiene una decisione o spiegazione storica, recuperare premesse, criterio, riferimento temporale e limiti pertinenti. Non conservare ogni calcolo transitorio né imporre nuova Assertion; la necessità di spiegare determina il minimo.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-003, K-027, K-074

### K-076 — Derivazione distinta da osservazione e giustificazione non solo fra Assertion

- **ID:** K-076
- **Conoscenza:** Derivazione distinta da osservazione e giustificazione non solo fra Assertion
- **Natura:** DEFINIZIONE; CRITERIO DI CONSERVAZIONE / PROVENANCE
- **Stato:** STABILE
- **Origine:** R3 §R3.4; R4 §R4.4 e R4.8
- **Problema che risolve:** derived_from fra sole Assertion non spiegava scadenze e riscontri negativi.
- **Ultima formulazione giustificata:** Distinguere attività, conclusione e giustificazione inferenziale. Premesse possono includere regola/metodo, parametri temporali, perimetro/assenze delimitate e limiti. Conclusione condizionata alla correttezza delle premesse; nessuna Source fittizia per il pagamento mancante.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-054, K-067, K-075

### K-077 — Nessun riscontro riconosciuto non significa nessuna Source arrivata

- **ID:** K-077
- **Conoscenza:** Nessun riscontro riconosciuto non significa nessuna Source arrivata
- **Natura:** GUARDRAIL / INVARIANTE
- **Stato:** STABILE
- **Origine:** R3 §R3.4 e R3.7
- **Problema che risolve:** Bolletta arrivata ma illeggibile veniva classificata non arrivata.
- **Ultima formulazione giustificata:** Distinguere materiale ricevuto, letto, interpretato, riconciliato e ammesso. Per assenze/completezza considerare anche proposte e materiale parzialmente elaborato, non solo Knowledge.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-033, K-034, K-041

### K-078 — Periodicità osservata, previsione e obbligo non coincidono

- **ID:** K-078
- **Conoscenza:** Periodicità osservata, previsione e obbligo non coincidono
- **Natura:** DISTINZIONE; REGOLA TEMPORALE
- **Stato:** STABILE
- **Origine:** R3 §R3.4 e R3.7
- **Problema che risolve:** Sei caricamenti mensili diventavano obbligo di emissione mensile.
- **Ultima formulazione giustificata:** Distinguere periodicità di emissione, periodo fatturato e caricamento. Previsione inferita, dichiarazione di emissione, obbligo e raccomandazione hanno basi e forza diverse.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-076

### K-079 — Attenzione temporale dipende dal comportamento promesso

- **ID:** K-079
- **Conoscenza:** Attenzione temporale dipende dal comportamento promesso
- **Natura:** RESPONSABILITÀ NECESSARIA; REGOLA OPERATIVA; REGOLA TEMPORALE
- **Stato:** STABILE
- **Origine:** R3 §R3.6 e Delta §B.7
- **Problema che risolve:** Senza nuovo documento non era chiaro come rivalutare una scadenza.
- **Ultima formulazione giustificata:** Temporal Evaluation riceve reference time; la Function dichiara risposta su richiesta o attenzione autonoma. Se promette autonomia, il coordinamento del Work autorizzato riconosce la condizione temporale e prosegue; il tempo non crea Source né alert necessario.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-007, K-024, K-067

### K-080 — Attesa: base informativa, riscontro e comportamento separati

- **ID:** K-080
- **Conoscenza:** Attesa: base informativa, riscontro e comportamento separati
- **Natura:** DEFINIZIONE; DISTINZIONE
- **Stato:** CANDIDATA
- **Origine:** R3 §R3.7, Soluzione candidata E
- **Problema che risolve:** Expectation mescolava previsione, obbligo, desiderio e promemoria.
- **Ultima formulazione giustificata:** Composizione minima: base dell'attesa, esito nel perimetro esaminato, comportamento. Derivation può prevedere, Query verificare, Policy scegliere attenzione, Function presentarla. Se riusata, recuperare base, condizioni e finestra; memoria operativa conserva l'attenzione.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-077, K-078, K-079

### K-081 — Nessuna primitiva Expectation o controller temporale dimostrati

- **ID:** K-081
- **Conoscenza:** Nessuna primitiva Expectation o controller temporale dimostrati
- **Natura:** DECISIONE NEGATIVA
- **Stato:** STABILE
- **Origine:** R3 §R3.6–R3.7 e Delta §A.10/B.10
- **Problema che risolve:** Un'attesa informativa induceva un nuovo oggetto universale o manager.
- **Ultima formulazione giustificata:** La distinzione fra previsione, mancato riscontro e azione può essere rappresentata senza tre oggetti. Il caso non impone Temporal Controller, Expectation Manager, Reprocessing Manager o Event temporale Core.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-047, K-080

### K-082 — Correzione, successione, conflitto e informazione tardiva distinti

- **ID:** K-082
- **Conoscenza:** Correzione, successione, conflitto e informazione tardiva distinti
- **Natura:** DISTINZIONE; REGOLA TEMPORALE
- **Stato:** STABILE
- **Origine:** R3 §R3.5
- **Problema che risolve:** Un unico superseded cancellava la natura dei cambiamenti.
- **Ultima formulazione giustificata:** Correzione rettifica un contenuto; successione cambia la realtà descritta; conflitto riguarda incompatibilità nel medesimo contesto; informazione tardiva cambia quando si apprende. Possono combinarsi ma non equivalgono.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** —

### K-083 — Comparabilità precede incompatibilità

- **ID:** K-083
- **Conoscenza:** Comparabilità precede incompatibilità
- **Natura:** RESPONSABILITÀ NECESSARIA; GUARDRAIL / INVARIANTE
- **Stato:** STABILE
- **Origine:** R3 §R3.5; R5 Quality dell'identità; AUDIT §25b/25f
- **Problema che risolve:** Due importi o fornitori diversi erano conflitto per sola diversità.
- **Ultima formulazione giustificata:** Confrontare stesso referente/ruolo, tempi e vincoli di dominio. Totale, saldo e pagamento parziale possono differire senza conflitto. Conflict Detection specializza Comparison e non decide prevalenza.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-082

### K-084 — Rettifica dichiarata, riconosciuta e applicata sono passaggi distinti

- **ID:** K-084
- **Conoscenza:** Rettifica dichiarata, riconosciuta e applicata sono passaggi distinti
- **Natura:** REGOLA DI GOVERNANCE; REGOLA TEMPORALE
- **Stato:** STABILE
- **Origine:** R3 §R3.5; GATE §2; AUDIT §25d
- **Problema che risolve:** Nuova nota di rettifica sostituiva tutto il documento automaticamente.
- **Ultima formulazione giustificata:** Preservare dichiarazione iniziale, interpretazione, nuova proposizione, bersaglio e relazione valutata, eventuale revisione. Una correzione locale non invalida link/attributi estranei; non raccontare 84,72 valido fino alla data di scoperta se era errore originario.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-038, K-082, K-083

### K-085 — Impatto comprende assenze, ambiti e continuità, non solo premesse positive

- **ID:** K-085
- **Conoscenza:** Impatto comprende assenze, ambiti e continuità, non solo premesse positive
- **Natura:** CRITERIO DI CONSERVAZIONE / PROVENANCE; RESPONSABILITÀ NECESSARIA
- **Stato:** STABILE
- **Origine:** R3 §R3.8
- **Problema che risolve:** Una nuova Assertion non poteva figurare fra le dipendenze del risultato passato.
- **Ultima formulazione giustificata:** Per individuare conseguenze recuperare referente, ruolo, tempo, perimetro esaminato e presupposti di assenza/completezza/continuità oltre alle premesse lette. Aggregazioni e risultati negativi possono cambiare per un nuovo membro.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-071, K-076, K-077

### K-086 — Dipendenza non trovata non dimostra assenza d'impatto

- **ID:** K-086
- **Conoscenza:** Dipendenza non trovata non dimostra assenza d'impatto
- **Natura:** GUARDRAIL / INVARIANTE
- **Stato:** STABILE
- **Origine:** R3 §R3.8
- **Problema che risolve:** Lineage insufficiente dava una falsa attestazione di nessun impatto.
- **Ultima formulazione giustificata:** L'insieme potenzialmente influenzato può non essere minimo/esatto. Se riferimenti o basi sono insufficienti, ampliare il controllo o dichiarare indeterminatezza; non presentare senza verifica il vecchio risultato come aggiornato.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-085

### K-087 — Impatto potenziale, rivalutazione e risultato accertato distinti

- **ID:** K-087
- **Conoscenza:** Impatto potenziale, rivalutazione e risultato accertato distinti
- **Natura:** DISTINZIONE; REGOLA TEMPORALE
- **Stato:** STABILE
- **Origine:** R3 §R3.9, apertura e Cinque passaggi; R6 §V.9
- **Problema che risolve:** Risorsa cambiata rendeva automaticamente falso ogni risultato dipendente.
- **Ultima formulazione giustificata:** Separare risultato storico, potenzialmente influenzato, rivalutato/confermato, rivalutato/corretto e non verificato per un uso. Impatto non equivale al ricalcolo già eseguito né al diverso valore finale.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-025, K-086

### K-088 — Stale non è uno stato globale di falsità

- **ID:** K-088
- **Conoscenza:** Stale non è uno stato globale di falsità
- **Natura:** DECISIONE NEGATIVA; REGOLA TEMPORALE
- **Stato:** STABILE
- **Origine:** R3 §R3.9 e Delta §F.8
- **Problema che risolve:** Una modifica invalidava retroattivamente materiale, lavori e conoscenza.
- **Ultima formulazione giustificata:** Un risultato può essere corretto come testimonianza storica e non verificato per uso attuale. Qualificare target e scopo invece di assegnare falsità globale o trasformare il vecchio lavoro in fallito.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-070, K-087

### K-089 — Impatto, autorizzazione, riesecuzione e storia sono responsabilità distinte

- **ID:** K-089
- **Conoscenza:** Impatto, autorizzazione, riesecuzione e storia sono responsabilità distinte
- **Natura:** RESPONSABILITÀ NECESSARIA; REGOLA OPERATIVA
- **Stato:** STABILE
- **Origine:** R3 §R3.9; R6 §V.9; GATE §3
- **Problema che risolve:** Il rilevamento d'impatto si trasformava in ricalcolo universale.
- **Ultima formulazione giustificata:** Individuare e qualificare l'impatto; scegliere/rispettare l'autorità per la rivalutazione; eseguirla; produrre esito nuovo mantenendo il precedente. Nessun reprocessing automatico generale né manager per tipo di modifica.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-007, K-087

### K-090 — Modifica Mapping, Domain, Core e Policy ha significati differenti

- **ID:** K-090
- **Conoscenza:** Modifica Mapping, Domain, Core e Policy ha significati differenti
- **Natura:** DISTINZIONE
- **Stato:** STABILE
- **Origine:** R3 §R3.9
- **Problema che risolve:** Configurazione cambiata provocava lo stesso effetto su tutto.
- **Ultima formulazione giustificata:** Seguire dipendenze reali: Mapping può cambiare interpretazione senza cambiare lettura; Domain può correggere comprensione o cambiare significato da una decorrenza; Policy cambia comportamento, non per sé i claim. Non applicare retroattività per default.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-064, K-089

### K-091 — Cambiare un Core invariant richiede decisione fondazionale esplicita

- **ID:** K-091
- **Conoscenza:** Cambiare un Core invariant richiede decisione fondazionale esplicita
- **Natura:** GUARDRAIL / INVARIANTE
- **Stato:** STABILE
- **Origine:** R3 §R3.9, Cambia un Core invariant
- **Problema che risolve:** Una modifica fondazionale veniva trattata come normale cambio di configurazione.
- **Ultima formulazione giustificata:** Identificare assunzione superata, rappresentazioni coinvolte e informazione ancora recuperabile. Il numero di versione non ricrea differenze già perdute; non autorizzare qui nuovi invarianti.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-047, K-090

### K-092 — Nuova Policy non annulla le decisioni storiche né revoca tutto

- **ID:** K-092
- **Conoscenza:** Nuova Policy non annulla le decisioni storiche né revoca tutto
- **Natura:** REGOLA DI GOVERNANCE; REGOLA TEMPORALE
- **Stato:** STABILE
- **Origine:** R3 §R3.9, Caso K; R3 §R3.10
- **Problema che risolve:** Policy nuova veniva applicata indistintamente a decisioni passate e pendenti.
- **Ultima formulazione giustificata:** Distinguere cosa si farebbe oggi, autorità della disposizione pendente e azione già avvenuta. Dipendenza dalla Policy attuale o da condizioni originarie deve essere esplicita; nessuna revoca automatica per sola versione.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-015, K-025, K-090

### K-093 — Versione nominale non basta: recuperare le definizioni effettivamente usate

- **ID:** K-093
- **Conoscenza:** Versione nominale non basta: recuperare le definizioni effettivamente usate
- **Natura:** CRITERIO DI CONSERVAZIONE / PROVENANCE
- **Stato:** STABILE
- **Origine:** R3 §R3.9; R4 §R4.8
- **Problema che risolve:** Etichetta versione precedente era l'unica base della spiegazione.
- **Ultima formulazione giustificata:** Conservare significato/parte pertinente della risorsa usata e dipendenza del risultato. Non tutti i risultati dipendono da tutte le risorse; il cambiamento deve essere descritto abbastanza da valutarne l'impatto.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-075, K-085, K-090

### K-094 — Applicabilità non ridotta al numero di versione del target

- **ID:** K-094
- **Conoscenza:** Applicabilità non ridotta al numero di versione del target
- **Natura:** REGOLA DI GOVERNANCE
- **Stato:** STABILE
- **Origine:** R3 §R3.10
- **Problema che risolve:** Target formalmente uguale faceva ignorare nuova evidenza contraria.
- **Ultima formulazione giustificata:** Verificare contenuto, aspetto, transizione e condizioni: nuova rappresentazione può non cambiare significato; nuova informazione può violare condizioni a target immutato. Non applicabile o non determinabile non si trasferisce tacitamente: richiede rivalutazione pertinente.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-018, K-025, K-089

### K-095 — Atto storico, conformità procedurale, correttezza fattuale e uso corrente distinti

- **ID:** K-095
- **Conoscenza:** Atto storico, conformità procedurale, correttezza fattuale e uso corrente distinti
- **Natura:** DISTINZIONE; REGOLA DI GOVERNANCE
- **Stato:** STABILE
- **Origine:** R3 §R3.10
- **Problema che risolve:** Conferma avvenuta allora era descritta come verità valida per sempre.
- **Ultima formulazione giustificata:** Conservare l'atto e la sua base senza farne uno scudo contro nuovi contributi. Una correzione dopo applicazione è una nuova transizione, non riscrittura dell'azione passata.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-019, K-074, K-092

### K-096 — Aperture temporali, di rivalutazione e conservazione ulteriore

- **ID:** K-096
- **Conoscenza:** Aperture temporali, di rivalutazione e conservazione ulteriore
- **Natura:** APERTURA
- **Stato:** APERTA
- **Origine:** R3 Delta §G
- **Problema che risolve:** I casi non determinano tutte le regole concrete.
- **Ultima formulazione giustificata:** Restano forma/precisione dei tempi, continuità per rapporto, condizioni effettive di applicabilità/revoca, riconoscimento rettifiche, gestione conflitti, policy di rivalutazione e conservazione dei derivati oltre i casi necessari a spiegare decisioni/effetti.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-071, K-075, K-084, K-094

## Round 4 — qualità, supporto, provenance e regole

### K-097 — Quality Assessment è valutazione storica di target, dimensione, base e scopo

- **ID:** K-097
- **Conoscenza:** Quality Assessment è valutazione storica di target, dimensione, base e scopo
- **Natura:** DEFINIZIONE; CRITERIO DI CONSERVAZIONE / PROVENANCE
- **Stato:** STABILE
- **Origine:** R4 §R4.1 e R4.9
- **Problema che risolve:** Qualità alta senza bersaglio non informava né spiegava le decisioni.
- **Ultima formulazione giustificata:** La valutazione non è qualità intrinseca globale; può cambiare senza cambiare il contenuto. Collegare bersaglio, dimensione, base, contesto/scopo e momento; conservare significato storico quando usata.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-020, K-061, K-075

### K-098 — Cinque famiglie di qualità senza score globale obbligatorio

- **ID:** K-098
- **Conoscenza:** Cinque famiglie di qualità senza score globale obbligatorio
- **Natura:** DISTINZIONE; DECISIONE NEGATIVA
- **Stato:** CANDIDATA
- **Origine:** R4 §R4.1–R4.2 e Delta §B; R6 §I.A
- **Problema che risolve:** OCR eccellente nascondeva semantica ambigua e link debole.
- **Ultima formulazione giustificata:** Distinguere rappresentazione/lettura, determinazione semantica, qualità referenziale, adeguatezza del supporto e inferenziale. Sintesi solo per scopo mantenendo basi locali; esito Work e conformità Decision restano valutazioni operative. Il numero e i confini definitivi delle cinque famiglie restano candidati; sono stabili le differenze che impediscono uno score globale.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-097

### K-099 — Prudenza dell'azione non abbassa retroattivamente la qualità

- **ID:** K-099
- **Conoscenza:** Prudenza dell'azione non abbassa retroattivamente la qualità
- **Natura:** REGOLA DI GOVERNANCE; GUARDRAIL / INVARIANTE
- **Stato:** STABILE
- **Origine:** R4 §R4.2, Situazione 4
- **Problema che risolve:** Richiedere conferma equivaleva a dichiarare poco credibile il contenuto.
- **Ultima formulazione giustificata:** Policy può richiedere conferma per rischio, reversibilità o autonomia anche con buono supporto. Quality descrive; autorizzazione e comportamento sono distinti.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-014, K-020, K-070

### K-100 — Reliability della Source non è una proprietà unica o intrinseca

- **ID:** K-100
- **Conoscenza:** Reliability della Source non è una proprietà unica o intrinseca
- **Natura:** DISTINZIONE; DECISIONE NEGATIVA
- **Stato:** STABILE
- **Origine:** R4 §R4.3
- **Problema che risolve:** Canale, autenticità e autorevolezza erano confusi con verità.
- **Ultima formulazione giustificata:** Separare provenienza, fedeltà/integrità, competenza/autorità relativa alla proposizione, indipendenza e corroborazione. Source esiste senza giudizio positivo; Adapter preserva fatti di canale, non assegna attendibilità generale.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-049, K-098

### K-101 — Origine comune e indipendenza dipendono dal bersaglio valutato

- **ID:** K-101
- **Conoscenza:** Origine comune e indipendenza dipendono dal bersaglio valutato
- **Natura:** GUARDRAIL / INVARIANTE; CRITERIO DI CONSERVAZIONE / PROVENANCE
- **Stato:** STABILE
- **Origine:** R4 §R4.3–R4.5; REG D03
- **Problema che risolve:** PDF, foto della stampa ed email venivano contati come tre attestazioni.
- **Ultima formulazione giustificata:** Più letture possono migliorare precisione/copertura senza fornire origini fattuali indipendenti. Conservare trasformazioni e origine comune pertinenti; compatibilità e molteplicità non provano corroborazione indipendente.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-021, K-054, K-100

### K-102 — Indipendenza non determinata è un esito legittimo

- **ID:** K-102
- **Conoscenza:** Indipendenza non determinata è un esito legittimo
- **Natura:** GUARDRAIL / INVARIANTE
- **Stato:** STABILE
- **Origine:** R4 §R4.5, Quality Assessment
- **Problema che risolve:** Origine parzialmente ignota costringeva a inventare dipendenza o indipendenza.
- **Ultima formulazione giustificata:** Quando la dipendenza non è risolta, l'assessment può dichiarare indipendenza non determinata rispetto al bersaglio. Quality non sceglie automaticamente l'azione prudenziale; nessuna primitiva Independence emerge.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-097, K-101

### K-103 — Supporto indirizzabile quando ha scope, qualità, verifica o contestazione propri

- **ID:** K-103
- **Conoscenza:** Supporto indirizzabile quando ha scope, qualità, verifica o contestazione propri
- **Natura:** CRITERIO DI CONSERVAZIONE / PROVENANCE
- **Stato:** STABILE
- **Origine:** R4 §R4.4
- **Problema che risolve:** Rinunciare a Evidence-oggetto eliminava anche la granularità del supporto.
- **Ultima formulazione giustificata:** Una relazione binaria nuda non basta: target, natura, scope, origine, dipendenze e valutazioni devono essere recuperabili; rendere richiamabile il legame quando necessario a verifica, contestazione, decisione o spiegazione.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-054, K-065

### K-104 — Costruzione del supporto distribuita fra produttori competenti

- **ID:** K-104
- **Conoscenza:** Costruzione del supporto distribuita fra produttori competenti
- **Natura:** RICLASSIFICAZIONE; RESPONSABILITÀ NECESSARIA
- **Stato:** STABILE
- **Origine:** R4 §R4.4; AUDIT §20
- **Problema che risolve:** Evidence Construction separata sembrava creare prova dal nulla.
- **Ultima formulazione giustificata:** Interpretation, Verification, Reconciliation e Derivation stabiliscono e conservano supporti/giustificazioni dove li producono. Nessun componente unico necessario e nessuna attendibilità per sola esistenza del collegamento.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-054, K-103

### K-105 — Provenance, Lineage, storia epistemica e audit operativo distinti

- **ID:** K-105
- **Conoscenza:** Provenance, Lineage, storia epistemica e audit operativo distinti
- **Natura:** DISTINZIONE; DECISIONE NEGATIVA
- **Stato:** STABILE
- **Origine:** R4 §R4.6
- **Problema che risolve:** Log eseguito veniva trattato come giustificazione dell'Assertion.
- **Ultima formulazione giustificata:** Distinguere origine, trasformazioni, evoluzione di supporti/commitment ed esecuzioni autorizzate/tentate. Una registrazione può contribuire a più viste; non richiedere quattro repository né duplicare il contenuto.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-059, K-062

### K-106 — Cattura locale delle tracce materialmente rilevanti

- **ID:** K-106
- **Conoscenza:** Cattura locale delle tracce materialmente rilevanti
- **Natura:** RESPONSABILITÀ NECESSARIA; CRITERIO DI CONSERVAZIONE / PROVENANCE
- **Stato:** STABILE
- **Origine:** R4 §R4.6; AUDIT §15 e §C
- **Problema che risolve:** Un Recorder centrale postumo perdeva scope e motivazioni locali.
- **Ultima formulazione giustificata:** Ogni produttore di risultato materiale conserva collegamenti input–trasformazione–output, basi e condizioni pertinenti. Tentativi falliti solo quando servono a capire l'esito/proseguire; nessun log indiscriminato né ricostruzione a posteriori inventata.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-027, K-093, K-105

### K-107 — Granularità minima: il bersaglio dell'effetto differente

- **ID:** K-107
- **Conoscenza:** Granularità minima: il bersaglio dell'effetto differente
- **Natura:** CRITERIO DI CONSERVAZIONE / PROVENANCE
- **Stato:** STABILE
- **Origine:** R4 §R4.7
- **Problema che risolve:** Una rettifica dell'importo diventava rettifica di tutta la bolletta.
- **Ultima formulazione giustificata:** Provenance, supporto e valutazione raggiungono la minima unità su cui conferma/correzione/contestazione/derivazione hanno effetto diverso: target semantico, parte supportante, risultato trasformativo e legame pertinente; non un oggetto per parola.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-031, K-038, K-084, K-103

### K-108 — Recuperare, spiegare e rieseguire sono capacità diverse

- **ID:** K-108
- **Conoscenza:** Recuperare, spiegare e rieseguire sono capacità diverse
- **Natura:** DISTINZIONE; CRITERIO DI CONSERVAZIONE / PROVENANCE
- **Stato:** STABILE
- **Origine:** R4 §R4.8
- **Problema che risolve:** Rieseguire oggi sostituiva il risultato realmente usato ieri.
- **Ultima formulazione giustificata:** Recuperare l'output storico e la sua base, spiegare il percorso e rieseguire non sono equivalenti. Non promettere identità perfetta dell'esecuzione; la riproducibilità non è prova di verità.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-074, K-075, K-093

### K-109 — Test di materialità delle dipendenze da conservare

- **ID:** K-109
- **Conoscenza:** Test di materialità delle dipendenze da conservare
- **Natura:** CRITERIO DI CONSERVAZIONE / PROVENANCE
- **Stato:** STABILE
- **Origine:** R4 §R4.8
- **Problema che risolve:** Ogni risultato sembrava dover allegare ogni versione di ogni modello.
- **Ultima formulazione giustificata:** Registrare una dipendenza se cambiarla potrebbe alterare materialmente significato, giustificazione/esito, o se serve a spiegare la scelta fra alternative. Recuperare la parte realmente usata, non copie indiscriminate di tutte le risorse.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-075, K-093, K-106

### K-110 — Explanation segue tracce reali, non ripara lacune inventando

- **ID:** K-110
- **Conoscenza:** Explanation segue tracce reali, non ripara lacune inventando
- **Natura:** RESPONSABILITÀ NECESSARIA; GUARDRAIL / INVARIANTE
- **Stato:** STABILE
- **Origine:** R4 §R4.8 e audit componenti; AUDIT §32
- **Problema che risolve:** Una spiegazione plausibile poteva sostituire la storia effettiva.
- **Ultima formulazione giustificata:** Comporre origine, supporti, trasformazioni, inferenze, conflitti e motivi dell'azione; niente Source mancanti inventate, definizioni retroattribuite, output storico sostituito o confidence ricalcolata implicitamente.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-105, K-108

### K-111 — Nuova valutazione richiede nuova base, criterio o contesto pertinente

- **ID:** K-111
- **Conoscenza:** Nuova valutazione richiede nuova base, criterio o contesto pertinente
- **Natura:** GUARDRAIL / INVARIANTE
- **Stato:** STABILE
- **Origine:** R1 §R7; R4 §R4.9; R6 §IV Quality↔Admission; REG D04
- **Problema che risolve:** Ripetizione, Admission e riuso operativo aumentavano artificiosamente il supporto.
- **Ultima formulazione giustificata:** Distinguere assessment storici; solo nuova base/criterio/contesto materialmente pertinente giustifica una nuova valutazione. Non basta trovarsi nella Knowledge, essere ammesso o attraversare un nuovo tentativo.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-021, K-097, K-101

### K-112 — Una regola composita va separata prima di collocarla

- **ID:** K-112
- **Conoscenza:** Una regola composita va separata prima di collocarla
- **Natura:** GUARDRAIL / INVARIANTE
- **Stato:** STABILE
- **Origine:** R4 §R4.10
- **Problema che risolve:** Scadenza superata→verifica inglobava significato, calcolo, prudenza e presentazione.
- **Ultima formulazione giustificata:** Separare cosa descrive, valuta, calcola, vincola, sceglie ed esegue. Non assegnare tutta una frase al Domain o alle Policy perché contiene un termine di dominio.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-064

### K-113 — Test di collocazione Core/Domain/Mapping/Quality/Engine/Policy

- **ID:** K-113
- **Conoscenza:** Test di collocazione Core/Domain/Mapping/Quality/Engine/Policy
- **Natura:** DEFINIZIONE; REGOLA DI GOVERNANCE
- **Stato:** STABILE
- **Origine:** R4 §R4.10, Passi 1–7
- **Problema che risolve:** Tutti i criteri residui finivano nel Domain o nel motore.
- **Ultima formulazione giustificata:** Core protegge distinzioni trasversali; Domain significati/vincoli; Mapping corrispondenze sorgente–significato; Quality dimensioni/basi; Engine opera sui significati forniti; Policy sceglie comportamento ammissibile. Esecuzione/presentazione appartengono a Workflow/Function/Admission, non forzate nelle risorse.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-014, K-112

### K-114 — Regola assoluta: ogni Assertion deve già avere supporto

- **ID:** K-114
- **Conoscenza:** Regola assoluta: ogni Assertion deve già avere supporto
- **Natura:** GUARDRAIL / INVARIANTE; SUPERAMENTO
- **Stato:** SUPERATA
- **Origine:** R4 §R4.10, regola A; Delta §H.9
- **Problema che risolve:** L'invariante escludeva ipotesi dichiaratamente non sostenute.
- **Ultima formulazione giustificata:** La regola A è riconosciuta troppo assoluta: confonde esistenza di una proposizione e presentazione come conoscenza sostenuta.
- **Supera:** —
- **Superata da:** K-115
- **Vincoli collegati:** K-055

### K-115 — Non presentare come sostenuta una Assertion perdendone la giustificazione

- **ID:** K-115
- **Conoscenza:** Non presentare come sostenuta una Assertion perdendone la giustificazione
- **Natura:** GUARDRAIL / INVARIANTE
- **Stato:** STABILE
- **Origine:** R4 §R4.10, regola A; R6 §I.G
- **Problema che risolve:** Occorre preservare la giustificazione senza vietare le ipotesi.
- **Ultima formulazione giustificata:** Un'ipotesi esplicitamente non sostenuta può esistere; quando Fold assume/mostra supporto deve mantenerne la base pertinente, documentale o inferenziale. Admission non fabbrica evidenza.
- **Supera:** K-114
- **Superata da:** —
- **Vincoli collegati:** K-054, K-055, K-075

### K-116 — Mapping aggiornato non è una nuova testimonianza fattuale

- **ID:** K-116
- **Conoscenza:** Mapping aggiornato non è una nuova testimonianza fattuale
- **Natura:** GUARDRAIL / INVARIANTE
- **Stato:** STABILE
- **Origine:** R4 §R4.4, J e stress T8
- **Problema che risolve:** Nuova interpretazione della stessa data diventava seconda prova della scadenza.
- **Ultima formulazione giustificata:** Un Mapping può giustificare una traduzione semantica più determinata; non modifica il materiale né crea origine indipendente del fatto.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-090, K-101, K-111

### K-117 — Rettifica pertinente non selezionata con ranking generico delle fonti

- **ID:** K-117
- **Conoscenza:** Rettifica pertinente non selezionata con ranking generico delle fonti
- **Natura:** GUARDRAIL / INVARIANTE
- **Stato:** STABILE
- **Origine:** R4 stress T7 e Delta §H.5
- **Problema che risolve:** Fonte più autorevole sostituiva il riconoscimento del rapporto correttivo.
- **Ultima formulazione giustificata:** 34,72 è pertinente quando è sostenuto il rapporto di rettifica del bersaglio; quantità di fonti, recenza o autorità globale da sole non spiegano la prevalenza.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-083, K-084, K-100

### K-118 — Aperture su Quality e indipendenza empirica

- **ID:** K-118
- **Conoscenza:** Aperture su Quality e indipendenza empirica
- **Natura:** APERTURA
- **Stato:** APERTA
- **Origine:** R4 Delta §I
- **Problema che risolve:** Le distinzioni non determinano un algoritmo di affidabilità.
- **Ultima formulazione giustificata:** Restano forma/dimensioni dettagliate degli assessment, distinzione integrità/autenticità/competenza, criteri per valutare indipendenza con origini parzialmente ignote, composizione per scopo e soglie concrete di automazione.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-097, K-100, K-102

### K-119 — Aperture su persistenza delle proposte e conferma delle Observation

- **ID:** K-119
- **Conoscenza:** Aperture su persistenza delle proposte e conferma delle Observation
- **Natura:** APERTURA
- **Stato:** APERTA
- **Origine:** R4 §R4.2, Situazione 2; Delta §I
- **Problema che risolve:** La storia recuperabile non sceglie ancora una rappresentazione unica.
- **Ultima formulazione giustificata:** Nuova Observation qualificata o supporto alla lettura esistente restano alternative, preservando l'esito automatico. R6 assegna la conservazione delle proposte alla memoria informativa (K-144): resta aperta la forma concreta, non la loro esistenza senza Work.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-043, K-053, K-097

## Round 5 — identità, identificatori e governo della Knowledge

### K-120 — Referent come soggetto della realtà/documentale con identità indipendente

- **ID:** K-120
- **Conoscenza:** Referent come soggetto della realtà/documentale con identità indipendente
- **Natura:** DEFINIZIONE
- **Stato:** SUPERATA
- **Origine:** R5 §R5.1; R6 §I.A e V.1
- **Problema che risolve:** Riferibilità generica non distingueva soggetti e risultati interni.
- **Ultima formulazione giustificata:** Definizione R5: rappresentazione di soggetto distinto la cui identità conta indipendentemente da Source, Observation, etichetta, Identifier o Assertion. Indicatori: contenuti sul soggetto, coreferenza, continuità e conseguenze dell'errore; non formula automatica.
- **Supera:** —
- **Superata da:** K-143
- **Vincoli collegati:** K-056
- **Note:** Il criterio di significato esterno all'elaborazione e l'esistenza del soggetto vengono riesaminati nel Round 6.

### K-121 — Identifier: schema, valore e assegnazione sono tre livelli

- **ID:** K-121
- **Conoscenza:** Identifier: schema, valore e assegnazione sono tre livelli
- **Natura:** DISTINZIONE; DEFINIZIONE
- **Stato:** STABILE
- **Origine:** R5 §R5.3; R6 §V.4
- **Problema che risolve:** Referent+stringa non spiegavano significato e ambito identificativo.
- **Ultima formulazione giustificata:** Domain definisce schema, normalizzazione, genere di soggetto, ambito e condizioni; Value conserva contenuto identificativo; assegnazione a Referent è proposizione qualificabile, temporale, contestabile e correggibile. Non sono tre primitive obbligatorie.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-047, K-058

### K-122 — Stringa identificativa osservata può precedere l'assegnazione

- **ID:** K-122
- **Conoscenza:** Stringa identificativa osservata può precedere l'assegnazione
- **Natura:** GUARDRAIL / INVARIANTE
- **Stato:** STABILE
- **Origine:** R5 §R5.3, Casi C–E
- **Problema che risolve:** POD sintatticamente corretto era automaticamente il POD vero dell'utenza.
- **Ultima formulazione giustificata:** Distinguere presenza nella Source, conformità allo schema, interpretazione identificativa e assegnazione sostenuta. Una stringa stampata errata resta Observation corretta; l'errore riguarda dichiarazione/assegnazione, non necessariamente OCR.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-045, K-050, K-121

### K-123 — Normalizzazione non corregge silenziosamente un identificatore

- **ID:** K-123
- **Conoscenza:** Normalizzazione non corregge silenziosamente un identificatore
- **Natura:** GUARDRAIL / INVARIANTE; CRITERIO DI CONSERVAZIONE / PROVENANCE
- **Stato:** STABILE
- **Origine:** R5 §R5.3 e stress finale §5–6/11
- **Problema che risolve:** POD quasi uguale era cambiato per ottenere un match.
- **Ultima formulazione giustificata:** Conservare forma originale, valore normalizzato e trasformazione. Somiglianza col noto non autorizza sostituire la stringa osservata; se si conosce solo l'errore e non il valore corretto, non inventarlo.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-057, K-121, K-122

### K-124 — Match identificativo non prova identità né autorizza auto-link

- **ID:** K-124
- **Conoscenza:** Match identificativo non prova identità né autorizza auto-link
- **Natura:** GUARDRAIL / INVARIANTE
- **Stato:** STABILE
- **Origine:** R5 §R5.3–R5.4
- **Problema che risolve:** Corrispondenza esatta o quasi esatta sostituiva schema, scope e supporto.
- **Ultima formulazione giustificata:** Valutare lettura, schema, ambito, assegnazione, tempi e indizi contrari. Il valore può essere unico solo in un ambito o identificare un altro tipo di soggetto; Policy/autorità governano l'applicazione.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-014, K-018, K-121

### K-125 — Reconciliation formula e valuta proposte, non scopre verità infallibili

- **ID:** K-125
- **Conoscenza:** Reconciliation formula e valuta proposte, non scopre verità infallibili
- **Natura:** RESPONSABILITÀ NECESSARIA
- **Stato:** STABILE
- **Origine:** R5 §R5.4; AUDIT §25a
- **Problema che risolve:** Prende candidati→restituisce Referent nascondeva alternative e nuovo soggetto.
- **Ultima formulazione giustificata:** Rendere recuperabili domanda, alternative, indizi compatibili/contrari, proposta, supporti e aspetti irrisolti. Può non discriminare o non trovare soggetto noto; nessun vincitore, creazione ammessa o fusione obbligatori.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-010, K-124

### K-126 — Ipotesi di coreferenza, sostegno, uso unitario e identità reale distinti

- **ID:** K-126
- **Conoscenza:** Ipotesi di coreferenza, sostegno, uso unitario e identità reale distinti
- **Natura:** DISTINZIONE; REGOLA DI GOVERNANCE
- **Stato:** STABILE
- **Origine:** R5 §R5.5
- **Problema che risolve:** same_as sembrava unire ontologicamente due cose e applicare un merge.
- **Ultima formulazione giustificata:** La proposizione riguarda rappresentazioni che possono denotare lo stesso soggetto; la loro identità nel mondo non viene creata da Fold. Uso unitario operativo richiede autorità e non è la proposizione identitaria.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-015, K-125

### K-127 — Coreferenza non distruttiva, contestabile e reversibile

- **ID:** K-127
- **Conoscenza:** Coreferenza non distruttiva, contestabile e reversibile
- **Natura:** GUARDRAIL / INVARIANTE; CRITERIO DI CONSERVAZIONE / PROVENANCE
- **Stato:** STABILE
- **Origine:** R5 §R5.5, Fusione reversibile e caso M; REG D05
- **Problema che risolve:** Merge eliminava le distinzioni necessarie a correggere una falsa identità.
- **Ultima formulazione giustificata:** Conservare rappresentazioni originarie, differenze, Provenance e giustificazione della coreferenza; consentire contestazione/revisione e ritorno alla distinzione sulla base ancora legittimamente conservata. Nessuna funzione software unmerge o conservazione indiscriminata imposta.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-027, K-106, K-126

### K-128 — Nessun predicato identitario nuovo per ogni stato epistemico

- **ID:** K-128
- **Conoscenza:** Nessun predicato identitario nuovo per ogni stato epistemico
- **Natura:** DECISIONE NEGATIVA
- **Stato:** STABILE
- **Origine:** R5 §R5.5, Serve possibly_same_as?
- **Problema che risolve:** Possibile/stesso/contestato diventavano significati diversi della relazione.
- **Ultima formulazione giustificata:** Una proposizione identitaria può avere posizioni diverse. Compatibile-con e stessa-identità restano significati distinti; possibly_same_as non è obbligatorio per esprimere incertezza.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-052, K-061, K-126

### K-129 — Stesso nome non implica stessa persona né stesso soggetto collegato

- **ID:** K-129
- **Conoscenza:** Stesso nome non implica stessa persona né stesso soggetto collegato
- **Natura:** GUARDRAIL / INVARIANTE
- **Stato:** STABILE
- **Origine:** R5 §R5.1, Mario Rossi; R5 stress finale
- **Problema che risolve:** Omonimie fondevano persone e utenze.
- **Ultima formulazione giustificata:** Mantenere soggetti/alternative distinti davanti a dati discriminanti incompatibili o insufficienti. La stringa condivisa non determina il numero dei Referent né autorizza un terzo soggetto ammesso per default.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-124, K-125

### K-130 — Descrivere una struttura con un'Assertion non la sostituisce

- **ID:** K-130
- **Conoscenza:** Descrivere una struttura con un'Assertion non la sostituisce
- **Natura:** DECISIONE NEGATIVA
- **Stato:** STABILE
- **Origine:** R5 §R5.6
- **Problema che risolve:** Assertion assorbiva supporto, derivazione, tempo e Observation.
- **Ultima formulazione giustificata:** Si possono formulare proposizioni su elementi interni senza eliminarne natura e obblighi: meta-Assertion sul supporto non sostituisce il supporto, frase sulla derivazione non conserva da sola premesse/criterio/parametri. Evitare regressi di supporto e qualificazioni artificialmente separate.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-047, K-055, K-076

### K-131 — Famiglie descrittive, epistemiche, rappresentative, inferenziali e operative

- **ID:** K-131
- **Conoscenza:** Famiglie descrittive, epistemiche, rappresentative, inferenziali e operative
- **Natura:** RICLASSIFICAZIONE
- **Stato:** STABILE
- **Origine:** R5 §R5.7 e Due grammatiche informative?; R6 §V.3
- **Problema che risolve:** Relazione generica uniforme cancellava invarianti differenti.
- **Ultima formulazione giustificata:** Relazioni sul mondo come contenuto proposizionale; supporto/conflitto/correzione, provenance/rappresentazione, giustificazione inferenziale e lavoro restano famiglie semanticamente distinte. Non cinque infrastrutture né distinzione basata solo sul numero degli endpoint.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-059, K-130

### K-132 — Endpoint referenziale, Value e qualificazione della proposizione distinti

- **ID:** K-132
- **Conoscenza:** Endpoint referenziale, Value e qualificazione della proposizione distinti
- **Natura:** DISTINZIONE
- **Stato:** STABILE
- **Origine:** R5 §R5.8
- **Problema che risolve:** Fornitore diventava stringa o importo diventava soggetto autonomo.
- **Ultima formulazione giustificata:** Distinguere Referent→Referent, Referent→Value, relazione epistemica ed elementi qualificanti il significato completo. Value resta categoria non referenziale necessaria; proiezione fornitore corrente non cambia la relazione sottostante.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-058, K-131

### K-133 — Document Identity Reconciliation nascondeva quattro problemi

- **ID:** K-133
- **Conoscenza:** Document Identity Reconciliation nascondeva quattro problemi
- **Natura:** RICLASSIFICAZIONE; RESPONSABILITÀ NECESSARIA
- **Stato:** STABILE
- **Origine:** R5 Document Identity Reconciliation; AUDIT §B 25b
- **Problema che risolve:** Una sola responsabilità mescolava copie, parti, identità e rettifiche.
- **Ultima formulazione giustificata:** Deduplicazione tecnica al confine d'ingresso; composizione documentale nell'interpretazione; sola coreferenza documentale come specializzazione di Reconciliation; versione/rettifica con confronto e semantica Domain. Nessuna capacità eliminata col nome.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-028, K-030, K-084, K-125

### K-134 — Proposte recuperabili senza Work attivo o Knowledge ammessa

- **ID:** K-134
- **Conoscenza:** Proposte recuperabili senza Work attivo o Knowledge ammessa
- **Natura:** RESPONSABILITÀ NECESSARIA; CRITERIO DI CONSERVAZIONE / PROVENANCE
- **Stato:** STABILE
- **Origine:** R5 §R5.10 e Memorie; R6 §VI.C
- **Problema che risolve:** Chiudere il Work cancellava ipotesi ancora utili o la durata le rendeva accettate.
- **Ultima formulazione giustificata:** Memoria informativa conserva ipotesi, alternative, supporti, assessment, conflitti e definizioni; Work conserva domanda, attesa e continuazione. Non contenere ontologicamente le proposte nel Work né promuoverle per persistenza.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-052, K-053, K-062

### K-135 — Knowledge intesa come solo insieme di Assertion ammesse

- **ID:** K-135
- **Conoscenza:** Knowledge intesa come solo insieme di Assertion ammesse
- **Natura:** DEFINIZIONE; SUPERAMENTO
- **Stato:** SUPERATA
- **Origine:** R5 §R5.11, Modello A; R6 §III.5
- **Problema che risolve:** La lettura escludeva Referent e contesto o li assorbiva nella super-primitiva.
- **Ultima formulazione giustificata:** Interpretazione troppo stretta esplicitamente respinta; rappresentazioni referenziali e giustificazioni non diventano tutte Assertion.
- **Supera:** —
- **Superata da:** K-136
- **Vincoli collegati:** K-055

### K-136 — Knowledge come corpo governato, memoria informativa più ampia

- **ID:** K-136
- **Conoscenza:** Knowledge come corpo governato, memoria informativa più ampia
- **Natura:** DEFINIZIONE
- **Stato:** CANDIDATA
- **Origine:** R5 §R5.11; R6 §V.2; GATE §1
- **Problema che risolve:** Archivio e posizione assunta da Fold erano confusi.
- **Ultima formulazione giustificata:** Referent e Assertion ammessi costituiscono il corpo governato con supporti, qualificazioni, revisioni e derivazioni raggiungibili. Source, Observation e proposte sono memoria informativa ma non commitment automaticamente; Admission non cambia natura o verità del contenuto.
- **Supera:** K-135
- **Superata da:** —
- **Vincoli collegati:** K-052, K-061, K-134

### K-137 — Ammissione di Referent e proposte referenziali: apertura R5

- **ID:** K-137
- **Conoscenza:** Ammissione di Referent e proposte referenziali: apertura R5
- **Natura:** APERTURA
- **Stato:** SUPERATA
- **Origine:** R5 Delta §M e Core minimo, Concetti irrisolti
- **Problema che risolve:** La proposta referenziale doveva essere indirizzabile prima del soggetto ammesso.
- **Ultima formulazione giustificata:** Resta da chiarire come rappresentare prima dell'Admission, come governarne il riconoscimento e se un Referent possa essere ammesso senza Assertion già ammessa. Verificare le risoluzioni di R6 senza cancellare l'apertura storica.
- **Supera:** —
- **Superata da:** K-144
- **Vincoli collegati:** K-120, K-125, K-136

### K-138 — Continuità d'identità dipende dal soggetto definito dal Domain

- **ID:** K-138
- **Conoscenza:** Continuità d'identità dipende dal soggetto definito dal Domain
- **Natura:** REGOLA TEMPORALE; DISTINZIONE
- **Stato:** STABILE
- **Origine:** R5 Identità e tempo
- **Problema che risolve:** Cambio fornitore rendeva automaticamente nuova o invariata l'utenza.
- **Ultima formulazione giustificata:** Core distingue identità e descrizioni mutevoli; Domain stabilisce se si parla di punto, rapporto o contratto e quando continui l'identità. Cambiamento di nome, indirizzo o Identifier non è automaticamente nuovo soggetto; assegnazioni possono essere temporali.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-071, K-121, K-126

### K-139 — Qualità referenziale rende visibili indizi discriminanti e alternative

- **ID:** K-139
- **Conoscenza:** Qualità referenziale rende visibili indizi discriminanti e alternative
- **Natura:** RESPONSABILITÀ NECESSARIA
- **Stato:** STABILE
- **Origine:** R5 Quality dell'identità
- **Problema che risolve:** Un solo identity confidence nascondeva perché U prevalesse su V.
- **Ultima formulazione giustificata:** Valutare tipo, schema/ambito, attributi, tempi, conflitti, alternative residue, contributo umano circoscritto, origine comune e dato mancante discriminante. Policy sceglie auto-link/verifica, non l'assessment.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-098, K-102, K-124, K-125

### K-140 — Projection non è memoria primaria dell'identità né nuova semantica

- **ID:** K-140
- **Conoscenza:** Projection non è memoria primaria dell'identità né nuova semantica
- **Natura:** GUARDRAIL / INVARIANTE
- **Stato:** STABILE
- **Origine:** R5 §R5.8, audit componenti e Delta §K; AUDIT §30
- **Problema che risolve:** Vista unitaria cancellava origini o ridefiniva il referente.
- **Ultima formulazione giustificata:** Una proiezione seleziona/organizza l'uso senza cambiare identità, nascondere conflitti o distruggere differenze necessarie alla revisione. Nuova conclusione/aggregazione appartiene al ragionamento, non alla sola presentazione.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-127, K-132, K-136

### K-141 — Forma ontologica e criteri identificativi specifici restano aperti

- **ID:** K-141
- **Conoscenza:** Forma ontologica e criteri identificativi specifici restano aperti
- **Natura:** APERTURA
- **Stato:** APERTA
- **Origine:** R5 Delta §M; R6 §V.4
- **Problema che risolve:** Distinzione necessaria veniva promossa a oggetto Identifier definitivo.
- **Ultima formulazione giustificata:** Aperti forma degli schemi/validità e dell'Identifier, criteri Domain di unicità/riassegnazione e politiche auto-link. Schema–valore–assegnazione già necessari; nessuna tecnologia o algoritmo scelti.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-121, K-124

### K-142 — Criteri documentali e vocabolario finale delle relazioni restano aperti

- **ID:** K-142
- **Conoscenza:** Criteri documentali e vocabolario finale delle relazioni restano aperti
- **Natura:** APERTURA
- **Stato:** APERTA
- **Origine:** R5 Delta §M; R6 §VII.9
- **Problema che risolve:** Specializzazione documentale sembrava fissare universalmente versione e identità.
- **Ultima formulazione giustificata:** Non decisi quando rettifica sia nuovo documento/versione/rappresentazione, confine classificazione–identità, vocabolario finale e indirizzabilità di tutte le relazioni epistemiche; preservare le differenze intanto.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-029, K-065, K-131, K-133

## Round 6 — stress fondazionale e readiness

### K-143 — Referent come locus interno, anche per soggetti proposti o ipotetici

- **ID:** K-143
- **Conoscenza:** Referent come locus interno, anche per soggetti proposti o ipotetici
- **Natura:** DEFINIZIONE; SUPERAMENTO
- **Stato:** CANDIDATA
- **Origine:** R6 §II Q1–Q3; §III.8; §V.1
- **Problema che risolve:** La definizione esterna R5 escludeva soggetti pianificati o contestati e confondeva riconoscimento con esistenza.
- **Ultima formulazione giustificata:** Referent è il locus referenziale interno di un soggetto proposto o riconosciuto. Può riferirsi a soggetti reali, passati, pianificati, ipotetici o documentali; natura ed esistenza sono sostenute da Assertion, non garantite dal locus. Non ogni elemento indirizzabile diventa Referent.
- **Supera:** K-120
- **Superata da:** —
- **Vincoli collegati:** K-047, K-056

### K-144 — Proposte referenziali e informative precedono l'Admission senza Work obbligatorio

- **ID:** K-144
- **Conoscenza:** Proposte referenziali e informative precedono l'Admission senza Work obbligatorio
- **Natura:** REGOLA DI GOVERNANCE; SUPERAMENTO
- **Stato:** STABILE
- **Origine:** R6 §V.1–2; §VI.C
- **Problema che risolve:** L'apertura R5 lasciava la proposta senza luogo informativo autonomo.
- **Ultima formulazione giustificata:** Referent e Assertion proposti e Interpretation Result appartengono alla memoria informativa prima del commitment; possono esistere senza Work. L'Admission governa il riconoscimento, non crea retroattivamente l'elemento. La questione residua dei criteri per Referent privo di Assertion ammessa è separata.
- **Supera:** K-137
- **Superata da:** —
- **Vincoli collegati:** K-134, K-143

### K-145 — Criteri di ammissione del Referent senza Assertion già ammessa

- **ID:** K-145
- **Conoscenza:** Criteri di ammissione del Referent senza Assertion già ammessa
- **Natura:** APERTURA
- **Stato:** APERTA
- **Origine:** R5 Delta §M; R6 §V.1–2 e §VI.C
- **Problema che risolve:** R6 risolve l'esistenza della proposta ma non dettaglia ogni criterio di riconoscimento.
- **Ultima formulazione giustificata:** Non è definito un requisito universale di Assertion già ammessa per ammettere un Referent né un contratto completo per quel caso; non dedurlo dall'elenco dei target.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-144, K-146
- **Note:** Residuo dell'apertura K-137, non nuovo bloccante inventato.

### K-146 — Target primari dell'Admission distinti dagli elementi informativi adiacenti

- **ID:** K-146
- **Conoscenza:** Target primari dell'Admission distinti dagli elementi informativi adiacenti
- **Natura:** REGOLA DI GOVERNANCE; DEFINIZIONE
- **Stato:** CANDIDATA
- **Origine:** R6 §II Q3/Q8; §V.2 e §V.5
- **Problema che risolve:** Tutto ciò che si conserva rischiava di dover diventare un fatto ammesso.
- **Ultima formulazione giustificata:** Il governo della Knowledge riguarda primariamente Referent e Assertion; Source, Observation, supporti, valutazioni e record di derivazione restano informazione raggiungibile e governata secondo il proprio ruolo. Conservare o usare un elemento non significa ammetterlo come fatto del mondo.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-003, K-033, K-136, K-144

### K-147 — Modalità descrittiva, normativa, intenzionale e predittiva

- **ID:** K-147
- **Conoscenza:** Modalità descrittiva, normativa, intenzionale e predittiva
- **Natura:** DISTINZIONE; GUARDRAIL / INVARIANTE
- **Stato:** STABILE
- **Origine:** R6 §II Q5–Q7; §V.8
- **Problema che risolve:** Un obbligo contrattuale sembrava comando per Fold, un'intenzione evento già avvenuto.
- **Ultima formulazione giustificata:** La modalità appartiene al contenuto proposizionale. Conoscere obbligo, piano o previsione non ne implica adempimento né autorizzazione operativa: Policy riguarda il comportamento di Fold.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-055, K-078, K-113

### K-148 — Source e Observation adiacenti alla grammatica dei soggetti

- **ID:** K-148
- **Conoscenza:** Source e Observation adiacenti alla grammatica dei soggetti
- **Natura:** RICLASSIFICAZIONE; DECISIONE NEGATIVA
- **Stato:** CANDIDATA
- **Origine:** R6 §V.5; §VII.1–2
- **Problema che risolve:** L'importanza di Source e Observation induceva a trasformarle in soggetti del dominio.
- **Ultima formulazione giustificata:** Appartengono al modello informativo complessivo; sono adiacenti al Core che descrive i soggetti, collegabili tramite supporto e Provenance senza convertirle obbligatoriamente in Referent o Assertion. Ingressi strutturati non richiedono Observation fittizie.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-036, K-049, K-050, K-146

### K-149 — Quattro forme di informazione negativa e relativi limiti

- **ID:** K-149
- **Conoscenza:** Quattro forme di informazione negativa e relativi limiti
- **Natura:** DISTINZIONE; GUARDRAIL / INVARIANTE; DECISIONE NEGATIVA
- **Stato:** STABILE
- **Origine:** R6 §II Q4; §V.7
- **Problema che risolve:** Risultato negativo locale veniva esteso al mondo.
- **Ultima formulazione giustificata:** Distinguere negazione sostenuta da una fonte, assenza osservata localmente, ricerca negativa delimitata e inferenza di assenza nel mondo. La ricerca conserva corpus, tempo, criteri, copertura e limiti; l'ultima richiede condizioni Domain e supporto. Non è dimostrata una primitiva NegativeInformation.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-034, K-076, K-077

### K-150 — Aggregazione nuova richiede base di inclusione e percorso inferenziale

- **ID:** K-150
- **Conoscenza:** Aggregazione nuova richiede base di inclusione e percorso inferenziale
- **Natura:** CRITERIO DI CONSERVAZIONE / PROVENANCE; DISTINZIONE
- **Stato:** STABILE
- **Origine:** R6 §II Q6/Q8
- **Problema che risolve:** Un totale calcolato rischiava di apparire osservato o semplice presentazione.
- **Ultima formulazione giustificata:** Una somma o aggregazione nuova conserva elementi inclusi, criteri, periodo e metodo; è conclusione prodotta dal ragionamento e non osservazione diretta. La Projection può esporla, non inventarne significato o certezza.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-076, K-140

### K-151 — Alternative interpretative non possono diventare congiuntamente verità ammesse

- **ID:** K-151
- **Conoscenza:** Alternative interpretative non possono diventare congiuntamente verità ammesse
- **Natura:** GUARDRAIL / INVARIANTE
- **Stato:** STABILE
- **Origine:** R6 §II Q9; §IV.1
- **Problema che risolve:** Alternative incompatibili sarebbero state trattate come fatti cumulabili.
- **Ultima formulazione giustificata:** Conservare contesto, alternative e limiti; non ammettere insieme ipotesi mutuamente esclusive come se fossero compatibili. Restringere alternative non genera da solo supporto indipendente.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-053, K-083

### K-152 — Cicli interpretazione, identità e qualità senza auto-supporto

- **ID:** K-152
- **Conoscenza:** Cicli interpretazione, identità e qualità senza auto-supporto
- **Natura:** GUARDRAIL / INVARIANTE; CRITERIO DI CONSERVAZIONE / PROVENANCE
- **Stato:** STABILE
- **Origine:** R6 §IV, quattro cicli
- **Problema che risolve:** Conoscenza letta e prodotta nella stessa iterazione poteva confermare se stessa.
- **Ultima formulazione giustificata:** Ogni iterazione conserva il contesto letto e le dipendenze materiali. Una proposta di assegnazione identificativa non prova indipendentemente la coreferenza che l'ha prodotta; identità documentale provvisoria non rende indipendenti copie; senza nuova base il ciclo non aumenta Quality.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-021, K-101, K-111, K-124

### K-153 — Formula R6: Policy può ignorare l'impatto

- **ID:** K-153
- **Conoscenza:** Formula R6: Policy può ignorare l'impatto
- **Natura:** REGOLA DI GOVERNANCE
- **Stato:** SUPERATA
- **Origine:** R6 §V.9
- **Problema che risolve:** Il testo separava rilevazione e azione ma lasciava ambiguo ciò che fosse ignorabile.
- **Ultima formulazione giustificata:** La formulazione elencava «ignorare» fra le scelte della Policy dopo l'Impact Assessment senza distinguere sufficientemente mancata rivalutazione e occultamento di un impatto determinato.
- **Supera:** —
- **Superata da:** K-161
- **Vincoli collegati:** K-085, K-087
- **Note:** Conservata come formulazione storica, chiarita dal controllo finale.

### K-154 — Formula R6: Policy decide se applicare una derivazione

- **ID:** K-154
- **Conoscenza:** Formula R6: Policy decide se applicare una derivazione
- **Natura:** REGOLA DI GOVERNANCE
- **Stato:** SUPERATA
- **Origine:** R6 §V.8
- **Problema che risolve:** Automazione e validità inferenziale erano ancora confuse.
- **Ultima formulazione giustificata:** La formulazione attribuiva alla Policy «applicare o non applicare una derivazione» senza separare applicabilità semantica da programmazione, materializzazione e uso.
- **Supera:** —
- **Superata da:** K-162
- **Vincoli collegati:** K-113
- **Note:** Conservata come formulazione storica, sostituita nel controllo finale.

### K-155 — Assertion R6 ancora sovrapposta a claim e commitment

- **ID:** K-155
- **Conoscenza:** Assertion R6 ancora sovrapposta a claim e commitment
- **Natura:** DEFINIZIONE
- **Stato:** SUPERATA
- **Origine:** R6 §V.2–3; GATE §A Controllo 1
- **Problema che risolve:** Il medesimo termine copriva ciò che viene detto, chi lo dice e cosa Fold ammette.
- **Ultima formulazione giustificata:** R6 usa Assertion come proposizione ma non separa ancora adeguatamente contributo attribuito e commitment di Fold; il controllo finale riconosce il problema reale.
- **Supera:** —
- **Superata da:** K-158
- **Vincoli collegati:** K-055, K-146

### K-156 — Distinzioni informative necessarie non fissano l'inventario software

- **ID:** K-156
- **Conoscenza:** Distinzioni informative necessarie non fissano l'inventario software
- **Natura:** DECISIONE NEGATIVA; RICLASSIFICAZIONE
- **Stato:** STABILE
- **Origine:** R6 §VI.F; §VII.6 e §VII.9
- **Problema che risolve:** Ogni responsabilità o memoria rischiava di diventare componente autonomo.
- **Ultima formulazione giustificata:** Memorie distinguibili non impongono archivi tecnici separati; supporto, qualità, validazione, cattura Provenance e produzione di proposte possono restare locali o aggregate. Nessun motore universale di reprocessing o relazioni è dimostrato.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-047, K-064, K-081, K-104, K-106

### K-157 — Readiness consente costruzione della candidata, non freeze o implementazione

- **ID:** K-157
- **Conoscenza:** Readiness consente costruzione della candidata, non freeze o implementazione
- **Natura:** REGOLA DI GOVERNANCE; DECISIONE NEGATIVA
- **Stato:** STABILE
- **Origine:** R6 §VI.G; GATE §E
- **Problema che risolve:** Il superamento del gate poteva promuovere l'intero modello a canonico.
- **Ultima formulazione giustificata:** Il gate dichiara materiale sufficiente per costruire e testare v2: non modello verificato o congelato, Core canonico, chiusura FOL-13 o readiness implementativa. Restano verifiche end-to-end, stress indipendenti e successiva delimitazione MVP.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-026, K-047

## Controllo finale del Readiness Gate — tre correzioni minime

### K-158 — Assertion porta contenuto, contributo attribuisce, Admission stabilisce commitment

- **ID:** K-158
- **Conoscenza:** Assertion porta contenuto, contributo attribuisce, Admission stabilisce commitment
- **Natura:** DEFINIZIONE; DISTINZIONE; SUPERAMENTO
- **Stato:** STABILE
- **Origine:** GATE §A Controllo 1; §C
- **Problema che risolve:** Claim sorgente e posizione di Fold collassavano nella stessa nozione.
- **Ultima formulazione giustificata:** Assertion è elemento semantico indirizzabile che porta contenuto proposizionale; contributi attribuiti indicano chi o quale origine sostiene quel contenuto; commitment è posizione di governance di Fold. Non servono automaticamente tre nuove primitive.
- **Supera:** K-155
- **Superata da:** —
- **Vincoli collegati:** K-035, K-055, K-146

### K-159 — Attribuzione distinta dal supporto adeguato; contributi preservati separatamente

- **ID:** K-159
- **Conoscenza:** Attribuzione distinta dal supporto adeguato; contributi preservati separatamente
- **Natura:** DISTINZIONE; CRITERIO DI CONSERVAZIONE / PROVENANCE
- **Stato:** STABILE
- **Origine:** GATE §A Controllo 1; §B.1–3; §C Relation families
- **Problema che risolve:** Più dichiarazioni equivalenti diventavano una sola voce o tre prove indipendenti.
- **Ultima formulazione giustificata:** Una stessa Assertion può ricevere contributi attribuiti distinti con tempi, qualità e provenienza propri. Dichiarare non implica supporto adeguato; corroborazione richiede compatibilità e indipendenza. La rettifica di un contributo non rettifica automaticamente gli altri o il commitment.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-054, K-101, K-103, K-117, K-158

### K-160 — Identità del contenuto proposizionale non ancora determinata universalmente

- **ID:** K-160
- **Conoscenza:** Identità del contenuto proposizionale non ancora determinata universalmente
- **Natura:** APERTURA; DECISIONE NEGATIVA
- **Stato:** APERTA
- **Origine:** GATE §D
- **Problema che risolve:** Formulazioni simili potevano essere fuse senza criterio semantico.
- **Ultima formulazione giustificata:** Aperti criteri esatti di equivalenza/identità del contenuto. Default conservativo: mantenere Assertion distinte e collegarle per equivalenza, compatibilità o implicazione quando stabilite; Mapping e Domain dovranno precisare i criteri.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-158, K-159

### K-161 — Impatto determinato deve qualificare l'uso corrente anche con rivalutazione rinviata

- **ID:** K-161
- **Conoscenza:** Impatto determinato deve qualificare l'uso corrente anche con rivalutazione rinviata
- **Natura:** REGOLA DI GOVERNANCE; SUPERAMENTO; GUARDRAIL / INVARIANTE
- **Stato:** STABILE
- **Origine:** GATE §A Controllo 2; §B.4–5; §C
- **Problema che risolve:** La facoltà di rinviare il lavoro diventava facoltà di nascondere informazione epistemica.
- **Ultima formulazione giustificata:** Rilevare l'impatto, conservarne la qualificazione, scegliere rivalutazione e regolare l'uso temporaneo sono responsabilità distinte. Un impatto determinato vincola Current Reconstruction e Functions; Policy non può cancellarlo né presentare il vecchio risultato come pienamente aggiornato. Non occorre STALE universale.
- **Supera:** K-153
- **Superata da:** —
- **Vincoli collegati:** K-087, K-088, K-094

### K-162 — Validità della derivazione distinta da attivazione, materializzazione e usi

- **ID:** K-162
- **Conoscenza:** Validità della derivazione distinta da attivazione, materializzazione e usi
- **Natura:** REGOLA DI GOVERNANCE; SUPERAMENTO; DISTINZIONE
- **Stato:** STABILE
- **Origine:** GATE §A Controllo 3; §B.6; §C
- **Problema che risolve:** Una scelta applicativa poteva rendere valida o invalida un'inferenza.
- **Ultima formulazione giustificata:** Domain/Core e regole inferenziali determinano applicabilità semantica; il meccanismo produce conclusione e Lineage, Quality ne valuta l'adeguatezza. Policy governa esecuzione opzionale, Admission e usi autorizzati, non correttezza o conclusione una volta applicate premesse e regola.
- **Supera:** K-154
- **Superata da:** —
- **Vincoli collegati:** K-076, K-113, K-150

## Audit dei 34 e Coverage Gate — copertura delle responsabilità

### K-163 — Consegna dal canale e acquisizione registrata restano distinguibili

- **ID:** K-163
- **Conoscenza:** Consegna dal canale e acquisizione registrata restano distinguibili
- **Natura:** RESPONSABILITÀ NECESSARIA; DISTINZIONE
- **Stato:** STABILE
- **Origine:** AUDIT §A.1–2; §F.1–2
- **Problema che risolve:** Normalizzare la consegna poteva cancellare mittente, canale o ricezioni ripetute.
- **Ultima formulazione giustificata:** Preservare peculiarità e metadati della consegna senza convertirli in fatti di dominio; registrare ogni ricezione e il collegamento a materiale nuovo, riusato o non disponibile. Il proprietario dell'acquisizione non orchestra l'intero sistema.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-008, K-011

### K-164 — Ammissibilità tecnica non è attendibilità epistemica

- **ID:** K-164
- **Conoscenza:** Ammissibilità tecnica non è attendibilità epistemica
- **Natura:** RESPONSABILITÀ NECESSARIA; DISTINZIONE
- **Stato:** STABILE
- **Origine:** AUDIT §A.3
- **Problema che risolve:** Un file integro o sicuro veniva trattato come fonte attendibile.
- **Ultima formulazione giustificata:** Controllare formato, integrità, limiti tecnici e sicurezza, conservando esiti e fallimenti. Input non processabile non giustifica conclusioni semantiche; regole tecniche non sono Policy sulla conoscenza.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-041

### K-165 — Uguaglianza tecnica non decide riuso semantico o identità

- **ID:** K-165
- **Conoscenza:** Uguaglianza tecnica non decide riuso semantico o identità
- **Natura:** RESPONSABILITÀ NECESSARIA; GUARDRAIL / INVARIANTE
- **Stato:** STABILE
- **Origine:** AUDIT §A.4; §B.25b
- **Problema che risolve:** Deduplicare cancellava ricezioni o riusava risultati sotto risorse cambiate.
- **Ultima formulazione giustificata:** Riconoscere contenuto tecnicamente identico senza moltiplicare effetti o cancellare acquisizioni. Riuso di Source non implica riuso dei risultati se Mapping/contesto cambiano; non prova identità documentale, coreferenza o equivalenza delle Assertion.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-013, K-028, K-090

### K-166 — Staging universale sostituito da condizioni del materiale e Work

- **ID:** K-166
- **Conoscenza:** Staging universale sostituito da condizioni del materiale e Work
- **Natura:** RICLASSIFICAZIONE; DECISIONE NEGATIVA
- **Stato:** STABILE
- **Origine:** AUDIT §A.5; §F.24
- **Problema che risolve:** Tutto il non definitivo era collocato nello stesso stadio intermedio.
- **Ultima formulazione giustificata:** Condizioni tecniche del materiale, avanzamento del Work e posizione informativa sono distinti. Conservare prerequisiti, attese e fallimenti senza staging obbligatorio che preceda ogni conoscenza.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-011, K-052, K-061, K-062

### K-167 — Preservazione indipendente da interpretazione e ammissione

- **ID:** K-167
- **Conoscenza:** Preservazione indipendente da interpretazione e ammissione
- **Natura:** RESPONSABILITÀ NECESSARIA; CRITERIO DI CONSERVAZIONE / PROVENANCE
- **Stato:** STABILE
- **Origine:** AUDIT §A.6; §G
- **Problema che risolve:** Solo il materiale semanticamente accettato rischiava di restare recuperabile.
- **Ultima formulazione giustificata:** Conservare contenuto originario o riferimento stabile, rappresentazioni originali/derivate e acquisizioni collegate anche se l'interpretazione fallisce. Governi di conservazione e autorizzazione restano pertinenti; Source non è sempre file o documento.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-028, K-041, K-049

### K-168 — Estrazione aggregata conserva sei capacità e risultati locali

- **ID:** K-168
- **Conoscenza:** Estrazione aggregata conserva sei capacità e risultati locali
- **Natura:** RESPONSABILITÀ NECESSARIA; RICLASSIFICAZIONE
- **Stato:** CANDIDATA
- **Origine:** AUDIT §A.7–13; §H.4
- **Problema che risolve:** L'accorpamento perdeva differenze fra accesso al formato, lettura e struttura.
- **Ultima formulazione giustificata:** Accesso/decodifica, testo nativo, OCR, layout, strutture composte e parsing restano riconoscibili dentro produzione di Observation indirizzabili. Conservare target, metodi, versioni, alternative, errori e qualità locali; nessun Builder centrale obbligatorio.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-050, K-097, K-106

### K-169 — Testo nativo e OCR sono percorsi distinti, nessuno è garanzia semantica

- **ID:** K-169
- **Conoscenza:** Testo nativo e OCR sono percorsi distinti, nessuno è garanzia semantica
- **Natura:** DISTINZIONE; GUARDRAIL / INVARIANTE
- **Stato:** STABILE
- **Origine:** AUDIT §A.8–9
- **Problema che risolve:** Il testo incorporato era considerato copia infallibile del documento visibile.
- **Ultima formulazione giustificata:** Testo digitale può divergere dalla rappresentazione visuale; OCR produce letture con posizioni, alternative e incertezza propria. Nuove letture non cancellano le precedenti e non determinano significato o identità.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-098, K-168

### K-170 — Layout, struttura e parsing non decidono il dominio

- **ID:** K-170
- **Conoscenza:** Layout, struttura e parsing non decidono il dominio
- **Natura:** DISTINZIONE; GUARDRAIL / INVARIANTE
- **Stato:** STABILE
- **Origine:** AUDIT §A.10–12
- **Problema che risolve:** Prossimità o normalizzazione trasformavano silenziosamente una lettura in fatto.
- **Ultima formulazione giustificata:** Distinguere geometria da associazioni osservate campo/riga/sezione. Preservare grezzo e letture sintattiche; scelta che richiede significato, come data ambigua, passa all'Interpretation. Associazione visiva non è relazione di dominio.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-057, K-123, K-168

### K-171 — Classificazione locale propone contesti e Mapping, non tipo ammesso

- **ID:** K-171
- **Conoscenza:** Classificazione locale propone contesti e Mapping, non tipo ammesso
- **Natura:** RESPONSABILITÀ NECESSARIA; RICLASSIFICAZIONE
- **Stato:** STABILE
- **Origine:** AUDIT §A.16
- **Problema che risolve:** Classificare il PDF imponeva un tipo unico a tutti i contenuti.
- **Ultima formulazione giustificata:** Proporre contesti, emittenti e Mapping per Source o porzioni pertinenti; contenitore eterogeneo non trasferisce automaticamente una classificazione ai documenti interni. Capacità di Interpretation, non classificatore universale obbligatorio.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-029, K-031, K-057

### K-172 — Mapping esegue corrispondenze applicabili; Interpretation compone significati

- **ID:** K-172
- **Conoscenza:** Mapping esegue corrispondenze applicabili; Interpretation compone significati
- **Natura:** RESPONSABILITÀ NECESSARIA; DISTINZIONE
- **Stato:** STABILE
- **Origine:** AUDIT §A.17 e §A.21
- **Problema che risolve:** Campi mappati e proposizione coerente diventavano la stessa operazione.
- **Ultima formulazione giustificata:** Mapping verifica condizioni e applica definizioni riutilizzabili, conservando versione e dipendenze. Interpretation integra risultati, contesto, ipotesi referenziali, attribuzioni e alternative. Nessuno dei due ammette o dimostra coreferenza per sola corrispondenza.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-009, K-045, K-053, K-090

### K-173 — Validazione senza Candidate Validator universale

- **ID:** K-173
- **Conoscenza:** Validazione senza Candidate Validator universale
- **Natura:** RESPONSABILITÀ NECESSARIA; RICLASSIFICAZIONE; DECISIONE NEGATIVA
- **Stato:** STABILE
- **Origine:** AUDIT §A.23
- **Problema che risolve:** Superare Candidate rischiava di eliminare anche i controlli.
- **Ultima formulazione giustificata:** Controlli locali di forma, tipo e vincoli presso produttori competenti; Comparison per compatibilità contestuale; Admission per invarianti e applicabilità della disposizione. Nessun validatore generale detiene tutte le decisioni.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-018, K-052, K-083, K-113

### K-174 — Core Engine famiglia, non autorità aggiuntiva

- **ID:** K-174
- **Conoscenza:** Core Engine famiglia, non autorità aggiuntiva
- **Natura:** RICLASSIFICAZIONE; DECISIONE NEGATIVA
- **Stato:** STABILE
- **Origine:** AUDIT §A.25; §B.25a–25i; REG L09
- **Problema che risolve:** La scatola superiore duplicava o inglobava indistintamente le responsabilità.
- **Ultima formulazione giustificata:** Il nome raggruppa riconciliazione, confronto, temporalità, derivazione, ricostruzione e impatto; non possiede problema, autorità o regia aggiuntivi. I meccanismi hanno output e confini propri.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-083, K-089, K-125, K-161, K-162

### K-175 — Query assorbe lettura della Knowledge e traversal

- **ID:** K-175
- **Conoscenza:** Query assorbe lettura della Knowledge e traversal
- **Natura:** RESPONSABILITÀ NECESSARIA; RICLASSIFICAZIONE
- **Stato:** STABILE
- **Origine:** AUDIT §A.18/29; §B.25i
- **Problema che risolve:** Consultazione di contesto e dipendenze erano implicite o duplicavano accesso.
- **Ultima formulazione giustificata:** Recuperare Source, Observation, proposte, commitment, qualificazioni e relazioni con corpus, tempo, autorizzazioni e natura dei risultati espliciti. Non forzare i nuovi dati nelle attese esistenti; traversal recupera, Explanation spiega e Impact valuta.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-033, K-034, K-108, K-110, K-152

### K-176 — Verification possiede la verifica, non la decisione di ammissione

- **ID:** K-176
- **Conoscenza:** Verification possiede la verifica, non la decisione di ammissione
- **Natura:** RESPONSABILITÀ NECESSARIA; REGOLA OPERATIVA
- **Stato:** STABILE
- **Origine:** AUDIT §A.27
- **Problema che risolve:** Un sì generico diventava approvazione globale.
- **Ultima formulazione giustificata:** Predisporre e conservare target, domanda, alternative, autore, risposta ed esito. Distinguere dichiarazione, conferma, contestazione, correzione e autorizzazione; attese/riprese nel Work. Il workflow non sceglie autonomamente che cosa verificare o ammettere.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-019, K-035, K-038, K-039

### K-177 — Functions, Projection, Explanation e Presentation possiedono problemi differenti

- **ID:** K-177
- **Conoscenza:** Functions, Projection, Explanation e Presentation possiedono problemi differenti
- **Natura:** RESPONSABILITÀ NECESSARIA; DISTINZIONE
- **Stato:** STABILE
- **Origine:** AUDIT §A.30–33
- **Problema che risolve:** La vista incorporava decisioni semantiche e comportamento operativo.
- **Ultima formulazione giustificata:** Functions realizzano casi d'uso e registrano effetti, anche avviando acquisizione/query/verifica. Projection organizza per scopo; Explanation compone giustificazioni vere; Presentation rende percepibili contenuti, qualificazioni ed esiti. Nessuna crea implicitamente significato, certezza o effetto non avvenuto.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-015, K-073, K-110, K-140, K-161

### K-178 — Intake utente distinto da adattamento del canale e da Admission

- **ID:** K-178
- **Conoscenza:** Intake utente distinto da adattamento del canale e da Admission
- **Natura:** RESPONSABILITÀ NECESSARIA; REGOLA DI GOVERNANCE
- **Stato:** STABILE
- **Origine:** AUDIT §A.34; REG D01
- **Problema che risolve:** Il feedback era applicato come sovrascrittura.
- **Ultima formulazione giustificata:** Collegare contributo a target/interazione, preservare contenuto ricevuto e interpretazione distinguibili, instradare verso semantica, verifica o gestione della disposizione. Ricevere non formalizza automaticamente ogni Decision e non modifica direttamente Knowledge.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-035, K-037, K-039, K-159

### K-179 — Attore, persona rappresentata e autorità ad agire distinti

- **ID:** K-179
- **Conoscenza:** Attore, persona rappresentata e autorità ad agire distinti
- **Natura:** DISTINZIONE; GUARDRAIL / INVARIANTE
- **Stato:** STABILE
- **Origine:** AUDIT §G, trasversali
- **Problema che risolve:** Identità di un soggetto o account sembrava sufficiente ad autorizzare operazioni.
- **Ultima formulazione giustificata:** Mantenere distinguibili persona rappresentata, account/attore e autorità concreta rispetto al target e all'azione. Non ricavare permessi dalla sola coreferenza né dall'attendibilità della fonte.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-038, K-124

### K-180 — Sicurezza, privacy, cancellazione, backup e ripristino preservano confini e legami

- **ID:** K-180
- **Conoscenza:** Sicurezza, privacy, cancellazione, backup e ripristino preservano confini e legami
- **Natura:** RESPONSABILITÀ NECESSARIA; CRITERIO DI CONSERVAZIONE / PROVENANCE
- **Stato:** STABILE
- **Origine:** AUDIT §G, trasversali
- **Problema che risolve:** La sola preservazione del file ignorava sicurezza e dipendenze informative.
- **Ultima formulazione giustificata:** Controllare accessi e confini di fiducia; conservazione/cancellazione autorizzata non deriva da qualità epistemica. Gli effetti della perdita di materiale sulla verificabilità restano riconoscibili. Backup/ripristino coprono contenuti e collegamenti necessari, non solo file.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-027, K-108, K-167

### K-181 — Audit delle azioni distinto dall'osservabilità del funzionamento

- **ID:** K-181
- **Conoscenza:** Audit delle azioni distinto dall'osservabilità del funzionamento
- **Natura:** DISTINZIONE; RESPONSABILITÀ NECESSARIA
- **Stato:** STABILE
- **Origine:** AUDIT §G, trasversali
- **Problema che risolve:** Indicatori tecnici venivano usati come storia completa delle decisioni.
- **Ultima formulazione giustificata:** Registrare Decision, Disposition, Application ed esiti pertinenti; metriche di funzionamento e audit operativo hanno scopi distinti e non sostituiscono Provenance o storia epistemica.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-015, K-062, K-105

### K-182 — Inventario dei 24 è checklist candidata, non catalogo obbligatorio

- **ID:** K-182
- **Conoscenza:** Inventario dei 24 è checklist candidata, non catalogo obbligatorio
- **Natura:** RICLASSIFICAZIONE; DECISIONE NEGATIVA
- **Stato:** CANDIDATA
- **Origine:** AUDIT §C–F; §H Coverage Gate
- **Problema che risolve:** La contabilità 34→24 poteva imporre 24 nuovi componenti.
- **Ultima formulazione giustificata:** Nessuna responsabilità necessaria dei 34 è dichiarata persa; 18 voci perdono autonomia ma conservano obblighi. I 24 gruppi sono organizzazione candidata, non software né garanzia che ogni futura sintesi conservi tutti i vincoli. Accorpamenti devono mantenere target, scope, produttori e Provenance.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-047, K-156, K-168, K-174

### K-183 — Granularità finale degli accorpamenti resta aperta

- **ID:** K-183
- **Conoscenza:** Granularità finale degli accorpamenti resta aperta
- **Natura:** APERTURA
- **Stato:** APERTA
- **Origine:** AUDIT §H.5
- **Problema che risolve:** Passare il Coverage Gate poteva congelare il numero di responsabilità.
- **Ultima formulazione giustificata:** Aperta la granularità finale dei raggruppamenti; non è aperta l'esistenza dei problemi coperti. Gate superato con aperti non bloccanti, inclusa equivalenza proposizionale.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-157, K-160, K-182

## Regression Audit — recuperi, chiarimenti e riserva di ownership

### K-184 — Una risorsa nominata non dimostra la conservazione di tutti i suoi vincoli

- **ID:** K-184
- **Conoscenza:** Una risorsa nominata non dimostra la conservazione di tutti i suoi vincoli
- **Natura:** GUARDRAIL / INVARIANTE; CRITERIO DI CONSERVAZIONE / PROVENANCE
- **Stato:** STABILE
- **Origine:** REG Criterio adottato; §A D01–D05; §I
- **Problema che risolve:** Lineage e Core invariants citati genericamente facevano apparire coperte garanzie omesse.
- **Ultima formulazione giustificata:** Verificare garanzie specifiche, non la sola presenza del contenitore: base umana recuperabile, no auto-supporto, origine comune, nuova base valutativa, reversibilità. Recuperarli non richiede nuove primitive né ritorno ai componenti v1.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-035, K-101, K-111, K-127, K-152

### K-185 — Formalizzazione non-Policy: ownership ancora da precisare

- **ID:** K-185
- **Conoscenza:** Formalizzazione non-Policy: ownership ancora da precisare
- **Natura:** APERTURA; SUPERAMENTO
- **Stato:** APERTA
- **Origine:** R1 §R6 → R6/ AUDIT §A.26/34 e §G → REG D06
- **Problema che risolve:** Assegnazione generale al responsabile del flusso non determina ogni percorso decisionale.
- **Ultima formulazione giustificata:** Autorità esplicita, memoria e responsabilità di governance sono acquisite, ma manca assegnazione concreta completa della formalizzazione/registrazione della Decision non-Policy. Intake raccoglie; non è automaticamente il decisore. Non inventare Decision Manager né dichiarare perduta un'assegnazione precisa mai consolidata.
- **Supera:** K-017
- **Superata da:** —
- **Vincoli collegati:** K-015, K-016, K-178
- **Note:** R1 proponeva Function/Verification come owner del flusso; REG esamina soprattutto R6 e Audit. Si conserva quella proposta storica, non la si cancella. La riserva supera la sua sufficienza come assegnazione completa, non dimostra che fosse totalmente assente.

### K-186 — Forza della distinzione non equivale ad autonomia ontologica

- **ID:** K-186
- **Conoscenza:** Forza della distinzione non equivale ad autonomia ontologica
- **Natura:** DISTINZIONE; REGOLA DI GOVERNANCE
- **Stato:** STABILE
- **Origine:** REG §C Value; §E Status audit
- **Problema che risolve:** FORTE o CANDIDATO potevano essere letti come primitive finali o responsabilità facoltative.
- **Ultima formulazione giustificata:** FORTE indica distinzione sostenuta; CANDIDATO può riguardare forma/organizzazione mantenendo necessario il problema. Per Value, Identifier, supporto, Work e ricostruzione non dedurre autonomia o rinuncia al requisito dalla sola etichetta.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-047, K-058, K-065, K-141, K-182

### K-187 — Aggregazione dell'ingresso legittima se entrambe le capacità restano riconoscibili

- **ID:** K-187
- **Conoscenza:** Aggregazione dell'ingresso legittima se entrambe le capacità restano riconoscibili
- **Natura:** RICLASSIFICAZIONE
- **Stato:** CANDIDATA
- **Origine:** AUDIT §H.4–5; REG D07
- **Problema che risolve:** Raggruppare canale e acquisizione sembrava una regressione solo numerica.
- **Ultima formulazione giustificata:** Ricezione tracciata può accorpare adattamento del canale e registrazione dell'Acquisition mantenendo problemi, output, collegamenti e storia distinti. La collocazione organizzativa non è di per sé perdita semantica.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-163, K-182

### K-188 — Esito Regression Audit riguarda cinque recuperi e una riserva, non approvazione definitiva

- **ID:** K-188
- **Conoscenza:** Esito Regression Audit riguarda cinque recuperi e una riserva, non approvazione definitiva
- **Natura:** REGOLA DI GOVERNANCE
- **Stato:** STABILE
- **Origine:** REG §G–I
- **Problema che risolve:** Correzioni minori potevano significare guardrail poco importanti o modello validato.
- **Ultima formulazione giustificata:** D01–D05 sono recuperi di obblighi già acquisiti, compatibili con struttura esistente; D06 è incerto nell'ownership. Il gate con correzioni minori non applica da sé correzioni e non canonizza. La qualifica minori riguarda impatto strutturale.
- **Supera:** —
- **Superata da:** —
- **Vincoli collegati:** K-157, K-184, K-185

## Controllo di ricostruzione storica

Il perimetro delle fonti è chiuso al Regression Audit: i recuperi D01–D05 aggiornano l'origine delle voci già emerse, non sono cinque nuove scoperte né cinque duplicati nel conteggio. D06 conserva una riserva esplicita. Nessuna conclusione della review indipendente o delle risposte successive è stata inserita come nuova conoscenza.

| Fonte / blocco | Voci che ne conservano le conclusioni |
|---|---|
| R1: aree, dipendenze, autorità, operatività e parallelismo | K-001–K-027 |
| R2: documento/materiale, contributo umano, risultati incompleti | K-028–K-046 |
| Chiarimento R2: Core, memorie e posizioni superate | K-047–K-066 |
| R3: tempo, ricostruzioni, attese, impatto e applicabilità | K-067–K-096 |
| R4: qualità, supporto, indipendenza, tracce e collocazione delle regole | K-097–K-119 |
| R5: identificatori, referenti, coreferenza e corpo governato | K-120–K-142 |
| R6: stress, nove decisioni minime, cicli e gate | K-143–K-157; precisazioni alle voci originarie |
| Controllo finale readiness: contenuto/claim/commitment, impatto, derivazione | K-158–K-162 |
| Audit 34, trasversali e Coverage Gate | K-163–K-183, con rinvii ai vincoli già acquisiti |
| Regression: cinque recuperi, ownership e status | K-184–K-188; origini aggiornate di K-035, K-021, K-101, K-111, K-127 |

### Riscontro dei 34, senza usarli come indice del Ledger

| Voci storiche dell'audit | Conoscenze pertinenti nel Ledger |
|---|---|
| 1–2 | K-008, K-011, K-163 |
| 3–6 | K-041, K-049, K-164–K-167 |
| 7–13 | K-050, K-057, K-123, K-168–K-170 |
| 14–15 | K-097–K-098, K-105–K-109 |
| 16–18 | K-033, K-171–K-172, K-175 |
| 19–21 | K-009–K-010, K-053–K-054, K-104, K-125, K-144, K-159, K-172 |
| 22–24 | K-020, K-097–K-099, K-111, K-173 |
| 25 e meccanismi 25a–25i | K-073–K-094, K-125–K-133, K-161–K-162, K-174–K-175 |
| 26–28 | K-015–K-019, K-035–K-039, K-061, K-146, K-158, K-161–K-162, K-176, K-185 |
| 29–34 | K-033–K-034, K-110, K-140, K-175–K-178 |
| Trasversali e gate | K-011–K-013, K-062, K-090–K-095, K-156–K-157, K-179–K-183 |

### Limiti e dubbi dichiarati

- **K-017 → K-185:** R1 conteneva una proposta generale di ownership non-Policy; REG non la ricostruisce in dettaglio e giudica incompleta l'assegnazione concreta. Non attribuisco al passato l'assenza totale di un'idea, né considero quell'idea un contratto definitivo.
- **K-066:** non è dimostrata una chiusura esplicita del caso specifico delle proposizioni su interpretazioni interne. Una definizione più generale di Assertion non basta da sola a provare tale chiusura.
- **K-137 → K-144, con residuo K-145:** R6 risolve l'esistenza pre-Admission della proposta, non dettaglia tutti i criteri per riconoscere un Referent senza Assertion già ammessa.
- **K-119:** la collocazione concettuale delle proposte è chiarita da R6; resta aperta la forma concreta e la rappresentazione della conferma di una lettura.
- Gli stati registrano il grado raggiunto nel percorso, non un'autorizzazione a implementare. Le cinque famiglie di Quality e altre organizzazioni restano candidate dove il percorso ne conserva la provvisorietà.
- Le posizioni SUPERATA sono formulate come posizioni storiche effettive o ambiguità espressamente riconosciute dai Round: non tutte furono decisioni canoniche. Il superamento non implica che il software le abbia mai implementate.

**Chiusura della fase Ledger:** 188 voci: 146 STABILE, 15 CANDIDATA, 14 APERTA, 13 SUPERATA. Le 161 attive sono le sole destinate alla matrice forward; le aperture ricevono un controllo supplementare. La verifica di copertura inizia dopo il salvataggio di questa ricostruzione.
