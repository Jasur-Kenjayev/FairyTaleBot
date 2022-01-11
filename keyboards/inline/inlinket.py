from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# 1-usul.
categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
    [
       InlineKeyboardButton(text="🔄Qayta Yozish🔄", callback_data="courses"),
    ],
    [
        InlineKeyboardButton(text="👥Do'stlarga Ulashish✉️", switch_inline_query="👋 Salom Ushbu 🤖Bot Orqali Kayfiyatingizni Ko'taring😊"),
    ],
])