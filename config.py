import logging
import os

import openai

from aiogram import Bot
from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

openai.api_key = os.getenv('openai_api_key')
openai.api_base = os.getenv('openai_api_base')

channel_id = os.getenv('channel_id')

storage = MemoryStorage()

bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot, storage=storage)
