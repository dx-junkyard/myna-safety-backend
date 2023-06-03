# Myna Safety Backend

マイナポータルハッカソンのバックエンドです。

## 概要

本アプリケーションは下記の URL で起動しています。

- https://myna-safety-backend-r2dn2ftu7a-uc.a.run.app/

API のインターフェースは下記の SwaggerDoc から確認してください

- [Myna Safety Backend API DOCS](https://myna-safety-backend-r2dn2ftu7a-uc.a.run.app/docs)

全体構成

![全体構成](docs/architecture.png)

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
