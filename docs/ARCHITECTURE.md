# Architecture

## Main flows

### Feed

```mermaid
sequenceDiagram
    participant A as App
    participant S as Supabase
    participant D as PostgreSQL

    A->>S: anonymous session
    A->>S: request feed page
    S->>D: RLS-aware query
    D-->>S: active products
    S-->>A: feed page
```

### Product ingestion

```text
scheduled trigger
  -> fetch provider feed
  -> normalise
  -> quality filter
  -> dedupe
  -> batch upsert
  -> structured result
```

### Click-out

The client opens a server-controlled redirect endpoint. The edge function validates the product, verifies the target domain against an allow-list, records the click event and returns a redirect.

This preserves an auditable server-side click trail even if client analytics fails.
