from app.models.user_report.domain import UserReportModel
from app.models.user_report.update_user_report import UpdateUserReportRequest
from app.repositories import user_report


def execute(request_id: str, request: UpdateUserReportRequest) -> str:
    """ユーザレポートを更新する

    Args:
        request_id (str): 更新するユーザレポートのID
        request (UpdateUserReportRequest): 更新内容

    Returns:
        str: 更新が完了したユーザレポートのID
    """
    update_user_report_model: UserReportModel = UserReportModel.parse_obj(
        {
            **request.dict(),
        },
    )
    user_report.update_user_report(request_id, update_user_report_model)

    return request_id
