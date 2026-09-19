<p align="center"><img src="./assets/hero.svg" width="100%" alt="DealFeed"/></p>

<p align="center">
  <img src="https://img.shields.io/badge/React_Native-61DAFB?style=flat-square&logo=react&logoColor=000"/>
  <img src="https://img.shields.io/badge/Expo-000020?style=flat-square&logo=expo&logoColor=white"/>
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white"/>
  <img src="https://img.shields.io/badge/Supabase-3FCF8E?style=flat-square&logo=supabase&logoColor=white"/>
  <img src="https://img.shields.io/badge/PostHog-EA580C?style=flat-square&logo=posthog&logoColor=white"/>
</p>

# DealFeed

A mobile product I built around a deliberately simple loop: **swipe deals, save what matters, open the merchant**.

No catalogue ceremony.

<p align="center"><img src="./assets/product-mockup.svg" width="100%" alt="DealFeed mobile mockups"/></p>

## <code>01 / product_surface</code>

<p align="center"><img src="./assets/features.svg" width="100%" alt="DealFeed features"/></p>

## <code>02 / core_model</code>

<p align="center"><img src="./assets/core-model.svg" width="100%" alt="Mobile loop model"/></p>

## <code>03 / architecture</code>

<p align="center"><img src="./assets/architecture-visual.svg" width="100%" alt="DealFeed architecture"/></p>

<p align="center"><img src="./assets/overview.svg" width="100%" alt="DealFeed system overview"/></p>

## <code>04 / shopping_loop</code>

<p align="center"><img src="./assets/flow-visual.svg" width="100%" alt="DealFeed product loop"/></p>

## <code>05 / decisions</code>

| Decision | Why |
|---|---|
| React Native + Expo | one mobile codebase, fast iteration |
| Zustand | enough state without framework ceremony |
| anonymous auth | value before signup |
| PostgreSQL RLS | user-owned isolation near storage |
| edge redirect | auditable click trail |
| explicit consent | analytics and ads are separate decisions |

**Keep the phone stupid:** clean, filter and dedupe the feed before it reaches the client.

## <code>06 / engineering_signature</code>

<p align="center">
  <img src="./assets/engineering-signature.svg" width="100%" alt="Engineering signature"/>
</p>

## <code>07 / inspect</code>

- [Architecture](docs/ARCHITECTURE.md)
- [Privacy model](docs/PRIVACY.md)
- [Sanitised ingestion logic](examples/ingest-products.ts)

<details><summary><b>Private source boundary</b></summary>

Provider configuration, store credentials and the full mobile implementation remain private.

</details>
