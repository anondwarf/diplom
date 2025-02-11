from dotenv import load_dotenv
from os import getenv


class _Environment(object):
    load_dotenv()

    BASE_URL = getenv("BASE_URL", "localhost:8000")
    FIREFOX_DRIVER = "/usr/bin/firefox"
    CHROME_DRIVER = "/usr/bin/google-chrome"


environment = _Environment()