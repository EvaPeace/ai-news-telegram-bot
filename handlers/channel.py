from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils import exceptions as AiogramExceptions

from apscheduler.triggers.cron import CronTrigger

from config import dp, bot, channel_id, scheduler
from functions import get_news_headlines, get_post_from_ChatGPT

from functions.Text import send_logs_auto
import logging

# creating logger2 to use in sending logs
logger2 = logging.getLogger(__name__)


# setting the state admin
class FSMClient(StatesGroup):
    solution = State()


''' creating function that sending news headlines into ChatCPT, 
which invents news and and then sending news into channel'''


async def write_news():
    try:
        news_headlines = get_news_headlines()
        news_post = await get_post_from_ChatGPT(news_headlines)

        await bot.send_message(
            chat_id=channel_id,
            text='Новости за сегодня:\n\n' + news_post
        )
    except TypeError as e:
        logger2.error(f"write_news {e}")
        await send_logs_auto(e)
    # Ошибка сети
    except AiogramExceptions.NetworkError as e:
        logger2.error(f"write_news {e}")
        await send_logs_auto(e)
    # Ошибка, когда бот не может найти ID чата
    except AiogramExceptions.ChatNotFound as e:
        logger2.error(f"write_news {e}")
        await send_logs_auto(e)
    # Все остальные ошибки
    except Exception as e:
        logger2.error(f"write_news {e}")
        await send_logs_auto(e)


def register_handlers_channel(dp: Dispatcher):
    dp.register_message_handler(write_news)
    start_schedule()


# function that starting sending posts into channel according to the schedule

def start_schedule():
    try:
        trigger1 = CronTrigger(timezone='Europe/Moscow', hour=7, minute=00, second=0)
        scheduler.add_job(write_news, trigger=trigger1)

        trigger2 = CronTrigger(timezone='Europe/Moscow', hour=18, minute=00, second=0)
        scheduler.add_job(write_news, trigger=trigger2)

        scheduler.start()
    except Exception as e:
        logger2.error(f"start_sch {e}")
        send_logs_auto(e)
