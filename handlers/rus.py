from aiogram import F
from aiogram.types import Message, CallbackQuery, FSInputFile
from loader import router_user, bot
from keyboards.inline.main import *
from keyboards.default.main import *
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from database.userdb import create_user, create_card, create_transaction, create_services, create_utilities, get_user, user_exists, change_password, get_cards ,get_card_by_user, get_card_by_number, update_balance, get_user_by_phone_number
import time
from random import *
from PIL import Image, ImageDraw, ImageFont
import httpx, os


# url = 'http://api.exchangeratesapi.io/v1/latest?access_key=2e9fd14872e68750f79aac70efb70d2c'

# class UserAge(StatesGroup):
#     user_age = State()

# class UserInformations(StatesGroup):
#     number = State()
#     name = State()
#     surname = State()
#     age = State()

# class NewPassword(StatesGroup):
#     now_password = State()
#     new_password = State()
#     again_enter = State()

# class ExchangeCurrency(StatesGroup):
#     from_currency = State()
#     to_currency = State()
#     amount = State()

# class PulOtkazish(StatesGroup):
#     kimga = State()
#     summa = State()
#     izoh = State()

# class Mobile(StatesGroup):
#     user_id  = State()
#     phone_number = State()
#     summa = State()

# class Komunals(StatesGroup):
#     komunal_name = State()
#     account_number = State()
#     summa = State()

# sent_bonus_users = set()

# async def currency_conversion(from_currency, to_currency, amount):
#     url = "https://api.exchangerate-api.com/v4/latest/USD"  
#     async with httpx.AsyncClient() as client:
#         response = await client.get(url)
#         rates = response.json().get("rates", {})
        
#         if from_currency not in rates or to_currency not in rates:
#             return None
        
#         rate_from = rates[from_currency]
#         rate_to = rates[to_currency]
#         amount_in_usd = amount / rate_from
#         converted_amount = amount_in_usd * rate_to
#         return round(converted_amount, 2)

# def edit_card_image(carta_path, output_path, card_number, name, expiry_date):
#     img = Image.open(carta_path)

#     draw = ImageDraw.Draw(img)

#     font_path = "card/firecode.ttf"
#     try:
#         font_num = ImageFont.truetype(font_path, 50)  
#         font_date = ImageFont.truetype(font_path, 30)  
#         font_name = ImageFont.truetype(font_path, 40)  
#     except IOError:
#         font = ImageFont.load_default()  

#     draw.text((300, 450), card_number, fill="white", font=font_num)  
#     draw.text((500, 530), expiry_date, fill="white", font=font_date)  
#     draw.text((200, 560), name, fill="white", font=font_name)         

#     img.save(output_path)

# def edit_card_image_information(carta_path, output_path, card_number, expiry_date):
#     img = Image.open(carta_path)

#     draw = ImageDraw.Draw(img)

#     font_path = "card/firecode.ttf"
#     try:
#         font_num = ImageFont.truetype(font_path, 50) 
#         font_date = ImageFont.truetype(font_path, 30)  
#         font_name = ImageFont.truetype(font_path, 40)  
#     except IOError:
#         font = ImageFont.load_default()  

#     draw.text((300, 450), card_number, fill="white", font=font_num)  
#     draw.text((500, 530), expiry_date, fill="white", font=font_date)  

#     img.save(output_path)


@router_user.callback_query(F.data == "ru")
async def start_uz(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Здравствуйте!")
#     check  = await user_exists(callback.from_user.id)
#     print(check)
#     if check:
#         await callback.message.answer("У вас есть карта!", reply_markup=menu_users_ru)
#         await callback.message.delete()
#         await callback.answer() 
#     else:
#         await callback.message.answer("Введите ваш возраст!")
#         await state.set_state(UserAge.user_age)
#         await callback.message.delete()
#         await callback.answer()

# # --------------------------------------- Create card ---------------------------------------------------------

# @router_user.message(UserAge.user_age)
# async def user_age(msg: Message, state: FSMContext):
#     await state.update_data(user_age=msg.text)
#     data = await state.get_data()
#     age = data['user_age']
#     if age >= '16':
#         await msg.answer("Создать карту?", reply_markup=choice_create_card_ru)
#     else:
#         await msg.answer("Вы еще не достигли совершеннолетия!")

#     await state.clear()

# @router_user.callback_query(F.data == 'kartayoq_ru')
# async def create_card_yoq(callback: CallbackQuery):
#     await callback.message.answer("Вы не сможете использовать нашего бота без создания карты!")
#     await callback.message.answer("Создать карту?", reply_markup=choice_create_card_ru)

# @router_user.callback_query(F.data =='kartaha_ru')
# async def create_card_ha(callback: CallbackQuery, state: FSMContext):
#     await callback.message.delete()
#     await callback.message.answer("Отправьте свой номер телефона для создания карты!", reply_markup=request_nomer)
#     await state.set_state(UserInformations.number)

# @router_user.message(UserInformations.number, F.contact)
# async def get_number(msg: Message, state: FSMContext):
#     if msg.contact:
#         contact = msg.contact.phone_number
#         print(contact)
#     else:
#         contact = msg.text
#     await state.update_data(number=contact)
#     await msg.answer("Отправьте ваше имя!")
#     await state.set_state(UserInformations.name)

# @router_user.message(UserInformations.name)
# async def name(msg: Message, state: FSMContext):
#     await state.update_data(name=msg.text)
#     await msg.answer("Отправьте вашу фамилию!")
#     await state.set_state(UserInformations.surname)

# @router_user.message(UserInformations.surname)
# async def surname(msg: Message, state: FSMContext):
#     await state.update_data(surname=msg.text)
#     await msg.answer("Отправьте ваш возраст!")
#     await state.set_state(UserInformations.age)

# @router_user.message(UserInformations.age)
# async def age(msg: Message, state: FSMContext):
#     await state.update_data(age=msg.text)
#     data = await state.get_data()

#     name = data['name']
#     surname = data['surname']
#     age = data['age']
#     number = data['number']
#     user_id = msg.from_user.id

#     await create_user(user_id, name, surname, age, number)
#     await msg.answer("Вы зарегистрировались!")

#     card_number = randint(4470000000000000, 4471000000000000)
#     card_pin = randint(1000, 9999)
#     card_number_formatted = f"{str(card_number)[:4]} {str(card_number)[4:8]} {str(card_number)[8:12]} {str(card_number)[12:]}"
#     expirydate = "01/25"

#     input_image_path = 'card/card.png'
#     output_image_path = f'card/{name.lower()}_card.png'
#     edit_card_image(input_image_path, output_image_path, card_number_formatted, name, expirydate)

#     await create_card(user_id, card_number, card_pin, balance=10000)

#     await msg.answer_photo(
#         photo=FSInputFile(output_image_path),
#         caption=f"Ваш номер карты: <b>{card_number_formatted[:9]}******{card_number_formatted[-4:]}</b>\n"
#                 f"Ваш PIN-код карты: <b>{card_pin}</b>\n\n"
#     )
#     await msg.answer("Пожалуйста, снова выполните команду /start!")
#     await state.clear()

# # ------------------------------------------ Password O'zgaritirish ------------------------------------

# @router_user.callback_query(F.data == 'parolalmashtirish_ru')
# async def parolalmashtirish(callback: CallbackQuery, state: FSMContext):
#     await callback.message.delete()
#     await callback.message.answer("Отправьте ваш текущий пароль!")
#     await state.set_state(NewPassword.now_password)

# @router_user.message(NewPassword.now_password)
# async def now_password(msg: Message, state: FSMContext):
#     await state.update_data(now_password=msg.text)
#     await msg.answer("Отправьте новый пароль!")
#     await state.set_state(NewPassword.new_password)

# @router_user.message(NewPassword.new_password)
# async def new_password(msg: Message, state: FSMContext):
#     await state.update_data(new_password=msg.text)
#     await msg.answer("Повторите новый пароль!")
#     await state.set_state(NewPassword.again_enter)

# @router_user.message(NewPassword.again_enter)
# async def again_password(msg: Message, state: FSMContext):
#     await state.update_data(again_password=msg.text)
#     data = await state.get_data()
#     now_password = data['now_password']
#     new_password = data['new_password']
#     again_password = data['again_password']
#     check = await change_password(msg.from_user.id, now_password, new_password, again_password)
#     if check:
#         await msg.answer("Ваш пароль изменен!", reply_markup=ortgaqaytish_ru)
#         await state.clear()
#     else:
#         await msg.answer("Что-то пошло не так")

# # ---------------------------------------- Karta ma'lumotlarini olish ----------------------------------------------------------------

# @router_user.callback_query(F.data == "kartamalumotlariolish_ru")
# async def ma_lumotlarni_olish(callback: CallbackQuery, state: FSMContext):
#     await callback.message.delete()

#     cards = await get_cards(callback.from_user.id)
#     for card in cards:
#         card_number = card[2]
#         card_password = card[3]
#         balance = card[4]

#         expirydate = '01/25'
#         card_number_formatted = f"{str(card_number)[:4]} {str(card_number)[4:8]} {str(card_number)[8:12]} {str(card_number)[12:]}"
        
#         user_id = card[1] 
#         user = await get_user(user_id)
#         username = user[0][2]
#         output_image_path = f'card/{username.lower()}_card.png'

#         gift_money_photo = "https://thumbs.dreamstime.com/b/uzbekistan-money-som-banknotes-uzs-uzbek-bills-d-illustration-money-uzbekistan-som-bills-uzs-banknotes-uzbek-business-finance-237100171.jpg"

#         if os.path.exists(output_image_path):
#             if user_id in sent_bonus_users:
#                 await callback.message.answer_photo(
#                     photo=FSInputFile(output_image_path),
#                     caption=(
#                     f"Ваш номер карты: <b>{card_number_formatted}</b>\n"
#                     f"Ваш пароль карты: <b>{card_password}</b>\n"
#                     f"Ваш баланс карты: <b>{balance}</b>"
#                 ), reply_markup=ortgaqaytish)
#             else:
#                 await callback.message.answer_photo(photo=gift_money_photo,
#                                                 caption="Вам начислен бонус 10000 сум за использование нашего сервиса!\n\nПоздравляем🥳")
#                 await callback.message.answer_photo(
#                     photo=FSInputFile(output_image_path),
#                     caption=(
#                         f"Ваш номер карты: <b>{card_number_formatted}</b>\n"
#                         f"Ваш пароль карты: <b>{card_password}</b>\n"
#                         f"Ваш баланс карты: <b>{balance}</b>"
#                     ), reply_markup=ortgaqaytish_ru)
#                 sent_bonus_users.add(user_id)
#         else:
#             await callback.message.answer(
#                 "Информация о карте недоступна. Пожалуйста, попробуйте создать карту заново!"
#             )


# # ---------------------------------------- Exchange currency --------------------------------------------------------

# @router_user.callback_query(F.data == 'valyutakursi_ru')
# async def exchange_currency(callback: CallbackQuery, state: FSMContext):
#     await callback.message.delete()
#     await callback.message.answer("Какую валюту хотите обменять? (Например: USD, EUR, UZS):")
#     await state.set_state(ExchangeCurrency.from_currency)

# @router_user.message(ExchangeCurrency.from_currency)
# async def from_currency(msg: Message, state: FSMContext):
#     await state.update_data(from_currency=msg.text.upper())
#     await msg.answer("На какую валюту хотите обменять? (Например: USD, EUR, UZS):")
#     await state.set_state(ExchangeCurrency.to_currency)

# @router_user.message(ExchangeCurrency.to_currency)
# async def to_currency(msg: Message, state: FSMContext):
#     await state.update_data(to_currency=msg.text.upper())
#     await msg.answer("Введите сумму (только цифры):")
#     await state.set_state(ExchangeCurrency.amount)

# @router_user.message(ExchangeCurrency.amount)
# async def amount(msg: Message, state: FSMContext):
#     try:
#         amount = float(msg.text)
#         await state.update_data(amount=amount)
#         data = await state.get_data()
#         from_currency = data['from_currency']
#         to_currency = data['to_currency']

#         result = await currency_conversion(from_currency, to_currency, amount)
#         if result is None:
#             await msg.answer("Введены неправильные валюты. Пожалуйста, попробуйте снова.")
#         else:
#             await msg.answer(f"Из валюты: {from_currency}\nВ валюту: {to_currency}\nРезультат: {result}", reply_markup=ortgaqaytish_ru)
#     except ValueError:
#         await msg.answer("Пожалуйста, введите только цифры.")
#     await state.clear()


# # ----------------------------------------------- Hamyonni tekshirish ---------------------------------------------

# @router_user.callback_query(F.data == 'hamyontekshirish_ru')
# async def hamyonni_tekshirish(callback: CallbackQuery):
#     await callback.message.delete()

#     cards = await get_cards(callback.from_user.id)
#     for card in cards:
#         balance = card[4]

#     await callback.message.answer(f"На вашем кошельке {balance} сум!", reply_markup=payorget_ru)

# @router_user.callback_query(F.data == 'hamyontoldirish_ru')
# async def hamyontoldirish(callback: CallbackQuery):
#     await callback.message.delete()
#     await callback.message.answer("Пополнение кошелька временно недоступно, вы можете пополнить свой кошелек только через перевод средств!\n\nПриносим извинения за неудобства!", reply_markup=ortgaqaytish)

# @router_user.callback_query(F.data == 'pulyechibolish_ru')
# async def pulyechibolish(callback: CallbackQuery):
#     await callback.message.delete()
#     await callback.message.answer("Снятие денег пока недоступно, но вы можете совершать оплату!\n\nПриносим извинения за неудобства!", reply_markup=ortgaqaytish_ru)

# # ------------------------------------------------ Pul o'tkazish --------------------------------------------------------------

# @router_user.callback_query(F.data == 'pulotkazish_ru')
# async def pulotkazish(callback: CallbackQuery, state: FSMContext):
#     await callback.message.delete()
#     await callback.message.answer("Отправьте номер карты человека, которому хотите перевести деньги:\n\nНапример: 4470 0000 0000 0000")
#     await state.set_state(PulOtkazish.kimga)

# @router_user.message(PulOtkazish.kimga)
# async def get_kimga(msg: Message, state: FSMContext):
#     await state.update_data(kimga=msg.text)
#     await msg.answer("Введите сумму перевода (только число):")
#     await state.set_state(PulOtkazish.summa)

# @router_user.message(PulOtkazish.summa)
# async def get_summa(msg: Message, state: FSMContext):
#     await state.update_data(summa=msg.text)
#     await msg.answer("Добавить комментарий?", reply_markup=izohyes_no_ru)

# @router_user.callback_query(F.data == 'izohno_ru')
# async def no_izoh(callback: CallbackQuery, state: FSMContext):
#     await callback.message.delete()
#     await state.update_data(izoh="Нет")
#     data = await state.get_data()

#     kimga = data['kimga']
#     summa = int(data['summa'])
#     izoh = data['izoh']

#     yuboruvchi = await get_card_by_user(callback.from_user.id)
#     yuboruvchi_id = yuboruvchi[0]
#     yuboruvchi_number = yuboruvchi[2]
#     print(f"Номер карты отправителя: {yuboruvchi_number}")
#     if not yuboruvchi:
#         await callback.message.answer("Карта не найдена.", reply_markup=ortgaqaytish_ru)
#         return

#     yuboruvchi_balance = yuboruvchi[4]  

#     if yuboruvchi_balance < summa:
#         await callback.message.answer("На вашем счете недостаточно средств.", reply_markup=ortgaqaytish_ru)
#         return

#     post_yuboruvchi_balance = yuboruvchi_balance - summa
#     await update_balance(yuboruvchi_id, post_yuboruvchi_balance)

#     qabul_qiluvchi = await get_card_by_number(kimga)
#     qabul_qiluvchi_id = qabul_qiluvchi[0]
#     qabul_qiluvchi_chat_id = qabul_qiluvchi[1]
#     qabul_qiluvchi_number = qabul_qiluvchi[2]
#     if not qabul_qiluvchi:
#         await callback.message.answer("Карта получателя не найдена.", reply_markup=ortgaqaytish_ru)
#         return

#     qabul_qiluvchi_balance = qabul_qiluvchi[4]  
#     post_qabul_qiluvchi_balance = qabul_qiluvchi_balance + summa
#     await update_balance(qabul_qiluvchi_id, post_qabul_qiluvchi_balance)
#     await create_transaction(yuboruvchi_number, qabul_qiluvchi_number, summa, izoh)

#     await callback.message.answer(
#         f"Ваш перевод на сумму {summa} сум был успешно отправлен.\n\nКому: {kimga}\nКомментарий: {izoh}",
#         reply_markup=ortgaqaytish_ru)
#     await bot.send_message(chat_id=qabul_qiluvchi_chat_id, text="Вам был переведен платеж!")
#     await state.clear()

# @router_user.callback_query(F.data == 'izohyes_ru')
# async def yes_izoh(callback: CallbackQuery, state: FSMContext):
#     await callback.message.delete()
#     await callback.message.answer("Введите комментарий: ")
#     await state.set_state(PulOtkazish.izoh)

# @router_user.message(PulOtkazish.izoh)
# async def get_izoh(msg: Message, state: FSMContext):
#     await state.update_data(izoh=msg.text)
#     data = await state.get_data()

#     kimga = data['kimga']
#     summa = int(data['summa'])
#     izoh = data['izoh']

#     yuboruvchi = await get_card_by_user(msg.from_user.id)
#     yuboruvchi_id = yuboruvchi[0]
#     yuboruvchi_number = yuboruvchi[2]
#     print(f"Номер карты отправителя: {yuboruvchi_number}")
#     if not yuboruvchi:
#         await msg.answer("Карта не найдена.", reply_markup=ortgaqaytish_ru)
#         return

#     yuboruvchi_balance = yuboruvchi[4]  

#     if yuboruvchi_balance < summa:
#         await msg.answer("На вашем счете недостаточно средств.", reply_markup=ortgaqaytish_ru)
#         return

#     post_yuboruvchi_balance = yuboruvchi_balance - summa
#     await update_balance(yuboruvchi_id, post_yuboruvchi_balance)

#     qabul_qiluvchi = await get_card_by_number(kimga)
#     qabul_qiluvchi_id = qabul_qiluvchi[0]
#     qabul_qiluvchi_chat_id = qabul_qiluvchi[1]
#     qabul_qiluvchi_number = qabul_qiluvchi[2]
#     if not qabul_qiluvchi:
#         await msg.answer("Карта получателя не найдена.", reply_markup=ortgaqaytish_ru)
#         return

#     qabul_qiluvchi_balance = qabul_qiluvchi[4]  
#     post_qabul_qiluvchi_balance = qabul_qiluvchi_balance + summa
#     await update_balance(qabul_qiluvchi_id, post_qabul_qiluvchi_balance)
#     await create_transaction(yuboruvchi_number, qabul_qiluvchi_number, summa, izoh)

#     await msg.answer(
#         f"Ваш перевод на сумму {summa} сум был успешно отправлен.\n\nКому: {kimga}\nКомментарий: {izoh}",
#         reply_markup=ortgaqaytish_ru)
#     await bot.send_message(chat_id=qabul_qiluvchi_chat_id, text="Вам был переведен платеж!")
#     await state.clear()

# # ------------------------------------------------------- To'lov qilish -------------------------------------------------------

# @router_user.callback_query(F.data == 'tolovqilish_ru')
# async def tolovqilish(callback: CallbackQuery):
#     await callback.message.delete()
#     await callback.message.answer("Выберите: ", reply_markup=menu_tolov_qilish_ru)

# # ---------------------- Mobile -----------------------------

# @router_user.callback_query(F.data == 'mobile_ru')
# async def mobile(callback: CallbackQuery, state: FSMContext):
#     await callback.message.delete()
#     await callback.message.answer("Введите номер телефона!\n\nНапример: <b>901234567</b>")
#     await state.set_state(Mobile.phone_number)

# @router_user.message(Mobile.phone_number)
# async def get_phone_number(msg: Message, state: FSMContext):
#     await state.update_data(phone_number=f'+998{msg.text}')
#     await msg.answer("Ваш номер телефона: <b>{}</b>".format(msg.text))
#     await state.set_state(Mobile.summa)
#     await msg.answer("Введите сумму: ")

# @router_user.message(Mobile.summa)
# async def get_summa(msg: Message, state: FSMContext):
#     await state.update_data(summa=int(msg.text))
#     await state.update_data(user_id=msg.from_user.id)
#     data = await state.get_data()
#     userid = data['user_id']
#     receiver_phone_num = data['phone_number']
#     summa = data['summa']

#     try:
#         receiver = await get_user_by_phone_number(receiver_phone_num)
#         receiver_user_id = receiver[0][1]
#         print(receiver)

#         yuboruvchi = await get_card_by_user(msg.from_user.id)
#         yuboruvchi_id = yuboruvchi[0]
#         yuboruvchi_balance = yuboruvchi[4]  

#         post_yuboruvchi_balance = yuboruvchi_balance - summa
#         await update_balance(yuboruvchi_id, post_yuboruvchi_balance)

#         await create_services(userid, receiver_phone_num, summa)
#         await msg.answer("Деньги переведены!", reply_markup=ortgaqaytish_ru)
#         await bot.send_message(chat_id=receiver_user_id, text=f"На ваш номер телефона было переведено {summa} сум!")
#         await state.clear()
#     except Exception as e:
#         print(f"Xato {e}")

#         yuboruvchi = await get_card_by_user(msg.from_user.id)
#         yuboruvchi_id = yuboruvchi[0]
#         yuboruvchi_balance = yuboruvchi[4]  

#         post_yuboruvchi_balance = yuboruvchi_balance - summa
#         await update_balance(yuboruvchi_id, post_yuboruvchi_balance)

#         await create_services(userid, receiver_phone_num, summa)
#         await msg.answer("Деньги переведены!", reply_markup=ortgaqaytish_ru)
#         # await bot.send_message(chat_id=receiver_user_id, text=f"На ваш номер телефона было переведено {summa} сум!")
#         await state.clear()

# # ---------------------- Komunal ----------------------------

# @router_user.callback_query(F.data == 'komunal_ru')
# async def komunal(callback: CallbackQuery, state: FSMContext):
#     await callback.message.delete()
#     await callback.message.answer("Выберите: ", reply_markup=menu_komunal_ru)
#     await state.set_state(Komunals.komunal_name)

# @router_user.callback_query(F.data.in_({'elektr', 'gaz', 'school', 'issiqsuv', 'internet', 'axlat'}), Komunals.komunal_name)
# async def all_komunals(callback: CallbackQuery, state: FSMContext):
#     await callback.message.delete()
#     await state.update_data(komunal_name=callback.data)
#     await callback.message.answer(f"Отправьте номер вашего лицевого счёта для {callback.data.capitalize()}!")
#     await state.set_state(Komunals.account_number)

# @router_user.message(Komunals.account_number)
# async def get_account_number(msg: Message, state: FSMContext):
#     await state.update_data(account_number=msg.text)
#     await msg.answer("Ваш номер лицевого счёта: <b>{}</b>".format(msg.text))
#     await state.set_state(Komunals.summa)
#     await msg.answer("Введите сумму: ")

# @router_user.message(Komunals.summa)
# async def get_summa(msg: Message, state: FSMContext):
#     await state.update_data(summa=int(msg.text))
#     await state.update_data(user_id=msg.from_user.id)
#     data = await state.get_data()
#     userid = data['user_id']
#     komunal_name = data['komunal_name']
#     account_number = data['account_number']
#     summa = data['summa']

#     yuboruvchi = await get_card_by_user(msg.from_user.id)
#     yuboruvchi_id = yuboruvchi[0]
#     yuboruvchi_balance = yuboruvchi[4]  

#     post_yuboruvchi_balance = yuboruvchi_balance - summa
#     await update_balance(yuboruvchi_id, post_yuboruvchi_balance)

#     await create_utilities(userid, komunal_name, account_number, summa)
#     await msg.answer("Платеж успешно выполнен!", reply_markup=ortgaqaytish_ru)

# # ------------------------------------------------------- Ortga qaytish -------------------------------------------------------

# @router_user.callback_query(F.data == 'ortgaqaytish_ru')
# async def ortgaqaytish_handler(callback: CallbackQuery):
#     await callback.message.delete()
#     await callback.message.answer("Вы вернулись в главное меню!", reply_markup=menu_users_ru)


