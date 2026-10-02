# Architecture

DealFeed is split into two independent contours.

## Deal desk

Runs locally while the operator is collecting sources and reviewing opportunities.

```text
Telegram chats
   ↓ Telethon
raw_messages
   ↓ deterministic noise filter + parser
opportunities
   ↓ hard filters + score
matches
   ↓ private aiogram bot
operator → outreach → terms → deal
```

Important properties:

- raw source messages are kept verbatim;
- parsed fields may be null when the source does not provide them;
- backfill is stored but does not generate fresh-match spam;
- optional AI fallback is not the primary parser and is disabled by default;
- outreach stays assisted by default.

## Edge tracker

Runs independently on Cloudflare Worker + D1.

```text
tracking link
   ↓
redirect endpoint → click row → 302 advertiser URL
   ↓
provider postback
   ↓
idempotent conversion
   ↓
advertiser payout - publisher payout = broker margin
```

The edge side also exposes a partner-facing cabinet and an owner/admin view.

## Distribution

Advertiser-side source signals can become grouped offer-inventory cards. The operator reviews the representative evidence, sets the public payout, edits the outbound text and explicitly approves the distribution job.

Only approved jobs for allowlisted destinations may enter the sender queue.
