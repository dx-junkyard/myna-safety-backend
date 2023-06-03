from fastapi import APIRouter
from app.models.user_report.list_user_reports import ListUserReportResponse
from app.models.user_report.entry_user_report import (
    EntryUserReportRequest,
    EntryUserReportResponse,
)
from app.models.user_report.update_user_report import (
    UpdateUserReportRequest,
    UpdateUserReportResponse,
)


user_report_router = APIRouter(prefix="/report", tags=["report"])


@user_report_router.post("", response_model=EntryUserReportResponse)
async def post_user_report(request: EntryUserReportRequest):
    """ユースケース1: ユーザがHelpを申請する"""
    return EntryUserReportResponse(request_id="sample")


@user_report_router.put(
    "/{request_id}", response_model=UpdateUserReportResponse
)
async def put_user_report(request_id: str, request: UpdateUserReportRequest):
    """ユースケース3: ユーザがヘルプ情報を更新する"""
    return UpdateUserReportResponse(request_id=request_id)


@user_report_router.get("", response_model=ListUserReportResponse)
async def get_user_reports():
    """ユースケース2: 申告内容の一覧を取得する"""
    return []
