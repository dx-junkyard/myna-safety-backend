import json
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_post_user_report(mocker):
    # Given
    test_user_report_id = "abc"
    request_body = {
        "user_id": 1,
        "location": {"longitude": 123, "latitude": 943},
        "content": "Need help with something",
    }
    mocker.patch(
        "app.services.report.entry_user_report_service.generate_id_str",
        return_value=test_user_report_id,
    )

    # When
    response = client.post(
        "/report",
        files={
            "request": (
                None,
                json.dumps(request_body),
            ),
            "file": open("./tests/assets/sample.jpeg", "rb"),
        },
    )

    # Then
    assert response.status_code == 200
    response_body = response.json()
    assert "user_report_id" in response_body


def test_put_user_report(mocker):
    test_post_user_report(mocker)
    # Given
    user_report_id = "abc"
    request_body = {
        "location": {"longitude": 234, "latitude": 987},
        "content": "Need help with something",
        "report_level": "High",
        "report_status": "COMPLETE",
    }

    # When
    response = client.put(
        f"/report/{user_report_id}",
        files={
            "request": (
                None,
                json.dumps(request_body),
            ),
            "file": open("./tests/assets/sample.jpeg", "rb"),
        },
    )

    # Then
    assert response.status_code == 200
    response_body = response.json()
    assert "user_report_id" in response_body


def test_get_user_reports(mocker):
    test_post_user_report(mocker)
    # When
    response = client.get("/report")

    # Then
    assert response.status_code == 200
    response_body = response.json()
    assert len(response_body.get("user_reports")) > 0
