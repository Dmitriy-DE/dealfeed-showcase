# Operational safety

The system automates discovery and repetitive transport, but keeps commercial actions controlled.

## Defaults

- historical backfill does not trigger fresh-match alerts;
- match notifications use a minimum score threshold;
- assisted outreach uses hourly/daily limits and per-contact cooldowns;
- FloodWait or equivalent provider throttling pauses the queue;
- distribution is disabled until explicitly configured;
- outbound distribution requires preview/edit + owner approval;
- destinations are allowlisted;
- tracker postbacks are idempotent.

## Evidence

The system retains enough evidence to explain why an object exists:

- source message;
- parsed opportunity;
- match score and filters;
- deal state and terms;
- approved distribution text;
- click and conversion events.

Sensitive credentials, contact details and production secrets are intentionally absent from the public showcase.
