import asyncio
from aiogram import Bot, Dispatcher

TOKEN="7740232101:AAHsT3P_9qqXs6h8JhYcym8D2dDdc_p5WpA"
bot=Bot(token=TOKEN)
dp=Dispatcher()


from handlers.user_private import user_router
from handlers.user_groupe import group_router

dp.include_router(user_router)
dp.include_router(group_router)




async def main():
    print("Бот запущен")
    await dp.start_polling(bot)

asyncio.run(main())



