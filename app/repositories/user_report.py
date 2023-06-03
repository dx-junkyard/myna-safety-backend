from typing import List
from app.models.user_report.domain import UserReportModel

from app.repositories import db

COLLECTION_PREFIX = "user_report"


def add_user_report(id: str, content: UserReportModel):
    """ユーザレポートの追加

    Args:
        id (str): ユーザレポートid
        content (UserReportModel): 登録するユーザレポートの内容
    """
    db.add(collection=COLLECTION_PREFIX, id=id, content=content.dict())


def update_user_report(id: str, content: UserReportModel):
    """ユーザレポートの更新

    Args:
        id (str): ユーザレポートid
        content (UserReportModel): 登録するユーザレポートの内容
    """
    db.add(collection=COLLECTION_PREFIX, id=id, content=content.dict())


def list_user_report() -> List[UserReportModel]:
    """全て取得する

    Returns:
        List[UserReportModel]: 一覧
    """

    user_reports = db().collection(COLLECTION_PREFIX).stream()
    return [UserReportModel.parse_obj(r.to_dict()) for r in user_reports]
