from os import getenv
from json import load
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class _Environment:

    def __init__(self):
        self._user = None

    _ROOT_PATH = Path(__file__).parents[2]
    USER_FILE = _ROOT_PATH / "data" / "users.json"
    BASE_URL: str = getenv("BASE_URL", "http://localhost:8000")

    def _get_user_data(self):
        with open(self.USER_FILE, "r") as file:
            self._user = load(file)

    @property
    def user(self):
        if not self._user:
            self._get_user_data()
        return self._user


environment = _Environment()
