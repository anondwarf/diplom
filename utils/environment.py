from dotenv import load_dotenv
from os import getenv
from pathlib import Path


class _Environment(object):
    load_dotenv()

    BASE_URL = getenv("BASE_URL", "http://localhost:8000")
    ROOT_PATH = Path(__file__).resolve().parents[1]
    PATH_DRIVER = ROOT_PATH / "data" / "drivers"


environment = _Environment()
