from app.models.user_report_feedback.domain import UserReportFeedbackComment
from app.models.user_report_feedback.entry_user_report_feedback import (
    EntryUserReportFeedBackCommentRequest,
)
from app.repositories import user_report
from app.utils import generate_id_str


async def execute(
    report_id: str, request: EntryUserReportFeedBackCommentRequest
):
    id = generate_id_str()

    content = UserReportFeedbackComment.parse_obj(
        {**request.dict(), "user_report_feedback_comment_id": id}
    )
    user_report.add_comment(report_id, content)

    return id
