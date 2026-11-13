import requests

def get_json(url: str, params: dict | None = None, timeout: int = 20):
    """Single choke point for network access so tests can monkeypatch it."""
    r = requests.get(url, params=params, timeout=timeout,
                     headers={"User-Agent": "signal-lab/0.1 (evaluation project)"})
    r.raise_for_status()
    return r.json()
