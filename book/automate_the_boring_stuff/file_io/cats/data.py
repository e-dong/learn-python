import json
from cats import get_asset_path

def load_data():
    with open(get_asset_path() / 'data.json', mode="r", encoding="utf-8") as f:
        return json.load(f)
        
