from aiogram import types
from aiogram.dispatcher.filters import Command
from keyboards.default.tayorkey import menuStart

from loader import dp

@dp.message_handler(Command("boshlash"))
async def create_post(message: types.Message):
	await message.answer(f"<b>👋 Salom, {message.from_user.full_name} Hozir siz bilan ajoyib 📋hikoya tuzamiz, Sizga Savol beramiz. Sizdan iltimosim, Barcha Savollarga Javob Bering Tayyormisiz???</b>",reply_markup=menuStart)

