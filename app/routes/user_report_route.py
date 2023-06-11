from typing import Optional
from fastapi import APIRouter, Body, File, UploadFile
from sqlalchemy import true
from app.facades.line_bot.line_message import push_message
from app.models.user_report.list_user_reports import ListUserReportResponse
from app.models.user_report.entry_user_report import (
    EntryUserReportRequest,
    EntryUserReportResponse,
)
from app.models.user_report.update_user_report import (
    UpdateUserReportRequest,
    UpdateUserReportResponse,
)
from app.repositories.user_report import fetch_user_report
from app.services.report import (
    entry_user_report_service,
    list_user_report_service,
    update_user_report_service,
)
from linebot.models import TextSendMessage

import json

user_report_router = APIRouter(prefix="/report", tags=["report"])


@user_report_router.post("", response_model=EntryUserReportResponse)
async def post_user_report(
    request: EntryUserReportRequest = Body(...),
    file: Optional[UploadFile] = File(None),
):
    """ユースケース1: ユーザがHelpを申請する"""
    user_report_id = await entry_user_report_service.execute(request, file)
    return EntryUserReportResponse(user_report_id=user_report_id)


@user_report_router.put(
    "/{user_report_id}", response_model=UpdateUserReportResponse
)
async def put_user_report(
    user_report_id: str,
    request: UploadFile = File(...),
    file: Optional[UploadFile] = File(None),
):
    """ユースケース3: ユーザがヘルプ情報を更新する"""
    json_data = json.loads(request.file.read())
    userRequest = UpdateUserReportRequest.parse_obj(json_data)

    user_report_id = await update_user_report_service.execute(
        user_report_id, userRequest, file
    )

    user_id = fetch_user_report(user_report_id).user_id
    push_message(user_id, TextSendMessage(text="被害状況報告の更新が完了しました"))

    return UpdateUserReportResponse(user_report_id=user_report_id)


@user_report_router.get("", response_model=ListUserReportResponse)
async def get_user_reports():
    """ユースケース2: 申告内容の一覧を取得する"""
    list_user_report = list_user_report_service.execute()
    return ListUserReportResponse(user_reports=list_user_report)


__dummy_user_report_router = APIRouter(
    prefix="/__dummy_report", deprecated=true
)


@__dummy_user_report_router.post("__dummy_post", deprecated=true)
async def _dummy_post_user_report(
    request: EntryUserReportRequest,
):
    """openapi-generatorの生成用"""
    pass


@__dummy_user_report_router.put("__dummy_put", deprecated=true)
async def _dummy_put_user_report(
    request: UploadFile,
):
    """openapi-generatorの生成用"""
    pass
