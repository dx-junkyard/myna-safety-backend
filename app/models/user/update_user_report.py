from pydantic import BaseModel, Field


class UpdateUserRequest(BaseModel):
    pass_phrase: str = Field(..., description="マイナポータルAPIの暗証番号")


class UpdateUserResponse(BaseModel):
    user_id: str = Field(..., description="ユーザID")
