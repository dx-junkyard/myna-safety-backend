import requests
from app import config


class MynaApi:
    def __init__(self) -> None:
        self.headers = {
            "Authorization": f"Bearer {config.MYNA_API_TOKEN}",
        }
        self.files = {
            "auth_code": (None, "9876"),
        }

    def _set_auth_code(self, code: str):
        return {"auth_code": (None, f"{code}")}

    def request(self, code: str, path: str) -> requests.Response:
        """マイナポータルAPIにリクエストする

        Args:
            code (str): 利用者証明用電子証明書のパスワード４桁
            path (str): リクエスト内容のパス

        Returns:
            requests.Response: APIの応答結果
        """
        return requests.post(
            f"{config.MYNA_API_URL}{path}",
            headers=self.headers,
            files=self._set_auth_code(code),
        )


ma = MynaApi()
print(ma.request("1234", "90").json())
print(ma.request("1234", "1").json())
