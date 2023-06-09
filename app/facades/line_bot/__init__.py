from linebot import LineBotApi
from app import config


line_bot_api = LineBotApi(config.LINE_CHANNEL_ACCESS_TOKEN)
