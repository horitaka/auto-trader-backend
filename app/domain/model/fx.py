from dataclasses import dataclass


@dataclass
class OHLC:
    timestamp: str
    open: float
    high: float
    low: float
    close: float
