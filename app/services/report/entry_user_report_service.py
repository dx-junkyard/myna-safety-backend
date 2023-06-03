from app.models.user_report.domain import (
    ReportLevel,
    ReportStatus,
    UserReportModel,
)
from app.models.user_report.entry_user_report import EntryUserReportRequest
from app.repositories import user_report
from app.utils import generate_id_str, now


def execute(request: EntryUserReportRequest) -> str:
    """ユーザレポートを登録する

    Args:
        request (EntryUserReportRequest): 登録するユーザレポートの内容

    Returns:
        str: 登録されたユーザレポートのID
    """
    id = generate_id_str()

    user_report_model: UserReportModel = UserReportModel.parse_obj(
        {
            **request.dict(),
            "report_level": ReportLevel.MIDDLE,
            "report_status": ReportStatus.NO_ASSIGN,
            "created_at": now(),
        },
    )
    user_report.add_user_report(id, user_report_model)
    return id
