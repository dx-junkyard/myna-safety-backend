from io import BytesIO
from typing import Optional
from fastapi import UploadFile
from app.facades.storage import thumbnail
from app.models.user_report.domain import (
    Location,
    ReportLevel,
    ReportStatus,
    UserReportModel,
)
from app.models.user_report.entry_user_report import EntryUserReportRequest
from app.repositories import user_report
from app.utils import generate_id_str, now
from PIL import Image


async def execute(
    request: EntryUserReportRequest, file: Optional[UploadFile]
) -> str:
    """ユーザレポートを登録する

    Args:
        request (EntryUserReportRequest): 登録するユーザレポートの内容

    Returns:
        str: 登録されたユーザレポートのID
    """
    id = generate_id_str()

    if file:
        thumbnail_url = await _upload_thumbnail_image(id, file=file)
    else:
        thumbnail_url = None

    user_report_model: UserReportModel = UserReportModel.parse_obj(
        {
            **request.dict(),
            "user_report_id": id,
            "report_level": ReportLevel.MIDDLE,
            "report_status": ReportStatus.NO_ASSIGN,
            "created_at": now(),
            "image_url": thumbnail_url,
        },
    )
    user_report.add_user_report(id, user_report_model)
    return id


def add_report(user_id: str, latitude: float, longitude: float) -> str:
    id = generate_id_str()

    user_report_model: UserReportModel = UserReportModel.parse_obj(
        {
            "user_id": user_id,  # TODO: 仮の値を入れている
            "user_report_id": id,
            "location": Location(latitude=latitude, longitude=longitude),
            "content": "",
            "image_url": None,
            "report_level": ReportLevel.MIDDLE,
            "report_status": ReportStatus.NO_ASSIGN,
            "created_at": now(),
        },
    )
    user_report.add_user_report(id, user_report_model)
    return id


async def _upload_thumbnail_image(id: str, file: UploadFile) -> str:
    """pdfからサムネイル画像を生成しGoogle Cloud Storageに保存する"""
    thumbnail_filename = f"{id}.jpeg"
    data = await file.read()
    img_pil = Image.open(BytesIO(data))
    image_url = thumbnail.upload(
        destination_blob_name=thumbnail_filename, image=img_pil
    )
    return image_url
