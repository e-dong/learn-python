from pathlib import Path

def get_asset_path():
    module_path = Path(list(__path__)[0])
    return module_path / 'assets'
