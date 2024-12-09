from aiogram import F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from loader import router_user
from keyboards.inline.main import *
from keyboards.default.main import *
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from database.userdb import create_user

class UserAge(StatesGroup):
    user_age = State()


class UserInformations(StatesGroup):
    number = State()
    name = State()
    surname = State()
    age = State()

@router_user.callback_query(F.data == "uz")
async def start_uz(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Assalomu aleykum!")
    await callback.message.answer("Yoshingizni kiriting!")
    await state.set_state(UserAge.user_age)
    await callback.message.delete()
    await callback.answer()  # Callbackni yopish

@router_user.message(UserAge.user_age)
async def user_age(msg: Message, state: FSMContext):
    await state.update_data(user_age=msg.text)
    data = await state.get_data()
    print(data)
    age = data['user_age']
    print(age)
    if age >= '16':
        await msg.answer("Karta yaratamizmi?", reply_markup=create_card)
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
    print(data)
    name = data['name']
    surname = data['surname']
    age = data['age']
    number = data['number']
    await create_user(name, surname, age, number)
