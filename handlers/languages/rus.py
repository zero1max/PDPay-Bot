from aiogram import F
from aiogram.types import Message, CallbackQuery
from loader import router_user

@router_user.message(F.data == 'ru')
async def start_uz(msg: Message):
    await msg.answer("Привет")