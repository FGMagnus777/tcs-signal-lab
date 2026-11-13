from ..http import get_json
URL = "https://www.federalregister.gov/api/v1/documents.json"

def search_documents(term: str, per_page: int = 25) -> list[dict]:
    data = get_json(URL, {"conditions[term]": term, "per_page": per_page, "order": "newest"})
    return [{"title": d.get("title", ""), "url": d.get("html_url", ""),
             "domain": "federalregister.gov", "seen": d.get("publication_date", ""),
             "abstract": d.get("abstract") or "", "source": "federal_register"}
            for d in data.get("results", [])]
