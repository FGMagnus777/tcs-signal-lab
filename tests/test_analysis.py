from signal_lab.analysis import dedupe, top_terms, source_mix, tag_theme, THEMES

def test_dedupe_normalizes_urls():
    items = [{"url": "https://www.a.com/x/?utm=1"}, {"url": "http://a.com/x"}, {"url": "https://b.com"}]
    assert len(dedupe(items)) == 2

def test_top_terms_ignores_stopwords():
    items = [{"title": "The deepfake of the year"}, {"title": "Deepfake law"}]
    assert top_terms(items, 1) == [("deepfake", 2)]

def test_source_mix():
    assert source_mix([]) == {}
    assert source_mix([{"source": "a"}, {"source": "a"}, {"source": "b"}]) == {"a": 0.667, "b": 0.333}

def test_tag_theme():
    assert tag_theme({"title": "Deepfake propaganda and new policy"}, THEMES) == ["disinformation", "policy"]
