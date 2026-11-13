import argparse, json
from .sources import gdelt, federal_register
from .analysis import dedupe, top_terms, source_mix, tag_theme, THEMES

def build_brief(query: str) -> dict:
    items = []
    for fn in (gdelt.search_news, federal_register.search_documents):
        try: items += fn(query)
        except Exception as e: print(f"warn: {fn.__module__} failed: {e}")
    items = dedupe(items)
    for i in items: i["themes"] = tag_theme(i, THEMES)
    return {"query": query, "count": len(items), "source_mix": source_mix(items),
            "top_terms": top_terms(items), "items": items}

def main():
    p = argparse.ArgumentParser(description="Build a brief from public sources")
    p.add_argument("query", nargs="?", default="artificial intelligence disinformation")
    print(json.dumps(build_brief(p.parse_args().query), indent=2))

if __name__ == "__main__": main()
