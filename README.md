<p align="center"><img src="./assets/hero.svg" width="100%" alt="DealFeed"/></p>

<p align="center">
  <img src="https://img.shields.io/badge/React_Native-61DAFB?style=flat-square&logo=react&logoColor=000"/>
  <img src="https://img.shields.io/badge/Expo-000020?style=flat-square&logo=expo&logoColor=white"/>
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white"/>
  <img src="https://img.shields.io/badge/Supabase-3FCF8E?style=flat-square&logo=supabase&logoColor=white"/>
  <img src="https://img.shields.io/badge/PostHog-EA580C?style=flat-square&logo=posthog&logoColor=white"/>
</p>

# DealFeed

A mobile product I built around a deliberately simple idea: **shopping deals should feel like a feed, not a catalogue**.

Swipe. Save. Open. Move on.

<p align="center">
  <img src="./assets/overview.svg" width="100%" alt="System overview"/>
</p>

## <code>01 / product_loop</code>

~~~text
open app
   ↓
swipe deals
   ↓
save / skip
   ↓
tap "get it"
   ↓
validated affiliate redirect
   ↓
merchant
~~~

<table>
<tr>
<td width="33%" valign="top">

### Feed

React Native / Expo, vertical paging, local state and low-friction anonymous sessions.

</td>
<td width="33%" valign="top">

### Backend

Supabase/PostgreSQL, RLS, Edge Functions and scheduled product ingestion.

</td>
<td width="33%" valign="top">

### Measurement

Server-side click trail + privacy-aware client analytics and ad consent.

</td>
</tr>
</table>

## <code>02 / architecture</code>

~~~mermaid
flowchart LR
    APP[React Native app]
    AUTH[Anonymous auth]
    PG[(Postgres + RLS)]
    EDGE[Edge Functions]
    INGEST[Ingestion]
    GO[Redirect]
    DEL[Deletion]
    PH[PostHog EU]
    AFF[Affiliate source / merchant]

    APP --> AUTH
    APP --> PG
    APP --> EDGE
    APP --> PH

    EDGE --> INGEST
    EDGE --> GO
    EDGE --> DEL
    INGEST --> AFF
    INGEST --> PG
    GO --> PG
    GO --> AFF
~~~

## <code>03 / decisions_i_made</code>

| Decision | Why |
|---|---|
| React Native + Expo | one mobile codebase, fast iteration |
| Zustand | enough state without framework ceremony |
| FlashList | smoother media-heavy feed |
| Anonymous auth | no signup wall before value |
| PostgreSQL RLS | user-owned data isolation close to storage |
| Edge redirect | auditable click trail even if client analytics fails |
| allow-listed target domains | redirect safety |
| explicit consent | analytics / ads are separate decisions |

## <code>04 / ingestion_pipeline</code>

~~~text
provider feed
  → normalise
  → quality filters
  → dedupe
  → batch upsert
  → active feed
~~~

The point is to keep the client stupid: ingestion cleans the stream before the phone ever sees it.

## <code>05 / privacy_is_a_flow</code>

Deletion is not “put a button in settings”.

It crosses:

- application profile;
- saved items;
- server-side event identity;
- analytics identity;
- local session state.

That is why it is implemented as a system flow.

## <code>06 / technical_proof</code>

- [Architecture](docs/ARCHITECTURE.md)
- [Privacy model](docs/PRIVACY.md)
- [Sanitised ingestion logic](examples/ingest-products.ts)

<details>
<summary><b>Private source boundary</b></summary>

Provider configuration, store credentials and the full mobile implementation stay private.

</details>
