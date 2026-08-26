# Decisions

**Status:** Canonical  
**Scope:** formato e ruolo delle decisioni

Questa cartella conserva le decisioni progettuali o architetturali che devono restare comprensibili anche mesi dopo, senza dipendere dalla conversazione in cui sono nate.

## Quando creare una decisione

Creare un documento quando una scelta:

- influenza più funzioni o parti del sistema;
- esclude un'alternativa plausibile;
- introduce un vincolo che Codex deve rispettare;
- rischierebbe altrimenti di essere reinterpretata in futuro;
- sostituisce una decisione precedente.

Non creare una decisione per ogni dettaglio minore di implementazione.

## Formato consigliato

Nome file:

```text
NNNN-titolo-breve.md
```

Contenuto minimo:

```text
# Titolo

Status: Canonical
Date: YYYY-MM-DD
Supersedes: [se applicabile]

## Contesto
Perché la decisione era necessaria.

## Decisione
Che cosa è stato scelto.

## Motivazione
Perché questa scelta è preferita alle alternative rilevanti.

## Conseguenze
Che cosa permette, impedisce o richiede da questo momento.
```

Una nuova decisione non deve cancellare la storia: quando sostituisce una scelta precedente, dichiararlo esplicitamente.