from typing import Union
from app.models.user.domain import User
from app.repositories import db

COLLECTION_PREFIX = "user"


def add_user(id: str, content: User):
    """ユーザId追加

    Args:
        id (str): ユーザId
        content (UserReportModel): 登録するユーザレポートの内容
    """
    db.add(collection=COLLECTION_PREFIX, id=id, content=content.dict())


def fetch_user(id: str) -> Union[User, None]:
    """ユーザの検索

    Args:
        id (str): ユーザid
    """
    user = db.fetch(collection=COLLECTION_PREFIX, id=id)
    return User.parse_obj(user) if user else None
