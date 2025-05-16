from aiogram import types, Router,F

group_router=Router()

no_words=["нет"]

@group_router.message(F.text)
async def cancell_words(message: types.Message):
    words_list = message.text.lower().split(" ")
    for word in words_list:
        if word in no_words:
            await message.delete()
            await(message.answer(f"{message.from_user.first_name} не принемается"))
            break
