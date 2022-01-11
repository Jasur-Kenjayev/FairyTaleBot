import logging

from aiogram import types
from data.config import CHANNELS
from keyboards.inline.subscription import check_button
from loader import bot, dp
from utils.misc import subscription


@dp.message_handler(commands=['start'])
async def show_channels(message: types.Message):
    channels_format = str()
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        
        channels_format += f"👉 <a href='{invite_link}'>{chat.title}</a>\n"

    await message.answer(f"<b>🤖Botdan To'liq Foydalanish Uchun Quyidagi Kanallarga ➕Obuna Bo'ling</b>\n"
                         f"{channels_format}",
                         reply_markup=check_button,
                         disable_web_page_preview=True)


@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    await call.answer()
    result = str()
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id,
                                          channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result += f"<b>{channel.title}	 Kanaliga obuna bo'lgansiz✅ Botdan to'liq foydalanish uchun /boshlash tugmasini bosing\n\n/boshlash /boshlash /boshlash\n /boshlash /boshlash /boshlash\n /boshlash /boshlash /boshlash</b>\n\n"
        else:
            invite_link = await channel.export_invite_link()
            result += (f"<b>{channel.title}</b> <b>Kanaliga ➕obuna bo'lmagansiz</b> 👉 "
                       f"<a href='{invite_link}'><b>Obuna bo'ling</b></a>\n\n")

    await call.message.answer(result, disable_web_page_preview=True)
