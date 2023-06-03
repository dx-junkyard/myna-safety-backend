# Myna Safety Backend

マイナポータルハッカソンのバックエンドです。

## Quick Start

はじめに仮想環境と必要ライブラリをインストーする。

```sh:
poetry install
```

環境変数を更新する。

```sh:
source .env
```

下記のコマンドで起動する

```sh:
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
```
