def calc_moving_average_line(data: list[float], n: int):
    moving_averages = []
    for i in range(len(data) - n + 1):
        average = sum(data[i : i + n]) / n
        moving_averages.append(average)
    return moving_averages
