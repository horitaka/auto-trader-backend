from app.application.service.technical_indicators import calc_moving_average_line
from kline_response_sample import response

values = [float(item.get("close")) for item in response.get("data", [])]
result = calc_moving_average_line(values, 5)
print(result)
