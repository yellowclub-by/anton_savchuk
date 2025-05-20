from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def payments_kb():
    builder=InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="карта", callback_data="way_1"),
        InlineKeyboardButton(text="крипта",callback_data="way_2"),
        width=1
    )
    return builder.as_markup()

links_kb = InlineKeyboardMarkup(
    inline_keyboard =[
        [
            InlineKeyboardButton(text="сайт", url ="https://i.ytimg.com/vi/BLoupTkJFIE/hqdefault.jpg"),
            InlineKeyboardButton(text="Я", url="tg://resolve?domain=Geto700")
        ]

    ]
)