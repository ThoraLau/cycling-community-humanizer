# Corpus schema

Use UTF-8 JSON Lines. One object represents one coherent text unit.

Required fields:

```json
{"id":"stable-local-id","text":"Normalized text","source":"r-bikewrench-export","source_type":"forum_comment","permission_basis":"user_provided_export"}
```

Recommended fields: `locale`, `country`, `discipline`, `role`, `format`, `created_at`, `author_hash`, `thread_id`, `url`, `satire`, `holdout`, and `notes`.

Do not retain a public handle merely to calculate author balance. Hash it before storage. Do not infer sensitive demographic attributes from text.

For plain `.txt` or `.md` imports, the ingestion script treats paragraphs separated by a blank line as records and applies command-line metadata.
