from typing import List
from app.models.user_report.domain import UserReportModel
from app.repositories import user_report


def execute() -> List[UserReportModel]:
    """ユーザレポートを全権取得

    Returns:
        List[UserReportModel]: 取得するユーザレポートの一覧
    """
    return user_report.list_user_report()
