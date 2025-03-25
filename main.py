import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN="7740232101:AAHsT3P_9qqXs6h8JhYcym8D2dDdc_p5WpA"
bot=Bot(token=TOKEN)
dp=Dispatcher()

async def main():
    print("Бот запущен")
    await dp.start_polling(bot)

asyncio.run(main())



