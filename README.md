<p align="center"><img src="./assets/hero.svg" width="100%" alt="DealFeed"/></p>

<table>
<tr>
<td width="20%" align="center"><b>Telegram intake</b><br/><sub>raw evidence</sub></td>
<td width="20%" align="center"><b>Rule matching</b><br/><sub>hard filters + score</sub></td>
<td width="20%" align="center"><b>Operator bot</b><br/><sub>human-in-the-loop</sub></td>
<td width="20%" align="center"><b>Cloudflare edge</b><br/><sub>tracking + postbacks</sub></td>
<td width="20%" align="center"><b>Margin ledger</b><br/><sub>deal economics</sub></td>
</tr>
</table>

<p align="center"><img src="./assets/actual-surfaces.svg" width="100%" alt="Product surfaces"/></p>

<table>
<tr>
<td width="50%" valign="top"><img src="./assets/features.svg" width="100%" alt="Modules"/></td>
<td width="50%" valign="top"><img src="./assets/core-model.svg" width="100%" alt="Evidence model"/></td>
</tr>
</table>

<table>
<tr>
<td width="48%" valign="top"><img src="./assets/overview.svg" width="100%" alt="Operator controls"/></td>
<td width="52%" valign="top"><img src="./assets/architecture-visual.svg" width="100%" alt="Architecture"/></td>
</tr>
</table>

<p align="center"><img src="./assets/flow-visual.svg" width="100%" alt="Automation flow"/></p>
<p align="center"><img src="./assets/engineering-signature.svg" width="100%" alt="Engineering signature"/></p>

<details>
<summary><b>Operating rules</b></summary>

- raw Telegram messages are retained as evidence
- parser does not invent absent GEO / payout / source facts
- backfill does not generate fresh-match spam
- outreach uses limits, cooldowns and operator control
- distribution requires preview/edit + explicit approval
- edge tracker stays available independently of the local deal desk

</details>