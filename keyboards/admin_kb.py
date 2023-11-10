from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# keyboard for admin
kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)

b_disable_schedule = KeyboardButton('/disable_schedule')
b_send_post_manually = KeyboardButton('/send_post_manually')
b_admin_logout = KeyboardButton('/admin_logout')

kb_admin.add(b_disable_schedule)
kb_admin.add(b_send_post_manually)
kb_admin.add(b_admin_logout)
