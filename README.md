# AI Overview Cited-Domains Study

**Which domains Google's AI Overview cites on 24 buyer searches, collected by hand on 10 June 2026**

| | |
|---|---|
| **Article** | https://ismybrandinai.com/most-cited-sources-in-ai-overviews |
| **Repository** | https://github.com/minelgunesoglu-code/ai-overview-cited-domains-study |
| **Archive** | DOI: to be added after the Zenodo release |
| **Collected** | 10 June 2026, by hand, one run per query |
| **Engine** | Google AI Overview, the source panel it labels "N sites" |
| **Sample** | 24 "best [category]" buyer searches across business software, consumer products, finance and lifestyle; 21 produced an AI Overview, 3 returned a Shopping grid instead |
| **Headline** | Reddit was cited in **13 of the 21** AI Overviews (62%), more than twice the next sites, Forbes and YouTube at 6 each. |
| **Licence** | CC BY 4.0 (`LICENSE`); see `LICENCE-NOTES.md` for what it does and does not cover |

Searches were run in Google with US English settings (`gl=us`, `hl=en`). Each of
24 ordinary "best [category]" searches was run once. Where
an AI Overview appeared, its source panel was opened and every distinct domain it
listed was written down, together with the panel's source count and a short note
on the kind of sites cited.

**What is measured:** whether a search produced an AI Overview, how many entries
its source panel listed, and which domains those entries pointed to.
**What is NOT measured:** how prominently a source was placed, whether a cited page
is accurate, and how the same searches behave on another day, account or market.

---

## 1. Findings

All figures below are the ones published in the article. Each is recounted from
the rows by `notes/verify.py`; see `notes/reproduction-check.md`.

### Most "best" searches get an AI Overview, but not all

21 of the 24 searches produced an AI Overview. The other three, running shoes,
mattress and standing desk, all physical retail products, returned a Shopping grid
instead. An AI Overview listed about 8 sources (mean 7.76, median 8, range 5 to 12).

### The most-cited sources

Counted as the number of the 21 AI Overviews that cited each domain:

| Rank | Source | AI Overviews citing it |
|---|---|---:|
| 1 | reddit.com | 13 |
| 2 | forbes.com | 6 |
| 3 | youtube.com | 6 |
| 4 | pcmag.com | 5 |
| 5 | zapier.com | 4 |
| 6 | nerdwallet.com | 3 |

Below these sits a long tail of domains cited once or twice, among them
bankrate.com, cnet.com, amazon.com and salesforce.com (twice each).

### Forums lead, and the mix changes by category

A forum, Reddit or the Clark Howard community (clark.com), was cited in 14 of the
21 AI Overviews; YouTube in 6. Reddit was absent from the business software
searches for accounting, AI writing, help desk and web conferencing, and from the
travel credit card search, which cited only finance media.

---

## 2. What is in this repository

```
data/ai-overview-cited-domains-2026-06-10.csv   24 rows, one per query
data/ai-overview-cited-domains-2026-06-10.json  the same rows plus the method and the known limits
notes/
  verify.py                 recounts the published figures from the rows
  reproduction-check.md     the result of that recount
  zenodo-release-steps.md   how this repository is archived on Zenodo
```

This is a data package with method notes. The two data files are the ones
published on the site with one column added, `panel_count_reading`; removing that
column gives the published files byte for byte.

### Columns

| Column | Meaning |
|---|---|
| `query` | the search, as typed |
| `ai_overview_present` | `yes` if an AI Overview appeared on the run |
| `sources_in_panel` | the source count the panel showed (0 when there was no AI Overview) |
| `panel_count_reading` | `exact` if the panel count was recorded as an exact number, `approximate` if it was recorded as approximate; empty when there was no AI Overview |
| `reddit_in_panel` | `yes` if reddit.com is among the cited domains; empty when there was no AI Overview |
| `cited_domains` | the distinct domains the panel listed, separated by `\|` |
| `raw_note` | the note written during collection, at most 400 characters |

### Rules worth knowing before recounting

- The panel groups several links under one entry ("Zapier +3"); such an entry is
  counted once.
- A few panel entries could not be resolved to a domain and are left out of
  `cited_domains`, so a row can list fewer domains than `sources_in_panel`.
- "No AI Overview" means none appeared on this run, not that none exists.

---

## 3. Recounting the figures

```bash
python3 notes/verify.py
```

Python 3.8 or later, standard library only. Run it from the repository root. It
prints each published figure next to the recounted one and ends with the number
of checks that match.

---

## 4. Limits

- One engine, one day and one run per query. AI Overviews are personalised and
  change between runs, both in their sources and in whether they appear at all; a
  re-check the next day found an AI Overview on a search that had shown only
  Shopping.
- Site types were assigned by hand from each source's title and brand, not by
  reading the page.
- English-language searches with US English settings only.

---

## 5. Citing this

> Gunesoglu, M. (2026). *AI Overview Cited-Domains Study* [Data set].
> Is My Brand in AI. https://ismybrandinai.com/most-cited-sources-in-ai-overviews

Related: the follow-up study of 30 searches across six industries,
[AI Overview Industry Study](https://ismybrandinai.com/ai-overview-citations-by-industry).

If a count here does not match what you get from the files, open an issue and a
correction will be published saying what changed.
