import json
from pathlib import Path

_DEFAULT_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "project",
}

_CONFIG_FILE = Path(__file__).with_name("db_config.json")


def load_db_config() -> dict:
    """Load DB config from db_config.json if present, else return defaults.

    The JSON file can contain any of: host, user, password, database.
    Missing keys fall back to sensible defaults.
    """
    if _CONFIG_FILE.is_file():
        try:
            with _CONFIG_FILE.open("r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, dict):
                cfg = _DEFAULT_CONFIG.copy()
                cfg.update({k: v for k, v in data.items() if k in cfg})
                return cfg
        except Exception:
            # On any error, fall back to defaults
            return _DEFAULT_CONFIG.copy()

    return _DEFAULT_CONFIG.copy()
