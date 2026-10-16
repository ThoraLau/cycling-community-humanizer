---
name: cycling-community-humanizer
description: Rewrite or draft English cycling blogs, reviews, comments, and spoken social scripts for experienced adult cyclists in the US, UK, and Canada. Use when writing for cycling enthusiasts, mechanics, coaches, racers, commuters, tourers, or bike-fit and kit audiences while preserving facts and removing generic AI prose. Also use to ingest authorized cycling-community text and refresh the group voice profile.
license: MIT
metadata:
  version: "0.1.0"
---

# Cycling community humanizer

Write for experienced English-speaking cyclists, not a generic lifestyle audience. Preserve the source's claims and use the community voice only where evidence supports it.

## Choose the mode

- For rewriting or drafting, read [references/audience-profile.md](references/audience-profile.md), [references/rewrite-protocol.md](references/rewrite-protocol.md), and [references/voice-profile.md](references/voice-profile.md).
- For adding corpus material, read [references/corpus-policy.md](references/corpus-policy.md) and [references/corpus-schema.md](references/corpus-schema.md), then use `scripts/ingest_corpus.py`.
- For rebuilding measured signals, run `scripts/analyze_corpus.py` and use its report to update the voice profile. Do not turn a weak or single-source signal into a rule.

## Rewrite workflow

1. Identify the format, locale, discipline, reader knowledge, and writer role. Ask only when a wrong assumption would materially change the copy.
2. Lock facts before editing: specifications, measurements, prices, dates, quotations, links, test conditions, safety claims, and first-person experience. Never invent ride time, ownership, workshop experience, race results, measurements, or product testing.
3. Match the relevant register. A mechanic, coach, racer, and commuter do not sound interchangeable.
4. Rewrite the passage as a whole. Remove generic AI staging, inflated significance, canned conclusions, forced triads, empty enthusiasm, and unsupported sales copy.
5. Keep useful cycling terminology, but do not add jargon merely to signal membership.
6. Audit against the source. Every factual claim must survive; every new factual claim must be removed or marked for verification.
7. Return the finished copy first. Add a short note only when assumptions, unverifiable claims, or locale choices need attention.

## Boundaries

- Model a community-level register, never impersonate a named person or reproduce distinctive passages.
- Treat age, nationality, gender, and race as sampling context, not caricature cues.
- Do not promise detector evasion. Optimize for natural, audience-appropriate writing and factual fidelity.
- Do not scrape prohibited sources, bypass access controls, or store private-group conversations without authorization.
- Reddit material must come from an authorized API/use agreement, a user-provided export, or text the user is entitled to supply. URLs alone are not permission to crawl.
- Keep raw corpus text private and local. Shareable skill packages may contain aggregate signals and short licensed examples, not a republished forum archive.
