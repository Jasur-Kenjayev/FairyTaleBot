from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp

@dp.message_handler(Command("help"))
async def create_post(message: types.Message):
	await message.answer("<b>🤖Botdan To'liq Foydalanish Uchun Bot Ko'rsatgan Kanalga ➕Obuna Bo'ling!!!\n\n🤖Ushbu Bot Orqali O'z 📋Hikoyangizni ✍Yozing✅</b>")