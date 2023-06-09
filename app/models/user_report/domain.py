from datetime import datetime
from enum import Enum
from typing import Union
from pydantic import BaseModel, Field
from app.models.user_report_feedback.domain import UserReportFeedbackComment

from app.utils import now


class Location(BaseModel):
    longitude: float = Field(..., description="経度")
    latitude: float = Field(..., description="緯度")


class ReportLevel(str, Enum):
    HIGHT = "High"  # 重度
    MIDDLE = "Middle"  # 中度
    LOW = "Low"  # 軽度


class ReportStatus(str, Enum):
    NO_ASSIGN = "NO ASSIGN"  # 未着手
    IN_PROGRESS = "IN PROGRESS"  # 進行中
    COMPLETE = "COMPLETE"  # 完了
    PENDING = "PENDING"  # 着手しない


class UserReportModel(BaseModel):
    user_id: str = Field(..., description="UserID、LINEのIDなど？")
    user_report_id: str = Field(..., description="申告ID")
    location: Location = Field(..., description="申告者の位置情報")
    content: str = Field(..., description="報告内容、選択式にする？")
    image_url: Union[str, None] = Field(None, description="画像のURL")

    report_level: ReportLevel = Field(..., description="申告内容の深刻度")
    report_status: ReportStatus = Field(..., description="申告内容の状態")

    created_at: datetime = Field(now(), description="作成時間")
    updated_at: Union[datetime, None] = Field(None, description="最終更新時間")

    user_report_feedback_comments: list[UserReportFeedbackComment] = Field(
        [], description="申告に対するフィードバックコメント"
    )
