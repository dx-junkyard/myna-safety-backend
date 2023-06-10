from typing import List
from app.models.user_report.domain import UserReportModel
from app.models.user_report.update_user_report import (
    UpdateUserReportRequestDto,
)
from app.models.user_report_feedback.domain import (
    UserReportFeedbackComment,
    UserReportFeedbackReaction,
)
from google.cloud import firestore

from app.repositories import db

COLLECTION_PREFIX = "user_report"


def add_user_report(id: str, content: UserReportModel):
    """ユーザレポートの追加

    Args:
        id (str): ユーザレポートid
        content (UserReportModel): 登録するユーザレポートの内容
    """
    db.add(collection=COLLECTION_PREFIX, id=id, content=content.dict())


def fetch_user_report(id: str) -> UserReportModel:
    """ユーザレポートの検索

    Args:
        id (str): ユーザレポートid
    """
    return UserReportModel.parse_obj(
        db.fetch(collection=COLLECTION_PREFIX, id=id)
    )


def add_comment(id: str, content: UserReportFeedbackComment):
    """コメントを登録する

    Args:
        id (str): _description_
        content (UserReportFeedbackComment): _description_
    """
    ur = fetch_user_report(id)
    ur.user_report_feedback_comments.append(content)

    db.add(collection=COLLECTION_PREFIX, id=id, content=ur.dict())


def add_reaction(id: str, content: UserReportFeedbackReaction):
    """リアクションを登録する

    Args:
        id (str): _description_
        content (UserReportFeedbackComment): _description_
    """
    ur = fetch_user_report(id)
    ur.user_report_feedback_reactions.append(content)

    db.add(collection=COLLECTION_PREFIX, id=id, content=ur.dict())


def update_user_report(id: str, content: UpdateUserReportRequestDto):
    """ユーザレポートの更新

    Args:
        id (str): ユーザレポートid
        content (UserReportModel): 登録するユーザレポートの内容
    """
    user_report_dict = db.fetch(collection=COLLECTION_PREFIX, id=id)

    # 差分のあるアイテムを見つける
    patch_items = [
        k for k in content.dict().keys() if content.dict()[k] is not None
    ]

    # もし差分アイテムが見つかれば、UserPatchModelから新しい辞書を生成する
    patch_dict = {k: v for k, v in content.dict().items() if k in patch_items}

    # 新しい差分のある辞書を元のユーザー情報にマージする
    updated_user_report_dict = {**user_report_dict, **patch_dict}
    db.add(
        collection=COLLECTION_PREFIX, id=id, content=updated_user_report_dict
    )


def list_user_report() -> List[UserReportModel]:
    """全て取得する

    Returns:
        List[UserReportModel]: 一覧
    """

    user_reports_ref = db().collection(COLLECTION_PREFIX)

    # 直近100件のみ表示
    user_reports = (
        user_reports_ref.order_by(
            "report_score", direction=firestore.Query.DESCENDING
        )
        .limit(100)
        .stream()
    )

    return [UserReportModel.parse_obj(r.to_dict()) for r in user_reports]
