#!/usr/bin/env python3
"""Normalize authorized local text or JSONL into the skill corpus schema."""
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path

SPACE_RE = re.compile(r"[ \t]+")
BLANK_RE = re.compile(r"\n\s*\n+")
EMAIL_RE = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)
PHONE_RE = re.compile(r"(?<!\w)(?:\+?\d[\d ().-]{7,}\d)(?!\w)")
HANDLE_RE = re.compile(r"(?<!\w)@[A-Za-z0-9_]{2,30}\b")

def normalize(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = EMAIL_RE.sub("[email]", text)
    text = PHONE_RE.sub("[phone]", text)
    text = HANDLE_RE.sub("[handle]", text)
    return "\n".join(SPACE_RE.sub(" ", line).strip() for line in text.splitlines() if line.strip()).strip()

def iter_records(path: Path):
    if path.suffix.lower() == ".jsonl":
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if line.strip():
                item = json.loads(line)
                if not isinstance(item, dict) or not isinstance(item.get("text"), str):
                    raise ValueError(f"{path}:{number}: expected an object with string field 'text'")
                yield item
    else:
        for paragraph in BLANK_RE.split(path.read_text(encoding="utf-8")):
            if paragraph.strip():
                yield {"text": paragraph}

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", nargs="+", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--source", required=True)
    parser.add_argument("--source-type", required=True)
    parser.add_argument("--permission-basis", required=True)
    parser.add_argument("--locale", default="unknown")
    parser.add_argument("--discipline", default="general")
    parser.add_argument("--format", dest="text_format", default="unknown")
    parser.add_argument("--min-chars", type=int, default=80)
    args = parser.parse_args()

    seen, output = set(), []
    for path in args.inputs:
        for incoming in iter_records(path):
            text = normalize(incoming["text"])
            fingerprint = hashlib.sha256(text.casefold().encode()).hexdigest()
            if len(text) < args.min_chars or fingerprint in seen:
                continue
            seen.add(fingerprint)
            record = dict(incoming)
            record.update({
                "id": incoming.get("id") or f"{args.source}:{fingerprint[:20]}",
                "text": text,
                "source": incoming.get("source") or args.source,
                "source_type": incoming.get("source_type") or args.source_type,
                "permission_basis": incoming.get("permission_basis") or args.permission_basis,
                "locale": incoming.get("locale") or args.locale,
                "discipline": incoming.get("discipline") or args.discipline,
                "format": incoming.get("format") or args.text_format,
            })
            output.append(record)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("".join(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n" for x in output), encoding="utf-8")
    print(json.dumps({"written": len(output), "output": str(args.output)}, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
