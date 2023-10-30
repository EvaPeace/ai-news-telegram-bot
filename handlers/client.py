from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State

from config import dp, bot
from keyboards import kb_client


class FSMClient(StatesGroup):
    solution = State()


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer(
        'Привет, я бот, который создаёт новостные посты',
        reply_markup=kb_client
    )


@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await message.answer(
        'help_message',
        reply_markup=kb_client
    )


@dp.message_handler(commands=['info'])
async def command_info(message: types.Message):
    await message.answer(
        'info_message',
        reply_markup=kb_client
    )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_info, commands=['info'])
    dp.register_message_handler(command_help, commands=['help'])
