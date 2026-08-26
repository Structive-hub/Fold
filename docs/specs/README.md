# Specs

**Status:** Canonical  
**Scope:** formato e ruolo delle specifiche implementabili

Questa cartella contiene le specifiche di funzioni o componenti abbastanza mature da guidare direttamente l'implementazione.

Una specifica non deve raccontare tutta la storia progettuale. Deve trasferire a Codex soltanto il contesto necessario per costruire e verificare correttamente il risultato.

## Contenuto minimo consigliato

```text
# Nome della funzione

Status: Canonical

## Obiettivo
Che risultato deve esistere alla fine.

## Perché serve
Solo il contesto che influenza il comportamento.

## Comportamento atteso
Cosa deve succedere.

## Dati e concetti coinvolti
Riferimenti ai documenti canonici pertinenti.

## Casi limite / errori
Situazioni che la funzione deve gestire.

## Fuori scope
Cosa non stiamo costruendo in questa task.

## Criteri di accettazione
Condizioni osservabili che permettono di dire “finito”.

## Decisioni collegate
Link alle decisioni rilevanti in `docs/decisions/`.
```

## Readiness

Una specifica entra qui come `Canonical` solo quando il comportamento necessario all'implementazione è stato deciso e i criteri di accettazione sono verificabili.

Se restano domande che possono cambiare sostanzialmente il comportamento della funzione, la specifica deve restare `Draft` e non va usata come mandato di implementazione.