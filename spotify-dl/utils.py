def format_timespan(num_seconds):
    num_minutes, seconds = divmod(num_seconds, 60)
    num_hours, minutes = divmod(num_minutes, 60)
    days, hours = divmod(num_hours, 24)
    # print(days, hours, minutes, seconds)
    # ret = ""
    # ret += f"{days} days " if days else ""
    # ret += f"{hours} hours " if hours else ""
    # ret += f"{minutes} minutes " if minutes else ""
    # ret += f"{seconds} seconds" if seconds else ""
    return f"{days} days, {hours} hours, {minutes} minutes and {seconds} seconds"


# print(format_timespan(21 + 5 * 60 + 10 * 60 * 60 + 2 * 60 * 60 * 24))
# for i in range(100000):
#     # d, h, m, s = format_timespan(i)
#     # assert i == s + m * 60 + h * 60 * 60 + d * 60 * 60 * 24
#     print(format_timespan(i))
