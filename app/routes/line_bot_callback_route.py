from fastapi import APIRouter, BackgroundTasks, Header, Request
from linebot import WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent,
    TextSendMessage,
    QuickReply,
    QuickReplyButton,
    LocationAction,
)
from starlette.exceptions import HTTPException
from app import config
from app.facades.chatgpt import ChatGPT
from app.facades.line_bot import line_message
from app.services.report.entry_user_report_service import add_report


line_bot_callback_router = APIRouter(prefix="", tags=["line_bot"])
handler = WebhookHandler(config.LINE_CHANNEL_SECRET)
chat = ChatGPT()


@line_bot_callback_router.post("/callback")
async def callback(
    request: Request,
    background_tasks: BackgroundTasks,
    x_line_signature=Header(None),
):
    """Line Bot用のエンドポイントです"""
    body = await request.body()

    try:
        background_tasks.add_task(
            handler.handle, body.decode("utf-8"), x_line_signature
        )
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    return "ok"


@handler.add(MessageEvent)
def handle_message(event):
    reply = None

    if event.type == "message" and event.message.type == "location":
        id = save_location(event)
        reply = [
            TextSendMessage(text="位置情報の入力を確認しました"),
            TextSendMessage(text="続いて被害状況を下記のフォームから入力してください"),
            TextSendMessage(text=get_liff_url(id)),
        ]
    elif event.type != "message" or event.message.type != "text":
        reply = TextSendMessage(text="申し訳ありません。入力を受け付けることができませんでした")
    else:
        reply = create_message(event.message.text)

    line_message.reply_message(event.reply_token, messages=reply)


def get_liff_url(id: str) -> str:
    return f"https://liff.line.me/1661252954-Gl9zJ1wY/?report_id={id}"


def create_message(msg: str | None):
    if msg == "救援を要請する":
        reply = [
            QuickReplyButton(action=LocationAction(label="位置情報を送信する")),
        ]
        return [
            TextSendMessage(text="救援要請を受け付けました"),
            TextSendMessage(
                text="被害の発生した場所を教えてください", quick_reply=QuickReply(items=reply)
            ),
        ]
    elif msg is not None:
        return TextSendMessage(text=chat.request(msg))
    else:
        return TextSendMessage(text="申し訳ありません。入力を受け付けることができませんでした")


def save_location(event):
    return add_report(
        # TODO: ハッシュ化すると通知できなくなるので解除
        event.source.user_id,
        event.message.latitude,
        event.message.longitude,
    )
