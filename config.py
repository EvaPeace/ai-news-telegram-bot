import logging
import os

import openai

from aiogram import Bot
from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# настройка базового логгера
logging.basicConfig(
    level=logging.INFO,  # Уровень логирования (может быть DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(name)s %(asctime)s %(levelname)s %(message)s",
    filename='main_log.log',  # Имя файла, куда будут записываться логи
    filemode='a+',  # Режим записи (a - добавление, w - перезапись)
    encoding='utf-8'
)

openai.api_key = os.getenv('openai_api_key')
openai.api_base = os.getenv('openai_api_base')

storage = MemoryStorage()

bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot, storage=storage)
