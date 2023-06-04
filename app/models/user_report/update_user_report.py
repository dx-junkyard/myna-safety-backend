from datetime import datetime
from typing import Union
from pydantic import BaseModel, Field

from app.models.user_report.domain import (
    Location,
    ReportLevel,
    ReportStatus,
)


class UpdateUserReportRequest(BaseModel):
    location: Location = Field(..., description="申告者の位置情報")
    content: str = Field(..., description="報告内容、選択式にする？")
    report_level: ReportLevel = Field(..., description="申告内容の深刻度")
    report_status: ReportStatus = Field(..., description="申告内容の状態")


class UpdateUserReportRequestDto(UpdateUserReportRequest):
    updated_at: Union[datetime, None] = Field(None, description="最終更新時間")


class UpdateUserReportResponse(BaseModel):
    user_request_id: str = Field(..., description="発行された申告ID")
