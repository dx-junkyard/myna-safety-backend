from typing import Union
from pydantic import BaseModel, Field

from app.models.user_report.domain import Location


class EntryUserReportFeedBackReactionRequest(BaseModel):
    user_id: str = Field(..., description="投稿者のユーザID")
    location: Union[Location, None] = Field(None, description="投稿者の位置情報")
    reaction: str = Field(
        "", description="リアクション内容(フロントで表示を切り替えるためここでは任意の文字列を入れる)"
    )


class EntryUserReportFeedBackReactionResponse(BaseModel):
    user_report_feedback_reaction_id: str = Field(..., description="リアクションID")
