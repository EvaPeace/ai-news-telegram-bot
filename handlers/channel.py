from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils import exceptions as AiogramExceptions

from apscheduler.triggers.cron import CronTrigger

from config import dp, bot, channel_id, scheduler
from functions import get_news_headlines, get_post_from_ChatGPT

from functions.Text import send_logs_auto
import logging

logger2 = logging.getLogger(__name__)


class FSMClient(StatesGroup):
    solution = State()


async def write_news():
    """
    Вызывается автоматически, получает новостные заголовки, генерирует новостной пост через ChatGPT, а затем высылает его в канал.

    :return: None
    """
    try:
        news_list = await get_news_headlines()  # getting news headlines from the rss

        for news in news_list:
            news_post = await get_post_from_ChatGPT(news)  # sending headlines to ChatGPT and getting the news
            news_post += '\n\n*Новость вымышленная. Мы не несем ответственности за текст выше.' \
                         'Этот текст написан нейросетью ChatGPT. Все вопросы к Open AI*'

            for c in ('_', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!'):
                news_post = news_post.replace(c, "\\" + c)

            await bot.send_photo(
                chat_id=channel_id,
                photo=news["img_url"],
                caption=news_post,
                parse_mode="MarkdownV2"
            )

    except Exception as e:
        logger2.error(f"write_news: {e}")
        await send_logs_auto(e)


def start_schedule():
    """
    Запускает автоматический вызов функции write_news по расписанию

    :return: None
    """
    try:
        # the first call of write_news at 7:00
        trigger1 = CronTrigger(timezone='Europe/Moscow', hour=7, minute=00, second=0)
        scheduler.add_job(write_news, trigger=trigger1)

        # the second call of write_news at 18:00
        trigger2 = CronTrigger(timezone='Europe/Moscow', hour=18, minute=00, second=0)
        scheduler.add_job(write_news, trigger=trigger2)

        scheduler.start()

    except Exception as e:
        logger2.error(f"start_schedule: {e}")
        send_logs_auto(e)


def register_handlers_channel(dp: Dispatcher):
    dp.register_message_handler(write_news)
    dp.register_message_handler(start_schedule)
    start_schedule()
