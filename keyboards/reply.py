from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
back_btn=KeyboardButton(text="назад")
main_kb= ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="каталог"), KeyboardButton(text="история покупок")],
        [KeyboardButton(text="корзина"), KeyboardButton(text="способ оплаты")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Что хотите?",
)
catalog_kb=ReplyKeyboardMarkup(
    keyboard=[
         [KeyboardButton(text="1-10"),KeyboardButton(text="11-20")],
         [KeyboardButton(text="21-30"),KeyboardButton(text="31-40")],
         [KeyboardButton(text="41-50"),KeyboardButton(text="51-60")],
         [KeyboardButton(text="61-70"),KeyboardButton(text="71-80")],
         [back_btn]
    ],
    resize_keyboard=True,
    input_field_placeholder="Что хотите?",
)



