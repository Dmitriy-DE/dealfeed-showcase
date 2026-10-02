<p align="center"><img src="./assets/hero.svg" width="100%" alt="DealFeed traffic broker"/></p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Telethon-2AABEE?style=flat-square&logo=telegram&logoColor=white"/>
  <img src="https://img.shields.io/badge/aiogram-2AABEE?style=flat-square&logo=telegram&logoColor=white"/>
  <img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white"/>
  <img src="https://img.shields.io/badge/Cloudflare-Worker%20%2B%20D1-F38020?style=flat-square&logo=cloudflare&logoColor=white"/>
</p>

# DealFeed

A private **deal desk + traffic tracker** built for an operator brokering traffic between advertisers and publishers.

The product is split into two independent contours:

- **Deal desk** — local Python/SQLite pipeline for Telegram collection, parsing, matching, operator outreach and deal management.
- **Edge tracker** — always-on Cloudflare Worker + D1 for redirects, clicks, postbacks, conversions, partner stats and margin accounting.

> **Automate discovery. Keep the operator in control.**

## <code>01 / actual_surfaces</code>

<p align="center"><img src="./assets/actual-surfaces.svg" width="100%" alt="DealFeed product surfaces"/></p>

The private bot is the main operator interface. It surfaces fresh high-quality matches, creates deals, stores terms, provisions tracking links and exposes tracker statistics without turning the workflow into a fully automatic black box.

## <code>02 / core_modules</code>

<p align="center"><img src="./assets/features.svg" width="100%" alt="DealFeed modules"/></p>

The original showcase described a consumer deal app; that was the wrong product. The actual system covers source intake, structured opportunity parsing, matching, assisted outreach, deal lifecycle, edge tracking, postbacks, grouped offer inventory, controlled distribution and broker analytics.

## <code>03 / core_model</code>

<p align="center"><img src="./assets/core-model.svg" width="100%" alt="DealFeed core model"/></p>

Raw Telegram messages are kept verbatim as audit evidence. Derived opportunities and matches point back to that source. The parser does not fabricate absent values: missing GEO, payout or other fields remain missing with appropriately low confidence.

## <code>04 / operator_controls</code>

<p align="center"><img src="./assets/overview.svg" width="100%" alt="DealFeed operator controls"/></p>

Backfill is stored without notification spam. Match notifications use quality thresholds. Outreach is assisted by default with limits/cooldowns. Distribution requires preview/edit and explicit approval to allowlisted channels.

## <code>05 / system</code>

<p align="center"><img src="./assets/architecture-visual.svg" width="100%" alt="DealFeed architecture"/></p>

The edge tracker stays online independently of the local deal desk. That separation keeps click/postback accounting available even when the collector/operator machine is offline.

## <code>06 / automation_flow</code>

<p align="center"><img src="./assets/flow-visual.svg" width="100%" alt="DealFeed end-to-end flow"/></p>

## <code>07 / engineering_signature</code>

<p align="center"><img src="./assets/engineering-signature.svg" width="100%" alt="DealFeed engineering signature"/></p>

## <code>08 / inspect</code>

- [Architecture](docs/ARCHITECTURE.md)
- [Operational safety](docs/OPERATIONS.md)
- [Sanitised matching example](examples/match-engine.py)

<details>
<summary><b>Public / private boundary</b></summary>

Source chats, accounts, credentials, tracking secrets, commercial terms, private contacts and production provider configuration remain private. The showcase publishes the architecture and engineering model, not operational access.

</details>