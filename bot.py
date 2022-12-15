import logging
import csv
from aiogram import Bot, Dispatcher, executor, types
import logging
from main import chat_anwser

logging.basicConfig(level=logging.INFO)

TOKEN = "5608949484:AAHiroYwLOvmwhTlEggIqe3YdtJEqMwQyDY"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start", "info"])
async def hello(message: types.Message):
    await message.answer("Assalomu alaykum! Xush kelibsiz. \n\nMen Sun'iy Intellekt yordamida ishlab chiqilayotgan MohirBot bo'laman, suhbat davomida savolingizga "
                         "to'g'ri javob bera olmasam #stop kalit so'zi yordamida savol va murojaatingizni yozib qoldiring!")\


@dp.message_handler()
async def hello(message: types.Message):
    answer = chat_anwser(message.text)
    print(answer)
    await message.answer(answer)


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)

