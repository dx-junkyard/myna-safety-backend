import os

from PIL import Image
from app.facades.storage import gcs
import app.config as config


FOLDER_NAME = "thumbnail"
TEMP_FOLDER_NAME = "./temp/thumbnail"
IMAGE_URL = f"https://storage.cloud.google.com/{config.GOOGLE_CLOUD_STORAGE_BUCKET_NAME}"

ASPECT_RATIO = 416, 312  # アスペクト比 w:h = 4:3とする


def upload(
    destination_blob_name: str,
    image: Image,
) -> str:
    temp_image_filename = _save_temp_image(destination_blob_name, image)
    try:
        path_name = f"{FOLDER_NAME}/{destination_blob_name}"
        blob = gcs().blob(path_name)

        blob.upload_from_filename(
            temp_image_filename,
        )

        print(f"File uploaded to {destination_blob_name}.")
        return f"{IMAGE_URL}/{path_name}"
    except Exception as e:
        print(f"upload error. {e}")
    finally:
        os.remove(temp_image_filename)


def _save_temp_image(destination_blob_name, image):
    """アップロードのため一時的にローカルに保存する"""
    os.makedirs(TEMP_FOLDER_NAME, exist_ok=True)
    temp_image_filename = f"{TEMP_FOLDER_NAME}/{destination_blob_name}"

    image.thumbnail(ASPECT_RATIO, Image.Resampling.LANCZOS)
    image.save(temp_image_filename)
    return temp_image_filename


def download(destination_blob_name: str) -> bytes:
    blob = gcs().blob(f"{FOLDER_NAME}/{destination_blob_name}")

    return blob.download_as_bytes()
