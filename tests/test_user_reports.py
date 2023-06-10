import json
from fastapi.testclient import TestClient
import pytest
from app.main import app


client = TestClient(app)


@pytest.mark.parametrize(
    "content", ["", "家族と逸れました、洪水の中一人で孤立していて大変です。誰か助けてください"]
)
def test_post_user_report(mocker, content):
    # Given
    test_user_report_id = "xyz"
    request_body = {
        "user_id": "test_user_id",
        "location": {"longitude": 123, "latitude": 943},
        "content": content,
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


@pytest.mark.parametrize(
    "content", ["", "建物は少し損傷していますが、怪我はありません。食糧も確保できています。"]
)
def test_put_user_report(mocker, content):
    test_post_user_report(mocker, content)
    # Given
    user_report_id = "xyz"
    request_body = {
        "location": {"longitude": 234, "latitude": 987},
        "content": content,
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
    test_post_user_report(mocker, "")
    # When
    response = client.get("/report")

    # Then
    assert response.status_code == 200
    response_body = response.json()
    assert len(response_body.get("user_reports")) > 0
