import sys, logging, asyncio

from database.userdb import *
from loader import dp, bot
import handlers

async def main():
    await setup_database()
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())