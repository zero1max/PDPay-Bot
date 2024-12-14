from aiogram import F
from aiogram.types import Message, CallbackQuery, FSInputFile
from loader import router_user, bot
from keyboards.inline.main import *
from keyboards.default.main import *
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from database.userdb import create_user, create_card, create_transaction ,get_user, user_exists, change_password, get_cards ,get_card_by_user, get_card_by_number, update_balance
import time
from random import *
from PIL import Image, ImageDraw, ImageFont
import httpx, os

url = 'http://api.exchangeratesapi.io/v1/latest?access_key=2e9fd14872e68750f79aac70efb70d2c'

class UserAge(StatesGroup):
    user_age = State()

class UserInformations(StatesGroup):
    number = State()
    name = State()
    surname = State()
    age = State()

class NewPassword(StatesGroup):
    now_password = State()
    new_password = State()
    again_enter = State()

class ExchangeCurrency(StatesGroup):
    from_currency = State()
    to_currency = State()
    amount = State()

class PulOtkazish(StatesGroup):
    kimga = State()
    summa = State()
    izoh = State()

sent_bonus_users = set()

async def currency_conversion(from_currency, to_currency, amount):
    url = "https://api.exchangerate-api.com/v4/latest/USD"  
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        rates = response.json().get("rates", {})
        
        if from_currency not in rates or to_currency not in rates:
            return None
        
        rate_from = rates[from_currency]
        rate_to = rates[to_currency]
        amount_in_usd = amount / rate_from
        converted_amount = amount_in_usd * rate_to
        return round(converted_amount, 2)

def edit_card_image(carta_path, output_path, card_number, name, expiry_date):
    img = Image.open(carta_path)

    draw = ImageDraw.Draw(img)

    font_path = "card/firecode.ttf"
    try:
        font_num = ImageFont.truetype(font_path, 50)  
        font_date = ImageFont.truetype(font_path, 30)  
        font_name = ImageFont.truetype(font_path, 40)  
    except IOError:
        font = ImageFont.load_default()  

    draw.text((300, 450), card_number, fill="white", font=font_num)  
    draw.text((500, 530), expiry_date, fill="white", font=font_date)  
    draw.text((200, 560), name, fill="white", font=font_name)         

    img.save(output_path)

def edit_card_image_information(carta_path, output_path, card_number, expiry_date):
    img = Image.open(carta_path)

    draw = ImageDraw.Draw(img)

    font_path = "card/firecode.ttf"
    try:
        font_num = ImageFont.truetype(font_path, 50) 
        font_date = ImageFont.truetype(font_path, 30)  
        font_name = ImageFont.truetype(font_path, 40)  
    except IOError:
        font = ImageFont.load_default()  

    draw.text((300, 450), card_number, fill="white", font=font_num)  
    draw.text((500, 530), expiry_date, fill="white", font=font_date)  

    img.save(output_path)

@router_user.callback_query(F.data == "uz")
async def start_uz(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Assalomu aleykum!")
    check  = await user_exists(callback.from_user.id)
    print(check)
    if check:
        await callback.message.answer("Sizda karta bor!", reply_markup=menu_users)
        await callback.message.delete()
        await callback.answer() 
    else:
        await callback.message.answer("Yoshingizni kiriting!")
        await state.set_state(UserAge.user_age)
        await callback.message.delete()
        await callback.answer()  

# --------------------------------------- Create card ---------------------------------------------------------
@router_user.message(UserAge.user_age)
async def user_age(msg: Message, state: FSMContext):
    await state.update_data(user_age=msg.text)
    data = await state.get_data()
    age = data['user_age']
    if age >= '16':
        await msg.answer("Karta yaratamizmi?", reply_markup=choice_create_card)
    else:
        await msg.answer("Siz hali balog'at yoshiga to'lmagansiz!")

    await state.clear()

@router_user.callback_query(F.data == 'kartayoq')
async def create_card_yoq(callback: CallbackQuery):
    await callback.message.answer("Karta yaratmasdan bizning botdan foydalana olmaysiz!")
    await callback.message.answer("Karta yaratamizmi?", reply_markup=choice_create_card)

@router_user.callback_query(F.data =='kartaha')
async def create_card_ha(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await callback.message.answer("Karta yaratish uchun telefon raqamingizni yuboring!", reply_markup=request_nomer)
    await state.set_state(UserInformations.number)

@router_user.message(UserInformations.number, F.contact)
async def get_number(msg: Message, state: FSMContext):
    if msg.contact:
        contact = msg.contact.phone_number
        print(contact)
    else:
        contact = msg.text
    await state.update_data(number=contact)
    await msg.answer("Ismingizni yuboring!")
    await state.set_state(UserInformations.name)

@router_user.message(UserInformations.name)
async def name(msg: Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await msg.answer("Familiyangizni yuboring!")
    await state.set_state(UserInformations.surname)

@router_user.message(UserInformations.surname)
async def surname(msg: Message, state: FSMContext):
    await state.update_data(surname=msg.text)
    await msg.answer("Yoshingizni yuboring!")
    await state.set_state(UserInformations.age)


@router_user.message(UserInformations.age)
async def age(msg: Message, state: FSMContext):
    await state.update_data(age=msg.text)
    data = await state.get_data()

    name = data['name']
    surname = data['surname']
    age = data['age']
    number = data['number']
    user_id = msg.from_user.id

    await create_user(user_id, name, surname, age, number)
    await msg.answer("Siz ro'yxatdan o'tdingiz!")

    card_number = randint(4470000000000000, 4471000000000000)
    card_pin = randint(1000, 9999)
    card_number_formatted = f"{str(card_number)[:4]} {str(card_number)[4:8]} {str(card_number)[8:12]} {str(card_number)[12:]}"
    expirydate = "01/25"

    input_image_path = 'card/card.png'
    output_image_path = f'card/{name.lower()}_card.png'
    edit_card_image(input_image_path, output_image_path, card_number_formatted, name, expirydate)

    await create_card(user_id, card_number, card_pin, balance=10000)

    await msg.answer_photo(
        photo=FSInputFile(output_image_path),
        caption=f"Your card number is <b>{card_number_formatted[:9]}******{card_number_formatted[-4:]}</b>\n"
                f"Your card PIN is <b>{card_pin}</b>\n\n"
    )
    await msg.answer("Iltimos qayta /start buyrug'ini bering!")
    await state.clear()

# ------------------------------------------ Password O'zgaritirish ------------------------------------

@router_user.callback_query(F.data == 'parolalmashtirish')
async def parolalmashtirish(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await callback.message.answer("Hozirgi parolingizni yuboring!")
    await state.set_state(NewPassword.now_password)

@router_user.message(NewPassword.now_password)
async def now_password(msg: Message, state: FSMContext):
    await state.update_data(now_password=msg.text)
    await msg.answer("Yangi Parolni yuboring!")
    await state.set_state(NewPassword.new_password)

@router_user.message(NewPassword.new_password)
async def new_password(msg: Message, state: FSMContext):
    await state.update_data(new_password=msg.text)
    await msg.answer("Parolni qayta yuboring!")
    await state.set_state(NewPassword.again_enter)

@router_user.message(NewPassword.again_enter)
async def again_password(msg: Message, state: FSMContext):
    await state.update_data(again_password=msg.text)
    data = await state.get_data()
    now_password = data['now_password']
    new_password = data['new_password']
    again_password = data['again_password']
    check = await change_password(msg.from_user.id, now_password, new_password, again_password)
    if check:
        await msg.answer("Parolingiz o'zgartirildi!", reply_markup=ortgaqaytish)
        await state.clear()
    else:
        await msg.answer("Nimadur xato ketdi")

# ---------------------------------------- Karta ma'lumotlarini olish ----------------------------------------------------------------
@router_user.callback_query(F.data == "kartamalumotlariolish")
async def ma_lumotlarni_olish(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()

    cards = await get_cards(callback.from_user.id)
    for card in cards:
        card_number = card[2]
        card_password = card[3]
        balance = card[4]

        expirydate = '01/25'
        card_number_formatted = f"{str(card_number)[:4]} {str(card_number)[4:8]} {str(card_number)[8:12]} {str(card_number)[12:]}"
        
        user_id = card[1] 
        user = await get_user(user_id)
        username = user[0][2]
        output_image_path = f'card/{username.lower()}_card.png'

        gift_money_photo = "https://thumbs.dreamstime.com/b/uzbekistan-money-som-banknotes-uzs-uzbek-bills-d-illustration-money-uzbekistan-som-bills-uzs-banknotes-uzbek-business-finance-237100171.jpg"

        if os.path.exists(output_image_path):
            if user_id in sent_bonus_users:
                await callback.message.answer_photo(
                    photo=FSInputFile(output_image_path),
                    caption=(
                    f"Your card number is <b>{card_number_formatted}</b>\n"
                    f"Your card password is <b>{card_password}</b>\n"
                    f"Your card balance is <b>{balance}</b>"
                ), reply_markup=ortgaqaytish)
            else:
                await callback.message.answer_photo(photo=gift_money_photo,
                                                caption="Bizning hizmatdan foydalanayotganligingiz uchun sizga bonus sifatida 10000 so'm berildi!\n\nTabriklaymiz🥳")
                await callback.message.answer_photo(
                    photo=FSInputFile(output_image_path),
                    caption=(
                        f"Your card number is <b>{card_number_formatted}</b>\n"
                        f"Your card password is <b>{card_password}</b>\n"
                        f"Your card balance is <b>{balance}</b>"
                    ), reply_markup=ortgaqaytish)
                sent_bonus_users.add(user_id)
        else:
            await callback.message.answer(
                "Karta ma'lumotlari mavjud emas. Iltimos, kartani qayta yaratib ko'ring!"
            )


# ---------------------------------------- Exchange currency --------------------------------------------------------

@router_user.callback_query(F.data == 'valyutakursi')
async def exchange_currency(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await callback.message.answer("Qaysi valyutani ayirboshlamoqchisiz? (Masalan: USD, EUR, UZS):")
    await state.set_state(ExchangeCurrency.from_currency)

@router_user.message(ExchangeCurrency.from_currency)
async def from_currency(msg: Message, state: FSMContext):
    await state.update_data(from_currency=msg.text.upper())
    await msg.answer("Qaysi valyutaga o'zgartirmoqchisiz? (Masalan: USD, EUR, UZS):")
    await state.set_state(ExchangeCurrency.to_currency)

@router_user.message(ExchangeCurrency.to_currency)
async def to_currency(msg: Message, state: FSMContext):
    await state.update_data(to_currency=msg.text.upper())
    await msg.answer("Summani kiriting (faqat son):")
    await state.set_state(ExchangeCurrency.amount)

@router_user.message(ExchangeCurrency.amount)
async def amount(msg: Message, state: FSMContext):
    try:
        amount = float(msg.text)
        await state.update_data(amount=amount)
        data = await state.get_data()
        from_currency = data['from_currency']
        to_currency = data['to_currency']

        result = await currency_conversion(from_currency, to_currency, amount)
        if result is None:
            await msg.answer("Kiritilgan valyutalar noto'g'ri. Iltimos, qayta urinib ko'ring.")
        else:
            await msg.answer(f"Valyutadan: {from_currency}\nValyutaga: {to_currency}\nNatija: {result}", reply_markup=ortgaqaytish)
    except ValueError:
        await msg.answer("Iltimos, faqat son kiriting.")
    await state.clear()

# ----------------------------------------------- Hamyonni tekshirish ---------------------------------------------

@router_user.callback_query(F.data == 'hamyontekshirish')
async def hamyonni_tekshirish(callback: CallbackQuery):
    await callback.message.delete()

    cards = await get_cards(callback.from_user.id)
    for card in cards:
        balance = card[4]

    await callback.message.answer(f"Sizning hamyoningizga {balance} so'm bor!", reply_markup=payorget)

@router_user.callback_query(F.data == 'hamyontoldirish')
async def hamyontoldirish(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Hamyonni to'ldirish ustida hali ishalanayotganligi sababli, faqat sizga pul o'tkazishligi bilan o'z hamyoningizni to'ldirishgiz mumkin!\n\nKamchiliklar uchun uzur so'raymiz!", reply_markup=ortgaqaytish)

@router_user.callback_query(F.data == 'pulyechibolish')
async def pulyechibolish(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Pul yechib olishning hozircha imkoni yo'q, ammo, to'lov qilsangiz bo'ladi!\n\nKamchiliklar uchun uzur so'raymiz!", reply_markup=ortgaqaytish)

# ------------------------------------------------ Pul o'tkazish --------------------------------------------------------------

@router_user.callback_query(F.data == 'pulotkazish')
async def pulotkazish(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await callback.message.answer("Pul o'tkazmoqchi bo'lgan insoningizning karta raqamini yuboring:\n\nFor example: 4470 0000 0000 0000")
    await state.set_state(PulOtkazish.kimga)

@router_user.message(PulOtkazish.kimga)
async def get_kimga(msg: Message, state: FSMContext):
    await state.update_data(kimga=msg.text)
    await msg.answer("Pulingizni kiriting (faqat son):")
    await state.set_state(PulOtkazish.summa)

@router_user.message(PulOtkazish.summa)
async def get_summa(msg: Message, state: FSMContext):
    await state.update_data(summa=msg.text)
    await msg.answer("Izoh kiritasizmi?", reply_markup=izohyes_no)

@router_user.callback_query(F.data == 'izohno')
async def no_izoh(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await state.update_data(izoh="None")
    data = await state.get_data()

    kimga = data['kimga']
    summa = int(data['summa'])
    izoh = data['izoh']

    yuboruvchi = await get_card_by_user(callback.from_user.id)
    yuboruvchi_id = yuboruvchi[0]
    yuboruvchi_number = yuboruvchi[2]
    print(f"Yuboruvchi card number: {yuboruvchi_number}")
    if not yuboruvchi:
        await callback.message.answer("Karta topilmadi.", reply_markup=ortgaqaytish)
        return

    yuboruvchi_balance = yuboruvchi[4]  

    if yuboruvchi_balance < summa:
        await callback.message.answer("Balansingizda yetarli mablag' yo'q.", reply_markup=ortgaqaytish)
        return

    post_yuboruvchi_balance = yuboruvchi_balance - summa
    await update_balance(yuboruvchi_id, post_yuboruvchi_balance)

    qabul_qiluvchi = await get_card_by_number(kimga)
    qabul_qiluvchi_id = qabul_qiluvchi[0]
    qabul_qiluvchi_chat_id = qabul_qiluvchi[1]
    qabul_qiluvchi_number = qabul_qiluvchi[2]
    if not qabul_qiluvchi:
        await callback.message.answer("Qabul qiluvchining kartasi topilmadi.", reply_markup=ortgaqaytish)
        return

    qabul_qiluvchi_balance = qabul_qiluvchi[4]  
    post_qabul_qiluvchi_balance = qabul_qiluvchi_balance + summa
    await update_balance(qabul_qiluvchi_id, post_qabul_qiluvchi_balance)
    await create_transaction(yuboruvchi_number, qabul_qiluvchi_number, summa, izoh)

    await callback.message.answer(
        f"Sizning pulingiz {summa} so'mga o'tkazildi.\n\nKimga: {kimga}\nIzoh: {izoh}",
        reply_markup=ortgaqaytish)
    await bot.send_message(chat_id=qabul_qiluvchi_chat_id, text="Sizga pul o'tkazildi!")
    await state.clear()

@router_user.callback_query(F.data == 'izohyes')
async def yes_izoh(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await callback.message.answer("Izohni yuboring: ")
    await state.set_state(PulOtkazish.izoh)

@router_user.message(PulOtkazish.izoh)
async def get_izoh(msg: Message, state: FSMContext):
    await state.update_data(izoh=msg.text)
    data = await state.get_data()

    kimga = data['kimga']
    summa = int(data['summa'])
    izoh = data['izoh']

    yuboruvchi = await get_card_by_user(msg.from_user.id)
    yuboruvchi_id = yuboruvchi[0]
    yuboruvchi_number = yuboruvchi[2]
    print(f"Yuboruvchi card number: {yuboruvchi_number}")
    if not yuboruvchi:
        await msg.answer("Karta topilmadi.", reply_markup=ortgaqaytish)
        return

    yuboruvchi_balance = yuboruvchi[4]  

    if yuboruvchi_balance < summa:
        await msg.answer("Balansingizda yetarli mablag' yo'q.", reply_markup=ortgaqaytish)
        return

    post_yuboruvchi_balance = yuboruvchi_balance - summa
    await update_balance(yuboruvchi_id, post_yuboruvchi_balance)

    qabul_qiluvchi = await get_card_by_number(kimga)
    qabul_qiluvchi_id = qabul_qiluvchi[0]
    qabul_qiluvchi_chat_id = qabul_qiluvchi[1]
    qabul_qiluvchi_number = qabul_qiluvchi[2]
    if not qabul_qiluvchi:
        await msg.answer("Qabul qiluvchining kartasi topilmadi.", reply_markup=ortgaqaytish)
        return

    qabul_qiluvchi_balance = qabul_qiluvchi[4]  
    post_qabul_qiluvchi_balance = qabul_qiluvchi_balance + summa
    await update_balance(qabul_qiluvchi_id, post_qabul_qiluvchi_balance)
    await create_transaction(yuboruvchi_number, qabul_qiluvchi_number, summa, izoh)

    await msg.answer(
        f"Sizning pulingiz {summa} so'mga o'tkazildi.\n\nKimga: {kimga}\nIzoh: {izoh}",
        reply_markup=ortgaqaytish)
    await bot.send_message(chat_id=qabul_qiluvchi_chat_id, text="Sizga pul o'tkazildi!")
    await state.clear()


# ------------------------------------------------------- Ortga qaytish -------------------------------------------------------

@router_user.callback_query(F.data == 'ortgaqaytish')
async def ortgaqaytish_handler(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Asosiy menyuga qaytdingiz!", reply_markup=menu_users)