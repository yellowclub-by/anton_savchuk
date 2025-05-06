from aiogram import types, Router,F
from aiogram.types import FSInputFile
catalog_router=Router()

@catalog_router.message(F.text.lower()==("1-10"))
async def first (message: types.Message):
    photo=FSInputFile("img/catalog/apple.png")
    await(message.answer_photo(photo,caption= "яблоко"))
    await(message.answer("вот первые десять билетов"))


@catalog_router.message(F.text.lower()==("11-20"))
async def second (messege: types.Message):
    photo=FSInputFile("img/catalog/a.png")
    await(messege.answer_photo(photo, caption="какая-то фигня"))
    await(messege.answer("вот десять билетов "))