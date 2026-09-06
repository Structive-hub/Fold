# Fold — Model Preservation Gate della candidata v2.1

Questo Gate verifica esclusivamente che l’evoluzione strutturale del modello di Fold sia stata preservata fedelmente e sia ricostruibile dagli artefatti versionabili prodotti in FOL-40.

Se superato, autorizza il passaggio alla preparazione del freeze della candidata v2.1.

Non dimostra che il modello sia vero, completo per il prodotto, validato sul dominio domestico o cross-domain, né pronto per l’implementazione.

**Status: Research — Model Preservation Gate**  
**Data:** 2026-09-06  
**Percorso:** FOL-40, nel contesto di FOL-36  
**Candidata esaminata:** v2.1 Draft; contenuto invariato  
**Verdetto:** MODEL PRESERVATION GATE SUPERATO  
**Risultato:** 0 blocker; 2 finding minori — stato documentale e rinvio secondario; percorso RECONSTRUCTIBLE.

## 1. Scope e metodo avversariale

Oggetto del controllo sono due catene, non la validità universale delle conclusioni di Fold:

- 34 elementi attivi della v1 → trasformazioni motivate → 24 gruppi di copertura → 22 schede H e piano operativo → candidata v2.1;
- ipotesi sui concetti Core e adiacenti → stress effettivamente documentati → conclusioni e limiti → primitive forti, distinzioni, governance, forme candidate, aperture e forme universali non sostenute → candidata v2.1.

Sono stati cercati controesempi documentali alla fedeltà della preservazione: disposizione diversa da AUDIT, problema cancellato insieme al nome, accorpamento trasformato in atomicità, responsabilità distribuita ricentralizzata, necessità trasformata in autonomia ontologica, test retrodatato, stato genealogico promosso, apertura chiusa implicitamente, correzione successiva attribuita a una formulazione precedente e trasformazione della candidata priva di percorso inverso.

La verifica non assume come prova i precedenti auto-check delle genealogie, i loro conteggi o il “nessun problema” dichiarato nella candidata. Confronta le schede con V1/Round, usa AUDIT per le disposizioni allora adottate, ASM1/REG/ASM2 per l’assemblaggio e la v2.1 soltanto come destinazione. Il Ledger determina lo stato delle conoscenze; una fonte primaria prova ciò che fu scritto in quella fase, non acquisisce per questo autorità per cambiare uno stato del Ledger.

I controlli meccanici verificano inventari, corrispondenze e integrità dei file. Non sostituiscono il controllo semantico: i casi critici e i tentativi di falsificazione sono esplicitati nelle sezioni seguenti.

Non sono stati rieseguiti Source Readiness Check, coverage delle 188 K, Knowledge Preservation Gate o relativo re-check. Non sono stati creati nuovi casi di test del prodotto, nuove decisioni o nuove distinzioni di Fold.

## 2. Autorizzazione e limiti

Il superamento riguarda la preparazione del freeze e la chiusura documentale successiva di FOL-40. Questo report non congela direttamente la candidata e non chiude operativamente alcuna issue.

Restano fuori dall’autorizzazione:

- implementazione e architettura tecnica;
- scelta di tecnologie, servizi, classi, database o algoritmi;
- freeze del perimetro MVP;
- validazione domestica o cross-domain;
- promozione di Research/Draft a Canonical;
- risoluzione delle aperture o aggiornamento di Linear/Notion.

I due finding minori individuano patch documentali finite successive; non vengono applicate da questo Gate.

## 3. Fonti effettivamente usate

### 3.1 Artefatti del repository

Tutti i nomi della tabella si riferiscono a docs/ricerca/.

| Sigla del report | Artefatto | Uso |
|---|---|---|
| SM | fold-model-preservation-source-map-2026-09-05.md | Identificazione già stabilita delle fonti; non nuovo controllo di readiness. |
| GC | fold-component-responsibility-genealogy-2026-09-05.md | Prima genealogia sottoposta ad audit. |
| GK | fold-core-concept-genealogy-2026-09-05.md | Seconda genealogia sottoposta ad audit. |
| V21 | fold-anatomia-v2.1-candidate-2026-09-04.md | Destinazione e partenza del controllo inverso. |
| KL | fold-knowledge-decision-ledger-2026-09-04.md | Stati, conclusioni e superamenti genealogici; include soltanto la patch EG-01 già autorizzata. |
| CV2 | fold-coverage-ledger-v2-2026-09-04.md | Copertura successiva: non prova dell’origine delle trasformazioni. |
| DV | fold-delta-v2-v2.1-2026-09-04.md | Ripristini, Ledger-only, aperti e tesi respinte autorizzati. |
| SV2 | fold-anatomia-v2-snapshot-2026-09-04.md | Preservazione di ASM2, non surrogato dei Round. |
| KG | fold-knowledge-preservation-gate-v2.1-2026-09-04.md | Finding della precedente verifica; non rieseguita. |
| KR | fold-knowledge-preservation-recheck-v2.1-2026-09-05.md | Esito documentato del re-check, inclusa l’invarianza della candidata. |

README, docs/README, metodo di lavoro, working model Core/Domain e decisione 0001 sono contesto di metodo e perimetro; non sostituiscono le fonti dei Round. Nessuna consultazione o modifica di Linear/Notion in questo Gate, conformemente al mandato.

### 3.2 Fonti primarie

Sono stati consultati i corpi originali identificati in SM, non soltanto prompt o titoli. Archivio:

~~~text
C:\Users\giuseppe\.codex\sessions\2026\09\01\rollout-2026-09-01T14-56-30-01a05d0a-e483-7793-a648-e46306e04177.jsonl
~~~

Gli ordinal sono identificativi JSONL, non numeri di riga. Le impronte dei corpi e i timestamp completi restano in SM §3.2 e nei registri delle genealogie; il presente controllo ne riusa l’identificazione.

| Fonte | Ordinal | Passaggio controllato |
|---|---:|---|
| V1 | 210 | Problemi originari, forme Core candidate, nove meccanismi, trasversali. |
| R1 | 287 | Aree non lineari; dipendenze; coordinamento; autorità; ciclo Quality; limiti del parallelismo. |
| R2 | 346 | Documenti e porzioni; ingressi umani; Work/Attempt; ricezione/esito; composizione parziale. |
| R2C | 428 | Correzioni a Source, Observation, Candidate, Evidence; test/non-test; famiglie e qualificazioni. |
| R3 | 491 | Tempo, ricostruzione, derivazione, attenzione, assenze, correzioni, impatto, versioni e applicabilità. |
| R4 | 561 | Target/aspetto, supporto, indipendenza, Provenance/Lineage, granularità, recuperabilità e regole. |
| R5 | 618 | Referent, Identifier, same_as/merge, documento, Relation, proposte e Knowledge. |
| R6 | 661 | Contraddizioni cross-round; soluzioni minime candidate; negativo, modalità, aggregazione e impatto. |
| GATE | 692 | Tre correzioni finali: Assertion/claim/commitment, impatto, Derivation/Policy. |
| AUDIT | 822 | Matrice e 34 schede; 25a–25i; contabilità; 24 gruppi; trasversali e aperture. |
| ASM1 | 888 | Scelta organizzativa e prima corrispondenza esplicita 24→22. |
| REG | 1070 | D01–D05 da recuperare, D06 incerto/aperto, D07 giustificato; trasformazioni L01–L10. |
| ASM2 | 1105 | Assemblaggio successivo: recuperi e riserva non-Policy preservati. |

R1 §R6 indica la sesta sezione del primo Round, non il Round 6. ASM1/ASM2 sono fonti dirette dell’assemblaggio, non della genesi delle distinzioni nei Round.

### 3.3 Identificazione materiale della base esaminata

Le impronte SHA-256 dei file sono riportate in fondo al report. Sono diverse per natura dalle impronte dei soli corpi delle risposte originali. Servono a identificare anche gli artefatti ancora non versionati; non certificano da sole la correttezza del contenuto.

## 4. Stato Git iniziale ed EG-01

Branch main; HEAD ef3b24f450e21173c07563aee02c96ef39babcf7. Nessuna modifica staged.

~~~text
 M docs/ricerca/fold-knowledge-decision-ledger-2026-09-04.md
?? docs/ricerca/fold-anatomia-v2.1-candidate-2026-09-04.md
?? docs/ricerca/fold-component-responsibility-genealogy-2026-09-05.md
?? docs/ricerca/fold-core-concept-genealogy-2026-09-05.md
?? docs/ricerca/fold-knowledge-preservation-gate-v2.1-2026-09-04.md
?? docs/ricerca/fold-knowledge-preservation-recheck-v2.1-2026-09-05.md
?? docs/ricerca/fold-model-preservation-source-map-2026-09-05.md
~~~

Lo stato coincide con il mandato, anche alla ripresa dopo l’interruzione. Il diff tracked contiene soltanto:

| K-ID | Prima | Dopo | Riscontro primario |
|---|---|---|---|
| K-072 | AUDIT §25g | AUDIT §B 25h | AUDIT §B, Current-State Derivation; R3 §R3.3. |
| K-073 | AUDIT §25g | AUDIT §B 25h | Stessa responsabilità di Current Reconstruction. |
| K-133 | AUDIT §25h | AUDIT §B 25b | AUDIT §B, Document Identity Reconciliation; R5, sezione omonima. |

Tre righe sostituite, senza cambiamenti di formulazione, stato o origine sostanziale delle conoscenze. EG-01 è chiuso nel suo perimetro di rinvii. Le note delle genealogie che lo descrivevano ancora da correggere conservano lo stato al momento della loro produzione: non provano un difetto tuttora presente nel Ledger. Questo report rende esplicita la successione senza riscrivere quelle note storiche.

## 5. Gate A — I 34 componenti e le loro trasformazioni

### 5.1 Inventario, campi e contabilità indipendente

Sono state estratte le 34 righe di AUDIT §A e confrontate con le 34 schede di GC §3: stessi numeri, stessi nomi, stessa disposizione principale. Nessun ID mancante o duplicato. La matrice finale di GC è un indice delle schede, non un secondo inventario.

Tutte le schede hanno i nove campi: problema, forma v1, stress/evidenza, conclusione, disposizione, destinazione, collocazione e rischio, più riferimenti puntuali. La verifica di presenza è stata accompagnata dal confronto del contenuto con le fonti.

La sola normalizzazione lessicale è MANTENUTO MA RIDEFINITO di AUDIT → MANTENUTO / RIDEFINITO di GC, dichiarata da GC §1.

| Disposizione | Conteggio da AUDIT §A | ID verificati | Conteggio GC |
|---|---:|---|---:|
| MANTENUTO AUTONOMO | 7 | 1, 3, 4, 17, 30, 32, 33 | 7 |
| MANTENUTO / RIDEFINITO | 9 | 2, 6, 21, 26, 27, 28, 29, 31, 34 | 9 |
| ACCORPATO | 7 | 7, 10, 11, 12, 13, 16, 18 | 7 |
| DISTRIBUITO | 7 | 14, 15, 19, 20, 22, 23, 24 | 7 |
| SPECIALIZZAZIONE | 2 | 8, 9 | 2 |
| RICLASSIFICATO | 2 | 5, 25 | 2 |
| ELIMINATO PURAMENTE | 0 | Nessuno | 0 |
| Totale | 34 | 1–34, una volta ciascuno | 34 |

Il totale non include le sei risorse/memorie escluse dal perimetro storico, le trasversali v1 §6 o i nove meccanismi interni di 25.

### 5.2 Riscontro delle singole catene

Ogni riga seguente rinvia alla scheda GC del medesimo numero. La disposizione è quella indipendentemente verificata sopra; AUDIT §A, scheda omonima, documenta la sua formalizzazione. “Conservato” significa che problema, ragione della trasformazione e destinazione sono ricostruibili, non che il componente sia diventato software approvato.

| # / componente v1 | Prova rilevante e rischio sottoposto a controllo | Destinazione verificata | Esito |
|---|---|---|---|
| 1 Channel Adapter | V1 §1.1; R2.7; REG D07: adattare il canale non elimina la distinta registrazione della ricezione. L’accorpamento in H1 non viene retrodatato ai Round. | Gruppo 1, capacità H1. | Conservato |
| 2 Acquisition Controller | V1 §1.2; R1 §R3; R2.7: ricezione riuscita e OCR fallito non sono lo stesso esito. | Gruppo 2/H1; avanzamento dei Work nel 24/F. | Conservato |
| 3 Technical Validation | V1 §1.3; R2C §8.2: processabilità e sicurezza non attestano verità del contenuto. | Gruppo 3/H2. | Conservato |
| 4 Fingerprinting / Technical Deduplication | V1 §1.4; R5 Document Identity: uguaglianza tecnica non prova identità del documento o indipendenza epistemica. | Gruppo 4/H3, ricezioni distinte in H1. | Conservato |
| 5 Staging / Technical Lifecycle | R1 §R5; R2.6: stati del materiale, attese e avanzamento non sono uno stato universale della conoscenza. | Gruppo 24/F/G e condizioni tecniche pertinenti. | Conservato |
| 6 Source Preservation | V1 §1.6 → R2C T1: un materiale non interpretabile può restare Source; preservazione, processabilità e Admission non vengono confuse. | Gruppo 5/H4, G/I. | Conservato |
| 7 Format Decoder | V1 §2.1; AUDIT A.7: capacità di accesso al formato, non semantica Domain. Nessuno stress nominativo inventato. | Capacità del gruppo 6/H5. | Conservato |
| 8 Text Extraction | V1 §2.2; AUDIT A.8: testo incorporato e resa visuale possono divergere. | Specializzazione gruppo 6/H5, I. | Conservato |
| 9 OCR | V1 §2.3; R1 §R7; R2.6; R4.2: errore di lettura, risultati parziali e conferma locale non diventano errore globale del caso. | Specializzazione gruppo 6/H5. | Conservato |
| 10 Layout Analyzer | V1 §2.4; R4.1; AUDIT A.10: corretta lettura dei caratteri non basta per associazioni spaziali corrette. | Capacità gruppo 6/H5. | Conservato |
| 11 Structure Detector | V1 §2.5; R4.1/R4.7; AUDIT A.11: struttura sorgente distinta dal significato attribuito. | Capacità gruppo 6/H5. | Conservato |
| 12 Lexical Parser | V1 §2.6; R2C §5; R3.1: parsing della data/numero non ne determina il ruolo Domain. | H5; H6/H7 per il significato. | Conservato |
| 13 Observation Builder | V1 §2.7; R2C T2/§8.4: risultati indirizzabili senza Observation fittizia obbligatoria per ogni input. | Produzione interna H5; percorsi alternativi D. | Conservato |
| 14 Extraction Quality Assessment | R1 §R7; R4.1/R4.9: confidenza estrattiva locale, non giudice centrale prima di ogni ragionamento. | Produttori H5; risorsa e storia G/I. | Conservato |
| 15 Extraction Provenance Recorder | R4.6–R4.8: chi produce cattura; il traversal non ricrea tracce mai conservate. | H5 e obblighi comuni; G; recupero H17. | Conservato |
| 16 Source Classifier | R2.2; R5.9/audit: tipo del contenitore non trasferito alle parti. | Classificazione contestuale H7, contesto H6. | Conservato |
| 17 Mapping Executor | R3.9; R4.8: riuso della definizione non equivale a riuso di un risultato già vero. Versioni materiali recuperabili. | Gruppo 7/H6, G. | Conservato |
| 18 Existing Knowledge Reader | R2C §8.6; R5 audit: recupero del contesto riusabile, non secondo deposito o decisore di sufficienza. | Gruppo 18/H17; consumatori H7/H8. | Conservato |
| 19 Referent Candidate Generator | R5.4; R6 V.1: proposta referenziale e valutazione della coreferenza non obbligano a un generatore universale. | H7/H8 e memoria delle proposte. | Conservato |
| 20 Evidence Construction | R2C T4; R4.4; GATE 1: collegare supporto a un target non è trasformare la Source in Evidence globale. | Obblighi locali H6/H7/H8/H11/H15. | Conservato |
| 21 Interpretation Coordinator | R1 §R4; R2C T3; R5.10; R6: composizione semantica distinta dalla regia del Work; parzialità conservabile. | Gruppo 8/H7; F operativo distinto. | Conservato |
| 22 Semantic Quality Assessment | R1 §R7; R4.1/R4.9: qualità di Mapping, interpretazione e link con bersagli diversi. | H6/H7/H8; G/I. | Conservato |
| 23 Candidate Validator | R2C T3/§8.9; R5 audit: l’eterogeneità delle proposte distribuisce i controlli, non li elimina né autorizza accettazione automatica. | H5–H9 e controllo finale H16. | Conservato |
| 24 Quality Assessment | R4.1/R4.2/R4.9: valutazioni competenti e sintesi per scopo, non truth scorer. | Produttori/verificatori; Quality Model consultato. | Conservato |
| 25 Core Engine | R3–GATE; AUDIT B/E/F: famiglia di problemi distinti, non ulteriore centro che ne possiede indistintamente l’autorità. | H8–H13 e quote distribuite; §6 del report. | Conservato |
| 26 Policy Evaluation | R1 §R6; GATE 2–3; REG D06: scelta comportamentale, non unica origine della Disposition né arbitro di verità/inferenza. | H14/E; ownership non-Policy aperta. | Conservato |
| 27 Verification Workflow | R2.4/R2.5; R3.10: domanda, contributo, autorità e scope tardivo non diventano conferma globale. | H15, H22, F. | Conservato |
| 28 Knowledge Admission & State Management | R2C §6; R6 V.2; GATE 1: commitment distinto dalle altre qualificazioni e dalla verità. | H16/E/G; altri stati presso i rispettivi target. | Conservato |
| 29 Query & Retrieval | R2.3; R2C §8.15; R4.8: può recuperare materiale non interpretato e risultati negativi delimitati. | Gruppo 18/H17; traversal incluso. | Conservato |
| 30 Projection Builder | R3.3; R5 audit; AUDIT A.30: ricostruzione e nuova aggregazione non nascono silenziosamente nella vista. | H18; richiede H11/H12. | Conservato |
| 31 Application Functions | R1 §R1; R3.6; GATE: risposta su richiesta e attenzione promessa diverse; esecuzione non prova di fatto. | H19, E/F. | Conservato |
| 32 Explanation Composer | R4.8; GATE 1: spiega basi effettive, non produce giustificazioni mancanti dopo il fatto. | H20; usa H17 e G. | Conservato |
| 33 Presentation Layer | V1 §5.5; GATE 2: rendere visibile senza aumentare certezza o occultare impatti pertinenti. | H21; coopera con H18/H20. | Conservato |
| 34 Feedback Handler | R2.4; R3.10; REG D01/D06: base originaria distinta da interpretazione e autorità; Intake non diventa Decision Manager. | H22, H7/H15, E/O. | Conservato |

### 5.3 Tentativi di falsificazione A7/A8

Non è sostenibile l’equazione “zero eliminazioni = 34 autonomie”: 18 disposizioni sono accorpamenti, distribuzioni, specializzazioni o riclassificazioni. GC la esclude e V21 conserva capacità/obblighi anche senza scheda dedicata.

Sono stati controllati soprattutto i falsi ritorni di Candidate Validator, Quality Assessment, Evidence Construction, Provenance Recorder e Core Engine come owner universali. GC §§4–6, GK nelle schede pertinenti e V21 G/H li collocano rispettivamente presso produttori/applicatori, risorse, memorie o famiglia di meccanismi. Nessuno riacquista una scatola universale attraverso il cambio di nome.

H5/H7 sono raggruppamenti, non operazioni dichiarate atomicamente indivisibili. L’apertura C04 non è una responsabilità perduta e non viene chiusa mediante una scissione di H7.

**Esito A1–A3 e A7–A8: PASS.**

## 6. Gate A4 — Nove meccanismi 25a–25i

Il confronto è con AUDIT §B, non con i vecchi rinvii errati del Ledger.

| ID | Problema/stress e disposizione verificata | Destinazione | Perdita cercata ed esclusa |
|---|---|---|---|
| 25a Identity Reconciliation | R5.3–R5.5: assegnazione e coreferenza non sono certezza o merge. MANTENUTO / RIDEFINITO. | Gruppo 9/H8. | Proposta e assessment non sostituiti da fusione automatica. |
| 25b Document Identity Reconciliation | R2C §8.11 → R5, sezione dedicata: quattro problemi. DISTRIBUITO. | 4/H3; 8/H7; 9/H8; 10–11/H9–H10; 17/H16. | Non trasferito tutto a H8: solo la coreferenza documentale è specializzazione. |
| 25c Comparison | R3.5/R4: controllare comparabilità di referente, ruolo, tempo e scope. MANTENUTO AUTONOMO. | 10/H9. | Confronto non sostituito da ranking o scelta della fonte. |
| 25d Temporal Evaluation | R3.1–R3.2; R6 V.6: ruoli e reference time. MANTENUTO / RIDEFINITO. | 11/H10. | Ultimo arrivo non diventa tempo del fatto o stato corrente. |
| 25e Conflict Detection | R3/R5 e AUDIT: incompatibilità come esito specializzato. SPECIALIZZAZIONE. | 10/H9. | Scelta d’uso di una fonte non cancella il conflitto. |
| 25f Correction / Supersession | R3.5; GATE: riconoscimento, successione, impatto ed effetto governato. DISTRIBUITO. | H7/H9/H10/H13; E/H16. | “D2 corregge D1” non applica già una revisione della Knowledge. |
| 25g Derivation | R3.4; R4.4; GATE 3. MANTENUTO AUTONOMO. | 12/H11. | Nessuna Observation derivata o validità decisa dalla Policy. |
| 25h Current-State Derivation | R3.3: ricostruzione non sempre nuova derivazione. MANTENUTO / RIDEFINITO. | 13/H12 Current Reconstruction. | Non confusa con 25g, ultimo dato o Projection. |
| 25i Provenance Traversal | R4.6/R4.8: accesso alle tracce conservate. ACCORPATO. | 18/H17; consumato da H20 e meccanismi. | Il recupero non assorbe cattura, validazione o spiegazione. |

Impact Assessment non è una decima sottovoce retroattiva della v1. GC §4 ne ricostruisce R3.8/R3.9 → R6 V.9 → GATE 2 → AUDIT E/F → ASM1 H13. Il nuovo gruppo 14 è spiegato come esplicitazione acquisita, non come conteggio occulto o componente inventato dalla genealogia.

**Esito: PASS, nove catene conservate.**

## 7. Gate A5–A6 — 24 gruppi e 22 H

Confrontate tutte le righe di AUDIT §F con GC §5, ASM1 §K, ASM2 §K e V21 §K. REG D07 è la motivazione esplicita dell’aggregazione della ricezione; non viene attribuita a un Round anteriore.

| Gruppo AUDIT | Responsabilità di copertura | Destinazione verificata |
|---:|---|---|
| 1 | Acquisizione dal canale | H1, adattamento della consegna |
| 2 | Registrazione/governo acquisizione | H1, registrazione e collegamento |
| 3 | Validazione tecnica | H2 |
| 4 | Identificazione/deduplicazione tecnica | H3 |
| 5 | Preservazione Source | H4 |
| 6 | Estrazione/Observation | H5 |
| 7 | Mapping | H6 |
| 8 | Composizione semantica | H7 |
| 9 | Identity Reconciliation | H8 |
| 10 | Comparison/relazioni fra contenuti | H9 |
| 11 | Temporal Evaluation | H10 |
| 12 | Derivation | H11 |
| 13 | Current Reconstruction | H12 |
| 14 | Impact Assessment | H13 |
| 15 | Policy Evaluation | H14 |
| 16 | Verification work management | H15 e F |
| 17 | Admission/revisioni di governance | H16 ed E |
| 18 | Query & Retrieval contestualizzato | H17, incluso traversal |
| 19 | Projection | H18 |
| 20 | Casi d’uso/applicazione | H19 |
| 21 | Explanation | H20 |
| 22 | Presentation | H21 |
| 23 | Contributi utente | H22 |
| 24 | Coordinamento dei Work | F/G, presso proprietari delle attività |

Il conteggio è: una H per 1–2 + ventuno H per 3–23 = 22. Il gruppo 24 resta sul piano operativo. Non sono state sottratte due capacità.

L’assenza di una H24 non prova un coordinamento mancante: V21 F esplicita proprietari, tentativi, attese e riprese. Non prova neppure un orchestratore centrale, che GC e V21 escludono. “Autonomia del problema” non equivale a modulo o confine software; la granularità finale resta K-183 APERTA.

**Esito: PASS.**

## 8. Gate B — 35 unità genealogiche, non 35 primitive

Verificati 35 titoli univoci in GK §3 e 35 schede con tutti i nove campi. L’accostamento di termini in una scheda non ne fonde la natura. Le sole schede il cui stato strutturale inizia con PRIMITIVA FORTEMENTE SOSTENUTA sono Referent e Assertion.

La tabella espone il riscontro del percorso, non un nuovo inventario ontologico.

| # / unità GK | Passaggio originale determinante | Conclusione/limite preservato e destinazione V21 |
|---|---|---|
| 1 Referent | R2C T5; R5.1 omonimi/subjecthood → R6 V.1 soggetti pianificati o ipotetici. | Necessità forte; locus interno, non cosa esterna o prova di esistenza. K-143 CANDIDATA; I/H7/H8. |
| 2 Assertion | R2C §3; R5.6; GATE 1, pagamento P e movimento Q. | Contenuto ≠ contributo ≠ supporto ≠ commitment; K-160/K-066 aperte. I/E/H7/H11/H16. |
| 3 Identifier | R2C §2 dichiara NON TESTATO → test diretto R5.3. | Schema–valore–assegnazione; non tre primitive. K-141 aperta; I/H7/H8. |
| 4 Value | R2C §5, 84,72 e sue occorrenze; R5.3/R5.8. | Contenuto strutturato necessario, autonomia non dimostrata; I. |
| 5 Source | V1 §1.6 → R2C T1, PDF non processabile ed evento privo di contenuto. | Definizione K-049 stabile; adiacenza K-148 candidata; D/G/H4/I. |
| 6 Observation | R2C T2, foto contro risposta strutturata; R4.2 conferma di lettura. | Lettura ≠ semantica; nessun pedaggio universale; K-050 stabile, K-148 candidata; H5/D/I. |
| 7 Relation | R1 direzioni; R2C §4 → R5.7 quattro alternative. | Famiglie semanticamente diverse; possibile forma tecnica comune non decisa; I/J. |
| 8 Candidate / Proposal | R2C T3 → R5.10 → R6 V.1–2. | Completezza, alternative e contenuti eterogenei; memoria non dipendente da Work; D/E/G/I. |
| 9 Knowledge | V1 repository → quattro modelli R5.11 → R6 V.2/GATE. | Corpo governato candidato, non nuova sostanza di tutta la memoria; E/G/I. |
| 10 Quality / Assessment | R1 §R7 ciclo; R4.1–R4.3/R4.9. | Target/aspetto/base/scopo/storia; cinque famiglie K-098 candidate; G/I e produttori. |
| 11 Evidence / supporto | R2C T4 → R4.4–R4.5 → GATE 1. | Supporto qualificato, non sola attribuzione né oggetto obbligatorio; K-065 aperta; I/G/H. |
| 12 Documento / identity | R2 foto/documenti → R5.2/R5.9 e quattro problemi documentali. | Possibile Referent candidato, non Source o radice obbligatoria; H3/H7/H8/H9/H10/I. |
| 13 Derivation | R2C NON TESTATO → R3.4 → GATE 3. | Attività, conclusione, giustificazione; Policy non decide validità; H11/G/I. |
| 14 Decision / Disposition / Application | R1 §R6; R3.10; REG D06. | Scelta, trattamento e effetto distinti; proposta storica di ownership non cancellata, sufficienza non acquisita; E/F/O. |
| 15 Work | R1 §R5; quattro alternative R2.6; R6 V.9. | Continuità operativa quando necessaria, non Work universale o stato del mondo; F/G/O. |
| 16 Subject / Property | R2C soggetto irrisolto; R5.8; R6 V.1. | Ruoli referenziali/predicativi e qualificazioni non duplicano il locus; I/J/Domain. |
| 17 Validity / tempo | R2C ruoli non test generale → R3.1–R3.3. | Decomposizione di tempo, storia, uso e riferimento; nessuna Validity universale; H10/H12/I. |
| 18 Knowledge State | R2C §6: incompleto/pending/ammesso su target diversi. | K-060 superata da K-061; qualificazioni locali, non enum unico; D/E/F/I. |
| 19 Current State / Reconstruction | V1 4.4.8 → R3.3 → AUDIT 25h. | K-073 stabile; risultato candidato, non sempre nuova Assertion; H12/I/O. |
| 20 Expectation / attention | R3.6–R3.7, bolletta/auto/raccomandazione e pagina illeggibile. | Composizione K-080 candidata; Work distinto da base e riscontro; D/F/I/O. |
| 21 Logical Document | R2.1 → R2C T5 grouping ≠ subjecthood → R5.2. | Nessun contenitore intermedio obbligatorio; identità/composizione sopravvivono; H7/H8/I. |
| 22 Source Portion / locator | R2.2 → cinque alternative R2C T6; R5.9. | Localizzazione ≠ ruolo documentale ≠ semantica; forma K-032 aperta; H5/H7/I. |
| 23 Human Statement / contributo | R2.4–R2.5; GATE 1; perdita e recupero REG D01. | Base ricevuta distinta da interpretazione e autorità; non primitiva umana universale; H22/D/G/I. |
| 24 Interpretation Result / Bundle | V1 §3.9; R2.9/R2C §7 → R5.10/R6. | Classificazione operativa del grouping non retrodatata come memoria informativa già definita; forma candidata; D/G/H7/I. |
| 25 Attempt | R1 §R5 → R2.6 esiti parziali/retry. | Tentativi e risultati distinguibili senza autonomia obbligatoria; F/G. |
| 26 Event / Reception | V1 §1.2 → R2.7/R2C §7. | Accadimento di ricezione ≠ Work/esito; Event/Result generali non dimostrati; H1/F/G/J. |
| 27 Verification | V1 §4.7 → R2.4/R2.5 → R3.10. | Workflow, contributo e autorizzazione distinti; conferma locale/tardiva; F/H15/H22/O. |
| 28 Admission | R1 §R6; R2C §8.14; R6 V.1–2; GATE 1. | Applicazione governata ≠ verità; proposte preesistenti, K-145 aperta; E/H16/I. |
| 29 Policy | V1 §4.5–4.6; R4.10; correzioni GATE 2–3. | Risorsa e valutazione distinte; comportamento non validità o soppressione d’impatto; G/E/H14. |
| 30 Provenance | V1 §6.1; R2C T1; R4.6–R4.8. | Origine/contesto catturati localmente; non supporto garantito o recorder centrale; G/H20. |
| 31 Lineage | R1 ciclo; R2C §11; R3.8; R4.5–R4.8. | Dipendenze informative ≠ operative; recuperabilità ≠ validità del supporto; G/H11/H13/H20. |
| 32 Impact | R3.8–R3.9 → R6 V.9 corretto da GATE 2. | Potenziale, basi, rivalutazione e risultato accertato distinti; K-087/K-161 stabili; E/H13/H12/O. |
| 33 Negativo / modalità | R2.3; R3.7 → R6 I.L/V.7–8. | Quattro forme negative e modalità semantiche, senza nuova primitiva; D/H17/I/O. |
| 34 Identity Reconciliation | R5.4–R5.5, omonimi e POD errato; REG D05. | Meccanismo, non primitiva; uso unitario non distruttivo e revisionabile; H8/E/I/J. |
| 35 Correction / Supersession / conflitto | R3.5 → R6 V.3/GATE. | Rettifica, successione, incompatibilità, arrivo tardivo ed effetto governato non fusi; H7/H9/H10/H13/H16. |

### 8.1 Prove di mancata retrodatazione

Sono stati cercati quattro salti particolarmente insidiosi:

1. **Identifier e Derivation già provati in R2.** R2C §2 li dichiara NON TESTATI come primitive. GK §§2–3 conserva questa limitazione e localizza i test successivi in R5 e R3 rispettivamente.
2. **Referent già locus interno pienamente definito in R5.** La definizione D di R5 era più esterna; GK registra il correttivo R6 e lo stato CANDIDATA K-143, non una continuità verbale fittizia.
3. **R6 già preciso su Assertion, impatto e Policy.** GATE dichiara reali i tre difetti. GK li attribuisce al controllo successivo; V21 usa le formulazioni corrette. Nessuna retrodatazione della correzione.
4. **D06 come perdita di un owner preciso già consolidato, oppure owner mai proposto.** R1 §R6 proponeva il responsabile Function/Verification; REG non dimostra una rimozione precisa. GK e K-185 preservano entrambe le informazioni: proposta storica esistente, contratto completo tuttora aperto.

Tutti e quattro i tentativi di dimostrare una perdita del percorso sono confutati dai passaggi espliciti delle genealogie. Il controllo puntuale dei rinvii ha però rilevato MP-M02: nella scheda Referent un rinvio secondario a R6 §III.1 è errato; la sezione pertinente è §III.8. Gli altri rinvii e la spiegazione preservano la trasformazione, senza rendere corretta quella citazione.

### 8.2 Limiti inderogabili delle due primitive forti

Per Referent, V21 I distingue locus e cosa esterna; R6 V.2 chiarisce che anche Admission non garantisce esistenza certa. GK Referent mantiene K-143 CANDIDATA. La forza della necessità non promuove la definizione.

Per Assertion, GATE 1 e GK Assertion mantengono proposizione, contributo attribuito e commitment distinguibili, con supporto collegato. Admission non cambia autore o contenuto. K-160 resta APERTA. Anche K-066 resta APERTA nel Ledger e in GK §§3/5: l’omissione nominale nell’elenco sintetico O della candidata non è una decisione che la chiuda. Il default generale sulle Assertion non risolve da solo le meta-Assertion interne.

**Esito: PASS. Nessuna qualificazione obbligatoria perduta nella catena documentale.**

## 9. Anti-promotion e anti-indebolimento

| Oggetto controllato | Possibile errore cercato | Riscontro che lo esclude |
|---|---|---|
| Identifier | Tre livelli diventati tre primitive. | GK Identifier; R5.3/R6 V.4; V21 I distingue schema, valore, assegnazione e lascia la forma aperta. |
| Value | FORTE diventato entità autonoma. | GK Value e V21 I lo negano esplicitamente; resta contenuto strutturato. |
| Source | K-049 e K-148 fusi in uno stato unico. | Definizione STABILE, collocazione CANDIDATA distinte in GK e V21 I. |
| Observation | K-050 promossa a percorso universale o adiacenza canonica. | Definizione stabile, K-148 candidata, percorso strutturato senza Observation fittizia. |
| Evidence/supporto | Indirizzabilità diventata primitiva obbligatoria. | K-065 aperta; GK/I preservano supporto qualificato senza ontologia definitiva. |
| Locator | Regione richiamabile trasformata in Referent. | R2C T6; GK locator; V21 I mantiene localizzazione e forma candidate. |
| Contributo attribuito | Generalizzazione di GATE diventata HumanStatement Core. | GK Human Statement; V21 H22/I conserva la base senza nuova primitiva. |
| Interpretation Result | Composizione diventata Candidate universale o bundle atomico. | K-053 candidata, proposte eterogenee e C04 aperta; GK/V21 D/G/H7/I. |
| Qualificazioni temporali | Necessità del tempo diventata Validity uniforme. | R3.1–R3.3; GK; V21 H10/I mantiene ruoli, precisione e ignoranza. |
| Work | Durabilità diventata primitiva informativa/per-attività. | GK Work/Attempt e V21 F/I: forma candidata, granularità aperta, non ogni attività richiede Work. |
| Current Reconstruction | Risultato candidato indebolisce K-073 STABILE. | GK e V21 I dichiarano distinti responsabilità stabile e forma candidata. |
| Referent | Necessità forte promuove K-143. | Entrambi gli artefatti conservano esplicitamente la candidatura della definizione. |

“Informazione adiacente” non significa irrilevante o eliminabile. “Governance/processo, non primitiva informativa” non significa processo privo di tracce: Decision, Disposition e Application hanno memoria e storia senza diventare Assertion.

**Esito: PASS.**

## 10. Dodici forme universali non sostenute

Il test non domanda soltanto se il nome sia vietato: verifica dove è finito il problema. GK §1/§4 distingue rifiuto della semantica uniforme, decomposizione e necessità non dimostrata; nessuno diventa impossibilità eterna.

| Forma | Problema e stress originale | Ragione del rifiuto/decomposizione | Destinazione sopravvissuta, riscontrata in V21 |
|---|---|---|---|
| 1 Relation universale uniforme | R2C §4; R5.7: stesso arco usato per fatto, supporto e attesa. | Non condividono conseguenze, autorità o criteri di validazione. | Famiglie I/J, contenuti e piani distinti; forma tecnica comune non decisa. |
| 2 Candidate universale | R2C T3; R5.10: importo determinato, data ambigua, referente irrisolto. | Un tipo unico non è dimostrato; il solo stato non rappresenta l’incompletezza. | Proposte e Interpretation Result, memoria G, Work separato. |
| 3 Knowledge State unitario | R2C §6: pending, determinato e ammesso riguardano bersagli diversi. | Non sono stadi successivi della stessa cosa. | D/E/F, assessment, Admission e Work locali. |
| 4 Validity universale | R3.1–R3.2: intervallo del contenuto, momento di conoscenza e uso. | Un intervallo unico confonde verità, storia e applicabilità. | H10/H12/I; tempo qualificato e reference time. |
| 5 LogicalDocument universale | R2C T5; R5.2: tre immagini non provano un documento unico. | Grouping/indirizzabilità non provano subjecthood. | Porzioni/composizione, possibile Referent documentale candidato, coreferenza. |
| 6 Expectation universale | R3.7: previsione, obbligo, raccomandazione e attenzione. | Non dimostrano una sola natura obbligatoria. | Base/finestra/riscontro/comportamento; K-080 candidata e C02 aperta. |
| 7 Temporal Controller universale | R3.6: condizione temporale senza nuova Source. | Obbligo operativo dipendente dalla funzione, non prova di un nuovo owner generale. | H10 e coordinamento Work/funzione autorizzata in F. |
| 8 Result / Event universali | R2.6–R2.7; R2C §7/§9: esito del tentativo, contenuto prodotto e ricezione distinti. | Le nature concrete non richiedono involucri Core generali. | Risultati tipizzati, Provenance della ricezione, storia Work/Attempt. |
| 9 Quality / truth scorer universale | R1 §R7; R4.1/R4.9: OCR buono ma link debole; riuso auto-confermante. | Uno score globale cancella target e può contare due volte la stessa base. | Assessment locali con risorsa Quality e possibili sintesi per scopo. |
| 10 Reliability globale intrinseca Source | R4.3/R4.5: copie, canale, competenza su P e non su Q. | Origine, fedeltà, competenza, indipendenza e corroborazione non coincidono. | Provenance e valutazioni relative a supporto/target; non proprietà unica della Source. |
| 11 Assertion super-primitiva | R2C §3; R5.6: soggetto irrisolto, supporto e struttura inferenziale. | Una proposizione che descrive la struttura non la sostituisce. | Assertion nel proprio ambito, altri contenuti/relazioni/processi distinti. |
| 12 STALE globale | R3.9; GATE 2: cambiamento Mapping e rivalutazione rinviata. | Potenziale, base in dubbio e conclusione corretta non sono la stessa invalidità. | Qualificazione d’impatto E/H13, uso pertinente H12/Functions; C03 aperta. |

**Esito: PASS per tutte e dodici.** Non emerge un problema scomparso insieme al contenitore, né un divieto più forte delle fonti. In particolare Event/Result e una futura struttura tecnica Relation non sono dichiarati impossibili; manca la loro necessità come forme universali del modello corrente.

## 11. Governance distinta dal Core informativo

| Ruolo | Fonte della distinzione | Confine riscontrato in GK/GC e V21 |
|---|---|---|
| Decision | R1 §R6; R3.10; REG D06. | Scelta motivata con origine, autorità, target, scope e contesto; non ogni giudizio di comparabilità è una Decision. |
| Disposition | R1 §R6. | Trattamento autorizzato, non fatto del mondo e non risultato esclusivo della Policy. |
| Application | R1 §R6; R2/R3. | Effetto tentato/applicato ed esito; non sinonimo di autorizzazione né prova fattuale del pagamento. |
| Verification | R2.4–R2.5; R3.10; R4.2. | Processo con domanda e contributo mirato; non sostegno globale di tutto ciò che il flusso usa. |
| Admission | R1 §R6; R6 V.2; GATE 1. | Applica commitment; non rende vero il contenuto, non aumenta Quality e non ne cambia attribuzione. |
| Policy | V1 §4.5; R4.10; GATE 2–3. | Risorsa comportamentale e sua valutazione; non determina validità semantica/inferenziale. |
| Work | R1 §R5; R2.6; R6 V.9. | Continuità di un obiettivo autorizzato; stato del lavoro distinto dallo stato del mondo. |
| Attempt | R2.6; R2C §9. | Esecuzione distinguibile e risultati propri, non primitiva informativa obbligatoria. |

GC 26–28/31/34 e GK Decision/Verification/Admission/Policy/Work/Attempt convergono su V21 E/F/G/H14–H16/H19/H22.

Il caso della risposta tardiva è una prova storica particolarmente discriminante: “sì” ricevuto due settimane dopo può essere un contributo pertinente alla domanda originaria senza autorizzare il trattamento di un target cambiato. Le genealogie conservano domanda, portata e autorità; V21 E/F conserva anche il controllo dell’effetto già applicato. Non viene inventata una nuova Decision soltanto per controllare condizioni già fissate.

**D06 resta aperta.** La memoria necessaria è stabilita, la formalizzazione non-Policy non è assegnata completamente. Non si deduce l’owner da H22, dall’esistenza di una memoria o dal fatto che la risposta provenga da un utente. Un owner operativo del Work non risolve automaticamente l’ownership della Decision.

**Esito: PASS.**

## 12. Tempo, attenzione e impatto

La verifica combina GK Validity/Current Reconstruction/Expectation/Impact/Correction con GC 25d/25f/25h e gruppo 14. Non tratta tutta la temporalità come problema unico.

| Passaggio | Controprova documentale cercata | Riscontro |
|---|---|---|
| Ruoli temporali | Data di ricezione usata come data del fatto o riempimento di un tempo ignoto. | R3.1–R3.2; V21 H10/I: ruolo, precisione e ignoranza conservati. |
| Reference time | “Corrente” fissato dall’ultimo arrivo. | R3.3; GK Current; H12/I: parametro della domanda e basi pertinenti. |
| Storia allora / passato ricostruito oggi | Nuova informazione retrodatata nella storia epistemica. | K-074, R3.3; GK Current; H12/I separano le due ricostruzioni. |
| Base dell’attesa | Work in attesa che prova obbligo, previsione o assenza. | R3.7; GK Expectation; V21 D/F/I distingue la base informativa. |
| Finestra/condizione | Passaggio del tempo senza alcuna possibilità di ripresa, oppure nuovo controller introdotto. | R3.6; V21 D/F: condizione temporale riconoscibile dal coordinamento autorizzato, H10 riceve il reference time. |
| Riscontro | Nessuna Assertion interpretata trasformata in nessun documento arrivato. | Pagina illeggibile R3.7; Query delimitata D/H17/I. |
| Comportamento | Scadenza trascorsa trasformata in “non pagato”. | R3.4/GATE 3; Policy/Function scelgono attenzione entro semantica e autorizzazioni. |
| Rilevazione d’impatto | Nessuna vecchia dipendenza trovata trasformata in nessun impatto. | R3.8–R3.9; GK Impact/Lineage; V21 G/H13 include assenze, perimetri e continuità. |
| Qualificazione d’impatto | Potenziale coinvolgimento, base dubbia e risultato corretto fusi. | K-087; GK Impact; V21 E/H12/H13 distingue livelli e rivalutazione. |
| Seguito dell’impatto | Policy che cancella l’impatto rinviando il lavoro. | GATE 2 corregge R6; GK lo racconta; V21 E conserva il vincolo sull’uso. |

La base di confronto della cadenza può riguardare emissione, periodo descritto o disponibilità: R3 non le equipara e V21 H10/I le distingue. Previsione, dichiarazione, obbligo e raccomandazione non si convertono automaticamente.

K-080 resta CANDIDATA: la composizione non viene dichiarata una nuova primitiva o contratto definitivamente chiuso. C02 rimane la domanda sul rapporto tra previsione e successivo riscontro negativo; C03 rimane quella sugli usi concreti di contenuti impattati. F2d riguarda la disponibilità di un cambiamento di versione e non viene risolta per analogia con una condizione temporale.

**Esito: PASS; nessuna Validity, Expectation, Temporal Controller o STALE universali reintrodotti.**

## 13. Documenti, identificatori e continuità

Il percorso non sostituisce LogicalDocument con un Referent documentale obbligatorio. GK Documento e Logical Document spiegano problemi diversi: necessità eventuale di identità e rifiuto di un contenitore generale interposto. V21 I mantiene il documento come possibile Referent CANDIDATO.

Le quattro responsabilità nascoste sotto il nome storico sono ricostruibili da R5 Document Identity Reconciliation, GC 25b e GK Documento:

| Problema | Prova discriminante originale | Destinazione |
|---|---|---|
| Deduplicazione tecnica | Stessi byte consegnati due volte. | H3; due ricezioni restano possibili in H1. |
| Composition/grouping | Fronte e retro; oppure una foto con parti di due documenti. | H7 e locator; nessuna prova automatica di identità/completezza. |
| Document coreference | PDF, foto della stampa e inoltro dello stesso atto. | Specializzazione H8, con proposte e supporti. |
| Version/correction | D2 dichiara una rettifica di D1. | H7/H9/H10 per significato e relazione; H16 per effetto governato. |

La sola uguaglianza del POD non prova che due documenti riguardino lo stesso contratto o la stessa persona. R5.3 separa schema, valore e assegnazione; R5 “Identità e tempo” distingue soggetti la cui continuità non coincide. GK Identifier/Referent/Reconciliation e V21 H8/I conservano il ruolo del Domain nel decidere quale soggetto si sta seguendo.

La falsa identità non viene resa irrimediabile: R5.5/REG D05, GC 25a/30 e GK Reconciliation richiedono non distruttività e revisionabilità. V21 G/H8/H16/I mantiene le differenze recuperabili nei limiti dell’informazione ancora legittimamente conservata. Questo non impone un’operazione software di unmerge o retention illimitata.

L’ancoraggio di Observation e locator resta alla Source/rappresentazione, non a un documento che occorrerebbe aver identificato prima dell’estrazione. Il vecchio argomento secondo cui la segmentazione successiva renderebbe incoerenti le Observation non trova sostegno nel testo.

**Esito: PASS.**

## 14. Supporto, Quality, Provenance e Lineage

Il caso R4.5 — PDF, fotografia della stampa e allegato inoltrato — permette di verificare separatamente:

- più rappresentazioni utili per leggere;
- una possibile origine documentale comune;
- più supporti disponibili;
- assenza di corroborazione indipendente aggiuntiva del fatto dichiarato.

GK Evidence/Quality/Provenance/Lineage conserva il caso, non soltanto il divieto finale. GC 14/15/20/22/24 distribuisce correttamente la produzione locale; H17 recupera e H20 spiega. V21 H3/H5/H7/H8/H11/H12/H17/H20 e I/J mantengono questi confini.

| Distinzione | Verifica della catena |
|---|---|
| Attribution ≠ support | GATE 1: un contributo può presentare P senza sostenerlo adeguatamente; GK e V21 I/J separano i due rapporti. |
| Support ≠ Provenance | R4.3–R4.4: sapere da dove arriva un contenuto non determina quanto sostenga P. |
| Provenance ≠ Lineage | R4.6: origine/contesto distinti da trasformazioni e dipendenze informative; conservazione collegata non significa equivalenza. |
| Lineage ≠ validità del supporto | R1 ciclo; R4.5; R6 IV; REG D02: il percorso può esistere ed essere circolare o non indipendente. |
| Ignoto ≠ indipendente ≠ dipendente accertato | R4.5 ammette espressamente indipendenza non determinata; K-102 e V21 I non la presumono e non impongono enum. |
| Qualità locale ≠ certezza globale | R4.1–R4.2: target, aspetto, base e scopo/storia; OCR, semantica e riconciliazione possono avere esiti differenti. |
| Nuovo assessment ≠ ripetizione | R4.9; REG D04: nuova base, criterio o contesto materialmente pertinente; non semplice Admission o riuso. |
| Recuperabilità ≠ conservazione indiscriminata | R3.4; R4.8: basi e risultati materialmente usati per decidere/spiegare; non ogni calcolo né riesecuzione bit-for-bit. |

Il sospetto che manchi un “verificatore centrale” dell’auto-supporto è stato controllato e respinto: gli obblighi sono dei produttori/consumatori competenti, che possono usare il contesto recuperabile. La distribuzione non cancella né l’invariante né le informazioni necessarie al controllo.

Non vengono richiesti un truth score, una reliability globale della Source o una tassonomia definitiva di cinque dimensioni. K-098 resta candidata nei confini; K-118 resta aperta sui criteri concreti.

**Esito: PASS.**

## 15. Negativo, modalità e Derivation

| Forma negativa | Fonte dello stress | Natura e destinazione preservate |
|---|---|---|
| Negazione esplicita | R6 I.L: una fonte nega l’assunzione di un farmaco. | Contenuto proposizionale attribuito e sostenuto, non constatazione di una ricerca vuota. |
| Assenza osservata locale | R6 I.L: nessuna data nel riquadro osservato. | Observation con regione/metodo e limiti propri; non assenza nel mondo. |
| Ricerca negativa delimitata | R2.3; R3.7; R6 I.L/V.7. | Esito H17 con corpus, tempo, criteri, copertura e limiti pertinenti. |
| Inferenza negativa sul mondo | R3.4; R6 I.L/V.7. | Richiede premesse, condizioni Domain e giustificazione; non segue dal solo mancato reperimento. |

GK Negativo e V21 D/H17/I conservano le quattro forme. Il produttore della ricerca negativa è presente; il perfezionamento del perimetro richiesto/accessibile/esaminato resta C05, non un vuoto di ownership.

Derivation resta articolata in attività, conclusione e giustificazione: R3.4 → GC 25g/GK Derivation → V21 H11/G/I. La conclusione non è Observation e non diventa supporto indipendente delle proprie premesse.

È stato controllato anche un possibile buco del percorso inverso: l’aggregazione nuova. GC 30 conclude esplicitamente che le aggregazioni con nuovo significato richiedono Derivation e rinvia a H11/H12; AUDIT A.30 preserva il confine. R6 I.K, “Totale aggregato”, esplicita elementi inclusi, criteri, periodo e metodo; K-150 conserva il dettaglio. V21 H11/G lo ripristina, H18 lo espone senza produrlo implicitamente. Non è una nuova responsabilità Aggregate; l’assenza di una scheda GK separata “Aggregazione” non dimostra perdita strutturale.

Le modalità descrittiva, normativa, intenzionale e predittiva restano nel significato. L’esecuzione o l’uso di una derivazione possono essere governati dalla Policy; la sua validità inferenziale no. La formulazione R6 imprecisa viene corretta da GATE 3, non assunta come ancora vigente.

**Esito: PASS.**

## 16. Aperture e candidature conservate

Il controllo è mirato agli stati richiesti dal Gate, non una nuova coverage di tutte le K. “Preservata” non significa che ogni K-ID debba essere stampato nominalmente in ogni scheda della candidata.

| K-ID | Stato KL riscontrato | Domanda residua riconoscibile in GK/GC e raccordo V21 |
|---|---|---|
| K-160 | APERTA | Identità/equivalenza proposizionale; GK Assertion/§5, V21 O. |
| K-066 | APERTA | Meta-Assertion interne; GK Assertion/§5 e KL espliciti. Non chiusa dal silenzio nominale di O. |
| K-065 | APERTA | Forma autonoma/granularità del supporto; GK Evidence/§5, V21 I/O. |
| K-026 | APERTA | Granularità Work, retry, riaperture e uso dei parziali; GK Work/Attempt/§5, V21 F/O. |
| K-032 | APERTA | Locator, confini incerti, ordine e completezza; GK locator/§5, V21 I/O e C04–C05 pertinenti. |
| K-046 | APERTA | Contratti di acquisizione/verifica/ammissione parziale; GK Verification/§5; V21 E/F non fissa contratti completi. |
| K-096 | APERTA | Dettagli temporali, revoca, rivalutazione e conservazione ulteriore; GK tempo/§5, V21 O/F2d. |
| K-118 | APERTA | Quality empirica e indipendenza con origini incomplete; GK Quality/§5, V21 O. |
| K-119 | APERTA | Forma delle proposte e conferma delle letture; GK Observation/Interpretation/§5. K-144 ne chiarisce l’esistenza, non tutta la forma. |
| K-141 | APERTA | Ontologia e criteri degli identificatori; GK Identifier/§5, V21 I/O. |
| K-142 | APERTA | Identità/versione documentale e vocabolario relazionale; GK Documento/Relation/§5, V21 I/O. |
| K-145 | APERTA | Ammettere Referent senza Assertion già ammessa; GK Admission/§5 e KL espliciti. R6 risolve l’esistenza della proposta, non il contratto completo. |
| K-183 | APERTA | Granularità finale degli accorpamenti; GC §§6/9, GK §5, V21 O. |

| Apertura successiva | Ciò che non viene deciso |
|---|---|
| C01 | Contratto uniforme di applicabilità nei rami Verification/Work/Application. Non un nuovo decisore. |
| C02 | Rapporto fra base predittiva e riscontro negativo. Non equivalenza automatica a conflitto. |
| C03 | Uso concreto dei contenuti ammessi e impattati. Non cancellazione dell’impatto noto. |
| C04 | Visibilità dei sub-risultati di Interpretation. Non scissione obbligatoria H7. |
| C05 | Corpus richiesto, accessibile, esaminato e copertura. Non nuovo produttore del negativo. |
| C06 | Criteri per considerare proposte non ammesse nella Reconstruction. Non Admission implicita. |
| C07 / D06 | Formalizzazione non-Policy. K-185 APERTA; nessun owner nuovo o Decision Manager. |
| F2d | Chi rende disponibile il cambiamento di versione. Nessun C08, scheduler, event bus o produttore assegnato. |

DV §C, GK §5 e V21 O concordano sulle domande e sui limiti acquisiti.

| Conoscenza candidata richiesta | Verifica |
|---|---|
| K-023 | CANDIDATA in KL; GK §5 e V21 O la mantengono Ledger-only con K-022. |
| K-080 | CANDIDATA in KL/GK; V21 D/I/O non consolida la composizione dell’attesa. |
| K-143 | CANDIDATA in KL/GK; V21 I distingue definizione dalla necessità referenziale forte. |
| K-148 | CANDIDATA in KL/GK; V21 I distingue collocazione da definizioni stabili Source/Observation. |

Anche K-091 resta intenzionalmente nel Ledger: governance fondazionale del cambiamento degli invarianti, non Application Policy runtime. Nessuna candidatura è promossa a STABILE per rendere il Gate superabile.

**Esito: PASS.**

## 17. Reverse traceability — Dalla candidata alle genealogie e alle fonti

Il controllo inverso parte dalle trasformazioni sostanziali in V21 A–O, dalle H e dai recuperi esposti nei record finali; non assume che basti la presenza della medesima parola. Le tabelle §§5, 7 e 8 costituiscono rispettivamente i raccordi analitici delle 34 origini, delle 24 destinazioni e delle 35 unità concettuali. La matrice seguente verifica trasversalmente i cambiamenti che quelle unità devono spiegare.

Classi: **A** spiegata da GC; **B** spiegata da GK; **C** deliberatamente fuori dal perimetro delle due genealogie; **D** non tracciata. Dove cooperano entrambe si indica prima la classe principale. C non significa “fuori da Fold” né “ignorabile”: le fonti e il motivo dell’esclusione devono essere espliciti.

| Trasformazione sostanziale nella v2.1 | Classe | Percorso inverso verificato |
|---|---|---|
| A/B/C: aree non pipeline, viste per nature e responsabilità | A, con B | GC §1/§6; GK §1/§2 → R1 §R1–R2, R2C §11; ASM1 A–C/REG scelta organizzativa/ASM2. La scelta di impaginazione non crea natura nuova. |
| H1: adattamento e registrazione insieme ma distinti | A | GC 1–2/§6 → AUDIT 1–2 → ASM1 K → REG D07 → ASM2. |
| H2/H4: processabilità distinta dalla Source preservata | A, con B | GC 3/6; GK Source → V1 §§1.3/1.6 → R2C T1. |
| H3/I: dedup distinta da identità e indipendenza | A, con B | GC 4/25b; GK Documento/Evidence → R5.9/document identity, R4.5. |
| H5: estrazione accorpata con capacità/esiti locali | A | GC 7–15 → V1 §2, R2.6, R4, AUDIT A.7–15. |
| H5/I: lettura nativa distinta da OCR e resa visuale | A | GC 8–9 → V1 §2.2–2.3/AUDIT A.8; K-169 e Patch Record B08 sono recupero, non teoria nuova. |
| H6/H7: Mapping riusabile e composizione semantica distinti | A | GC 16/17/21 → R1 §R4, R3.9, R5.9/R5.10. |
| H6/H7/I: tipo del contenitore non ereditato dalle parti | A | GC 16 → R2.2/R5.9 e audit Source Classifier; K-171. |
| H7/G: proposte, alternative e memoria indipendente dal Work | B, con A | GK Candidate/Interpretation/Knowledge; GC 19/21/23 → R2C T3, R5.10, R6 V.1–2. |
| H7/H9/H16: alternative esclusive non ammesse congiuntamente | B, con A | GK Candidate/Interpretation; GC 23 → R2C T3/R5.10/R6 III.3; limite epistemico anche in GK Quality. |
| G/H: controlli, supporto e assessment distribuiti | A, con B | GC 14/15/20/22–24; GK Quality/Evidence/Provenance → R2C/R4/R6. |
| H8: proposta di coreferenza, non generazione obbligatoria o merge | B, con A | GK Reconciliation/Identifier; GC 19/25a → R5.3–R5.5/REG D05. |
| I: schema–valore–assegnazione | B | GK Identifier → NON TESTATO R2C §2 → R5.3/R6 V.4; K-141 aperta. |
| I: Referent interno anche proposto/ipotetico | B | GK Referent → R5.1 corretto da R6 V.1; K-120→K-143 candidata. |
| I: Assertion distinta da contributo/supporto/commitment | B | GK Assertion/Human Statement/Admission → R6 corretto da GATE 1; K-155→K-158. |
| I: Source/Observation adiacenti, non soggetti obbligatori | B | GK Source/Observation → R2C T1/T2 → R6 V.5; K-148 candidata. |
| I/J: Value, attributi e relazioni con nature differenti | B | GK Value/Subject–Property/Relation → R2C §5, R5.7–R5.8; K-132. |
| H9/H10/E: confronto, conflitto, rettifica, successione ed effetto distinti | A, con B | GC 25c–25f; GK Correction → R3.5/R4.10/R6 V.3/GATE. |
| H11/G/H18: nuova aggregazione come derivazione pertinente | A, con B | GC 30/25g; GK Derivation → AUDIT A.30, R3.4 e R6 I.K; dettaglio K-150 in KL. |
| H12/I: Current Reconstruction non ultimo dato/sempre nuova Assertion | B, con A | GK Current; GC 25h → R3.3/AUDIT 25h; K-072→K-073. |
| D/F/I: attenzione temporale senza Source o controller fittizi | B, con A | GK Expectation/Work; GC 25d/31 e gruppo 24 → R3.6–R3.7; Δ01. |
| E/H13: impatto come informazione, non solo apertura Work | B, con A | GK Impact; GC §4 gruppo 14 → R3.8–R3.9/R6 V.9/GATE 2. |
| G/H13: impatto su assenze, corpus e continuità | B | GK Impact/Lineage → R3.8–R3.9; Δ03; non solo archi positivi preesistenti. |
| E/H12/H13: livelli d’impatto e vincolo sull’uso | B | GK Impact/Current/Policy → R3.9/GATE 2; Δ04; C03 aperta. |
| G/I/J: no auto-supporto, origine comune e indipendenza ignota | B, con A | GK Evidence/Quality/Lineage; GC 14/20/24/25g → R1 §R7/R4.5/R6 IV/REG D02–D04/Δ05. |
| G/H12/H20: recupero di risultati e basi materialmente usati | B, con A | GK Derivation/Current/Provenance/Lineage; GC 17/29/32 → R3.4/R4.8/Δ02. |
| E/F/H14–H16/H19: Decision/Disposition/Application e applicabilità | B, con A | GK Decision/Admission/Policy; GC 26–28/31 → R1 §R6/R3.10/GATE; Δ07. |
| F: Work, Attempt, esiti parziali, retry e rivalutazione | B, con A | GK Work/Attempt/Event; GC 2/5/9/27 e gruppo 24 → R1/R2.6–R2.7/R2C §9/R4.9. |
| H17: accesso anche pre-Admission, negativo e traversal | A, con B | GC 18/29/25i; GK Negativo/Provenance → R2.3/R4.6–R4.8/R6 V.7. |
| H18–H21: comporre/usare/spiegare/presentare senza nuova semantica nascosta | A | GC 30–33 → V1 §5, R3.3/R4.8/GATE 2/REG D05. |
| H22/D/G: contributo ricevuto distinto dalla sua interpretazione | A, con B | GC 34; GK Human Statement → R2.4/GATE 1/REG D01. |
| H8/H19/H22: persona rappresentata ≠ account ≠ autorità | B | GK Human Statement e riferimenti K-179 → V1 §6.2; Δ08; nessuna nuova primitiva Actor. |
| O: D06 non risolta e memoria non-Policy obbligatoria | B, con A | GK Decision/§5; GC 26/34/§6 → R1 §R6/REG D06/K-185. |
| O/M: forme universali non sostenute e forme ancora candidate | B | GK §§3–5 → percorsi specifici §§8–10 del report; nessun problema eliminato col nome. |
| O: lifecycle/calcolo/effetti, parallelismo e governance degli invarianti Ledger-only | C, esplicitata anche in GK §5 | Esclusione deliberata DV B/V21 O; R1 §R8/K-022–K-023 e R3.9/K-091. Non cancellazione o logica runtime nuova. |
| C/G/H4/H20: privacy, sicurezza, retention e recovery dei collegamenti | C per il complesso trasversale; A/B per le quote di preservazione | GC §2 esclude espressamente le trasversali dal 34 senza eliminarle; V1 §§6.3/6.4/6.8 → AUDIT G/K-180 → Δ09. GK Source/Provenance/Lineage e GC 6 preservano le quote informative. |
| G: osservabilità operativa distinta da audit e storia epistemica | C per l’osservabilità; B per le storie | V1 §6.7 → AUDIT G/K-181; esclusione trasversali GC §2; GK Provenance/Lineage → R4.6. La patch non crea monitoring o nuovo owner. |

### Esito inverso e criterio di esclusione

**Nessun elemento D materialmente strutturale.**

La classificazione C è limitata a esclusioni esplicite dell’inventario e della funzione dell’anatomia, non usata per coprire un concetto Core mancante. Questi temi hanno fonti, collocazione e vincoli recuperabili nel repository; i dettagli tecnici non sono trasformazioni strutturali già decise.

La riga sull’aggregazione dimostra perché non basta cercare una K-ID o un titolo nella genealogia: il confine H18/H11 è spiegato in GC 30, mentre il dettaglio delle basi è nel Ledger. Viceversa un rinvio generico a “Core Engine” non sarebbe bastato a giustificare l’assenza di tale confine.

I record finali della candidata sono stati usati per individuare recuperi da ricondurre alle catene, non come autorità che prova da sola la propria correttezza. Nessuna frase editoriale è stata forzata a diventare una nuova trasformazione del modello.

## 18. Reconstructibility test senza memoria della chat

Il test riguarda il futuro lettore dotato di repository, SM, GC, GK, KL e V21, non dell’archivio originale o di ricordi dell’assistente.

| Domanda | Dove si ricostruisce il percorso e perché basta | Esito |
|---|---|---|
| 1 Quali erano i 34 componenti? | GC §3 ha inventario e forma v1 di ogni voce; §7 è indice univoco. Non serve ricontare tutti i titoli della chat. | RECONSTRUCTIBLE |
| 2 Perché non sono 34 autonomie? | GC §§1/3/7 distingue disposizioni e spiega cause/rischi; non solo elenco dei nomi nuovi. | RECONSTRUCTIBLE |
| 3 Dove sono finite le responsabilità? | Ogni scheda GC collega gruppo, H/viste e quote distribuite; §4 copre i nove meccanismi. | RECONSTRUCTIBLE |
| 4 Perché 24 gruppi ma 22 H? | GC §§5–6 spiega 1–2→H1, 3–23→H2–H22 e 24→F/G, con motivazione REG D07. | RECONSTRUCTIBLE |
| 5 Quali concetti erano candidati Core? | GK registra forma iniziale e confini; avverte che 35 sono unità espositive, non primitive o catalogo v1. | RECONSTRUCTIBLE |
| 6 Quali sono stati stressati? | GK §2 e schede distinguono Round e non-test; casi e alternative sono distillati, non lasciati nel solo rinvio. | RECONSTRUCTIBLE |
| 7 Perché Referent/Assertion hanno forza diversa? | Omonimi, subjecthood, soggetti ipotetici, proposizione/claim/commitment e fallimenti delle super-primitive sono spiegati nelle schede e confrontati con Value/Identifier. | RECONSTRUCTIBLE |
| 8 Perché le forme universali non sono sostenute? | GK §4 espone problema, ragione e destinazione; le schede conservano casi/alternative. “Non necessario” non diventa impossibilità. | RECONSTRUCTIBLE |
| 9 Quali problemi sopravvivono al rifiuto? | Colonne di destinazione e rischi delle due genealogie: proposte, tempo, supporto, documento, qualità, impatto e lavoro restano reperibili. | RECONSTRUCTIBLE |
| 10 Che cosa resta aperto? | GK §5, GC limiti, KL e V21 O distinguono residui da vincoli acquisiti, inclusi K-066/K-145 e D06. | RECONSTRUCTIBLE |

**Classificazione complessiva: RECONSTRUCTIBLE.**

Non è necessario ricordare la conversazione per comprendere il percorso strutturale fondamentale. L’archivio esterno resta necessario per verificare filologicamente il testo integrale e la sequenza delle risposte originali: è un limite esplicitamente dichiarato in SM e nelle genealogie, non un percorso fondamentale lasciato implicito. Il Gate non certifica l’archiviazione integrale dei Round nel repository.

Gli artefatti ancora non versionati sono versionabili e materialmente presenti; la ricostruibilità qui verificata non afferma che siano già stati committati o pubblicati.

## 19. Coerenza fra le due genealogie

| Possibile incompatibilità | Confronto | Esito |
|---|---|---|
| Componente distribuito ma concetto owner universale | GC 20/24 e GK Evidence/Quality assegnano attività locali; forma del supporto e Quality Model non diventano produttori centrali. | Nessuna incompatibilità materiale |
| Core Engine riclassificato ma meccanismi resi primitive | GC 25/§4 tratta famiglia e capacità; GK Derivation/Reconciliation/Impact separa attività e risultati. | Nessuna incompatibilità materiale |
| H7 unico ma proposta descritta come Work atomico | GC 21 e GK Candidate/Interpretation distinguono composizione, parzialità e memoria informativa; C04 aperta. | Nessuna incompatibilità materiale |
| Current Reconstruction stabile in una, candidata nell’altra | GC 25h descrive la responsabilità; GK Current esplicita K-073 stabile e forma candidata. Due assi, non due verdetti discordanti. | Nessuna incompatibilità materiale |
| Documento distribuito contro Referent universale | GC 25b distribuisce quattro problemi; GK Documento/LogicalDocument mantiene il solo Referent eventuale candidato. | Nessuna incompatibilità materiale |
| Provenance Recorder eliminato ma Explanation ricrea tracce | GC 15/25i/32 e GK Provenance/Lineage distinguono cattura, recupero e spiegazione. | Nessuna incompatibilità materiale |
| Governance descritta come forma Core | GK distingue processo e contenuto; GC H14–H16/H19/H22 conserva autorità e applicazione senza super-Assertion. | Nessuna incompatibilità materiale |
| D06 chiusa da un’assegnazione implicita | Entrambe preservano memoria obbligatoria e owner non completamente assegnato; proposta R1 non negata. | Nessuna incompatibilità materiale |
| Indeterminatezza eliminata dalle distribuzioni | K-026/K-065/K-119/K-183 e C01–C07/F2d rimangono nelle sezioni dei limiti. | Nessuna incompatibilità materiale |

Le differenze di classificazione sono legittime quando riguardano oggetti diversi: “DISTRIBUITO” qualifica una responsabilità storica; “forma candidata” qualifica la rappresentazione del suo risultato. Non si è usata questa distinzione per assolvere contraddizioni sul medesimo oggetto: quelle sarebbero finding, ma non ne sono emerse.

## 20. Coerenza della candidata v2.1

| Categoria richiesta | Esito |
|---|---|
| REGRESSIONE STRUTTURALE | Nessuna dimostrata nei confronti effettuati. |
| COMPRESSIONE AMBIGUA | Nessuna che perda una trasformazione o renda incompatibile la candidata con le genealogie. C01–C07 sono domande già aperte, non criteri nuovi da chiudere nel Gate. |
| PROBLEMA EDITORIALE | Nessun problema editoriale strutturale nella candidata. MP-M02 riguarda invece un rinvio secondario in GK/KL, non una formulazione di V21. |
| STATUS/METADATA STALE | MP-M01: candidato ancora descritto come in attesa del re-check Knowledge già documentato in KR. |
| NESSUN PROBLEMA | Inventari/destinazioni, due primitive forti con limiti, anti-promotion, governance, tempo, documenti, supporti, negativo e aperture. |

Sono stati controllati esplicitamente tre falsi positivi:

1. **K-066/K-145 non nominali nell’elenco O.** GK e KL le mantengono aperte e la candidata non formula una chiusura contraria. Il Gate di preservazione del percorso non richiede di duplicare ogni voce del Ledger nell’anatomia.
2. **“Materialmente affetto” nelle formulazioni sintetiche.** V21 E e H13 distinguono potenziale, tenuta delle basi, rivalutazione e risultato accertato; H12 vieta di presentare il potenziale come risultato corretto. La lettura globale non reintroduce STALE.
3. **EG-01 ancora da correggere nelle fotografie delle genealogie.** Il diff del Ledger prova la correzione successiva; le genealogie riportano già le destinazioni corrette 25h/25b. Non è una nuova divergenza di contenuto.

I titoli “H — Responsabilità autonome” e “Core / modello informativo” non vengono letti fuori dalle rispettive legende: autonomia del problema non significa confine software e il modello informativo complessivo comprende elementi adiacenti/governativi senza farne tutte primitive.

## 21. Finding

### MP-M01 — Stato Knowledge Preservation della candidata non aggiornato

- **Severità:** MINORE — STATUS/METADATA STALE.
- **Artefatto:** V21, frontmatter riga 9; introduzione riga 19; sezione P, titolo e passaggi alle righe 1584–1597.
- **Fonte pertinente:** KG documenta il primo Gate non superato; KR §§8–9 documenta il successivo KNOWLEDGE PRESERVATION RE-CHECK SUPERATO. La sequenza è esplicita; non è un’interpretazione delle conclusioni dei Round.
- **Formulazione problematica:** “re-check mirato necessario”, “richiede ancora un re-check mirato” e “ancora in attesa del re-check mirato”.
- **Perché costituisce un problema:** descrive come futuro un controllo già concluso e può indirizzare il lettore al passo operativo sbagliato. Non perde una trasformazione, non altera una K e non cambia il contenuto concettuale della candidata.
- **Conseguenza:** disallineamento di stato fra V21 e KR, non regressione strutturale. Non blocca l’affermazione che il percorso del modello sia preservato.
- **Correzione minima successiva, non applicata:** aggiornare soltanto i tre punti documentali indicati — metadato, introduzione e stato P — per distinguere primo Gate non superato, patch applicata e re-check superato con rinvio a KR. Se si registra anche questo Model Gate, descriverlo esclusivamente nel suo perimetro; non dichiarare già eseguito il freeze, validazione reale o implementazione.
- **Limite della patch:** conservare storia del primo fallimento, record degli interventi, stato Draft e aperture. Nessuna modifica alle formulazioni del modello è necessaria per questo finding.

### MP-M02 — Referent: rinvio R6 §III.1 al posto di §III.8

- **Severità:** MINORE — RINVIO SECONDARIO ERRATO.
- **Artefatti:** GK, scheda Referent / Fonti primarie, riga 123, e riga corrispondente della matrice §6, riga 1565; KL, K-143 / Origine, riga 1915.
- **Fonte originale pertinente:** R6, sezione III, punto 8 “Referent come cosa reale vs rappresentazione interna”. Il punto III.1 è invece “Source come documento/evidenza vs Source come rappresentazione acquisita”. SM §5.2, riga Referent, indica già correttamente R6 §III.8.
- **Formulazione problematica:** il rinvio “§III.1” è incluso fra le fonti della trasformazione del Referent in locus interno.
- **Perché costituisce un problema:** porta il lettore a un’altra contraddizione cross-round. È una perdita di precisione della tracciabilità, non la prova che la trasformazione sia stata inventata: lo stesso campo conserva i rinvii pertinenti R6 §II Q1–Q3 e §V.1; GK racconta correttamente problema, stress, conclusione e limite K-143 CANDIDATA.
- **Conseguenza:** controllo storico meno diretto, ma percorso fondamentale ricostruibile e conclusione sostenuta dalle fonti corrette già indicate. Non è blocker; non contraddice la candidata.
- **Correzione minima successiva, non applicata:** sostituire soltanto §III.1 con §III.8 nei tre punti sopra. Nessuna modifica di formulazione, stato, superamento, datazione o origine genealogica sostanziale di K-143. SM non richiede correzione.
- **Rapporto con EG-01:** è un altro rinvio emerso dal controllo mirato della primitiva Referent, non una riapertura dei rinvii 25g/25h/25b già corretti.

### Contabilità

| Finding | Numero | Disposizione |
|---|---:|---|
| MP-B — BLOCKER | 0 | Nessuna correzione strutturale richiesta da questo audit. |
| MP-M — MINORI | 2 | MP-M01, stato documentale; MP-M02, tre sostituzioni di un rinvio secondario. Patch finite successive, non applicate. |

Non sono stati introdotti finding per miglioramenti editoriali opportunistici, criteri empirici ancora aperti o nuove soluzioni desiderabili. EG-01 non viene riaperto; MP-M01 e MP-M02 non vengono corretti in questa attività.

## 22. Verdetto e portata

# MODEL PRESERVATION GATE SUPERATO

Il verdetto deriva dai confronti documentali esposti, non dai precedenti auto-check.

| Condizione di superamento | Esito |
|---|---|
| Nessun blocker | Sì: 0 MP-B. |
| Nessuna trasformazione strutturale persa | Sì, entro gli inventari e il controllo inverso dichiarati. |
| Nessuna promozione o indebolimento improprio | Sì: assi/stati e limiti preservati. |
| Nessuna riclassificazione interpretata come eliminazione | Sì: problemi e destinazioni restano recuperabili. |
| Reverse traceability senza elementi strutturali D | Sì. |
| Genealogie fra loro coerenti | Sì. |
| Candidata strutturalmente coerente con le genealogie | Sì; il solo disallineamento rilevato è MP-M01. |
| RECONSTRUCTIBLE senza memoria della conversazione | Sì per tutte le dieci domande del mandato. |
| Aperture e candidature conservate | Sì; nessuna nuova decisione le risolve. |
| Minori delimitati e non semantici | Sì: MP-M01 e MP-M02 hanno patch documentali finite, senza modifica del modello. |

Il Gate autorizza esclusivamente la preparazione del freeze della candidata v2.1 e la chiusura documentale di FOL-40. Non autorizza implementazione, architettura tecnica, freeze del perimetro MVP o dichiarazioni sulla validità del modello nei casi reali.

La chiusura documentale successiva non viene eseguita da questo report: nessuna issue aggiornata, nessun commit, push o branch. Il superamento non dimostra che il modello sia vero o completo, ma che il percorso esaminato è preservato fedelmente e ricostruibile.

## 23. Integrità materiale e stato Git finale

È stato creato soltanto docs/ricerca/fold-model-preservation-gate-v2.1-2026-09-06.md.

I 35 file preesistenti individuati tramite l’unione dei file tracked e untracked non ignorati sono confrontati byte-per-byte tramite SHA-256 prima e dopo la creazione. Il controllo include gli artefatti non ancora versionati, che il solo git diff non coprirebbe. Nessun file preesistente è stato modificato; nessun file è stato eliminato o aggiunto oltre al report.

Il diff tracked rimane esclusivamente EG-01: tre righe del Ledger, 3 inserimenti e 3 rimozioni. L’indice rimane invariato e vuoto di modifiche staged. Branch e HEAD sono quelli della sezione 4.

### Impronte dei dieci artefatti esaminati

Queste impronte identificano i file della base preservata, non i corpi dei messaggi originali.

| Artefatto | SHA-256 |
|---|---|
| fold-model-preservation-source-map-2026-09-05.md | 593ab3c02f8187bff9d72d569931956eb0be21fafb038a2800285f8785a32b98 |
| fold-component-responsibility-genealogy-2026-09-05.md | faee58a4c355590035676c4ec1c00eb512674fb52d238681daee19e79fd71314 |
| fold-core-concept-genealogy-2026-09-05.md | eaa81ee73e6633ae0f2760efbe9c1b074e9791ed022742ea12e4a221f67298da |
| fold-anatomia-v2.1-candidate-2026-09-04.md | 98ef21e3128b217afaa863c616fc3c12eb579507103b495ffcc9c7f90e8de754 |
| fold-knowledge-decision-ledger-2026-09-04.md | 4d049e1ec5b103b8b1e8d9811b2c6e351798cb618afcb6c00fa581062565908d |
| fold-anatomia-v2-snapshot-2026-09-04.md | 3e517fee286bf727aa927e5d368863194c578d4746af3cb93a41afef9ab74f72 |
| fold-coverage-ledger-v2-2026-09-04.md | 9bfb8afd4dfb09110c47f749d33a54d23782a3617bbf48fd058e255389331bda |
| fold-delta-v2-v2.1-2026-09-04.md | f47cb5dd82e9dde3cf81caceaaeffb905bd2e3f00d661bda3730aea41811802d |
| fold-knowledge-preservation-gate-v2.1-2026-09-04.md | d450d819999494d50ab3c1ccba96c956576a552cc9106c6545fdfb4772b74f13 |
| fold-knowledge-preservation-recheck-v2.1-2026-09-05.md | 5ed12c170c7c129196200ff53cc8ba7b2cc0dfb517cce7148a3bd8e995c91a2d |

### git status --short finale

~~~text
 M docs/ricerca/fold-knowledge-decision-ledger-2026-09-04.md
?? docs/ricerca/fold-anatomia-v2.1-candidate-2026-09-04.md
?? docs/ricerca/fold-component-responsibility-genealogy-2026-09-05.md
?? docs/ricerca/fold-core-concept-genealogy-2026-09-05.md
?? docs/ricerca/fold-knowledge-preservation-gate-v2.1-2026-09-04.md
?? docs/ricerca/fold-knowledge-preservation-recheck-v2.1-2026-09-05.md
?? docs/ricerca/fold-model-preservation-gate-v2.1-2026-09-06.md
?? docs/ricerca/fold-model-preservation-source-map-2026-09-05.md
~~~

Nessuna modifica a candidata, genealogie, Ledger, Source Map, Coverage, delta, snapshot o Gate precedenti durante questo intervento. Nessuna modifica a Notion o Linear, nessun Fold Sync, nessun nuovo Round o test reale, nessuna architettura o implementazione, nessun commit/push/branch.
