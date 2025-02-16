from dotenv import load_dotenv
from os import getenv
from pathlib import Path

load_dotenv()


class _Environment(object):

    BASE_URL = getenv("BASE_URL", "http://localhost:8000")
    ROOT_PATH = Path(__file__).resolve().parents[1]
    PATH_DRIVER = ROOT_PATH / "data" / "drivers"
    USER_LOGIN = getenv("USER__LOGIN", "test_user")
    USER_PASSWORD = getenv("USER__PASSWORD", "test_password")


environment = _Environment()
