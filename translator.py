import json

def load_translations(lang="nl"):
    with open(f"translations/{lang}.json", encoding='utf-8') as f:
        return json.load(f)

def t(key, lang="nl"):
    translations = load_translations(lang)
    return translations.get(key, key)
