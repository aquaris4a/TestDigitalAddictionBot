from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
import os

from menu import register_menu_handlers
from tests.internet import register_handlers_internet
from tests.stroop import register_handlers_stroop
from tests.bourdon import register_handlers_bourdon
from tests.beck import register_handlers_beck

API_TOKEN = os.getenv("API_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

register_menu_handlers(dp)
register_handlers_internet(dp)
register_handlers_stroop(dp)
register_handlers_bourdon(dp)
register_handlers_beck(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
