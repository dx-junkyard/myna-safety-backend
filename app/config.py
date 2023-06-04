from os import environ
from dotenv import load_dotenv

load_dotenv(verbose=True)

# LINEBotの認証情報
LINE_CHANNEL_ACCESS_TOKEN = environ.get("LINE_CHANNEL_ACCESS_TOKEN", "")
LINE_CHANNEL_SECRET = environ.get("LINE_CHANNEL_SECRET", "")

# OpenAIのAPIキー
OPENAI_API_KEY = environ.get("OPENAI_API_KEY", "")

# マイナポータルAPIの接続情報
MYNA_API_URL = environ.get("MYNA_API_URL", "")
MYNA_API_TOKEN = environ.get("MYNA_API_TOKEN", "")

# FireStoreの認証キー
CRED_PATH = environ.get("CRED_PATH", "app/key/credential.json")
GOOGLE_CLOUD_STORAGE_BUCKET_NAME = environ.get(
    "GOOGLE_CLOUD_STORAGE_BUCKET_NAME", "myna-safety"
)
