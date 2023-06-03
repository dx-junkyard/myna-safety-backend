from os import environ
from dotenv import load_dotenv

load_dotenv(verbose=True)

LINE_CHANNEL_ACCESS_TOKEN = environ.get("LINE_CHANNEL_ACCESS_TOKEN", "")
LINE_CHANNEL_SECRET = environ.get("LINE_CHANNEL_SECRET", "")
OPENAI_API_KEY = environ.get("OPENAI_API_KEY", "")

MYNA_API_URL = environ.get("MYNA_API_URL", "")
MYNA_API_TOKEN = environ.get("MYNA_API_TOKEN", "")
