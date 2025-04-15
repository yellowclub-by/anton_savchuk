from aiogram import types, Router,F
from aiogram.filters import CommandStart,Command


user_router = Router()

@user_router.message(CommandStart())
async def start(message: types.Message):
    await (message.answer("привет это бот который может предоставить тебе отвветы к экзамену по математике "))

@user_router.message(Command("payment"))
async def catalog(message: types.Message):
    await(message.answer("способы оплаты"))

@user_router.message(F.text.lower().startswith("как").contains("цен")|
                     F.text.lower().contains("стоит").endswith("?"))
@user_router.message(Command("catalog"))
async def catalog_2(message: types.Message):
    await(message.answer("это список билетов"))

@user_router.message(Command("story"))
async def story(message: types.Message):
    await(message.answer("история покупок"))

@user_router.message(Command("basket"))
async def basket(message: types.Message):
    await(message.answer("ваши покупки"))
@user_router.message(F.text.lower().startswith("как").contains("цен")|
                     F.text.lower().contains("стоит").endswith("?"))
async def echo(message: types.Message):
    await(message.answer("бот находится в разроботке"))







