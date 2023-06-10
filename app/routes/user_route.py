from fastapi import APIRouter

from app.models.user.update_user_report import (
    UpdateUserRequest,
    UpdateUserResponse,
)
from app.services.user import put_user_service

user_router = APIRouter(prefix="/user", tags=["user"])


@user_router.put(
    "/{line_user_id}",
    response_model=UpdateUserResponse,
)
async def put_user(
    line_user_id: str,
    request: UpdateUserRequest,
):
    """ユーザのヘルプにコメントをつける"""
    line_user_id = await put_user_service.execute(line_user_id, request)
    return UpdateUserResponse(user_id=line_user_id)
