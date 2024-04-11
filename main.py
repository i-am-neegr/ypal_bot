from src.message_time import morning_random_moment, evening_random_moment
from aiogram import Bot, Dispatcher

# создаем бота и его диспетчера
# bot = Bot(token="токен сюда ctrl + v")
# dp = Dispatcher()

morning_time = morning_random_moment("9:30", "11:45")
evening_time = evening_random_moment("17:45", "20:30")

print("idi na xyu")
