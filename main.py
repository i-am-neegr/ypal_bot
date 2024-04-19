import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message

from src.choise_function import random_function
from src.choise_text import (random_compliment, random_motivation,
                             random_phrases)
from src.message_time import (evening_random_moment, is_valid_message_time,
                              morning_random_moment)

# создаем бота и его диспетчера
bot = Bot(token="7144015604:AAGLcjg8lVnVw8V_wkZXqgQFJy0FVH61mxE")
dp = Dispatcher()
channel_id = -1002080640327

morning_time = morning_random_moment("9:30", "11:00")
evening_time = evening_random_moment("17:30", "20:00")


@dp.channel_post()
async def main(msg: Message):
    while True:
        if is_valid_message_time(morning_time) or is_valid_message_time(evening_time):
            phrase = random_function([random_motivation, random_phrases, random_compliment])
            await bot.send_message(chat_id=channel_id, text=phrase)
            await asyncio.sleep(60)


if __name__ == "__main__":
    dp.run_polling(bot)
