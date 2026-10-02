<p align="center"><img src="./assets/hero.svg" width="100%" alt="DealFeed"/></p>

> **A private traffic-broker deal desk plus an always-on tracking edge.**  
> Telegram source posts become structured opportunities, candidate matches, operator-approved deals and measurable click/conversion flows.

<table>
<tr>
<td align="center"><b>Telethon</b><br/><sub>read-only source intake</sub></td>
<td align="center"><b>aiogram</b><br/><sub>private operator bot</sub></td>
<td align="center"><b>SQLite</b><br/><sub>deal-desk state</sub></td>
<td align="center"><b>Cloudflare Worker</b><br/><sub>edge tracker</sub></td>
<td align="center"><b>D1</b><br/><sub>tracking / inventory state</sub></td>
<td align="center"><b>Human-in-the-loop</b><br/><sub>commercial control</sub></td>
</tr>
</table>

## What the system actually does

<p align="center"><img src="./assets/actual-surfaces.svg" width="100%" alt="DealFeed surfaces"/></p>

<table>
<tr>
<td width="33%" valign="top"><b>Collect</b><br/><sub>Read configured Telegram chats through a collector account and store source messages verbatim.</sub></td>
<td width="33%" valign="top"><b>Understand</b><br/><sub>Extract BUY/SELL traffic or offer intent, GEO, traffic source and payout when the message actually contains them.</sub></td>
<td width="33%" valign="top"><b>Match</b><br/><sub>Apply hard filters first, then a relevance score. Only fresh/high-quality candidates should alert the operator.</sub></td>
</tr>
<tr>
<td valign="top"><b>Operate</b><br/><sub>The private bot lets the operator review matches, contact sides, set terms, activate/close deals and provision tracking.</sub></td>
<td valign="top"><b>Track</b><br/><sub>Broker-controlled links record clicks and redirect traffic to the advertiser with a click ID.</sub></td>
<td valign="top"><b>Measure</b><br/><sub>Advertiser postbacks become idempotent conversions; the tracker can calculate advertiser payout, publisher payout and broker margin.</sub></td>
</tr>
</table>

## Core objects

<p align="center"><img src="./assets/readme-broker-objects.svg" width="100%" alt="DealFeed core objects"/></p>

> **Parser rule:** if the source message does not provide GEO, payout, traffic source or another field, the parser leaves it missing instead of inventing a value.

## Why there are two systems

<p align="center"><img src="./assets/readme-two-contours.svg" width="100%" alt="Deal desk and edge tracker"/></p>

<table>
<tr>
<td width="50%" valign="top"><b>Deal desk = decision workflow.</b><br/><sub>It can be offline when the operator is not collecting sources or reviewing matches.</sub></td>
<td width="50%" valign="top"><b>Edge tracker = accounting path.</b><br/><sub>It stays online independently so redirect, click, postback and partner-stat flows do not depend on the operator machine.</sub></td>
</tr>
</table>

## Operator controls

<table>
<tr>
<td width="33%" valign="top"><b>Backfill stays quiet</b><br/><sub>Historical messages can be stored and searched without generating a storm of “fresh match” notifications.</sub></td>
<td width="33%" valign="top"><b>Outreach is assisted</b><br/><sub>Messages can be prepared/queued with rate limits, cooldowns and FloodWait handling instead of uncontrolled auto-spam.</sub></td>
<td width="33%" valign="top"><b>Distribution requires approval</b><br/><sub>Offer-inventory text is previewed/edited and explicitly approved before allowlisted distribution jobs are sent.</sub></td>
</tr>
</table>

## Offer inventory / distribution

<p align="center"><img src="./assets/overview.svg" width="100%" alt="DealFeed operator controls"/></p>

- Advertiser-side signals are also stored as raw offer-inventory evidence.
- Repeated commercial signals can be grouped into one actionable owner card.
- The representative source and raw-post count remain visible.
- Advertiser payout stays private.
- Public outbound text is stored exactly as approved.
- Distribution is disabled by default until capability/allowlist checks pass.

## Architecture

<p align="center"><img src="./assets/architecture-visual.svg" width="100%" alt="DealFeed architecture"/></p>

## End-to-end flow

<p align="center"><img src="./assets/flow-visual.svg" width="100%" alt="DealFeed flow"/></p>

<details>
<summary><b>Operational notes</b></summary>

- Deal desk: Python + SQLite, one event loop, Telethon collector + aiogram operator bot.
- Edge tracker: Cloudflare Worker + D1, independent from the local deal desk.
- Partner cabinet shows partner-owned links/clicks/conversions/earnings.
- Owner/admin view exposes deal, contact, payout and margin context.
- Postbacks are idempotent.
- Source evidence and approved outbound text are retained for traceability.

</details>