"""Recount the figures published in the AI Overview Cited-Domains Study.

This script was written after publication, to check the article's figures
against the published rows. The data were collected by hand. Standard library only. Run from the repository root:

    python3 notes/verify.py
"""
import csv
import json
import statistics
from collections import Counter
from pathlib import Path

DATA = Path("data")
CSV_FILE = DATA / "ai-overview-cited-domains-2026-06-10.csv"
JSON_FILE = DATA / "ai-overview-cited-domains-2026-06-10.json"

checks = []


def check(label, published, computed):
    ok = published == computed
    checks.append(ok)
    print(f"[{'OK ' if ok else 'DIFF'}] {label}: published {published!r}, computed {computed!r}")


with CSV_FILE.open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
meta = json.loads(JSON_FILE.read_text(encoding="utf-8"))

# The CSV and the JSON hold the same rows.
json_rows = [{k: ("" if v is None else str(v)) for k, v in r.items()} for r in meta["rows"]]
check("CSV rows equal JSON rows", True, json_rows == rows)

aio = [r for r in rows if r["ai_overview_present"] == "yes"]

# panel_count_reading: added in the archive copy; not part of the article.
readings = Counter(r["panel_count_reading"] for r in aio)
print(f"NOTE  panel_count_reading among the 21 AI Overviews: {readings['exact']} exact, "
      f"{readings['approximate']} approximate")
check("searches", 24, len(rows))
check("searches with an AI Overview", 21, len(aio))
check("JSON 'with_ai_overview'", 21, meta["with_ai_overview"])

counts = [int(r["sources_in_panel"]) for r in aio]
check("sources per AI Overview, mean rounded", 8, round(statistics.mean(counts)))
check("sources per AI Overview, median", 8, statistics.median(counts))
check("sources per AI Overview, range", (5, 12), (min(counts), max(counts)))
print(f"       (exact mean: {statistics.mean(counts):.2f})")

domains = Counter()
for r in aio:
    for d in set(filter(None, r["cited_domains"].split("|"))):
        domains[d] += 1

for name, n in [("reddit.com", 13), ("forbes.com", 6), ("youtube.com", 6),
                ("pcmag.com", 5), ("zapier.com", 4), ("nerdwallet.com", 3)]:
    check(f"AI Overviews citing {name}", n, domains[name])
check("top six by count", ["reddit.com", "forbes.com", "youtube.com", "pcmag.com", "zapier.com", "nerdwallet.com"],
      [d for d, _ in sorted(domains.items(), key=lambda x: (-x[1], x[0]))[:6]])
check("Reddit share of AI Overviews, %", 62, round(100 * domains["reddit.com"] / len(aio)))
check("reddit_in_panel = yes", 13, sum(r["reddit_in_panel"] == "yes" for r in rows))

# Forums: Reddit plus the Clark Howard community (clark.com).
forum = sum(1 for r in aio if {"reddit.com", "clark.com"} & set(r["cited_domains"].split("|")))
check("AI Overviews citing a forum (reddit.com or clark.com)", 14, forum)

# Named B2B queries without Reddit.
by_q = {r["query"]: r for r in rows}
for q in ["best accounting software for small business", "best ai writing tools",
          "best help desk software", "best web conferencing software", "best travel credit card"]:
    check(f"Reddit absent: {q}", "no", by_q[q]["reddit_in_panel"])
check("travel credit card domains",
      "nerdwallet.com|bankrate.com|experian.com|creditkarma.com|thepointsguy.com|cnn.com|remitly.com",
      by_q["best travel credit card"]["cited_domains"])

# Long-tail sources named as two-time or one-time.
for d in ["bankrate.com", "cnet.com", "amazon.com", "salesforce.com", "nytimes.com/wirecutter",
          "consumerreports.org", "healthline.com", "seriouseats.com", "hubspot.com",
          "hostinger.com", "experian.com"]:
    ok = domains[d] in (1, 2)
    checks.append(ok)
    print(f"[{'OK ' if ok else 'DIFF'}] long tail {d}: cited {domains[d]} time(s)")

print()
print(f"{sum(checks)} of {len(checks)} checks match.")
