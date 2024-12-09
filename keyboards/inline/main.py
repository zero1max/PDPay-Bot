from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

choice_language = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="English🇺🇸", callback_data="en"),
            InlineKeyboardButton(text="Русский🇷🇺", callback_data="ru"),
            InlineKeyboardButton(text="Uzbek🇺🇿", callback_data="uz")
        ]
    ]
)

create_card = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ha", callback_data='kartaha'),
            InlineKeyboardButton(text="Yo'q", callback_data="kartayoq")
        ]
    ]
)