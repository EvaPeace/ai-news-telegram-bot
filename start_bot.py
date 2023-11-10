from aiogram.utils import executor

from config import dp

from handlers import register_handlers_client, register_handlers_channel, register_handlers_admin


async def on_startup(_):
    print('Bot started')


register_handlers_client(dp)
register_handlers_channel(dp)
register_handlers_admin(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
