import uuid
from datetime import datetime, timedelta, timezone

from geopy.geocoders import Nominatim


def generate_id_str() -> str:
    return str(uuid.uuid4())


def now() -> datetime:
    return datetime.now(timezone(timedelta(hours=9)))


def timestamp_(dt: datetime):
    return datetime.timestamp(dt)


def timestamp_to_datetime(ts: float):
    return datetime.fromtimestamp(ts, timezone.utc)


def convert_address(location):
    """緯度経度を位置情報に変換する

    Args:
        location (_type_): _description_

    Returns:
        _type_: _description_
    """
    return (
        Nominatim(user_agent="test")
        .reverse(f"{location.latitude}, {location.longitude}")
        .address
    )
