from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp

@dp.message_handler(Command("creator"))
async def create_Creator(message: types.Message):
	await message.answer("<b>🤖Bot Yaratuvchisi🤖\n\n💻Dasturchi 👉 @Python_Koders\n📡Channel 👉 @Python_Koderuz</b>")