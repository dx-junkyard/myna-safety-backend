from fastapi.testclient import TestClient
from app.main import app
from app.models.user_report_feedback.entry_user_report_feedback import (
    EntryUserReportFeedBackCommentRequest,
)

client = TestClient(app)


def test_post_user_report_feedback_comment(mocker):
    report_id = "abc"

    test_user_report_id = "cde"
    mocker.patch(
        "app.services.report_feedback.entry_user_report_feedback_comment_service.generate_id_str",
        return_value=test_user_report_id,
    )

    request = EntryUserReportFeedBackCommentRequest(
        comment="test_comment",
        user_id="test_user",
    )
    response = client.post(
        f"/report/{report_id}/feedback_comment", data=request.json()
    )

    assert response.status_code == 200
    assert response.json() == {
        "user_report_feedback_comment_id": test_user_report_id
    }
