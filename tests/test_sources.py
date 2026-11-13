from signal_lab.sources import gdelt, federal_register, un_sdg, huggingface

def test_gdelt(monkeypatch):
    monkeypatch.setattr(gdelt, "get_json", lambda *a, **k: {"articles": [{"title": "T", "url": "u", "domain": "d", "seendate": "s"}]})
    assert gdelt.search_news("x")[0]["source"] == "gdelt"

def test_fr(monkeypatch):
    monkeypatch.setattr(federal_register, "get_json", lambda *a, **k: {"results": [{"title": "T", "html_url": "u", "abstract": None}]})
    assert federal_register.search_documents("x")[0]["abstract"] == ""

def test_sdg(monkeypatch):
    monkeypatch.setattr(un_sdg, "get_json", lambda *a, **k: [{"code": "16", "title": "Peace", "description": "d"}])
    assert un_sdg.list_goals() == [{"code": "16", "title": "Peace"}]

def test_hf(monkeypatch):
    monkeypatch.setattr(huggingface, "get_json", lambda *a, **k: [{"id": "a/b", "downloads": 3}])
    assert huggingface.search_models("x")[0]["task"] is None
