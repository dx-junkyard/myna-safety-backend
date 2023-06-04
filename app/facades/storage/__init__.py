from google.cloud import storage
from google.cloud.storage.bucket import Bucket

import app.config as config


class GoogleCloudStorage:
    def __init__(self, cred_path: str) -> None:
        _storage_client = storage.Client.from_service_account_json(cred_path)
        self._bucket = _storage_client.bucket(
            config.GOOGLE_CLOUD_STORAGE_BUCKET_NAME
        )
        print(f"GCS Initialize Complete!. bucket name: {self._bucket.name}")

    def __call__(
        self,
    ) -> Bucket:
        return self._bucket


gcs = GoogleCloudStorage(config.CRED_PATH)
