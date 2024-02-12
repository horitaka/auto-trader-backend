from dataclasses import dataclass
from enum import Enum

import requests


class PriceType(Enum):
    ASK = "ASK"
    BID = "BID"


class Interval(Enum):
    ONE_MINUTE = "1min"
    FIVE_MINUTE = "5min"
    TEN_MINUTE = "10min"
    FIFTEEN_MINUTE = "15min"
    THIRTY_MINUTE = "30min"
    ONE_HOUR = "1hour"
    FOUR_HOUR = "4hour"
    EIGHT_HOUR = "8hour"
    TWELVE_HOUR = "12hour"
    ONE_DAY = "1day"
    ONE_WEEK = "1week"
    ONE_MONTH = "1month"


GMO_PUBLIC_API_ENDPOINT = "https://forex-api.coin.z.com/public"


@dataclass
class OHLCV:
    openTime: int
    open: float
    high: float
    low: float
    close: float


@dataclass
class Klines:
    status: int
    data: list[OHLCV]
    responsetime: str


def get_klines(symbol: str, price_type: PriceType, interval: Interval, date: str) -> Klines:
    url = f"{GMO_PUBLIC_API_ENDPOINT}/v1/klines?symbol={symbol}&priceType={price_type.value}&interval={interval.value}&date={date}"  # noqa: E501

    response = requests.get(url)
    return response.json()
