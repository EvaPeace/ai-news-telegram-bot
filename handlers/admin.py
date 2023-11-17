from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from config import dp, bot, admins_ids, scheduler

from handlers.channel import write_news, start_schedule
from keyboards import kb_admin


class FSMAdmin(StatesGroup):
    admin = State()


@dp.message_handler(commands=['admin_login'])
async def admin_login(message: types.Message, state: FSMContext):
    """
    Вход в админку. Проверяет id пользователя, если он дминский, то впускает.
    """
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
    await message.answer('Отправляю пост вручную...')

    await write_news()

    await message.answer('Пост has been отправлен')


@dp.message_handler(commands=['send_logs_manually'], state=FSMAdmin.admin)
async def send_logs_manually(message: types.Message):
    """
    Вручную отправляет логги.

    :param message: Сообщение, что выслал пользователь
    :type message: aiogram.types.Message
    """
    await message.answer(
        'Отправляю логги...',
    )

    with open('.\main_log.log', 'rb') as log_file:
        await bot.send_document(
            chat_id=message.chat.id,
            document=log_file)


async def send_logs_auto(exception: Exception):
    """
    Автоматически отправляет логги в лс всех админов, при каких-либо ошибках

    :param exception: Ошибка, которая вынудила вызвать функцию.
    :type exception: Exception
    """
    with open('.\main_log.log', 'rb') as log_file:
        for admin_id in admins_ids:
            await bot.send_message(
                chat_id=admin_id,
                text='Внимание! Случилась какая-то ошибка. Высылаю логги.\n\n'
                     'Логги высланы по вине следующей ошибки:\n\n' + str(exception)
            )

            await bot.send_document(
                chat_id=admin_id,
                document=log_file
            )


@dp.message_handler(commands=['disable_schedule'], state=FSMAdmin.admin)
async def disable_schedule(message: types.Message):
    """
    Отключает вызов функции `write_news` по расписанию

    :param message: Сообщение, что выслал пользователь
    :type message: aiogram.types.Message
    """
    if scheduler.running:
        await message.answer(
            "Отключаю расписание...🚧 \n Пуск ручного режима... \n Ручной режим запущен."
        )
        scheduler.shutdown()
    else:
        await message.answer(
            "Расписание уже в отключке. не жди врубай, время денга!"
        )


@dp.message_handler(commands=['enable_schedule'], state=FSMAdmin.admin)
async def enable_schedule(message: types.Message):
    """
    Включает вызов функции `write_news` по расписанию

    :param message: Сообщение, что выслал пользователь
    :type message: aiogram.types.Message
    """
    if scheduler.running:
        await message.answer(
            "Расписание уже запущено, попей пока кифирчику."
        )

    else:
        await message.answer(
            "Подрубаю расписание...✅\n Отключение ручного режима...\n Ручной режим отключён."
        )
        await start_schedule()


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(admin_login, commands=['admin_login'])
    dp.register_message_handler(admin_logout, commands=['admin_logout'], state=FSMAdmin.admin)
    dp.register_message_handler(send_logs_manually, commands=['send_logs_manually'], state=FSMAdmin.admin)
