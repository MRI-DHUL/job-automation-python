import yaml
from pathlib import Path

CFG_PATH = Path("config/config.yaml")


def load_config():
    with open(CFG_PATH, "r") as f:
        return yaml.safe_load(f)