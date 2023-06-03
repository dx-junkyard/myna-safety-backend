import uuid
from datetime import datetime, timedelta, timezone


def generate_id_str() -> str:
    return str(uuid.uuid4())


def now() -> datetime:
    return datetime.now(timezone(timedelta(hours=9)))


def timestamp_(dt: datetime):
    return datetime.timestamp(dt)


def timestamp_to_datetime(ts: float):
    return datetime.fromtimestamp(ts, timezone.utc)
