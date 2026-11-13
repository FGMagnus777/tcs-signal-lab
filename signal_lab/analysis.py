"""Pure functions: the core targets for coding-evaluation tasks."""
import re
from collections import Counter

STOP = set("a an the of and or to in on for with is are was were by at as from that this it its be has have".split())

def tokenize(text: str) -> list[str]:
    return [t for t in re.findall(r"[a-z0-9']+", text.lower()) if t not in STOP and len(t) > 2]

def dedupe(items: list[dict]) -> list[dict]:
    """Drop items with the same normalized URL (ignores scheme, www, query, trailing slash)."""
    seen, out = set(), []
    for it in items:
        key = re.sub(r"^https?://(www\.)?", "", it["url"].split("?")[0]).rstrip("/").lower()
        if key and key not in seen:
            seen.add(key); out.append(it)
    return out

def top_terms(items: list[dict], n: int = 10) -> list[tuple[str, int]]:
    c = Counter()
    for it in items:
        c.update(tokenize(it.get("title", "") + " " + it.get("abstract", "")))
    return c.most_common(n)

def source_mix(items: list[dict]) -> dict[str, float]:
    """Share of items per source, rounded to 3 places; empty input returns {}."""
    if not items: return {}
    c = Counter(i["source"] for i in items)
    return {k: round(v / len(items), 3) for k, v in sorted(c.items())}

def tag_theme(item: dict, themes: dict[str, list[str]]) -> list[str]:
    toks = set(tokenize(item.get("title", "") + " " + item.get("abstract", "")))
    return sorted(t for t, kws in themes.items() if toks & set(kws))

THEMES = {
    "disinformation": ["disinformation", "misinformation", "deepfake", "influence", "propaganda"],
    "osint": ["osint", "open-source", "intelligence", "surveillance", "analysis"],
    "policy": ["regulation", "rule", "policy", "executive", "governance", "safety"],
    "communications": ["media", "communications", "messaging", "journalism", "content"],
}
