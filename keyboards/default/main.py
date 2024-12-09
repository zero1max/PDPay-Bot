from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

request_nomer = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Telefon raqam yuborish", request_contact=True)
        ]
]
)