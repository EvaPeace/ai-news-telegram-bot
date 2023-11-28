from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils import exceptions as AiogramExceptions

from config import dp, bot, admins_ids, scheduler

from handlers.channel import write_news, start_schedule
from keyboards import kb_admin

from functions.Text import send_logs_auto
import logging

logger2 = logging.getLogger(__name__)


class FSMAdmin(StatesGroup):
    admin = State()


@dp.message_handler(commands=['admin_login'])
async def admin_login(message: types.Message, state: FSMContext):
    """
    Вход в админку. Проверяет id пользователя, если он дминский, то впускает.
    """
    try:
        await message.answer(
            'Проверяем вас на админа...',
        )

        user_id = str(message.from_user.id)
        full_name = message.from_user.full_name

        if user_id in admins_ids:
            await FSMAdmin.admin.set()

            await message.answer(
                f'Добро пожаловать в панель администратора, {full_name}',
                reply_markup=kb_admin
            )

        else:
            await message.answer(
                f'Извините, но вы, {full_name}, не админ. Я вызываю полицию',
            )
    except AiogramExceptions.NetworkError as e:
        logger2.error(f"admin_login {e}")
        await send_logs_auto(e)
    except AiogramExceptions.ChatNotFound as e:
        logger2.error(f"admin_login {e}")
        await send_logs_auto(e)
    except Exception as e:
        logger2.error(f"admin_login {e}")
        await send_logs_auto(e)


@dp.message_handler(commands=['admin_logout'], state=FSMAdmin.admin)
async def admin_logout(message: types.Message, state: FSMContext):
    """
    Выход из админки
    """
    await state.finish()

    full_name = message.from_user.full_name

    await message.answer(
        f'Выход из панели администратора успешен. Пока-пока, {full_name}',
    )


@dp.message_handler(commands=['send_post_manually'], state=FSMAdmin.admin)
async def send_post_manually(message: types.Message, n_news=3):
    """
    Вручную запускает `write_news` для написания поста.

    :param message: Сообщение, что выслал пользователь
    :type message: aiogram.types.Message
    :param n_news: Количество новостей для поста.
    :type n_news: int
    """
    try:
        await message.answer('Отправляю пост вручную...')

        await write_news()

        await message.answer('Пост has been отправлен')
    except AiogramExceptions.ChatNotFound as e:
        logger2.error(f"send_post_manually {e}")
        await send_logs_auto(e)
    except AiogramExceptions.NetworkError as e:
        logger2.error(f"send_post_manually {e}")
        await send_logs_auto(e)
    except NameError as e:
        logger2.error(f"send_post_manually {e}")
        await send_logs_auto(e)
    except Exception as e:
        logger2.error(f"send_post_manually {e}")
        await send_logs_auto(e)


@dp.message_handler(commands=['send_logs_manually'], state=FSMAdmin.admin)
async def send_logs_manually(message: types.Message):
    """
    Вручную отправляет логги. Логги отправляются в лс того, кто вызвал.

    :param message: Сообщение, что выслал пользователь
    :type message: aiogram.types.Message
    """
    try:
        await message.answer(
            'Отправляю логги...',
        )

        with open('.\main_log.log', 'rb') as log_file:
            await bot.send_document(
                chat_id=message.chat.id,
                document=log_file)
    except IOError as e:
        logger2.error(f"send_logs_manually {e}")
        await send_logs_auto(e)
    except Exception as e:
        logger2.error(f"send_logs_manually {e}")
        await send_logs_auto(e)


@dp.message_handler(commands=['disable_schedule'], state=FSMAdmin.admin)
async def disable_schedule(message: types.Message):
    """
    Отключает вызов функции `write_news` по расписанию

    :param message: Сообщение, что выслал пользователь
    :type message: aiogram.types.Message
    """
    try:
        if scheduler.running:
            await message.answer(
                "Отключаю расписание...🚧 \n Пуск ручного режима... \n Ручной режим запущен."
            )
            scheduler.shutdown()
        else:
            await message.answer(
                "Расписание уже в отключке. не жди врубай, время денга!"
            )
    except AiogramExceptions.NetworkError as e:
        logger2.error(f"dis_sch{e}")
        await send_logs_auto(e)
    except AiogramExceptions.ChatNotFound as e:
        logger2.error(f"dis_sch {e}")
        await send_logs_auto(e)
    except Exception as e:
        logger2.error(f"dis_sch {e}")
        await send_logs_auto(e)


@dp.message_handler(commands=['enable_schedule'], state=FSMAdmin.admin)
async def enable_schedule(message: types.Message):
    """
    Включает вызов функции `write_news` по расписанию

    :param message: Сообщение, что выслал пользователь
    :type message: aiogram.types.Message
    """
    try:
        if scheduler.running:
            await message.answer(
                "Расписание уже запущено, попей пока кифирчику."
            )

        else:
            await message.answer(
                "Подрубаю расписание...✅\n Отключение ручного режима...\n Ручной режим отключён."
            )
            await start_schedule()
    except AiogramExceptions.NetworkError as e:
        logger2.error(f"en_sch{e}")
        await send_logs_auto(e)
    except AiogramExceptions.ChatNotFound as e:
        logger2.error(f"en_sch {e}")
        await send_logs_auto(e)
    except Exception as e:
        logger2.error(f"en_sch {e}")
        await send_logs_auto(e)


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(admin_login, commands=['admin_login'])
    dp.register_message_handler(admin_logout, commands=['admin_logout'], state=FSMAdmin.admin)
    dp.register_message_handler(send_logs_manually, commands=['send_logs_manually'], state=FSMAdmin.admin)
    dp.register_message_handler(disable_schedule, commands=['disable_schedule'], state=FSMAdmin.admin)
    dp.register_message_handler(enable_schedule, commands=['enable_schedule'], state=FSMAdmin.admin)
