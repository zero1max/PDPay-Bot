from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from loader import router_user
from keyboards.default.main import *
from keyboards.inline.main import *

@router_user.message(Command('start'))
async def start(msg: Message):
    await msg.answer("Assalomu aleykum!", reply_markup=choice_language)