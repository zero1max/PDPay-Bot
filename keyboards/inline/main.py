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

choice_create_card = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ha", callback_data='kartaha'),
            InlineKeyboardButton(text="Yo'q", callback_data="kartayoq")
        ]
    ]
)

menu_users = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Karta parolini o'zgartirish🔗", callback_data="parolalmashtirish")],
        [InlineKeyboardButton(text="Hamyonni tekshirish💳", callback_data="hamyontekshirish"), InlineKeyboardButton(text="Valyuta kursi💱",callback_data="valyutakursi")],
        [InlineKeyboardButton(text="To'lov qilish💰", callback_data="tolovqilish"), InlineKeyboardButton(text="Pul o'tkazish💸", callback_data='pulotkazish')],
        [InlineKeyboardButton(text="Karta ma'lumotlarini olish📲", callback_data="kartamalumotlariolish")],
        [InlineKeyboardButton(text="Chiqish🔙", callback_data='chiqish')]
        
    ]
)

menu_tolov_qilish = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Mobil Operatorga to'lov qilish 📱", callback_data='mobile')],
        [InlineKeyboardButton(text="Kommunal xizmatlarga to'lov qilish 💡", callback_data='komunal')],
        [InlineKeyboardButton(text="Ortga qaytish🔙", callback_data='ortgaqaytish')]
    ]
)

menu_komunal = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="⚡ Elektr toki", callback_data='elektr'), InlineKeyboardButton(text='🔥 Gaz', callback_data='gaz')],
        [InlineKeyboardButton(text="🏫 Maktab", callback_data='school'), InlineKeyboardButton(text='💧 Issiq suv', callback_data="issiqsuv")],
        [InlineKeyboardButton(text='🌐 Internet provayder', callback_data='internet'), InlineKeyboardButton(text='🗑️ Axlat', callback_data="axlat")],
        [InlineKeyboardButton(text="Ortga qaytish🔙", callback_data='ortgaqaytish')]
    ]
)

payorget = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Hamyonni to'ldirish➕", callback_data='hamyontoldirish')],
        [InlineKeyboardButton(text="Pul yechib olish➖", callback_data='pulyechibolish')]
    ]
)


izohyes_no = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Ha', callback_data='izohyes'), InlineKeyboardButton(text="Yo'q", callback_data='izohno')]
    ]
)

ortgaqaytish = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ortga qaytish🔙", callback_data='ortgaqaytish')]
    ]
)