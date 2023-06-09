from fastapi import APIRouter
from app.models.user_report_feedback.entry_user_report_feedback import (
    EntryUserReportFeedBackCommentRequest,
    EntryUserReportFeedBackCommentResponse,
)
from app.services.report_feedback import (
    entry_user_report_feedback_comment_service,
)

user_report_feedback_router = APIRouter(prefix="/report", tags=["report"])


@user_report_feedback_router.post(
    "/{report_id}/feedback_comment",
    response_model=EntryUserReportFeedBackCommentResponse,
)
async def post_user_report_feedback_comment(
    report_id: str,
    request: EntryUserReportFeedBackCommentRequest,
):
    """ユーザのヘルプにコメントをつける"""
    user_report_feedback_id = (
        await entry_user_report_feedback_comment_service.execute(
            report_id, request
        )
    )
    return EntryUserReportFeedBackCommentResponse(
        user_report_feedback_comment_id=user_report_feedback_id
    )
