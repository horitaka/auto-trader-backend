from app.infrastructure.externalapi.klines import Interval, PriceType, get_klines

result = get_klines("USD_JPY", PriceType.BID, Interval.ONE_DAY, "2023")
print(result)
