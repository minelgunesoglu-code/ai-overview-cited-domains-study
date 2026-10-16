# Reproduction check

Checked on 17 October 2026 against the article as published at
https://ismybrandinai.com/most-cited-sources-in-ai-overviews (published 10 June
2026, last updated 10 October 2026).

## Result

**Every figure checked matches.** `notes/verify.py` runs 34 checks, the published
figures and statements plus two consistency checks on the files, and all 34 pass.
No figure was changed, and no value in the data was changed.

## What was checked

1. **The files are the published files, with one column added.** The site
   publishes these two files (SHA-256):

    1c880188c9b1bf20d6eb75f20f62fc2035dd67e8440ef6c71e10c355db771afc  ai-overview-cited-domains-2026-06-10.csv
    a73dfef0505c704333aea95e0e30553fcba5ef2b4be1c6a16e3389c89d295e3c  ai-overview-cited-domains-2026-06-10.json

   The archive copy adds one column, `panel_count_reading`, after
   `sources_in_panel` in both the CSV and the JSON rows. It records whether the
   panel count was written down at collection as an exact number (`exact`, 12
   rows) or as an approximate one (`approximate`, 9 rows); it is empty for the
   three searches without an AI Overview. No other value was touched: removing
   the column gives the published files byte for byte. SHA-256 of the archive
   copy:

    cfcc4579bc8588440eafd0c14e79efc564d8dc898e4957bedfe7b9fe43d2a923  data/ai-overview-cited-domains-2026-06-10.csv
    db8b2945079f8a0b17706f4f352d18eaeccfebad005489beaaea78663f4f5221  data/ai-overview-cited-domains-2026-06-10.json

   Rows marked `approximate`: best vpn, best web hosting, best office chair,
   best robot vacuum, best electric toothbrush, best travel credit card, best
   budgeting app, best protein powder, best note taking app.

2. **The CSV and the JSON agree.** The JSON's `rows` equal the CSV rows.

3. **Every figure in the article recounts from the rows.** Output of
   `python3 notes/verify.py`:

```
[OK ] CSV rows equal JSON rows: published True, computed True
NOTE  panel_count_reading among the 21 AI Overviews: 12 exact, 9 approximate
[OK ] searches: published 24, computed 24
[OK ] searches with an AI Overview: published 21, computed 21
[OK ] JSON 'with_ai_overview': published 21, computed 21
[OK ] sources per AI Overview, mean rounded: published 8, computed 8
[OK ] sources per AI Overview, median: published 8, computed 8
[OK ] sources per AI Overview, range: published (5, 12), computed (5, 12)
       (exact mean: 7.76)
[OK ] AI Overviews citing reddit.com: published 13, computed 13
[OK ] AI Overviews citing forbes.com: published 6, computed 6
[OK ] AI Overviews citing youtube.com: published 6, computed 6
[OK ] AI Overviews citing pcmag.com: published 5, computed 5
[OK ] AI Overviews citing zapier.com: published 4, computed 4
[OK ] AI Overviews citing nerdwallet.com: published 3, computed 3
[OK ] top six by count: published ['reddit.com', 'forbes.com', 'youtube.com', 'pcmag.com', 'zapier.com', 'nerdwallet.com'], computed ['reddit.com', 'forbes.com', 'youtube.com', 'pcmag.com', 'zapier.com', 'nerdwallet.com']
[OK ] Reddit share of AI Overviews, %: published 62, computed 62
[OK ] reddit_in_panel = yes: published 13, computed 13
[OK ] AI Overviews citing a forum (reddit.com or clark.com): published 14, computed 14
[OK ] Reddit absent: best accounting software for small business: published 'no', computed 'no'
[OK ] Reddit absent: best ai writing tools: published 'no', computed 'no'
[OK ] Reddit absent: best help desk software: published 'no', computed 'no'
[OK ] Reddit absent: best web conferencing software: published 'no', computed 'no'
[OK ] Reddit absent: best travel credit card: published 'no', computed 'no'
[OK ] travel credit card domains: published 'nerdwallet.com|bankrate.com|experian.com|creditkarma.com|thepointsguy.com|cnn.com|remitly.com', computed 'nerdwallet.com|bankrate.com|experian.com|creditkarma.com|thepointsguy.com|cnn.com|remitly.com'
[OK ] long tail bankrate.com: cited 2 time(s)
[OK ] long tail cnet.com: cited 2 time(s)
[OK ] long tail amazon.com: cited 2 time(s)
[OK ] long tail salesforce.com: cited 2 time(s)
[OK ] long tail nytimes.com/wirecutter: cited 1 time(s)
[OK ] long tail consumerreports.org: cited 1 time(s)
[OK ] long tail healthline.com: cited 1 time(s)
[OK ] long tail seriouseats.com: cited 1 time(s)
[OK ] long tail hubspot.com: cited 1 time(s)
[OK ] long tail hostinger.com: cited 1 time(s)
[OK ] long tail experian.com: cited 1 time(s)

34 of 34 checks match.
```

## Notes on the counts

- "About 8 sources on average" is a mean of 7.76 rounded; the median is 8. The
  mean, median and range use `sources_in_panel` as published, including the nine
  approximate counts. The range end points, 5 and 12, are both exact counts.
- Forbes and YouTube tie at 6. The article lists Forbes second and YouTube third;
  the order between them is not a measured difference.
- The forum count of 14 is Reddit (13) plus the Clark Howard community
  (clark.com) on the electric toothbrush search, where Reddit was absent.
