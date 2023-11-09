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
    news_post = get_post_from_ChatGPT(news_headlines)

    await bot.send_message(
        chat_id=channel_id,
        text='Новости за сегодня:\n\n' + news_post
    )


def register_handlers_channel(dp: Dispatcher):
    dp.register_message_handler(write_news)
    start_schedule()


def start_schedule():
    scheduler = AsyncIOScheduler()

    trigger1 = CronTrigger(timezone='Europe/Moscow', hour=7, minute=00, second=0)
    scheduler.add_job(write_news, trigger=trigger1)

    trigger2 = CronTrigger(timezone='Europe/Moscow', hour=18, minute=00, second=0)
    scheduler.add_job(write_news, trigger=trigger2)

    scheduler.start()
