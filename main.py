from src.message_time import morning_random_moment, evening_random_moment
from aiogram import Bot, Dispatcher
import asyncio

from src.message_time import random_moment, is_valid_message_time
from aiogram import Bot, Dispatcher
from asyncio import sleep

# создаем бота и его диспетчера
# bot = Bot(token="токен сюда ctrl + v")
# dp = Dispatcher()


should_sleep = False

async def timer():
    global should_sleep
    if should_sleep:
        await sleep(5)
    morning_time = random_moment("9:30", "11:00")
    lunch_time = random_moment("13:00", "14:30")
    evening_time = random_moment("19:00", "20:30")
    print(morning_time)

    should_sleep = True

    return morning_time, lunch_time, evening_time

async def main():
    for i in range(5):
        await timer()

if __name__ == "__main__":
    asyncio.run(main())