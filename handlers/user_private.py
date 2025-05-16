from aiogram import types, Router,F
from aiogram.filters import CommandStart,Command
from keyboards import reply,inline


user_router = Router()

@user_router.message(CommandStart())
async def start(message: types.Message):
    await (message.answer("привет это бот который может предоставить тебе отвветы к экзамену по математике ", reply_markup=reply.main_kb))

@user_router.message(F.text.lower().contains("способ"))
@user_router.message(Command("payment"))
async def catalog(message: types.Message):
    await(message.answer("способы оплаты", reply_markup=inline.payments_kb()))

@user_router.callback_query(F.data.lower().startswith("way"))
async def pay_info(callback:types.CallbackQuery):
    query=callback.data.split("_")[1]
    if query=="1":
        await callback.message.answer("введите номер карты")
    elif query=="2":
        await callback.message.answer("переведите на этот адрес: 1984")
    await callback.answer("инструкция отправлена")
@user_router.message(F.text.lower().contains("каталог"))
@user_router.message(Command("catalog"))
async def catalog_2(message: types.Message):
    await(message.answer("это список билетов",  reply_markup=reply.catalog_kb))

@user_router.message(Command("story"))
async def story(message: types.Message):
    await(message.answer("история покупок"))

@user_router.message(Command("basket"))
async def basket(message: types.Message):
    await(message.answer("ваши покупки"))

@user_router.message(F.text.lower().contains("назад"))
async def catalog(message: types.Message):
    await(message.answer("главное меню", reply_markup=reply.main_kb))


# @user_router.message(F.text.lower().startswith("как").contains("цен")|
#                      F.text.lower().contains("стоит").endswith("?"))
# async def echo(message: types.Message):
#     await(message.answer("бот находится в разроботке"))







