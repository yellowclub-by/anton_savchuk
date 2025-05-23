import asyncio
from aiogram import Bot, Dispatcher
from handlers.user_private import user_router
from handlers.catalog import catalog_router
from handlers.user_groupe import group_router
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

TOKEN="7740232101:AAHsT3P_9qqXs6h8JhYcym8D2dDdc_p5WpA"
bot=Bot(token=TOKEN,Default= DefaultBotProperties(parse_mode=ParseMode.HTML))
dp=Dispatcher()




dp.include_router(user_router)
dp.include_router(catalog_router)
dp.include_router(group_router)




async def main():
    print("Бот запущен")
    await dp.start_polling(bot)

asyncio.run(main())



