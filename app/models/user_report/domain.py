from enum import Enum
from pydantic import BaseModel, Field


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
    location: Location = Field(..., description="申告者の位置情報")
    content: str = Field(..., description="報告内容、選択式にする？")
    report_level: ReportLevel = Field(..., description="申告内容の深刻度")
    report_status: ReportStatus = Field(..., description="申告内容の状態")
