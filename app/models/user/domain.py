from pydantic import BaseModel, Field


class User(BaseModel):
    user_id: str = Field(..., description="UserID、LINEのIDを利用する")
    score: int = Field(0, description="通院歴")
