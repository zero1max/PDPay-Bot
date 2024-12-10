from aiogram import F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import Command
from loader import router_user
from keyboards.inline.main import *
from keyboards.default.main import *
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from database.userdb import create_user, create_card, get_user, user_exists, change_password
from random import *
from PIL import Image, ImageDraw, ImageFont

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


def edit_card_image(carta_path, output_path, card_number, name, expiry_date):
    # Rasmni yuklash
    img = Image.open(carta_path)

    # Rasmga chizish uchun ob'ekt
    draw = ImageDraw.Draw(img)

    font_path = "card/firecode.ttf"
    # Shriftni yuklash
    try:
        font_num = ImageFont.truetype(font_path, 50)  # Windows tizimida ishlaydi
        font_date = ImageFont.truetype(font_path, 30)  
        font_name = ImageFont.truetype(font_path, 40)  
    except IOError:
        font = ImageFont.load_default()  # Agar shrift yo'q bo'lsa, tizimning default shriftini yuklaydi

    # Matnlarni joylashtirish
    draw.text((300, 450), card_number, fill="white", font=font_num)  # Karta raqami
    draw.text((500, 530), expiry_date, fill="white", font=font_date)  # Amal qilish muddati
    draw.text((200, 560), name, fill="white", font=font_name)         # Foydalanuvchi ismi

    # O'zgartirilgan rasmni saqlash
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
        await callback.answer()  # Callbackni yopish

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

    # Foydalanuvchi ma'lumotlari
    name = data['name']
    surname = data['surname']
    age = data['age']
    number = data['number']
    user_id = msg.from_user.id

    # Foydalanuvchini bazaga qo'shish (loyiha talabiga ko'ra funksiya chaqirildi)
    await create_user(user_id, name, surname, age, number)
    await msg.answer("Siz ro'yxatdan o'tdingiz!")

    # Karta raqami va PIN kodini yaratish
    card_number = randint(4470000000000000, 4471000000000000)
    card_pin = randint(1000, 9999)
    card_number_formatted = f"{str(card_number)[:4]} {str(card_number)[4:8]} {str(card_number)[8:12]} {str(card_number)[12:]}"
    expirydate = "01/25"

    # Karta tasvirini yaratish
    input_image_path = 'card/card.png'
    output_image_path = 'card/output_card.png'
    edit_card_image(input_image_path, output_image_path, card_number_formatted, name, expirydate)

    # Kartani bazaga qo'shish (agar mavjud funksiya bo'lsa)
    await create_card(user_id, card_number, card_pin)

    # Foydalanuvchiga karta ma'lumotlarini yuborish
    await msg.answer_photo(
        photo=FSInputFile(output_image_path),
        caption=f"Your card number is <b>{card_number_formatted[:9]}******{card_number_formatted[-4:]}</b>\n"
                f"Your card PIN is <b>{card_pin}</b>\n\n"
                "Ogohlantiramiz bu ma'lumotlarni hech kimga oshkor qilmang!",
        parse_mode="HTML"
    )
    await msg.answer("Iltimos qayta /start buyrug'ini bering!")

# ------------------------------------------ Password O'zgaritirish ------------------------------------

@router_user.callback_query(F.data == 'parolalmashtirish')
async def parolalmashtirish(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await callback.message.answer("Hozirgi parolingizni yuboring!")
    await state.set_state(NewPassword.now_password)

@router_user.message(NewPassword.now_password)
async def now_password(msg: Message, state: FSMContext):
    await state.update_data(now_password=msg.text)
    await msg.answer("yangi Parolni yuboring!")
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
        await msg.answer("Parolingiz o'zgartirildi!", reply_markup=menu_users)
        await state.clear()
    else:
        await msg.answer("Nimadur xato ketdi")

