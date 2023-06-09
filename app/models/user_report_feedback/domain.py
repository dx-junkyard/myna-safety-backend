from datetime import datetime
from typing import Union
from pydantic import BaseModel, Field

from app.utils import now


class Location(BaseModel):
    longitude: float = Field(..., description="経度")
    latitude: float = Field(..., description="緯度")


class UserReportFeedbackComment(BaseModel):
    """ユーザリクエストに対する返信に含める項目"""

    user_report_feedback_comment_id: str = Field(..., description="コメントID")
    user_id: str = Field(..., description="投稿者のユーザID")
    location: Union[Location, None] = Field(None, description="投稿者の位置情報")
    comment: str = Field("", description="コメント内容")

    created_at: datetime = Field(now(), description="作成時間")
    updated_at: Union[datetime, None] = Field(None, description="最終更新時間")


class UserReportFeedbackReaction(BaseModel):
    """ユーザリクエストに対するリアクションに含める項目"""

    user_report_feedback_reaction_id: str = Field(..., description="リアクションID")
    user_id: str = Field(..., description="投稿者のユーザID")
    location: Union[Location, None] = Field(None, description="投稿者の位置情報")
    reaction: str = Field(
        "", description="リアクション内容(フロントで表示を切り替えるためここでは任意の文字列を入れる)"
    )

    created_at: datetime = Field(now(), description="作成時間")
    updated_at: Union[datetime, None] = Field(None, description="最終更新時間")
