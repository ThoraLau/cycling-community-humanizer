# Corpus collection policy

## Allowed inputs

- Text the user wrote or owns.
- User-provided exports the user is permitted to reuse.
- Public-domain or suitably licensed datasets.
- Pages whose terms and robots policy allow the intended access and reuse.
- Official APIs used within their terms and rate limits.

## Disallowed by default

- Bypassing login, paywalls, CAPTCHAs, rate limits, or anti-bot controls.
- Crawling a platform whose terms prohibit the intended collection or AI-related use.
- Private group chats without authorization.
- Retaining real names, handles, emails, phone numbers, precise locations, or unnecessary personal data.
- Profiling one identifiable writer without permission.

Reddit is import-only by default. A public subreddit URL is not authorization to scrape.

## Sampling

- Keep forum, editorial, review, comment, and spoken registers separate.
- Cap each author's contribution.
- Track country, platform, discipline, format, and date when known.
- Require multiple authors and source types before calling a feature strong.
- Keep satire and meme communities in their own register.
- Keep posts and replies distinguishable.
- Maintain a holdout set not used to create the profile.

Store raw, normalized, curated, and holdout data separately. Retain a source ID and content hash, not a public username. Document collection date, permission basis, filters, removals, and sampling bias. If a source must be removed, delete its records, rebuild aggregates, and bump the corpus version.
