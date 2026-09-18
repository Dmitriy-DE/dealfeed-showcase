<p align="center">
  <img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=190&color=0:0D1117,45:E1306C,100:FF9F1C&text=DealFeed&fontSize=42&fontColor=FFFFFF&fontAlignY=38&desc=Swipeable%20shopping%20feed%20for%20EU%20deals&descSize=16&descAlignY=60" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/React_Native-61DAFB?style=for-the-badge&logo=react&logoColor=000" />
  <img src="https://img.shields.io/badge/Expo-000020?style=for-the-badge&logo=expo&logoColor=white" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" />
  <img src="https://img.shields.io/badge/Supabase-3FCF8E?style=for-the-badge&logo=supabase&logoColor=white" />
  <img src="https://img.shields.io/badge/PostHog-000000?style=for-the-badge&logo=posthog&logoColor=white" />
</p>

# DealFeed — mobile product engineering showcase

A TikTok-style vertical feed for shopping deals: swipe, save, open the merchant, keep the product experience fast and keep analytics/consent explicit.

The implementation repository is private. This showcase documents the architecture and core engineering decisions.

## Architecture

```mermaid
flowchart TB
    APP[React Native / Expo]
    AUTH[Anonymous Supabase Auth]
    PG[(PostgreSQL + RLS)]
    EDGE[Supabase Edge Functions]
    INGEST[Affiliate ingestion]
    REDIRECT[Validated redirect]
    DELETE[GDPR deletion]
    ANALYTICS[PostHog EU]
    ADS[AdMob]
    AFF[Affiliate providers]

    APP --> AUTH
    APP --> PG
    APP --> EDGE
    APP --> ANALYTICS
    APP --> ADS

    EDGE --> INGEST
    EDGE --> REDIRECT
    EDGE --> DELETE
    INGEST --> AFF
    INGEST --> PG
    REDIRECT --> PG
    REDIRECT --> AFF
```

## Product / engineering decisions

- React Native + Expo for a single iOS/Android codebase.
- TypeScript throughout the app.
- Zustand for lightweight persisted client state.
- FlashList for media-heavy vertical feed rendering.
- Supabase anonymous auth to minimise signup friction.
- PostgreSQL RLS to keep user-owned state isolated.
- Edge Functions for ingestion, redirect tracking and deletion flows.
- Server-side affiliate redirect allow-listing.
- Daily product ingestion with quality filters + deduplication.
- Explicit analytics and advertising consent.
- GDPR data deletion across application state and analytics identity.

## Data flow

```text
affiliate source
      ↓
scheduled ingestion
      ↓
quality filter + dedupe
      ↓
PostgreSQL
      ↓
mobile feed
      ↓
validated /go redirect
      ↓
merchant
```

## Privacy by design

The project treats consent and deletion as system behaviour rather than a settings-page afterthought.

- Analytics can remain disabled until consent.
- Advertising consent is tracked separately.
- Saved user data is scoped by RLS.
- Deletion removes owned state and de-identifies retained aggregate events.

## Repository map

- [Architecture](docs/ARCHITECTURE.md)
- [Privacy model](docs/PRIVACY.md)
- [Sanitised ingestion example](examples/ingest-products.ts)

## Source availability

Full app source, provider configuration and store credentials remain private.
