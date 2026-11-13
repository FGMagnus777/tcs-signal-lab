from ..http import get_json
URL = "https://unstats.un.org/SDGAPI/v1/sdg/Goal/List"

def list_goals() -> list[dict]:
    data = get_json(URL, {"includechildren": "false"})
    return [{"code": g["code"], "title": g["title"]} for g in data]
