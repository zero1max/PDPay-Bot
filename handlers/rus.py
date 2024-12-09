from aiogram import F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from loader import router_user

@router_user.callback_query(F.data == "ru")
async def start_ru(callback: CallbackQuery):
    await callback.message.answer("Привет!")
    await callback.message.delete()
    await callback.answer()  # Callbackni yopish