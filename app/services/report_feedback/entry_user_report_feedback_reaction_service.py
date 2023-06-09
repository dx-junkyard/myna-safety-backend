from app.models.user_report_feedback.domain import (
    UserReportFeedbackReaction,
)
from app.models.user_report_feedback.entry_user_report_feedback_reaction import (
    EntryUserReportFeedBackReactionRequest,
)
from app.repositories import user_report
from app.utils import generate_id_str


async def execute(
    report_id: str, request: EntryUserReportFeedBackReactionRequest
):
    id = generate_id_str()

    content = UserReportFeedbackReaction.parse_obj(
        {**request.dict(), "user_report_feedback_reaction_id": id}
    )
    user_report.add_reaction(report_id, content)

    return id
