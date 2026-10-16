#!/usr/bin/env python3
"""Produce a transparent baseline report from normalized corpus JSONL."""
from __future__ import annotations
import argparse, collections, json, math, re, statistics
from pathlib import Path

WORD_RE = re.compile(r"[A-Za-z]+(?:['’-][A-Za-z]+)*")
SENTENCE_RE = re.compile(r"(?<=[.!?])\s+")
STOPWORDS = set("a an and are as at be been but by for from had has have he her his i if in is it its me my not of on or our she so that the their them they this to was we were what when which who will with would you your".split())

def percentile(values: list[int], fraction: float) -> float:
    if not values: return 0.0
    ordered, index = sorted(values), (len(values) - 1) * fraction
    low, high = math.floor(index), math.ceil(index)
    return float(ordered[low]) if low == high else ordered[low] * (high-index) + ordered[high] * (index-low)

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("corpus", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--top", type=int, default=40)
    args = parser.parse_args()
    records = []
    for number, line in enumerate(args.corpus.read_text(encoding="utf-8").splitlines(), 1):
        if line.strip():
            item = json.loads(line)
            if not isinstance(item.get("text"), str): raise ValueError(f"{args.corpus}:{number}: missing string field 'text'")
            if not item.get("holdout", False): records.append(item)

    words, lengths = [], []
    sources, types, locales, disciplines, punctuation = (collections.Counter() for _ in range(5))
    for item in records:
        text = item["text"]
        tokens = [x.casefold().replace("’", "'") for x in WORD_RE.findall(text)]
        words.extend(tokens)
        lengths.extend(n for n in (len(WORD_RE.findall(s)) for s in SENTENCE_RE.split(text)) if n)
        for mark in "!?;:()—–": punctuation[mark] += text.count(mark)
        sources[str(item.get("source", "unknown"))] += 1
        types[str(item.get("source_type", "unknown"))] += 1
        locales[str(item.get("locale", "unknown"))] += 1
        disciplines[str(item.get("discipline", "unknown"))] += 1
    content = collections.Counter(x for x in words if x not in STOPWORDS and len(x) > 2)
    bigrams = collections.Counter(zip(words, words[1:]))
    report = {
        "records": len(records), "words": len(words), "sources": dict(sources),
        "source_types": dict(types), "locales": dict(locales), "disciplines": dict(disciplines),
        "sentence_length": {"mean": round(statistics.mean(lengths),2) if lengths else 0,
            "median": round(statistics.median(lengths),2) if lengths else 0,
            "stdev": round(statistics.pstdev(lengths),2) if lengths else 0,
            "p10": round(percentile(lengths,.1),2), "p90": round(percentile(lengths,.9),2)},
        "punctuation_per_1000_words": {k: round(v*1000/max(1,len(words)),3) for k,v in punctuation.items()},
        "top_content_words": content.most_common(args.top),
        "top_bigrams": [(" ".join(k),v) for k,v in bigrams.most_common(args.top)],
        "warning": "Topic words are not automatically style features. Compare registers and a control corpus before adding rules."
    }
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True); args.output.write_text(rendered, encoding="utf-8")
    else: print(rendered, end="")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
