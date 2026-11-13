from ..http import get_json
URL = "https://api.gdeltproject.org/api/v2/doc/doc"

def search_news(query: str, max_records: int = 25) -> list[dict]:
    data = get_json(URL, {"query": query, "mode": "artlist",
                          "maxrecords": max_records, "format": "json"})
    return [{"title": a.get("title", ""), "url": a.get("url", ""),
             "domain": a.get("domain", ""), "seen": a.get("seendate", ""),
             "source": "gdelt"} for a in data.get("articles", [])]
