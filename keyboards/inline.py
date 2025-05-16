from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
def payments_kb():
    builder=InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="карта", callback_data="way_1"),
        InlineKeyboardButton(text="крипта",callback_data="way_2"),
        width=1
    )
    return builder.as_markup()