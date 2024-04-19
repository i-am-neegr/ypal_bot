import random
from datetime import datetime, time


def morning_random_moment(start_time: str, end_time: str) -> time:
    start_hour, start_minutes = start_time.split(":")
    end_hours, end_minutes = end_time.split(":")

    start_time = time(int(start_hour), int(start_minutes), 0)
    end_time = time(int(end_hours), int(end_minutes), 0)

    random_hour = random.randint(start_time.hour, end_time.hour)
    random_minute = random.randint(start_time.minute, end_time.minute)
    random_second = random.randint(0, 59)
    random_microsecond = random.randint(0, 999999)

    random_time = time(random_hour, random_minute, random_second, random_microsecond)

    return random_time


def evening_random_moment(start_time: str, end_time: str) -> time:
    start_hour, start_minutes = start_time.split(":")
    end_hours, end_minutes = end_time.split(":")

    start_time = time(int(start_hour), int(start_minutes), 0)
    end_time = time(int(end_hours), int(end_minutes), 0)

    random_hour = random.randint(start_time.hour, end_time.hour)
    random_minute = random.randint(0, 59)
    random_second = random.randint(0, 59)
    random_microsecond = random.randint(0, 999999)

    random_time = time(random_hour, random_minute, random_second, random_microsecond)

    return random_time


def is_valid_message_time(sending_time: time) -> bool:
    sending_time = str(sending_time.strftime('%H:%M'))
    current_time = str(datetime.now().strftime('%H:%M'))
    return current_time == sending_time
