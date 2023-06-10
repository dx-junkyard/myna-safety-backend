from fastapi.testclient import TestClient

from app.models.user.update_user_report import (
    UpdateUserRequest,
)

from app.main import app

client = TestClient(app)


def test_put_user():
    request = UpdateUserRequest(pass_phrase="1234")

    # create a mock response object
    line_user_id = "test_line_user_id"
    # expected_response = UpdateUserResponse(line_user_id=line_user_id)

    # make the HTTP request
    response = client.put(f"/user/{line_user_id}", data=request.json())

    # assert that the response has the expected status code and body
    assert response.status_code == 200
    # assert response.json() == expected_response.dict()
