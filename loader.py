from aiogram import Dispatcher , Router, Bot
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from config import BOT_TOKEN, CLICK_TOKEN

click_token = CLICK_TOKEN
dp = Dispatcher()
router_admin = Router()
router_user = Router()
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp.include_router(router=router_admin)
dp.include_router(router=router_user)