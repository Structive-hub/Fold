---
title: "Fold — Knowledge Preservation Gate della candidata v2.1"
status: Research
date: 2026-09-04
issue: FOL-36
candidate: "docs/ricerca/fold-anatomia-v2.1-candidate-2026-09-04.md"
baseline_commit: "ef3b24f450e21173c07563aee02c96ef39babcf7"
verdict: "KNOWLEDGE PRESERVATION GATE NON SUPERATO"
---

# Fold — Knowledge Preservation Gate v2.1

## A. Perimetro e metodo

Questo Gate risponde a una sola domanda: la candidata v2.1 può essere congelata come baseline dei test senza perdere, deformare, promuovere o chiudere implicitamente conoscenza già acquisita?

L’autorità genealogica primaria è il [Knowledge / Decision Ledger](fold-knowledge-decision-ledger-2026-09-04.md). La [candidata v2.1](fold-anatomia-v2.1-candidate-2026-09-04.md) è esclusivamente il bersaglio dell’audit. Come controlli secondari sono stati usati [Coverage v2](fold-coverage-ledger-v2-2026-09-04.md), [delta v2→v2.1](fold-delta-v2-v2.1-2026-09-04.md), [snapshot v2](fold-anatomia-v2-snapshot-2026-09-04.md) e [coverage FOL-34](fold-fol34-coverage-ledger-2026-09-04.md). FOL-36 è stata consultata in Linear solo in lettura: il Gate è prerequisito del freeze e non autorizza teoria, test, MVP o scelte tecniche.

Metodo:

1. parsing completo delle 188 voci del Ledger, verifica di unicità e stati;
2. confronto forward di ogni K-ID con il contenuto sostanziale della candidata;
3. uso della Coverage v2 solo come baseline di localizzazione, controllando il diff reale v2→v2.1 e riesaminando semanticamente tutte le righe non complete, i delta e i guardrail;
4. audit separato degli stati genealogici, delle decisioni negative, della coerenza interna, delle 22 responsabilità H e delle aperture;
5. audit inverso di ogni gruppo omogeneo di affermazioni nuove nel diff, senza accettare come prova le autodichiarazioni K–P della candidata.

Le quattro destinazioni riuscite richieste dal mandato sono mantenute. Per non qualificare falsamente come “rappresentata fedelmente” una voce incompleta, la matrice usa anche due esiti diagnostici temporanei: **RAPPRESENTATA NELLA V2.1 — FEDELTÀ PARZIALE** e **ETICHETTA GENEALOGICA DA CORREGGERE**. Non sono nuove destinazioni progettuali: identificano righe che impediscono il superamento del Gate.

### Controlli quantitativi iniziali

| Misura | Esito |
|---|---:|
| K-ID totali | 188 |
| K-ID unici | 188 |
| STABILE | 146 |
| CANDIDATA | 15 |
| APERTA | 14 |
| SUPERATA | 13 |
| Conoscenze attive STABILE+CANDIDATA | 161 |
| Responsabilità H da verificare | 22 |
| Aperture di review C01–C07 + F2d | 8 |
| Delta da verificare | 9 |
| Tesi respinte R01–R10 | 10 |

## B. Forward coverage completa per K-ID

La partizione di fedeltà è:

| Fedeltà | Conteggio |
|---|---:|
| COMPLETA | 134 |
| PARZIALE | 20 |
| ALTERATA | 4 |
| ASSENTE | 0 |
| N/A — APERTA | 14 |
| N/A — SUPERATA | 13 |
| N/A — INTENZIONALMENTE FUORI | 3 |
| **Totale** | **188** |

La partizione per destinazione è:

| Destinazione/esito diagnostico | Conteggio |
|---|---:|
| RAPPRESENTATA FEDELMENTE NELLA V2.1 | 134 |
| RAPPRESENTATA NELLA V2.1 — FEDELTÀ PARZIALE | 20 |
| RAPPRESENTATA — SCELTA DI ASSEMBLAGGIO GIUSTIFICATA | 1 |
| RAPPRESENTATA NELLA V2.1 — ETICHETTA GENEALOGICA DA CORREGGERE | 3 |
| INTENZIONALMENTE FUORI DALL’ANATOMIA | 3 |
| APERTA E PRESERVATA COME APERTA | 14 |
| SUPERATA CON GENEALOGIA RECUPERABILE | 13 |
| **Totale** | **188** |

| K-ID | stato Ledger | natura | destinazione | localizzazione v2.1 o motivo esterno | fedeltà | note |
|---|---|---|---|---|---|---|
| K-001 | STABILE | DISTINZIONE; DECISIONE NEGATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | B; C; D | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Le viste non sono una sequenza universale e gli accessi laterali sono espliciti. |
| K-002 | STABILE | GUARDRAIL / INVARIANTE | RAPPRESENTATA NELLA V2.1 — FEDELTÀ PARZIALE | F — Esecuzione; J | PARZIALE | [m01] Relazioni tipate presenti, ma risultato/condizione richiesta e tratto abilitato non sono un contratto esplicito; la conclusione del produttore può ancora essere letta come sufficienza per il consumatore. |
| K-003 | STABILE | DISTINZIONE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | D; E; G | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Source, Observation, proposte e conclusioni possono essere conservate/usate senza Admission. |
| K-004 | CANDIDATA | RICLASSIFICAZIONE | RAPPRESENTATA — SCELTA DI ASSEMBLAGGIO GIUSTIFICATA | C/J — CONSULTS | ALTERATA | [A01] CONSULTS resta relazione autonoma invece della lettura qualificata proposta in R1; è una scelta d’assemblaggio dichiarabile e non è dimostrata perdita semantica. |
| K-005 | STABILE | DECISIONE NEGATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | C — Direzioni principali; J | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Relazioni tipate al posto della freccia generica FEEDS; il suo rigetto è ricavabile dal vocabolario, non dichiarato. |
| K-006 | CANDIDATA | DISTINZIONE | RAPPRESENTATA NELLA V2.1 — FEDELTÀ PARZIALE | J; D/F | PARZIALE | [m02] REACTS_TO e CONSTRAINED_BY sono distinti; EMITS e la differenza evento/risultato non sono preservati. La scelta degli eventi resta candidata, ma la distinzione non dovrebbe scomparire. |
| K-007 | STABILE | RESPONSABILITÀ NECESSARIA; REGOLA OPERATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | F — Esecuzione; H19 | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Il proprietario del lavoro governa dipendenze, attese e seguito autorizzato. |
| K-008 | STABILE | DECISIONE NEGATIVA; REGOLA OPERATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | F — Acquisition; H1 | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: La ricezione non è la regia delle elaborazioni successive. |
| K-009 | STABILE | RICLASSIFICAZIONE; RESPONSABILITÀ NECESSARIA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | H7; F; M | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Composizione semantica distinta dal coordinamento operativo. |
| K-010 | STABILE | GUARDRAIL / INVARIANTE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | D; H7; I — Interpretation Result | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Alternative, dipendenze mancanti e proposte non ammesse sono lecite. |
| K-011 | STABILE | DISTINZIONE; REGOLA OPERATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | F; E — Quattro significati | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Acquisition, Work, Attempt, risultato informativo ed Application non collassano. |
| K-012 | CANDIDATA | DEFINIZIONE; DECISIONE NEGATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | F; I; O | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Work durevole non universale, con proprietario, obiettivo, dipendenze e tentativi; granularità aperta. |
| K-013 | STABILE | DISTINZIONE; REGOLA OPERATIVA | RAPPRESENTATA NELLA V2.1 — FEDELTÀ PARZIALE | F — Rivalutazione; G — storie | PARZIALE | [m03] Nuovo tentativo e nuova storia sono visibili, ma non è esplicito quando presupposti mutati trasformano il retry in nuova valutazione né che l’esito riuscito storico non venga riscritto. |
| K-014 | STABILE | GUARDRAIL / INVARIANTE; REGOLA DI GOVERNANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | G — Policies; H14 | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Il criterio è scegliere comportamento/prudenza fra esiti ammissibili: include regole deterministiche, ma questo caso non è detto. |
| K-015 | STABILE | DISTINZIONE; REGOLA DI GOVERNANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | E — Quattro significati; F | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Scelta, trattamento autorizzato ed esecuzione riuscita/tentata distinti. |
| K-016 | STABILE | DECISIONE NEGATIVA; REGOLA DI GOVERNANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | E; H14; O | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Percorso da autorità esplicita distinto dalla valutazione delle Policy. |
| K-017 | SUPERATA | REGOLA DI GOVERNANCE | SUPERATA CON GENEALOGIA RECUPERABILE | Ledger: superata da K-185; candidata coerente con il successore | N/A — SUPERATA | La posizione storica non riappare come regola corrente. |
| K-018 | STABILE | RESPONSABILITÀ NECESSARIA; REGOLA DI GOVERNANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | E — Applicabilità; H16; Δ07 | COMPLETA | Ripristinati controllo dell’effetto già applicato e limite della mancata applicazione; nessun exactly-once tecnico. |
| K-019 | STABILE | GUARDRAIL / INVARIANTE; REGOLA DI GOVERNANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | D — Ingresso umano; H15; H22 | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Natura della risposta e autorità non equiparate a conferma o Admission. |
| K-020 | STABILE | RICLASSIFICAZIONE; RESPONSABILITÀ NECESSARIA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | D; G; H — obblighi comuni | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Assessment locali e rivalutabili, non passaggio unico. |
| K-021 | STABILE | GUARDRAIL / INVARIANTE; DECISIONE NEGATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | C — Vincoli; D; I; M | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: D02 e D04 ripristinano il divieto di autoconferma. |
| K-022 | STABILE | DISTINZIONE; REGOLA OPERATIVA | INTENZIONALMENTE FUORI DALL’ANATOMIA | O — B01; Ledger | N/A — INTENZIONALMENTE FUORI | Lifecycle/calcolo/effetti e test di parallelizzabilità: attivi nel Ledger, non duplicati nella funzione dell’anatomia. |
| K-023 | CANDIDATA | GUARDRAIL / INVARIANTE | INTENZIONALMENTE FUORI DALL’ANATOMIA | O — B01; Ledger | N/A — INTENZIONALMENTE FUORI | Lifecycle/calcolo/effetti e test di parallelizzabilità: attivi nel Ledger, non duplicati nella funzione dell’anatomia. |
| K-024 | STABILE | DECISIONE NEGATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | F; I; M | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Attempt/esiti restano aspetti operativi, non nuove primitive del mondo. |
| K-025 | STABILE | DISTINZIONE; REGOLA TEMPORALE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | E — Applicabilità; F; H13 | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Decision storica e nuovo controllo di condizioni sono distinti. |
| K-026 | APERTA | APERTURA | APERTA E PRESERVATA COME APERTA | O — granularità Work/accorpamenti; metadata di non-readiness; Ledger | N/A — APERTA | La candidata non assegna una soluzione definitiva né promuove l’apertura a responsabilità/primitiva. |
| K-027 | STABILE | DECISIONE NEGATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | G — Conservazione; O; P | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Nessuna conservazione indiscriminata né forma software/MVP già decisa; la non-obbligatorietà del parallelismo è solo conseguenza del fuori scope, non discussa. |
| K-028 | STABILE | DISTINZIONE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | I — Documenti e rappresentazioni | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Cardinalità multiple e identità documentale distinta da forma tecnica. |
| K-029 | CANDIDATA | DEFINIZIONE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | I — Elementi; I — Documenti | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Referent documentale facoltativo quando serve identità indipendente. |
| K-030 | STABILE | DECISIONE NEGATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | M — Logical Document | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Escluso Logical Document obbligatorio. |
| K-031 | STABILE | RESPONSABILITÀ NECESSARIA; DECISIONE NEGATIVA | RAPPRESENTATA NELLA V2.1 — FEDELTÀ PARZIALE | I — Documenti/locator; H5/H7 | PARZIALE | [m04] Porzioni e confini sono rappresentabili; manca il divieto esplicito di richiedere segmentazione completa preventiva e di dedurre ordine/completezza dal raggruppamento. |
| K-032 | APERTA | APERTURA | APERTA E PRESERVATA COME APERTA | I — Locator CANDIDATO; O — criteri documentali/forma; Ledger | N/A — APERTA | La candidata non assegna una soluzione definitiva né promuove l’apertura a responsabilità/primitiva. |
| K-033 | STABILE | RESPONSABILITÀ NECESSARIA; DECISIONE NEGATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | D; H17 | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Accesso a Source, Observation e proposte senza Knowledge artificiale. |
| K-034 | STABILE | GUARDRAIL / INVARIANTE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | H17; I — Informazione negativa | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Risultato negativo circoscritto a corpus, scope e limiti. |
| K-035 | STABILE | DISTINZIONE; CRITERIO DI CONSERVAZIONE / PROVENANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | D — Ingresso umano; H22; G | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: D01 conserva base ricevuta, interpretazione ed autorità separabili. |
| K-036 | STABILE | DECISIONE NEGATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | D; H22; M | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Nessuna Observation umana artificiale o classificazione universale come Source; nessuna nuova primitiva richiesta. |
| K-037 | STABILE | GUARDRAIL / INVARIANTE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | D — Ingresso umano; H15; H22 | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Target e natura circoscritti implicano che correggere una lettura non confermi ruolo, soggetto o pagamento; il caso non è sviluppato. |
| K-038 | STABILE | REGOLA DI GOVERNANCE; CRITERIO DI CONSERVAZIONE / PROVENANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | E — Applicabilità; F — Verification; H15; Δ07 | COMPLETA | Risposta tardiva ancorata a domanda, target, contenuto presentato, scope e natura originari. |
| K-039 | STABILE | GUARDRAIL / INVARIANTE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | E — Applicabilità; H16; I — Supporto; Δ07 | COMPLETA | Conferma abilitante distinta dal supporto diretto delle premesse. |
| K-040 | STABILE | DECISIONE NEGATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | F; I | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Attempt ed esito non promossi a primitive; memorie eterogenee senza Result universale. |
| K-041 | STABILE | DISTINZIONE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | H2; H4; F | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Processabilità e storia dell'acquisizione distinte da preservazione e verità. |
| K-042 | STABILE | RESPONSABILITÀ NECESSARIA | RAPPRESENTATA NELLA V2.1 — FEDELTÀ PARZIALE | H5/H7; F — Esecuzione | PARZIALE | [m05] Produttore, consumatore e Work sono riconoscibili; resta ambiguo chi giudica la sufficienza del risultato parziale per il risultato richiesto. |
| K-043 | STABILE | REGOLA OPERATIVA; CRITERIO DI CONSERVAZIONE / PROVENANCE | RAPPRESENTATA NELLA V2.1 — FEDELTÀ PARZIALE | H5; F — Esecuzione/Rivalutazione; G — Lineage | PARZIALE | [B01] Risultati parziali e tentativi esistono, ma manca il vincolo che i risultati utili sopravvivano a un tentativo interrotto e che un retry riuscito non selezioni in blocco tutte le proprie letture. |
| K-044 | STABILE | DEFINIZIONE; DECISIONE NEGATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | D; E; I — Proposed/Interpretation Result; H16 | COMPLETA | Le proposte restano indirizzabili singolarmente e Admission opera su Referent/Assertion, senza Candidate o gate atomico del bundle. |
| K-045 | STABILE | GUARDRAIL / INVARIANTE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | H5–H7; I — Observation/Assertion | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Distinzione estrazione/semantica e dipendenze irrisolte rendono ricavabile che un token chiaro non basti per una proposizione completa. |
| K-046 | APERTA | APERTURA | APERTA E PRESERVATA COME APERTA | H1/H15 restano contratti concettuali; O/non-readiness; Ledger | N/A — APERTA | La candidata non assegna una soluzione definitiva né promuove l’apertura a responsabilità/primitiva. |
| K-047 | STABILE | GUARDRAIL / INVARIANTE; DECISIONE NEGATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | C — Anti-bloat; I — Legenda; O | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Distinzione necessaria non impone primitiva, archivio o componente. |
| K-048 | SUPERATA | DEFINIZIONE; SUPERAMENTO | SUPERATA CON GENEALOGIA RECUPERABILE | Ledger: superata da K-049; candidata coerente con il successore | N/A — SUPERATA | La posizione storica non riappare come regola corrente. |
| K-049 | STABILE | DEFINIZIONE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | I — Source; H4; D | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Origine contenutistica referenziabile, non evento di ricezione né esito. |
| K-050 | STABILE | DEFINIZIONE; DECISIONE NEGATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | I — Observation; D; H5 | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Osservazione della Source distinta da Assertion e non obbligatoria per ogni ingresso. |
| K-051 | SUPERATA | DEFINIZIONE; SUPERAMENTO | SUPERATA CON GENEALOGIA RECUPERABILE | Ledger: superata da K-052; candidata coerente con il successore | N/A — SUPERATA | La posizione storica non riappare come regola corrente. |
| K-052 | STABILE | RICLASSIFICAZIONE; DECISIONE NEGATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | E — Proposta; I; M | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Proposed è posizione, non Candidate universale. |
| K-053 | CANDIDATA | DEFINIZIONE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | D; H7; I | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Interpretation Result candidato conserva composizione, alternative e dipendenze. |
| K-054 | STABILE | RICLASSIFICAZIONE; DECISIONE NEGATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | I — Supporto; J; O | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Supporto qualificato necessario, forma concreta aperta senza Evidence universale. |
| K-055 | STABILE | DEFINIZIONE; DECISIONE NEGATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | I; J; M | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Informazioni adiacenti, relazioni epistemiche, operative e inferenziali non ridotte ad Assertion. |
| K-056 | STABILE | GUARDRAIL / INVARIANTE; DECISIONE NEGATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | I — Referent; I — Elementi | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Locator e risultati indirizzabili distinti dal locus referenziale; il criterio generale indirizzabilità non sufficiente è ricavabile, non formulato. |
| K-057 | STABILE | DISTINZIONE; CRITERIO DI CONSERVAZIONE / PROVENANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | I — Documenti; H5–H7; J | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Localizzazione, composizione e ruolo semantico hanno produttori e nature distinti. |
| K-058 | STABILE | DEFINIZIONE; DECISIONE NEGATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | I — Value | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Necessario contenuto strutturato non referenziale, non primitiva autonoma. |
| K-059 | STABILE | DISTINZIONE; RICLASSIFICAZIONE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | J; G — Storie | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Famiglie semanticamente non intercambiabili. |
| K-060 | SUPERATA | DEFINIZIONE; SUPERAMENTO | SUPERATA CON GENEALOGIA RECUPERABILE | Ledger: superata da K-061; candidata coerente con il successore | N/A — SUPERATA | La posizione storica non riappare come regola corrente. |
| K-061 | STABILE | DISTINZIONE; RICLASSIFICAZIONE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | E; F; I; M | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Commitment, Quality, conflitto, applicabilità e attesa hanno target distinti. |
| K-062 | STABILE | RESPONSABILITÀ NECESSARIA; CRITERIO DI CONSERVAZIONE / PROVENANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | G — Memoria operativa; F | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Work, tentativi e storia decisionale non sostituiti dalla Provenance informativa. |
| K-063 | STABILE | DISTINZIONE; REGOLA OPERATIVA | RAPPRESENTATA NELLA V2.1 — FEDELTÀ PARZIALE | H2; F — Work; H17 | PARZIALE | [m06] Sono distinti esito tecnico e risultato negativo, ma output vuoto non è qualificato esplicitamente come successo, incompletezza o non processabilità con copertura/tentativo. |
| K-064 | STABILE | DISTINZIONE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | G; B; C — Anti-bloat | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Risorse riutilizzabili non sono processi attivi né memorie dei casi. |
| K-065 | APERTA | APERTURA | APERTA E PRESERVATA COME APERTA | I/O — forma concreta del supporto indirizzabile | N/A — APERTA | La candidata non assegna una soluzione definitiva né promuove l’apertura a responsabilità/primitiva. |
| K-066 | APERTA | APERTURA | APERTA E PRESERVATA COME APERTA | O — identità del contenuto/meta-Assertion; Ledger | N/A — APERTA | La candidata non assegna una soluzione definitiva né promuove l’apertura a responsabilità/primitiva. |
| K-067 | STABILE | DISTINZIONE; REGOLA TEMPORALE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | I — Tempo; H10; F | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Content time, storia epistemica, operativa e reference time espliciti. |
| K-068 | STABILE | GUARDRAIL / INVARIANTE; REGOLA TEMPORALE | RAPPRESENTATA NELLA V2.1 — FEDELTÀ PARZIALE | H10; I — Tempo | PARZIALE | [B02] Ruoli temporali distinti e nessuna migrazione automatica, ma mancano precisione/incertezza e il divieto di completare un tempo ignoto con una data disponibile; non sono dichiarate le condizioni di comparabilità. |
| K-069 | SUPERATA | DEFINIZIONE; SUPERAMENTO | SUPERATA CON GENEALOGIA RECUPERABILE | Ledger: superata da K-070; candidata coerente con il successore | N/A — SUPERATA | La posizione storica non riappare come regola corrente. |
| K-070 | STABILE | DISTINZIONE; RICLASSIFICAZIONE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | I — Tempo; E — Applicabilità; H12 | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Tempo del contenuto, pertinenza per scopo e condizioni della disposizione separati, senza Validity universale. |
| K-071 | STABILE | REGOLA TEMPORALE; GUARDRAIL / INVARIANTE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | H8; H10; H12; I — Tempo; Δ06 | COMPLETA | Continuità non estesa oltre base e semantica disponibili; fine mancante non prova durata infinita. |
| K-072 | SUPERATA | RICLASSIFICAZIONE; SUPERAMENTO | SUPERATA CON GENEALOGIA RECUPERABILE | Ledger: superata da K-073; candidata coerente con il successore | N/A — SUPERATA | La posizione storica non riappare come regola corrente. |
| K-073 | STABILE | RESPONSABILITÀ NECESSARIA; DEFINIZIONE | RAPPRESENTATA NELLA V2.1 — ETICHETTA GENEALOGICA DA CORREGGERE | H12; I — Elementi e famiglie | ALTERATA | [m12] Il contenuto della Reconstruction è fedele, ma la tabella locale la etichetta CANDIDATO benché K-073 sia STABILE: indebolimento genealogico terminologico. |
| K-074 | STABILE | REGOLA TEMPORALE; CRITERIO DI CONSERVAZIONE / PROVENANCE | RAPPRESENTATA NELLA V2.1 — FEDELTÀ PARZIALE | G — storie; H12; I — Tempo | PARZIALE | [m07] Reference time e storia epistemica sono presenti; non sono esplicitamente separate la domanda «che cosa Fold sosteneva allora?» dalla ricostruzione odierna del passato. |
| K-075 | STABILE | CRITERIO DI CONSERVAZIONE / PROVENANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | G — Risorse/Conservazione; H12; H20; Δ02 | COMPLETA | Risultato e basi materialmente usati per Decision o spiegazione storica restano recuperabili. |
| K-076 | STABILE | DEFINIZIONE; CRITERIO DI CONSERVAZIONE / PROVENANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | G — Lineage; H11; I — Derivation/negativo; J | COMPLETA | Premesse, metodo, tempo, contesto, perimetri e assenze materialmente usati sono recuperabili; nessuna Source fittizia. |
| K-077 | STABILE | GUARDRAIL / INVARIANTE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | D — accessi laterali; H17; I — negativo | COMPLETA | H17 distingue esplicitamente risultato negativo, assenza nel mondo e mancato arrivo di Source; Query può leggere materiali di più livelli. |
| K-078 | STABILE | DISTINZIONE; REGOLA TEMPORALE | RAPPRESENTATA NELLA V2.1 — FEDELTÀ PARZIALE | D — Attenzione; H11/H10; I — modalità | PARZIALE | [B03] Predittivo, normativo e riscontro sono distinti, ma periodicità di emissione, periodo fatturato e caricamento non lo sono; previsione, obbligo e raccomandazione possono ancora ricevere forza impropria. |
| K-079 | STABILE | RESPONSABILITÀ NECESSARIA; REGOLA OPERATIVA; REGOLA TEMPORALE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | D — Attenzione temporale; F — Attesa; H10/H19; Δ01 | COMPLETA | Attenzione autonoma promessa composta tramite Work autorizzato, condizione temporale e reference time. |
| K-080 | CANDIDATA | DEFINIZIONE; DISTINZIONE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | D — Attenzione temporale; F; I — Tempo; Δ01 | COMPLETA | Base, condizioni/finestra, riscontro e comportamento sono distinti; composizione esplicitamente CANDIDATA. |
| K-081 | STABILE | DECISIONE NEGATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | D — Attenzione temporale; I — Tempo; M; Δ01 | COMPLETA | Esclusi Expectation e Temporal Controller universali, scheduler e alert universali. |
| K-082 | STABILE | DISTINZIONE; REGOLA TEMPORALE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | D — Riaperture; E — Correzione; H9–H10; J | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Arrivo tardivo, correzione, successione e incompatibilità restano distinti. |
| K-083 | STABILE | RESPONSABILITÀ NECESSARIA; GUARDRAIL / INVARIANTE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | H9; J — incompatibilità sotto scope | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Comparabilità semantica preliminare e scelta applicativa separata. |
| K-084 | STABILE | REGOLA DI GOVERNANCE; REGOLA TEMPORALE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | E — Correzione; C — Correction/Supersession; J | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Dichiarazione, riconoscimento e revisione governata distinti. |
| K-085 | STABILE | CRITERIO DI CONSERVAZIONE / PROVENANCE; RESPONSABILITÀ NECESSARIA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | E — Impatto; G — Lineage; H13; Δ03 | COMPLETA | Impatto esteso a assenze, scope, completezza, continuità e nuovi membri materialmente pertinenti. |
| K-086 | STABILE | GUARDRAIL / INVARIANTE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | G — Lineage; H13; Δ03 | COMPLETA | Dipendenza non trovata non prova assenza d’impatto; insufficienza mantiene indeterminatezza o amplia il controllo. |
| K-087 | STABILE | DISTINZIONE; REGOLA TEMPORALE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | E — Impatto; H12/H13; Δ04 | COMPLETA | Separati coinvolgimento potenziale, tenuta delle basi, rivalutazione e risultato accertato; nessuno STALE globale. |
| K-088 | STABILE | DECISIONE NEGATIVA; REGOLA TEMPORALE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | H13; E; M — Knowledge State | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Non tutto ciò che dipende dal cambiamento è falso; nessun asse globale dello stato. Il nome STALE non è necessario per preservare il confine. |
| K-089 | STABILE | RESPONSABILITÀ NECESSARIA; REGOLA OPERATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | D — Riaperture; E — Impatto; F | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Impatto informativo, scelta operativa e nuova esecuzione distinti. |
| K-090 | STABILE | DISTINZIONE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | D — cambiamento di risorsa; G — risorse; H13 | COMPLETA | Risorse distinte e impatto dipendente dal loro significato; Mapping/Domain/Core/Policy non sono collassati né retroattivi per default. |
| K-091 | STABILE | GUARDRAIL / INVARIANTE | INTENZIONALMENTE FUORI DALL’ANATOMIA | O — B02; Ledger | N/A — INTENZIONALMENTE FUORI | Governance fondazionale del cambiamento Core: attiva, non comportamento runtime né Application Policy. |
| K-092 | STABILE | REGOLA DI GOVERNANCE; REGOLA TEMPORALE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | E — Applicabilità/Impatto; F — Rivalutazione; G | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Decision storica conservata e Policy cambia applicabilità senza riscrivere automaticamente il contenuto. |
| K-093 | STABILE | CRITERIO DI CONSERVAZIONE / PROVENANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | G — Risorse; H12/H20; Δ02 | COMPLETA | Recuperabili parti semanticamente pertinenti delle risorse effettivamente usate, non solo il nome versione. |
| K-094 | STABILE | REGOLA DI GOVERNANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | E — Applicabilità; H16 | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Condizioni correnti, autorità, target e impatti oltre il solo numero di versione; mancata applicazione motivata. |
| K-095 | STABILE | DISTINZIONE; REGOLA DI GOVERNANCE | RAPPRESENTATA NELLA V2.1 — FEDELTÀ PARZIALE | E — Decision/Application; F/G — storie | PARZIALE | [m08] Atto storico, commitment e uso corrente sono distinti; conformità procedurale dell’atto e correttezza fattuale restano solo inferibili, non due valutazioni esplicite. |
| K-096 | APERTA | APERTURA | APERTA E PRESERVATA COME APERTA | O — tempi, Quality e criteri specifici; C01–C03; Ledger | N/A — APERTA | La candidata non assegna una soluzione definitiva né promuove l’apertura a responsabilità/primitiva. |
| K-097 | STABILE | DEFINIZIONE; CRITERIO DI CONSERVAZIONE / PROVENANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | I — Quality; G | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Target, dimensione, base, scopo e storia dell'assessment espliciti. |
| K-098 | CANDIDATA | DISTINZIONE; DECISIONE NEGATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | H5–H8/H11; I — Quality; O | COMPLETA | Assessment locali e nessuno score globale; numero e confini delle famiglie restano candidati, senza promozione. |
| K-099 | STABILE | REGOLA DI GOVERNANCE; GUARDRAIL / INVARIANTE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | E — Impatto/Policy; H14; I — Quality | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Policy sceglie comportamento, Quality resta fondata sulla propria base; prudenza non cambia il giudizio per sola decisione. |
| K-100 | STABILE | DISTINZIONE; DECISIONE NEGATIVA | RAPPRESENTATA NELLA V2.1 — FEDELTÀ PARZIALE | H1/H2; I — Supporto/Quality; G | PARZIALE | [m09] Source, canale, supporto e indipendenza sono separati; provenienza, fedeltà/integrità e competenza relativa alla proposizione non sono enumerate come dimensioni non collassabili. |
| K-101 | STABILE | GUARDRAIL / INVARIANTE; CRITERIO DI CONSERVAZIONE / PROVENANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | G — Provenance; I — Supporto; H5; H20 | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: D03 generalizzato: copie e derivati utili ma non attestazioni indipendenti per numero. |
| K-102 | STABILE | GUARDRAIL / INVARIANTE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | C — Vincoli; G — Lineage; H12; I — Supporto/Quality; Δ05 | COMPLETA | Indipendenza non stabilita non è presunta; può restare indeterminata senza enum o controllore. |
| K-103 | STABILE | CRITERIO DI CONSERVAZIONE / PROVENANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | I — Supporto; O; J | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Target/scope/storia e supporto indirizzabile mantenuti; autonomia/granularità restano aperte. |
| K-104 | STABILE | RICLASSIFICAZIONE; RESPONSABILITÀ NECESSARIA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | D; H — obblighi comuni; H7–H8; H15 | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Supporti locali e pertinenti, non costruttore Evidence universale. |
| K-105 | STABILE | DISTINZIONE; DECISIONE NEGATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | G — Provenance, Lineage e storie | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Quattro significati distinti, pur potendo percorrere la stessa storia conservata. |
| K-106 | STABILE | RESPONSABILITÀ NECESSARIA; CRITERIO DI CONSERVAZIONE / PROVENANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | C — Direzioni; G; H — obblighi comuni | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Ogni produttore registra localmente tracce e dipendenze pertinenti. |
| K-107 | STABILE | CRITERIO DI CONSERVAZIONE / PROVENANCE | RAPPRESENTATA NELLA V2.1 — FEDELTÀ PARZIALE | G — Lineage; H15/H20; I/J — target/locator | PARZIALE | [m10] Target e parti pertinenti sono recuperabili; manca il criterio della minima unità sulla quale conferma, correzione, contestazione o derivazione producono effetti differenti. |
| K-108 | STABILE | DISTINZIONE; CRITERIO DI CONSERVAZIONE / PROVENANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | G — Conservazione/Storie; H12/H20 | COMPLETA | Recupero, spiegazione e riesecuzione restano distinti; esplicitamente esclusa la promessa di riesecuzione identica. |
| K-109 | STABILE | CRITERIO DI CONSERVAZIONE / PROVENANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | G — Risorse; H12/H20; Δ02 | COMPLETA | Materialità definita controfattualmente rispetto a significato, giustificazione, esito o scelta fra alternative. |
| K-110 | STABILE | RESPONSABILITÀ NECESSARIA; GUARDRAIL / INVARIANTE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | H20; G — traversal | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Nessuna narrazione inventata per supplire a tracce mancanti. |
| K-111 | STABILE | GUARDRAIL / INVARIANTE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | D; F; G; H; I; M | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: D04 ripristina nuova base/criterio/contesto materialmente pertinente. |
| K-112 | STABILE | GUARDRAIL / INVARIANTE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | G — tabella delle risorse; H6–H16 | COMPLETA | La scomposizione tra descrivere, valutare, derivare, scegliere ed eseguire è strutturalmente visibile; nessuna regola composita è assegnata in blocco. |
| K-113 | STABILE | DEFINIZIONE; REGOLA DI GOVERNANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | G — Risorse; H6–H16 | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Ruoli di Core, Domain, Mapping, Quality, meccanismi, Policy ed esecuzione preservati. |
| K-114 | SUPERATA | GUARDRAIL / INVARIANTE; SUPERAMENTO | SUPERATA CON GENEALOGIA RECUPERABILE | Ledger: superata da K-115; candidata coerente con il successore | N/A — SUPERATA | La posizione storica non riappare come regola corrente. |
| K-115 | STABILE | GUARDRAIL / INVARIANTE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | D — Proposte; I — Assertion/Supporto; H16 | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Supporto collegato e non incorporato, proposte prima del commitment, Admission non aumenta Quality; possibilità di ipotesi non sostenuta è ricavabile, non illustrata. |
| K-116 | STABILE | GUARDRAIL / INVARIANTE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | D — Riaperture; F — Rivalutazione; I — Supporto | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Stessa origine riusata non diventa nuova fonte; applicato implicitamente al Mapping aggiornato. |
| K-117 | STABILE | GUARDRAIL / INVARIANTE | RAPPRESENTATA NELLA V2.1 — FEDELTÀ PARZIALE | E — Correzione; H9/H12; I — Quality | PARZIALE | [B04] La relazione correttiva è riconosciuta, ma manca il guardrail che vieta di sostituirla con ranking globale, quantità delle fonti, recenza o autorità generica. |
| K-118 | APERTA | APERTURA | APERTA E PRESERVATA COME APERTA | I — indipendenza non determinata; O — formule/soglie Quality; Ledger | N/A — APERTA | La candidata non assegna una soluzione definitiva né promuove l’apertura a responsabilità/primitiva. |
| K-119 | APERTA | APERTURA | APERTA E PRESERVATA COME APERTA | H5/H7 e memorie informative; O — forma concreta; Ledger | N/A — APERTA | La candidata non assegna una soluzione definitiva né promuove l’apertura a responsabilità/primitiva. |
| K-120 | SUPERATA | DEFINIZIONE | SUPERATA CON GENEALOGIA RECUPERABILE | Ledger: superata da K-143; candidata coerente con il successore | N/A — SUPERATA | La posizione storica non riappare come regola corrente. |
| K-121 | STABILE | DISTINZIONE; DEFINIZIONE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | I — Identifier; G — Schemi | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Schema, valore e assegnazione distinti e correggibili. |
| K-122 | STABILE | GUARDRAIL / INVARIANTE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | I — Identifier; H5–H7 | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Valore osservato e compatibilità di schema precedono l'assegnazione proposta. |
| K-123 | STABILE | GUARDRAIL / INVARIANTE; CRITERIO DI CONSERVAZIONE / PROVENANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | H5; I — Identifier | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Originale conservato e nessuna normalizzazione silenziosa; vietato inferire correzione certa dal solo match per i medesimi vincoli, senza esempio specifico. |
| K-124 | STABILE | GUARDRAIL / INVARIANTE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | H6; H8; E; I — Identifier | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Assegnazione e proposta non provano né autorizzano autonomamente coreferenza. |
| K-125 | STABILE | RESPONSABILITÀ NECESSARIA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | H8; E — Coreferenza | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Alternative, indizi contrari, assessment e Admission distinti dall'identità infallibile. |
| K-126 | STABILE | DISTINZIONE; REGOLA DI GOVERNANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | H8; E — Coreferenza; H19 | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Proposizione identitaria, supporto, uso unitario ed effetti non coincidono. |
| K-127 | STABILE | GUARDRAIL / INVARIANTE; CRITERIO DI CONSERVAZIONE / PROVENANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | E; G; H8/H16/H18/H19; I | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: D05 preserva differenze e giustificazioni per contestare e separare, entro informazione legittimamente conservata. |
| K-128 | STABILE | DECISIONE NEGATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | E — Coreferenza; I; J | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Proposizione identitaria con posizioni diverse consente incertezza senza predicato nuovo; non nominato il rifiuto di possibly_same_as. |
| K-129 | STABILE | GUARDRAIL / INVARIANTE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | H8; I — Referent/Identifier | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Più indizi e alternative non equiparano stringa e soggetto; il caso omonimia è ricavabile, non esplicito. |
| K-130 | STABILE | DECISIONE NEGATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | I — famiglie; J — grammatica; M | COMPLETA | Assertion, supporto, Derivation, Quality e relazioni restano famiglie non sostituibili; una descrizione proposizionale non ne assorbe gli obblighi. |
| K-131 | STABILE | RICLASSIFICAZIONE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | J; M | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Famiglie non intercambiabili e nessuna struttura tecnica Relation decisa. |
| K-132 | STABILE | DISTINZIONE | RAPPRESENTATA NELLA V2.1 — FEDELTÀ PARZIALE | I — Value/Referent; J — grammatica | PARZIALE | [B05] Value, Referent e relazioni epistemiche esistono, ma la grammatica non distingue esplicitamente endpoint Referent→Referent, Referent→Value e qualificazioni del contenuto completo. |
| K-133 | STABILE | RICLASSIFICAZIONE; RESPONSABILITÀ NECESSARIA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | H3; H7–H10; H16; I | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Dedup, composizione, coreferenza documentale e gestione versioni/correzioni distribuite. |
| K-134 | STABILE | RESPONSABILITÀ NECESSARIA; CRITERIO DI CONSERVAZIONE / PROVENANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | D; F; G; N | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Proposte in memoria indipendenti da Work attivo e Admission. |
| K-135 | SUPERATA | DEFINIZIONE; SUPERAMENTO | SUPERATA CON GENEALOGIA RECUPERABILE | Ledger: superata da K-136; candidata coerente con il successore | N/A — SUPERATA | La posizione storica non riappare come regola corrente. |
| K-136 | CANDIDATA | DEFINIZIONE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | G; I | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Knowledge come corpo governato, con storie raggiungibili e senza duplicazione fisica obbligatoria. |
| K-137 | SUPERATA | APERTURA | SUPERATA CON GENEALOGIA RECUPERABILE | Ledger: superata da K-144; candidata coerente con il successore | N/A — SUPERATA | La posizione storica non riappare come regola corrente. |
| K-138 | STABILE | REGOLA TEMPORALE; DISTINZIONE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | H8/H10/H12; I — Identifier/Tempo; Δ06 | COMPLETA | Il Domain determina il soggetto della continuità; Identifier o nome non decidono identità/separazione. |
| K-139 | STABILE | RESPONSABILITÀ NECESSARIA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | H7/H8; I — Supporto/Quality | COMPLETA | H8 legge schemi, attributi, tempi e contributi e produce alternative/indizi contrari; H7 conserva dipendenze mancanti; indipendenza può restare indeterminata. |
| K-140 | STABILE | GUARDRAIL / INVARIANTE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | H18; H19; I — Documenti | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Projection non crea semantica o certezza e non distrugge differenze referenziali. |
| K-141 | APERTA | APERTURA | APERTA E PRESERVATA COME APERTA | I — forma Identifier aperta; O — criteri/algoritmi identitari | N/A — APERTA | La candidata non assegna una soluzione definitiva né promuove l’apertura a responsabilità/primitiva. |
| K-142 | APERTA | APERTURA | APERTA E PRESERVATA COME APERTA | O — criteri documentali e vocabolario relazionale | N/A — APERTA | La candidata non assegna una soluzione definitiva né promuove l’apertura a responsabilità/primitiva. |
| K-143 | CANDIDATA | DEFINIZIONE; SUPERAMENTO | RAPPRESENTATA NELLA V2.1 — ETICHETTA GENEALOGICA DA CORREGGERE | I — Elementi e famiglie/Referent | ALTERATA | [m13] Il contenuto è fedele, ma Referent è etichettato FORTE benché la definizione K-143 sia CANDIDATA: promozione terminologica locale. |
| K-144 | STABILE | REGOLA DI GOVERNANCE; SUPERAMENTO | RAPPRESENTATA FEDELMENTE NELLA V2.1 | D; F; I; N | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Proposte informative prima del commitment e indipendenti da Work. |
| K-145 | APERTA | APERTURA | APERTA E PRESERVATA COME APERTA | H16 ammette target senza fissare il prerequisito universale; Ledger | N/A — APERTA | La candidata non assegna una soluzione definitiva né promuove l’apertura a responsabilità/primitiva. |
| K-146 | CANDIDATA | REGOLA DI GOVERNANCE; DEFINIZIONE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | I — Knowledge; H16; G | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Target Referent/Assertion e memorie adiacenti non ammesse come fatti per sola conservazione. |
| K-147 | STABILE | DISTINZIONE; GUARDRAIL / INVARIANTE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | I — Informazione negativa e modalità | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Descrittivo/normativo/intenzionale/predittivo appartengono al significato, non alla Policy. |
| K-148 | CANDIDATA | RICLASSIFICAZIONE; DECISIONE NEGATIVA | RAPPRESENTATA NELLA V2.1 — ETICHETTA GENEALOGICA DA CORREGGERE | I — Elementi e famiglie; C/D | ALTERATA | [m14] Definizioni stabili di Source/Observation sono corrette, ma la loro adiacenza alla grammatica è K-148 CANDIDATA mentre entrambe sono etichettate FORTE: promozione terminologica locale. |
| K-149 | STABILE | DISTINZIONE; GUARDRAIL / INVARIANTE; DECISIONE NEGATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | H17; I — Informazione negativa; I — Supporto | COMPLETA | Quattro forme negative distinte; il risultato delimitato non prova assenza nel mondo e un’Assertion richiede il normale supporto/Domain pertinente. |
| K-150 | STABILE | CRITERIO DI CONSERVAZIONE / PROVENANCE; DISTINZIONE | RAPPRESENTATA NELLA V2.1 — FEDELTÀ PARZIALE | G — Lineage; H11/H18 | PARZIALE | [B06] Aggregazione come derivazione è implicita; non è preservato il contratto specifico che conserva membri inclusi, criteri di inclusione, periodo e metodo. |
| K-151 | STABILE | GUARDRAIL / INVARIANTE | RAPPRESENTATA NELLA V2.1 — FEDELTÀ PARZIALE | D — alternative; H7/H9/H16; I | PARZIALE | [B07] Alternative e incompatibilità sono rappresentabili, ma manca il divieto di ammettere congiuntamente ipotesi mutuamente esclusive e di scambiare la loro restrizione per nuovo supporto. |
| K-152 | STABILE | GUARDRAIL / INVARIANTE; CRITERIO DI CONSERVAZIONE / PROVENANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | C; D — Contesto; H8; I; M | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Cicli senza auto-supporto, contesto e dipendenze recuperabili, origine comune e nuova base valutativa. |
| K-153 | SUPERATA | REGOLA DI GOVERNANCE | SUPERATA CON GENEALOGIA RECUPERABILE | Ledger: superata da K-161; candidata coerente con il successore | N/A — SUPERATA | La posizione storica non riappare come regola corrente. |
| K-154 | SUPERATA | REGOLA DI GOVERNANCE | SUPERATA CON GENEALOGIA RECUPERABILE | Ledger: superata da K-162; candidata coerente con il successore | N/A — SUPERATA | La posizione storica non riappare come regola corrente. |
| K-155 | SUPERATA | DEFINIZIONE | SUPERATA CON GENEALOGIA RECUPERABILE | Ledger: superata da K-158; candidata coerente con il successore | N/A — SUPERATA | La posizione storica non riappare come regola corrente. |
| K-156 | STABILE | DECISIONE NEGATIVA; RICLASSIFICAZIONE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | C — Anti-bloat; H — intro; M; O | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Memorie/obblighi locali non impongono controllori o archivi separati. |
| K-157 | STABILE | REGOLA DI GOVERNANCE; DECISIONE NEGATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | Introduzione; N; P | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Provvisorietà, non canonizzazione, fuori MVP e necessità di ulteriori test espliciti. |
| K-158 | STABILE | DEFINIZIONE; DISTINZIONE; SUPERAMENTO | RAPPRESENTATA FEDELMENTE NELLA V2.1 | I — Assertion e commitment; E | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Contenuto, contributo attribuito e commitment distinti senza tre primitive imposte. |
| K-159 | STABILE | DISTINZIONE; CRITERIO DI CONSERVAZIONE / PROVENANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | E — Correzione; I — Assertion/contributi; J | COMPLETA | Contributi, supporto e commitment sono distinti; la correzione è riconosciuta prima dell’eventuale revisione governata, senza propagazione automatica. |
| K-160 | APERTA | APERTURA; DECISIONE NEGATIVA | APERTA E PRESERVATA COME APERTA | O — quando due contenuti condividano una Assertion | N/A — APERTA | La candidata non assegna una soluzione definitiva né promuove l’apertura a responsabilità/primitiva. |
| K-161 | STABILE | REGOLA DI GOVERNANCE; SUPERAMENTO; GUARDRAIL / INVARIANTE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | D — Riaperture; E — Impatto; H12–H14; M | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Impatto determinato recuperabile e vincolante sull'uso anche senza immediata rivalutazione. |
| K-162 | STABILE | REGOLA DI GOVERNANCE; SUPERAMENTO; DISTINZIONE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | H11; H14; D — Derivazione; M | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Policy governa attivazione/usi, non correttezza inferenziale. |
| K-163 | STABILE | RESPONSABILITÀ NECESSARIA; DISTINZIONE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | H1; F; K | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Due capacità di ricezione preservate dentro lo stesso raggruppamento. |
| K-164 | STABILE | RESPONSABILITÀ NECESSARIA; DISTINZIONE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | H2; F — Separazioni | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Ammissibilità tecnica distinta da verità del contenuto. |
| K-165 | STABILE | RESPONSABILITÀ NECESSARIA; GUARDRAIL / INVARIANTE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | H3; F — Rivalutazione; D | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Uguaglianza tecnica non equivale a identità; diversa risorsa può generare nuova elaborazione sul materiale conservato. |
| K-166 | STABILE | RICLASSIFICAZIONE; DECISIONE NEGATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | F; G; M | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Condizioni tecniche e Work separati da proposte/commitment; nessuno staging universale. |
| K-167 | STABILE | RESPONSABILITÀ NECESSARIA; CRITERIO DI CONSERVAZIONE / PROVENANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | H4; D; G | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Preservazione autonoma dal successo semantico, con rappresentazioni e criteri autorizzativi. |
| K-168 | CANDIDATA | RESPONSABILITÀ NECESSARIA; RICLASSIFICAZIONE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | C — Estrazione; H5; H — obblighi comuni | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Sottocapacità distinte, grezzo, localizzazione, risultati parziali, assessment e Lineage. |
| K-169 | STABILE | DISTINZIONE; GUARDRAIL / INVARIANTE | RAPPRESENTATA NELLA V2.1 — FEDELTÀ PARZIALE | H5; I — Documenti | PARZIALE | [B08] Testo nativo e OCR sono separati e il grezzo non è sovrascritto; manca il guardrail che il testo incorporato può divergere dalla rappresentazione visuale. |
| K-170 | STABILE | DISTINZIONE; GUARDRAIL / INVARIANTE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | H5–H7; I — Observation/Assertion; Documenti | COMPLETA | Layout, struttura e parsing restano letture; scelte di significato appartengono all’Interpretation e non discendono dall’associazione visiva. |
| K-171 | STABILE | RESPONSABILITÀ NECESSARIA; RICLASSIFICAZIONE | RAPPRESENTATA NELLA V2.1 — FEDELTÀ PARZIALE | H6/H7; I — Documenti | PARZIALE | [B09] Classificazione contestuale e Source multi-documento sono presenti; manca il divieto che il tipo del contenitore si trasferisca automaticamente alle porzioni/documenti interni. |
| K-172 | STABILE | RESPONSABILITÀ NECESSARIA; DISTINZIONE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | H6–H7; G | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Applicabilità/versione Mapping e composizione semantica con confini distinti. |
| K-173 | STABILE | RESPONSABILITÀ NECESSARIA; RICLASSIFICAZIONE; DECISIONE NEGATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | H — obblighi comuni; H9; H16; M | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Validazioni locali, confronto e applicabilità, senza validatore universale. |
| K-174 | STABILE | RICLASSIFICAZIONE; DECISIONE NEGATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | C — Anti-bloat; H8–H13; M | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Core Engine solo nome di famiglia, non autorità aggiuntiva. |
| K-175 | STABILE | RESPONSABILITÀ NECESSARIA; RICLASSIFICAZIONE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | D — Contesto; H17; G | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Query di tutte le nature, scope, autorizzazioni e traversal; contesto usato recuperabile. |
| K-176 | STABILE | RESPONSABILITÀ NECESSARIA; REGOLA OPERATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | H15; F — Verifica; H22 | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Domanda, target, risposta, attesa e ruolo della verifica distinti da Admission. |
| K-177 | STABILE | RESPONSABILITÀ NECESSARIA; DISTINZIONE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | H18–H21; D; F | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Problemi di organizzazione, spiegazione, uso ed espressione distinti, senza nuova semantica implicita. |
| K-178 | STABILE | RESPONSABILITÀ NECESSARIA; REGOLA DI GOVERNANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | H22; D; E — Ownership | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Intake preserva e instrada senza sovrascrittura o proprietà automatica della Decision. |
| K-179 | STABILE | DISTINZIONE; GUARDRAIL / INVARIANTE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | C — Trasversali; G — Accesso; H8/H19/H22; Δ08 | COMPLETA | Persona rappresentata, account/attore e autorità concreta per target/azione sono distinti. |
| K-180 | STABILE | RESPONSABILITÀ NECESSARIA; CRITERIO DI CONSERVAZIONE / PROVENANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | C — Trasversali; G — Conservazione; H4/H20; Δ09 | COMPLETA | Cancellazione/retention possono ridurre verificabilità; recovery preserva contenuti e legami senza promettere backup. |
| K-181 | STABILE | DISTINZIONE; RESPONSABILITÀ NECESSARIA | RAPPRESENTATA NELLA V2.1 — FEDELTÀ PARZIALE | F/G — storie; trasversali | PARZIALE | [m11] L’audit delle azioni è presente; l’osservabilità del funzionamento non è nominata, quindi la distinzione non è contraddetta ma resta invisibile e riapribile. |
| K-182 | CANDIDATA | RICLASSIFICAZIONE; DECISIONE NEGATIVA | RAPPRESENTATA FEDELMENTE NELLA V2.1 | A; H — intro; K; L; O | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Checklist 24 non è inventario software; capacità locali e responsabilità preservate. Non prova però copertura di ogni guardrail del Ledger. |
| K-183 | APERTA | APERTURA | APERTA E PRESERVATA COME APERTA | A/H/K/O — granularità finale degli accorpamenti | N/A — APERTA | La candidata non assegna una soluzione definitiva né promuove l’apertura a responsabilità/primitiva. |
| K-184 | STABILE | GUARDRAIL / INVARIANTE; CRITERIO DI CONSERVAZIONE / PROVENANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | P; M; Delta finale | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: D01–D05 verificati puntualmente; il criterio generale che nominare una risorsa non preservi tutti i suoi vincoli è applicato ma non enunciato. |
| K-185 | APERTA | APERTURA; SUPERAMENTO | APERTA E PRESERVATA COME APERTA | E — Ownership non-Policy; O — C07/D06 | N/A — APERTA | La candidata non assegna una soluzione definitiva né promuove l’apertura a responsabilità/primitiva. |
| K-186 | STABILE | DISTINZIONE; REGOLA DI GOVERNANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | I — Legenda; I — Value; O | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: FORTE distinto da primitiva autonoma; CANDIDATO non rende opzionale la responsabilità. |
| K-187 | CANDIDATA | RICLASSIFICAZIONE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | H1; K; A | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Due capacità interne con output/storie distinti: accorpamento organizzativo legittimo. |
| K-188 | STABILE | REGOLA DI GOVERNANCE | RAPPRESENTATA FEDELMENTE NELLA V2.1 | P; Delta finale; E/O | COMPLETA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Cinque recuperi integrati e D06 ancora aperto; gate limitato alla review e non canonizzazione. |

## C. Decisioni negative / guardrail audit

Il Ledger contiene 37 voci la cui natura include **DECISIONE NEGATIVA**: 36 attive e K-160 aperta. La tabella seguente non sostituisce la matrice forward; verifica separatamente che il divieto non sia stato perso dietro una somiglianza lessicale.

| K-ID | Stato | Guardrail | Esito | Nota |
|---|---|---|---|---|
| K-001 | STABILE | Aree funzionali, non stadi runtime obbligatori | PRESERVATA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Le viste non sono una sequenza universale e gli accessi laterali sono espliciti. |
| K-005 | STABILE | FEEDS e frecce generiche non spiegano la cooperazione | PRESERVATA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Relazioni tipate al posto della freccia generica FEEDS; il suo rigetto è ricavabile dal vocabolario, non dichiarato. |
| K-008 | STABILE | Acquisition non governa tutto il futuro della Source | PRESERVATA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: La ricezione non è la regia delle elaborazioni successive. |
| K-012 | CANDIDATA | Work durevole quando serve continuità, non per ogni trasformazione | PRESERVATA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Work durevole non universale, con proprietario, obiettivo, dipendenze e tentativi; granularità aperta. |
| K-016 | STABILE | Policy Evaluation non è l'unica origine dell'autorità | PRESERVATA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Percorso da autorità esplicita distinto dalla valutazione delle Policy. |
| K-021 | STABILE | Niente autoconferma attraverso contesto e qualità | PRESERVATA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: D02 e D04 ripristinano il divieto di autoconferma. |
| K-024 | STABILE | Operatività interna non prova primitive Core del mondo | PRESERVATA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Attempt/esiti restano aspetti operativi, non nuove primitive del mondo. |
| K-027 | STABILE | Conservazione indefinita e parallelismo MVP non sono conseguenze | PRESERVATA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Nessuna conservazione indiscriminata né forma software/MVP già decisa; la non-obbligatorietà del parallelismo è solo conseguenza del fuori scope, non discussa. |
| K-030 | STABILE | Nessuna primitiva universale Logical Document | PRESERVATA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Escluso Logical Document obbligatorio. |
| K-031 | STABILE | Porzioni indirizzabili senza segmentazione automatica completa | PARZIALE | [m04] Porzioni e confini sono rappresentabili; manca il divieto esplicito di richiedere segmentazione completa preventiva e di dedurre ordine/completezza dal raggruppamento. |
| K-033 | STABILE | Query può recuperare materiale senza Knowledge artificiale | PRESERVATA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Accesso a Source, Observation e proposte senza Knowledge artificiale. |
| K-036 | STABILE | Nessuna Human Evidence universale né Observation umana artificiale | PRESERVATA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Nessuna Observation umana artificiale o classificazione universale come Source; nessuna nuova primitiva richiesta. |
| K-040 | STABILE | Nessun involucro universale Result o Attempt/Event autonomi necessari | PRESERVATA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Attempt ed esito non promossi a primitive; memorie eterogenee senza Result universale. |
| K-044 | STABILE | Bundle come contesto, non gate atomico di accettazione | PRESERVATA | Le proposte restano indirizzabili singolarmente e Admission opera su Referent/Assertion, senza Candidate o gate atomico del bundle. |
| K-047 | STABILE | Distinzione necessaria non implica primitiva autonoma | PRESERVATA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Distinzione necessaria non impone primitiva, archivio o componente. |
| K-050 | STABILE | Observation è risultato di osservazione, non pedaggio universale | PRESERVATA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Osservazione della Source distinta da Assertion e non obbligatoria per ogni ingresso. |
| K-052 | STABILE | Proposed qualifica la posizione, non una sostanza universale | PRESERVATA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Proposed è posizione, non Candidate universale. |
| K-054 | STABILE | Supporto qualificato necessario, Evidence-oggetto non dimostrato | PRESERVATA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Supporto qualificato necessario, forma concreta aperta senza Evidence universale. |
| K-055 | STABILE | Assertion non è la forma universale di ogni informazione | PRESERVATA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Informazioni adiacenti, relazioni epistemiche, operative e inferenziali non ridotte ad Assertion. |
| K-056 | STABILE | Essere indirizzabile non basta per essere Referent | PRESERVATA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Locator e risultati indirizzabili distinti dal locus referenziale; il criterio generale indirizzabilità non sufficiente è ricavabile, non formulato. |
| K-058 | STABILE | Value strutturato non implica entità autonoma | PRESERVATA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Necessario contenuto strutturato non referenziale, non primitiva autonoma. |
| K-081 | STABILE | Nessuna primitiva Expectation o controller temporale dimostrati | PRESERVATA | Esclusi Expectation e Temporal Controller universali, scheduler e alert universali. |
| K-088 | STABILE | Stale non è uno stato globale di falsità | PRESERVATA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Non tutto ciò che dipende dal cambiamento è falso; nessun asse globale dello stato. Il nome STALE non è necessario per preservare il confine. |
| K-098 | CANDIDATA | Cinque famiglie di qualità senza score globale obbligatorio | PRESERVATA | Assessment locali e nessuno score globale; numero e confini delle famiglie restano candidati, senza promozione. |
| K-100 | STABILE | Reliability della Source non è una proprietà unica o intrinseca | PARZIALE | [m09] Source, canale, supporto e indipendenza sono separati; provenienza, fedeltà/integrità e competenza relativa alla proposizione non sono enumerate come dimensioni non collassabili. |
| K-105 | STABILE | Provenance, Lineage, storia epistemica e audit operativo distinti | PRESERVATA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Quattro significati distinti, pur potendo percorrere la stessa storia conservata. |
| K-128 | STABILE | Nessun predicato identitario nuovo per ogni stato epistemico | PRESERVATA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Proposizione identitaria con posizioni diverse consente incertezza senza predicato nuovo; non nominato il rifiuto di possibly_same_as. |
| K-130 | STABILE | Descrivere una struttura con un'Assertion non la sostituisce | PRESERVATA | Assertion, supporto, Derivation, Quality e relazioni restano famiglie non sostituibili; una descrizione proposizionale non ne assorbe gli obblighi. |
| K-148 | CANDIDATA | Source e Observation adiacenti alla grammatica dei soggetti | SEMANTICA PRESERVATA; etichetta/stato da correggere | [m14] Definizioni stabili di Source/Observation sono corrette, ma la loro adiacenza alla grammatica è K-148 CANDIDATA mentre entrambe sono etichettate FORTE: promozione terminologica locale. |
| K-149 | STABILE | Quattro forme di informazione negativa e relativi limiti | PRESERVATA | Quattro forme negative distinte; il risultato delimitato non prova assenza nel mondo e un’Assertion richiede il normale supporto/Domain pertinente. |
| K-156 | STABILE | Distinzioni informative necessarie non fissano l'inventario software | PRESERVATA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Memorie/obblighi locali non impongono controllori o archivi separati. |
| K-157 | STABILE | Readiness consente costruzione della candidata, non freeze o implementazione | PRESERVATA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Provvisorietà, non canonizzazione, fuori MVP e necessità di ulteriori test espliciti. |
| K-160 | APERTA | Identità del contenuto proposizionale non ancora determinata universalmente | APERTA, non chiusa | La candidata non assegna una soluzione definitiva né promuove l’apertura a responsabilità/primitiva. |
| K-166 | STABILE | Staging universale sostituito da condizioni del materiale e Work | PRESERVATA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Condizioni tecniche e Work separati da proposte/commitment; nessuno staging universale. |
| K-173 | STABILE | Validazione senza Candidate Validator universale | PRESERVATA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Validazioni locali, confronto e applicabilità, senza validatore universale. |
| K-174 | STABILE | Core Engine famiglia, non autorità aggiuntiva | PRESERVATA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Core Engine solo nome di famiglia, non autorità aggiuntiva. |
| K-182 | CANDIDATA | Inventario dei 24 è checklist candidata, non catalogo obbligatorio | PRESERVATA | Contenuto della baseline invariato nel diff v2→v2.1; controllo semantico conferma: Checklist 24 non è inventario software; capacità locali e responsabilità preservate. Non prova però copertura di ogni guardrail del Ledger. |

### Collassi fondamentali richiesti dal mandato

| Distinzione/guardrail | K-ID principali | Esito |
|---|---|---|
| Source ≠ Evidence/supporto | K-049, K-054, K-100 | **Preservato**, con m09 sulla scomposizione della reliability. |
| Source ≠ Acquisition | K-008, K-041, K-049, K-163 | **Preservato**. |
| Artifact/File ≠ identità documentale | K-028–K-031, K-133 | **Preservato**, con m04 sui confini/segmentazione. |
| Observation ≠ Assertion; estrazione ≠ interpretazione | K-045, K-050, K-057, K-168, K-170 | **Preservato**. |
| Identifier ≠ Referent | K-121–K-126, K-138 | **Preservato**. |
| Evidence/supporto ≠ Assertion | K-054, K-130, K-158–K-159 | **Preservato**. |
| Proposal ≠ Knowledge; Admission ≠ verità | K-003, K-052–K-053, K-115, K-136, K-146 | **Preservato**. |
| Derivation ≠ Observation | K-076, K-150 | **Parziale**: distinzione preservata, ma B06 perde la base specifica dell’aggregazione. |
| Current Reconstruction ≠ ultimo fatto | K-073–K-074 | **Preservato nel nucleo**, con m07 e m12. |
| Attribution ≠ supporto; confirmation ≠ authorization | K-019, K-035–K-039, K-158–K-159 | **Preservato**. |
| Co-reference ≠ merge distruttivo | K-125–K-128 | **Preservato**. |
| Origine comune ≠ corroborazione indipendente | K-021, K-101–K-102, K-152 | **Preservato** dopo Δ05. |
| Risultato negativo ≠ assenza nel mondo | K-034, K-077, K-149 | **Preservato**. |
| Passaggio del tempo ≠ Source | K-079–K-081 | **Preservato** dopo Δ01. |
| Domain rule ≠ Core invariant ≠ meccanismo ≠ Policy | K-090, K-112–K-113 | **Preservato**. |
| Decision ≠ Disposition ≠ Application | K-015–K-018, K-095 | **Preservato**, con m08 sulla conformità procedurale. |
| Descrizione del mondo ≠ giustificazione epistemica ≠ autorizzazione operativa | K-055, K-076, K-113, K-147, K-162 | **Preservato**. |
| Alternative incompatibili ≠ verità congiuntamente ammesse | K-151 | **Non sufficientemente preservato: B07**. |
| Correzione pertinente ≠ ranking globale delle fonti | K-117 | **Non sufficientemente preservato: B04**. |
| Testo nativo ≠ rappresentazione visuale garantita | K-169 | **Non sufficientemente preservato: B08**. |
| Classificazione del contenitore ≠ tipo delle parti interne | K-171 | **Non sufficientemente preservato: B09**. |

Esito guardrail: i collassi portanti introdotti o ripristinati dal delta sono conservati; quattro guardrail stabili ulteriori restano materialmente incompleti e contribuiscono al verdetto negativo. L’apertura K-160 rimane tale.

## D. State integrity audit

| Stato Ledger | Conteggio | Esito |
|---|---:|---|
| STABILE | 146 | Nessuna voce è dichiarata APERTA o rimossa; tuttavia le righe parziali includono nove perdite materiali e undici ambiguità da correggere. |
| CANDIDATA | 15 | Nessuna diventa requisito implementativo o primitiva obbligatoria. K-023 e K-080 restano esplicitamente CANDIDATA. |
| APERTA | 14 | Tutte restano irrisolte; nessuna riceve owner, algoritmo, soglia o forma tecnica per supposizione. |
| SUPERATA | 13 | Nessuna posizione superata riappare come corrente; i successori restano rintracciabili nel Ledger. |

### Discrepanze fra etichette locali e stato genealogico

| K-ID | Ledger | Etichetta locale | Valutazione |
|---|---|---|---|
| K-073 | STABILE | “Ricostruzione contestualizzata — CANDIDATO” | **Indebolimento terminologico**. La definizione sostanziale è fedele, ma la stabilità non è visibile. m12. |
| K-143 | CANDIDATA | “Referent — FORTE” | **Promozione terminologica locale**. Il preambolo dice che FORTE non è autorità canonica, ma il mandato impone comunque di segnalarla. m13. |
| K-148 | CANDIDATA | “Source/Observation — FORTE” insieme alla loro adiacenza alla grammatica | **Promozione terminologica locale** della collocazione candidata; le definizioni K-049/K-050 restano stabili. m14. |

K-004 è l’unica alterazione di assemblaggio non genealogica: CONSULTS resta relazione autonoma. È giustificata perché non modifica il significato operativo e K-004 era già CANDIDATA.

### Aperture e superamenti

Le 14 aperture sono K-026, K-032, K-046, K-065, K-066, K-096, K-118, K-119, K-141, K-142, K-145, K-160, K-183 e K-185. La candidata non le chiude. Le 13 posizioni superate — K-017, K-048, K-051, K-060, K-069, K-072, K-114, K-120, K-135, K-137, K-153, K-154 e K-155 — non vengono reintrodotte.

## E. Internal consistency audit

Non è emersa una coppia di sezioni che imponga direttamente due comportamenti incompatibili. Le regressioni sono omissioni di contratti già acquisiti, non contraddizioni esplicite. Restano però questi punti di pressione:

| Area | Lettura coerente preservata | Incompletezza/ambiguità |
|---|---|---|
| Identità | Referent, Identifier, assegnazione, coreferenza, uso unitario e merge restano distinti; Δ06 preserva la continuità Domain-specifica. | B05 sugli endpoint e B09 sulla classificazione interna. |
| Epistemica | Assertion, contributo, supporto, Quality, Admission e Knowledge non collassano. | B04 e B07; m09/m10 precisano qualità e granularità. |
| Tempo | Content time, storia epistemica, storia operativa e reference time sono separati; late information non retrodata l’acquisizione. | B02/B03; m07 distingue due interrogazioni storiche. |
| Derivazione e impatto | Δ03/Δ04 preservano dipendenze materiali, impatto potenziale, tenuta delle basi, rivalutazione e risultato accertato. | B06 sulle basi dell’aggregazione. |
| Operatività | Work, Attempt, risultato informativo, Decision, Disposition e Application restano distinti; Δ01 non trasforma il tempo in Source. | B01; m01–m06; C01 resta aperta. |
| Trasversali | Autorità, permessi, retention, recovery, versioning, Provenance e audit hanno confini riconoscibili. | m09–m11; F2d non è visibile in O. |

Le sezioni K–P della candidata sono state trattate come affermazioni da verificare. K e L sono coerenti come mappe d’assemblaggio ma non provano la coverage per-K; M conserva R01–R10 ma non enumera tutti i guardrail del Ledger; N dice soltanto che non vi erano gap bloccanti **per la review della candidata**, non per il freeze; P dichiara correttamente che il Gate non era stato eseguito. Il verdetto di questo report prevale su quelle autodichiarazioni senza modificarle.

## F. Reverse traceability audit

Il diff reale snapshot v2→candidata v2.1 è stato segmentato in 31 gruppi omogenei. Le ripetizioni della stessa regola in viste diverse sono una sola unità semantica con tutte le localizzazioni indicate.

| ID | Affermazione nuova/gruppo | Origine | Localizzazione candidata | Esito |
|---|---|---|---|---|
| V-ED01 | Preambolo Draft, baseline, gate non eseguito, no implementation readiness | Adattamento editoriale/versionale | Front matter; introduzione; P | TRACCIATA |
| V-ED02 | Rinomina v2→v2.1 e aggiornamento delle intestazioni | Adattamento editoriale/versionale | B; C; K; M; P | TRACCIATA |
| V-ED03 | Il prossimo passo è il Knowledge Preservation Gate | Adattamento editoriale/versionale | P | TRACCIATA |
| V-Δ01 | Attenzione autonoma promessa; base/finestra/riscontro/comportamento; tempo≠Source; no controller universale | Δ01 | D — Attenzione; F; H10/H19; I; record Δ | TRACCIATA |
| V-Δ02 | Recuperabilità di risultato e basi materialmente usati; materialità controfattuale; no conservazione totale/riesecuzione identica | Δ02 | G; H12/H20; record Δ | TRACCIATA |
| V-Δ03 | Impatto include assenze, scope, completezza, continuità e nuovi membri; dipendenza non trovata≠nessun impatto | Δ03 | G; H13; record Δ | TRACCIATA |
| V-Δ04 | Potenziale coinvolgimento, tenuta basi, rivalutazione e risultato accertato distinti; no STALE | Δ04 | E; H12/H13; record Δ | TRACCIATA |
| V-Δ05 | Indipendenza non stabilita non presunta; indeterminatezza legittima; no enum/controller | Δ05 | C; G; H12; I; record Δ | TRACCIATA |
| V-Δ06 | Continuità non automatica; Domain determina il soggetto; Identifier non decide identità | Δ06 | H8/H10/H12; I; record Δ | TRACCIATA |
| V-Δ07 | Effetto già applicato; scope originario risposte tardive; conferma abilitante≠supporto universale | Δ07 | E; F; H15/H16; I; record Δ | TRACCIATA |
| V-Δ08 | Persona rappresentata≠account/attore≠autorità concreta | Δ08 | C; G; H8/H19/H22; record Δ | TRACCIATA |
| V-Δ09 | Retention/cancellazione riducono verificabilità; recovery di contenuti+legami; no backup/retention illimitata | Δ09 | C; G; H4/H20; record Δ | TRACCIATA |
| V-B01 | K-022/K-023 restano attivi nel Ledger ma fuori dall’anatomia | B01 | O — conoscenze fuori funzione | TRACCIATA |
| V-B02 | K-091 resta attiva nel Ledger ma fuori dal runtime/anatomia | B02 | O — conoscenze fuori funzione | TRACCIATA |
| V-C01 | Applicabilità uniforme Verification/Work/Application non risolta | C01 | E/F/H15/H19; O | TRACCIATA |
| V-C02 | Predizione e successivo riscontro negativo non risolti | C02 | D/I; O | TRACCIATA |
| V-C03 | Uso di commitment impattati non risolto | C03 | E/H12; O | TRACCIATA |
| V-C04 | Visibilità sub-risultati H7 non risolta | C04 | H7; O | TRACCIATA |
| V-C05 | Corpus richiesto/accessibile/esaminato/copertura non risolti | C05 | H17/I; O | TRACCIATA |
| V-C06 | Uso di proposte non ammesse in Reconstruction non risolto | C06 | H12; O | TRACCIATA |
| V-C07 | Ownership Decision/Disposition non-Policy non risolta | C07/D06 | E; H22; O | TRACCIATA |
| V-R01 | Applicabilità non è automaticamente nuova Decision | R01 | M; E/F; record Δ07 | TRACCIATA |
| V-R02 | Nessuna Expectation universale necessaria | R02 | M; D/I; record Δ01 | TRACCIATA |
| V-R03 | Nessun Temporal Controller universale necessario | R03 | M; D/F/H10/H19 | TRACCIATA |
| V-R04 | Nessun asse universale Admission/Usability | R04 | M; D/E/O | TRACCIATA |
| V-R05 | Nessuna scissione obbligatoria di H7 | R05 | M; H7/O | TRACCIATA |
| V-R06 | Nessun controllore centrale dell’auto-supporto | R06 | C/M | TRACCIATA |
| V-R07 | Nessun enum obbligatorio per indipendenza | R07 | C/I/M | TRACCIATA |
| V-R08 | Nessun Candidate universale | R08 | D/I/M | TRACCIATA |
| V-R09 | Risultato intermedio non cambia natura perché usato | R09 | G/H20/M | TRACCIATA |
| V-R10 | H17 è già produttore del risultato negativo | R10 | H17/I/M | TRACCIATA |

Conteggi reverse:

| Classificazione | Conteggio |
|---|---:|
| Derivata da Δ01–Δ09 | 9 |
| Necessaria per B01/B02 | 2 |
| Necessaria per C01–C07 | 7 |
| Necessaria per R01–R10 | 10 |
| Adattamento editoriale/versionale | 3 |
| NON TRACCIATA | 0 |
| **Totale gruppi** | **31** |

**Esito reverse:** superato. Tutte le aggiunte sostanziali sono tracciate; nessuna giustificazione retroattiva è stata inventata. Le nove Δ e le dieci R sono tutte presenti. L’assenza di NON TRACCIATA non compensa le regressioni forward.

## G. Responsibility/contract audit H1–H22

Per ciascuna responsabilità sono stati verificati problema, input, output, risorse, memorie/cooperazioni, limiti decisionali, assorbimenti impropri e owner mancanti.

| H | Responsabilità | Contratto verificato | Gap/limite | Esito |
|---|---|---|---|---|
| H1 | Ricezione tracciata | Input, output, regole di canale, memoria Acquisition, limite semantico e cooperazioni sono espliciti. | Nessun assorbimento improprio; K-163 preserva entrambe le capacità. | ADEGUATA |
| H2 | Validazione tecnica | Diagnosi, condizioni tecniche e limite rispetto alla verità sono espliciti. | m06: il raccordo tra output vuoto, copertura e outcome Work resta poco preciso. | ADEGUATA CON CORREZIONE MINORE |
| H3 | Deduplicazione tecnica | Input tecnici, corrispondenze/riuso e limite rispetto a identità/indipendenza sono espliciti. | Nessun gap di ownership. | ADEGUATA |
| H4 | Preservazione Source | Origine, rappresentazioni, retention, accesso e limite rispetto all’interpretazione sono espliciti. | Δ09 correttamente integrato senza progettare backup. | ADEGUATA |
| H5 | Estrazione/Observation | Source in ingresso, Observation/alternative/parziali in uscita, criteri estrattivi e limiti semantici sono espliciti. | B01 e B08: selezione tra tentativi e divergenza testo nativo/visuale non preservate. | INADEGUATA PER IL FREEZE |
| H6 | Mapping | Applicabilità, ruoli proposti, ambiguità, dipendenze e limite rispetto ad Admission sono espliciti. | B09: manca il divieto di trasferire il tipo del contenitore alle porzioni. | INADEGUATA PER IL FREEZE |
| H7 | Interpretation | Input eterogenei, proposte/alternative/supporti, risorse e limiti sono riconoscibili. | m01/m05 sul contratto di sufficienza; C04 resta aperta; B07 coinvolge il passaggio verso H16. | ADEGUATA SOLO DOPO CORREZIONI |
| H8 | Identity Reconciliation | Identificatori, attributi, alternative, indizi contrari, Quality e non distruttività sono espliciti. | Δ05/Δ06/Δ08 preservati; nessun algoritmo o decisione automatica introdotti. | ADEGUATA |
| H9 | Comparison | Comparabilità, relazioni di correzione e limite rispetto alla scelta operativa sono espliciti. | B04: manca il guardrail contro ranking/recenza/numero come surrogato della rettifica pertinente. | INADEGUATA PER IL FREEZE |
| H10 | Temporal Evaluation | Tempi, reference time, confronti e limite rispetto ad attivazione/Source sono espliciti. | B02/B03: precisione ignota e periodicità differenti non sono preservate. | INADEGUATA PER IL FREEZE |
| H11 | Derivation | Premesse, metodo, condizioni, conclusione, giustificazione e limite inferenza/Policy sono espliciti. | B06: contratto specifico delle aggregazioni non preservato. | INADEGUATA PER IL FREEZE |
| H12 | Current Reconstruction | Tempo, scopo, Knowledge, conflitti, impatti, alternative e limiti d’uso sono espliciti. | m07 e m12; C03/C06 restano correttamente aperte. | ADEGUATA CON CORREZIONI MINORI |
| H13 | Impact Assessment | Δ03/Δ04 rendono espliciti target, presupposti, quattro livelli ed indeterminatezza. | Nessun STALE globale o ricomputazione automatica. | ADEGUATA |
| H14 | Policy Evaluation | Scelta fra comportamenti, autorità, Decision/Disposition e limiti rispetto a semantica/Quality sono espliciti. | Non assorbe Domain, Core Engine o i percorsi non-Policy. | ADEGUATA |
| H15 | Verification | Domanda, target, attore, contributo/esito, Work e limiti rispetto a conferma/Admission sono espliciti. | C01 e C07 restano aperture note, non gap risolti per supposizione. | ADEGUATA CON CONTRATTO APERTO NOTO |
| H16 | Admission | Proposte, Disposition, condizioni correnti, effetto già applicato, commitment/storia e mancata applicazione sono espliciti. | B07: manca il divieto espresso sull’ammissione congiunta di alternative incompatibili. | INADEGUATA PER IL FREEZE |
| H17 | Query/Retrieval | Corpus, scope, tempo, autorizzazioni, output negativo delimitato e limiti inferenziali sono espliciti. | m06; C05 resta correttamente aperta. K-077 è ora preservata. | ADEGUATA CON CORREZIONE MINORE/APERTURA NOTA |
| H18 | Projection | Riceve risultati semanticamente determinati e non crea semantica, certezza o identità. | Dipende dal recupero B06 in H11, ma non ne usurpa la responsabilità. | ADEGUATA |
| H19 | Application Functions | Richiesta/Disposition, contesto, risultato/azione, autorizzazioni e limiti semantici sono espliciti. | C01 resta aperta; Δ01 e Δ08 sono correttamente confinati. | ADEGUATA CON CONTRATTO APERTO NOTO |
| H20 | Explanation | Risultato, supporti, Lineage, Decision, limiti e recuperabilità materiale sono espliciti. | Δ02/Δ09 preservati; non inventa tracce. | ADEGUATA |
| H21 | Presentation | Projection/Explanation in ingresso e vincolo di non alterare significato/certezza sono espliciti. | Nessun assorbimento di semantica o governance. | ADEGUATA |
| H22 | User Contribution Intake | Base ricevuta, autore, target, tempo, contesto, natura dell’atto e instradamento sono espliciti. | C07 resta aperta; Intake non viene promosso a decisore. | ADEGUATA CON CONTRATTO APERTO NOTO |

Riepilogo H:

| Esito | Numero |
|---|---:|
| ADEGUATA | 10 |
| ADEGUATA CON CORREZIONE MINORE | 2 |
| ADEGUATA CON CONTRATTO APERTO NOTO | 3 |
| ADEGUATA CON CORREZIONE MINORE/APERTURA NOTA | 1 |
| ADEGUATA SOLO DOPO CORREZIONI | 1 |
| INADEGUATA PER IL FREEZE | 5 |
| **Totale** | **22** |

Non deriva automaticamente la necessità di una H23: i gap sono formulazioni/contratti nelle responsabilità esistenti o aperture già note.

## H. Open-issue integrity

| Apertura | È ancora aperta? | Soluzione implicita introdotta? | Vincolo stabile distinguibile | Falsificabile dal test successivo? |
|---|---|---|---|---|
| C01 — applicabilità uniforme Verification/Work/Application | Sì | No. H16 è preciso, H15/H19 no. | Applicabilità ≠ nuova Decision; effetto già applicato e scope originario restano acquisiti. | Sì: risposta tardiva o Work ripreso dopo mutamento del contesto. |
| C02 — base predittiva vs riscontro negativo | Sì | No. Non è imposto conflitto, Assertion ammessa o assenza nel mondo. | Base, finestra, riscontro e comportamento distinti; H17 produce il negativo delimitato. | Sì: attesa domestica con mancato reperimento delimitato. |
| C03 — uso di contenuti ammessi ma impattati | Sì | No. Nessuna policy universale di esclusione/inclusione. | Impatto determinato non occultabile; livelli Δ04 distinti. | Sì: funzioni con scopi diversi sullo stesso commitment impattato. |
| C04 — visibilità esiti parziali H7 | Sì | No. H7 non è scissa e gli esiti sono rappresentabili. | K-010/K-053 consentono alternative e dipendenze; B01 riguarda invece la conservazione stabile fra tentativi H5. | Sì: Interpretation con sub-risultati divergenti. |
| C05 — corpus richiesto/accessibile/esaminato/copertura | Sì | No. H17 non sceglie una struttura concreta. | Risultato negativo delimitato e distinzione non trovato/non avvenuto sono stabili. | Sì: autorizzazioni e coperture differenti sullo stesso quesito. |
| C06 — uso di proposte non ammesse in Reconstruction | Sì | No. H12 rinvia ai criteri d’uso. | Conservazione/presentazione ≠ Admission; Knowledge resta corpo governato. | Sì: ricostruzioni che includono/escludono proposte qualificate. |
| C07/D06 — ownership Decision/Disposition non-Policy | Sì | No. Nessun Decision Manager e nessuna promozione di Intake/Verification/Function. | Autorità, target, scope, contesto, Decision, Disposition e Application restano obbligatori. | Sì: scelta deliberata autorizzata che non deriva da Policy. |
| F2d — produttore del cambiamento di versione | Sì | No. Il diagramma mostra il cambiamento, non chi lo rende disponibile. | K-090 distingue effetti delle risorse; K-006 lascia candidati eventi/comunicazioni; K-096 resta aperta. | Sì: modifica di Mapping/Domain/Policy durante un Work. |

**Integrità delle aperture:** 8/8 confermate, nessuna chiusa implicitamente. F2d è però assente dall’elenco O della candidata: m15 richiede solo di renderla visibile, non di risolverla.

## I. Findings

### REGRESSIONI BLOCCANTI

Sono nove. Ognuna riguarda una conoscenza STABILE già nel Ledger; nessuna è una nuova teoria o un’apertura da risolvere con un componente.

Sono regressioni rispetto alla conoscenza acquisita, non nuove regressioni causate dai nove delta: erano già compressioni della v2 che l’assemblaggio v2.1 ha ereditato senza assegnare loro una destinazione fedele o intenzionalmente esterna.

| ID | K-ID | Localizzazione | Perdita materiale | Modifica minima proposta, non applicata |
|---|---|---|---|---|
| B01 | K-043 | H5; F — Esecuzione/Rivalutazione; G | La candidata ammette risultati parziali, ma non conserva il vincolo di selezione: un risultato utile del tentativo interrotto sopravvive e il successo del retry non rende preferibili in blocco tutte le letture del secondo tentativo. | Aggiungere una sola regola nel contratto H5/F che preservi output parziali per tentativo e vieti la selezione wholesale del retry. |
| B02 | K-068 | H10; I — Tempo | Ruoli temporali e divieto di migrazione sono presenti, ma scompaiono precisione, incertezza, anno ignoto e divieto di riempire il tempo mancante con una data disponibile. | Precisare in I/H10 che tempo ignoto o impreciso resta tale e che il confronto è ammesso solo quando ruolo, precisione e contesto lo consentono. |
| B03 | K-078 | D — Attenzione temporale; H10/H11; I — modalità | La v2.1 distingue predizione, normatività e riscontro, ma non periodicità di emissione, periodo fatturato e caricamento; una cadenza osservata può quindi essere promossa impropriamente a previsione o obbligo. | Reintrodurre la distinzione delle tre periodicità e delle diverse basi/forze di previsione, dichiarazione, obbligo e raccomandazione. |
| B04 | K-117 | E — Correzione; H9/H12 | La relazione di rettifica è modellata, ma manca il divieto di sostituirne la pertinenza con quantità, recenza o autorità globale delle fonti. | Aggiungere al confine di Comparison/Correction che la prevalenza richiede la relazione pertinente al bersaglio; ranking generico, numero e recenza da soli non bastano. |
| B05 | K-132 | I — Referent/Value; J — grammatica | La grammatica distingue Value e Referent, ma non esplicita le tre famiglie di endpoint. Un implementatore può ancora collassare relazione fra soggetti, valore predicato e qualificazione epistemica. | Aggiungere una frase/tabella che distingua Referent→Referent, Referent→Value e qualificazioni della proposizione completa, senza imporre una struttura tecnica Relation. |
| B06 | K-150 | G — Lineage; H11/H18 | La somma/aggregazione è riconducibile a Derivation, ma la candidata non obbliga a conservare membri inclusi, criteri d’inclusione, periodo e metodo. | Integrare il contratto di H11/G per le aggregazioni con questi quattro elementi; H18 deve soltanto proiettarne il risultato. |
| B07 | K-151 | D — alternative; H7/H9/H16 | Alternative e incompatibilità sono rappresentabili, ma manca il guardrail che impedisce l’ammissione congiunta di ipotesi mutuamente esclusive; restringere alternative potrebbe essere contato come nuovo supporto. | Aggiungere il divieto nel confine H7/H9/H16, preservando alternative, contesto e supporti senza un nuovo Candidate universale. |
| B08 | K-169 | H5; I — Documenti | Testo nativo e OCR sono separati, ma manca il fatto acquisito che il testo incorporato possa divergere dalla rappresentazione visuale. | Aggiungere a H5 il guardrail sulla possibile divergenza visuale e mantenere entrambe le letture con provenienza/qualità proprie. |
| B09 | K-171 | H6/H7; I — Documenti | La classificazione è contestuale e una Source può contenere più documenti, ma non è vietato trasferire automaticamente il tipo del contenitore alle porzioni interne. | Precisare nel contratto H6/H7 che la classificazione del contenitore propone contesto/Mapping e non ammette automaticamente il tipo dei documenti o delle porzioni interne. |

Nota di confine:

- B01 non chiude C04: preserva una regola già stabile sui tentativi; C04 resta aperta sulla visibilità interna di H7.
- B03 non chiude C02: ripristina distinzioni temporali già stabili; il rapporto predizione–riscontro resta aperto.
- B09 non chiude K-142: vieta un trasferimento automatico già respinto; criteri documentali specifici e vocabolario restano aperti.

### CORREZIONI MINORI NECESSARIE

Sono quindici: undici contratti semantici, tre discrepanze di stato locale e la visibilità di F2d.

| ID | K-ID/tema | Localizzazione | Modifica minima proposta, non applicata |
|---|---|---|---|
| m01 | K-002 | J; F | Esplicitare risultato/condizione richiesto e tratto abilitato; la conclusione del produttore non garantisce la sufficienza per il consumatore. |
| m02 | K-006 | J; D/F | Mantenere distinguibili EMITS, REACTS_TO e CONSTRAINED_BY pur lasciando candidata la scelta degli eventi/comunicazioni. |
| m03 | K-013 | F — Rivalutazione | Esplicitare il confine retry su stessi presupposti / nuova valutazione su presupposti materialmente mutati e non riscrivere l’esito storico. |
| m04 | K-031 | I — locator; H5/H7 | Dichiarare che porzioni sovrapposte/incomplete non richiedono segmentazione preventiva completa né provano ordine/completezza. |
| m05 | K-042 | H5/H7; F | Rendere esplicito che il produttore dichiara disponibilità/limiti, il consumatore giudica sufficienza per il risultato richiesto e Work conserva il seguito. |
| m06 | K-063 | H2; F; H17 | Qualificare l’output vuoto con esito, copertura e tentativo invece di lasciarlo deducibile dal solo insieme dei risultati. |
| m07 | K-074 | G — storie; H12; I — Tempo | Nominare le due domande storiche: ciò che Fold sosteneva allora e ciò che oggi ricostruisce di allora. |
| m08 | K-095 | E/F/G | Esplicitare che conformità procedurale dell’atto e correttezza fattuale sono valutazioni indipendenti. |
| m09 | K-100 | H1/H2; I — Quality/Supporto | Elencare come dimensioni distinte provenienza, fedeltà/integrità, competenza relativa, indipendenza e corroborazione; nessuna reliability intrinseca della Source. |
| m10 | K-107 | G; H15/H20; I/J | Formulare il criterio della minima unità sulla quale conferma, correzione, contestazione o derivazione producono effetti differenti. |
| m11 | K-181 | F/G — storie; trasversali | Esplicitare che audit delle azioni e osservabilità/metriche del funzionamento hanno scopi diversi e non sostituiscono Provenance o storia epistemica. |
| m12 | K-073 | I — Elementi e famiglie | Correggere la sola etichetta locale della Reconstruction: K-073 è STABILE, non CANDIDATA. |
| m13 | K-143 | I — Elementi e famiglie | Non presentare come FORTE la definizione di Referent K-143, che nel Ledger resta CANDIDATA; il contenuto può restare invariato. |
| m14 | K-148 | I — Elementi e famiglie | Distinguere le definizioni stabili di Source/Observation dalla loro collocazione adiacente al Core, che K-148 mantiene CANDIDATA. |
| m15 | F2d (K-006/K-090/K-096) | D — cambiamento di risorsa; O | Rendere visibile fra le aperture che non è ancora assegnato chi rende disponibile un cambiamento di versione. Non adottare la proposta di produttore emersa nello stress. |

### APERTI GIÀ NOTI

C01–C07 e F2d restano aperti; inoltre restano aperte le 14 K-ID del Ledger elencate in D. Nessuno di questi aperti viene usato per mascherare una regressione stabile.

### SCELTE DI ASSEMBLAGGIO GIUSTIFICATE

1. K-004: CONSULTS autonoma invece della sola READS qualificata. ALTERATA, ma senza regressione semantica dimostrata.
2. K-022/K-023: lifecycle, calcolo, effetti e test di parallelizzabilità restano Ledger-only (B01).
3. K-091: governance fondazionale dei Core invariants resta Ledger-only (B02).
4. I raggruppamenti H1–H22 restano organizzativi: non introducono componenti software, controller o nuove primitive.
5. Le ripetizioni dei delta nelle diverse viste sono rafforzamenti editoriali tracciati, non nuove decisioni.

### NUOVE QUESTIONI

**Nessuna.** I nove blocker e le quindici correzioni minori sono tutti riconducibili al Ledger o al delta. Non vengono creati K-ID.

## J. Verdict

# KNOWLEDGE PRESERVATION GATE NON SUPERATO

La candidata v2.1 non è ancora congelabile come baseline per i test. Il reverse audit è pulito, Δ01–Δ09 sono tracciati, R01–R10 restano respinti, le aperture note sono integre e nessuna nuova responsabilità/primitiva è stata introdotta. Tuttavia nove conoscenze STABILI restano materialmente indebolite e quindici formulazioni richiedono correzioni minori.

Il verdetto non autorizza modifiche automatiche. La candidata, il Ledger, il delta, lo snapshot, le Coverage Map, Linear e Notion restano invariati. Le correzioni proposte sono diagnostiche e devono essere revisionate prima di qualsiasi applicazione.
