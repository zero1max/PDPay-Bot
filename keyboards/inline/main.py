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

# --------------------------------------------------------------------

choice_language_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="English🇺🇸", callback_data="en"),
            InlineKeyboardButton(text="Русский🇷🇺", callback_data="ru"),
            InlineKeyboardButton(text="Узбекский🇺🇿", callback_data="uz")
        ]
    ]
)

choice_create_card_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Да", callback_data='kartaha_ru'),
            InlineKeyboardButton(text="Нет", callback_data="kartayoq_ru")
        ]
    ]
)

menu_users_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Сменить пароль карты🔗", callback_data="parolalmashtirish_ru")],
        [InlineKeyboardButton(text="Проверить баланс кошелька💳", callback_data="hamyontekshirish_ru"), InlineKeyboardButton(text="Курс валюты💱", callback_data="valyutakursi_ru")],
        [InlineKeyboardButton(text="Оплатить💰", callback_data="tolovqilish_ru"), InlineKeyboardButton(text="Перевести деньги💸", callback_data='pulotkazish_ru')],
        [InlineKeyboardButton(text="Получить информацию о карте📲", callback_data="kartamalumotlariolish_ru")],
        [InlineKeyboardButton(text="Выйти🔙", callback_data='chiqish_ru')]
    ]
)

menu_tolov_qilish_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Оплатить мобильному оператору 📱", callback_data='mobile_ru')],
        [InlineKeyboardButton(text="Оплатить коммунальные услуги 💡", callback_data='komunal_ru')],
        [InlineKeyboardButton(text="Назад🔙", callback_data='ortgaqaytish_ru')]
    ]
)

menu_komunal_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="⚡ Электричество", callback_data='elektr_ru'), InlineKeyboardButton(text='🔥 Газ', callback_data='gaz_ru')],
        [InlineKeyboardButton(text="🏫 Школа", callback_data='school_ru'), InlineKeyboardButton(text='💧 Горячая вода', callback_data="issiqsuv_ru")],
        [InlineKeyboardButton(text='🌐 Интернет провайдер', callback_data='internet_ru'), InlineKeyboardButton(text='🗑️ Мусор', callback_data="axlat_ru")],
        [InlineKeyboardButton(text="Назад🔙", callback_data='ortgaqaytish_ru')]
    ]
)

payorget_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Пополнить кошелек➕", callback_data='hamyontoldirish_ru')],
        [InlineKeyboardButton(text="Снять деньги➖", callback_data='pulyechibolish_ru')]
    ]
)

izohyes_no_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Да', callback_data='izohyes_ru'), InlineKeyboardButton(text="Нет", callback_data='izohno_ru')]
    ]
)

ortgaqaytish_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Назад🔙", callback_data='ortgaqaytish_ru')]
    ]
)
