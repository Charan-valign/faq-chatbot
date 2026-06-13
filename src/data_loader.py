import json

def load_faqs(path="data/faqs.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)