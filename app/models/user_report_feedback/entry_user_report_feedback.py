from typing import Union
from pydantic import BaseModel, Field

from app.models.user_report.domain import Location


class EntryUserReportFeedBackCommentRequest(BaseModel):
    user_id: str = Field(..., description="投稿者のユーザID")
    location: Union[Location, None] = Field(None, description="投稿者の位置情報")
    comment: str = Field("", description="コメント内容")


class EntryUserReportFeedBackCommentResponse(BaseModel):
    user_report_feedback_comment_id: str = Field(..., description="コメントID")
