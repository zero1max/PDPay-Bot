from aiogram import F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from loader import router_user

@router_user.callback_query(F.data == "en")
async def start_en(callback: CallbackQuery):
    await callback.message.answer("Hello!")
    await callback.message.delete()
    await callback.answer()  # Callbackni yopish
    