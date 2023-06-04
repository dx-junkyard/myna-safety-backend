import json
from pydantic import BaseModel, Field

from app.models.user_report.domain import Location


class EntryUserReportRequest(BaseModel):
    """ユーザ通知リクエストに含める項目"""

    user_id: str = Field(..., description="UserID、LINEのIDなど？")
    location: Location = Field(..., description="申告者の位置情報")
    content: str = Field(..., description="報告内容、選択式にする？")

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value


class EntryUserReportResponse(BaseModel):
    user_request_id: str = Field(..., description="発行された申告ID")
