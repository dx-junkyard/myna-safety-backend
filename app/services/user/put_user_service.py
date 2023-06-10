import json
from app.models.user.domain import User
from app.models.user.update_user_report import UpdateUserRequest
from app.repositories import user
from app.facades.myna_api import myna_api

MYNA_DUMMY_ID = "2-1"


async def execute(
    line_user_id: str,
    request: UpdateUserRequest,
):
    response = myna_api.request(request.pass_phrase, MYNA_DUMMY_ID)
    medical_treatment_history = json.loads(response.content)[0]["わたしの情報"][
        "診療・薬剤情報"
    ]["受診歴"]
    score = len(medical_treatment_history) / 2

    content = User.parse_obj({"user_id": line_user_id, "score": score})

    user.add_user(line_user_id, content)

    return line_user_id
