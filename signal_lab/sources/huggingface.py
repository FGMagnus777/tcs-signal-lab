from ..http import get_json
URL = "https://huggingface.co/api/models"

def search_models(term: str, limit: int = 10) -> list[dict]:
    data = get_json(URL, {"search": term, "limit": limit, "sort": "downloads"})
    return [{"id": m["id"], "downloads": m.get("downloads", 0),
             "task": m.get("pipeline_tag")} for m in data]
