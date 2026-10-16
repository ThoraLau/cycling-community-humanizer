# Cycling Community Humanizer

An agent skill for writing and rewriting English cycling content for experienced riders in the United States, United Kingdom, and Canada.

It supports cycling blogs, product reviews, forum replies, emails, and spoken social scripts. The skill separates mechanic, coach, racer, commuter, tourer, and enthusiast registers while preserving facts, measurements, safety claims, and stated experience.

## What it does

- Rewrites generic or AI-sounding prose in a grounded cycling-community voice.
- Preserves specifications, numbers, compatibility details, quotations, and uncertainty.
- Handles US, UK, and Canadian English without mixing spelling or units.
- Keeps different cycling roles and disciplines from collapsing into one generic persona.
- Imports authorized local text into a private JSONL corpus.
- Produces transparent corpus statistics for later voice-profile updates.

The included voice profile is a **provisional editorial baseline**. It is not presented as a measured summary of Reddit or any other named community. Build measured profiles only from content you are authorized to use.

## Repository structure

```text
cycling-community-humanizer/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── audience-profile.md
│   ├── corpus-policy.md
│   ├── corpus-schema.md
│   ├── rewrite-protocol.md
│   └── voice-profile.md
├── scripts/
│   ├── analyze_corpus.py
│   └── ingest_corpus.py
├── examples/
│   └── authorized-sample.txt
└── tests/
    └── test_pipeline.py
```

## Installation

### Codex

Copy the repository folder into your Codex skills directory:

```text
~/.codex/skills/cycling-community-humanizer/
```

Restart or reload Codex so the skill is discovered.

### Other skill-compatible agents

Copy the complete folder into the agent's skills directory. Keep `SKILL.md`, `references/`, and `scripts/` together because the entrypoint links to those files.

## Use

Invoke the skill explicitly:

```text
Use $cycling-community-humanizer to rewrite this product review for experienced US commuters. Preserve every specification and do not invent test experience.
```

Or ask naturally:

```text
Rewrite this cycling blog in a practical UK club-rider voice. Keep the original measurements and uncertainty.
```

## Build a private corpus

The scripts require Python 3.9 or newer and use only the standard library.

Import an authorized text file:

```bash
python scripts/ingest_corpus.py examples/authorized-sample.txt \
  --output data/curated/sample.jsonl \
  --source user-supplied-sample \
  --source-type forum_comment \
  --permission-basis user_owned \
  --locale en-US \
  --discipline commuting \
  --format reply
```

Analyze the normalized corpus:

```bash
python scripts/analyze_corpus.py data/curated/sample.jsonl \
  --output data/reports/sample-profile.json
```

Topic words are not automatically style features. Compare platforms, roles, formats, locales, and a control corpus before changing the shared voice profile.

## Data and safety boundaries

- Do not treat a public URL as permission to crawl.
- Do not bypass login, paywalls, CAPTCHAs, rate limits, or anti-bot measures.
- Reddit is import-only by default unless you have an authorized API agreement or another lawful permission basis.
- Do not include private club chats without authorization.
- Remove unnecessary personal data and avoid profiling one identifiable writer.
- Do not publish a raw forum archive with this repository.
- Do not claim that a rewrite is guaranteed to evade AI detection.

See [references/corpus-policy.md](references/corpus-policy.md) for the full policy.

## Tests

```bash
python -m unittest discover -s tests -v
```

## License

MIT. See [LICENSE](LICENSE).
