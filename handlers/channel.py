from datetime import datetime, timedelta

from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher.filters.state import StatesGroup, State
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from config import dp, bot, channel_id
from functions import get_news_headlines, get_post_from_ChatGPT


class FSMClient(StatesGroup):
    solution = State()


async def write_news():
    news_headlines = get_news_headlines()
    # news_post = get_post_from_ChatGPT(news_headlines)

    await bot.send_message(chat_id=channel_id,
                           text='Для экономии здесь только заголовки:\n' + '\n\n'.join(news_headlines))


def register_handlers_channel(dp: Dispatcher):
    dp.register_message_handler(write_news)
    start_schedule()


def start_schedule():
    scheduler = AsyncIOScheduler(timezone='Europe/Moscow')

    scheduler.add_job(write_news, trigger='date', run_date=datetime.now() + timedelta(seconds=10))

    # trigger1 = CronTrigger(hour=7, minute=00, second=0)
    # scheduler.add_job(write_news, trigger=trigger1)
    #
    # trigger2 = CronTrigger(hour=18, minute=00, second=0)
    # scheduler.add_job(write_news, trigger=trigger2)

    scheduler.start()
