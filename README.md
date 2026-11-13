# Signal Lab

A small, generic Python project for coding evaluations, themed on why AI matters in communications and intelligence work.

It pulls from public, keyless sources: [GDELT](https://blog.gdeltproject.org/gdelt-doc-2-0-api-debuts/) news, the [Federal Register API](https://www.federalregister.gov/developers/documentation/api/v1), the [UN SDG API](https://unstats.un.org/sdgs/UNSDGAPIV5/swagger/index.html), and the Hugging Face Hub. It then dedupes, tags themes, and produces a source-cited brief.

## Why AI matters here
- Volume: open-source intelligence now outruns human reading capacity; the [IC OSINT Strategy 2024-2026](https://www.dni.gov/files/ODNI/documents/IC_OSINT_Strategy.pdf) frames OSINT as the "INT of first resort."
- Threat: generative models scale influence operations, and labs publish [takedown reports](https://openai.com/global-affairs/disrupting-malicious-uses-of-ai-june-2025/).
- Trust: communicators and analysts need output that separates documented records from interpretation, so this project makes every item carry a source URL and date.

## Quick start
```bash
pip install -e ".[dev]"
pytest -q                      # offline, network mocked
python -m signal_lab.cli "AI deepfake election"   # live brief
```

## Layout
- `signal_lab/sources/` API clients (one file each)
- `signal_lab/analysis.py` pure functions, the main evaluation targets
- `tasks/` graded exercises; `evals/rubric.md` scoring
- `site/` the companion page

Sources are used as-is under their own terms; this repo stores no API keys.
