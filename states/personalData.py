from aiogram.dispatcher.filters.state import StatesGroup, State


# Shaxsiy ma'lumotlarni yig'sih uchun PersonalData holatdan yaratamiz
class PersonalData(StatesGroup):
	ism = State()
	familya = State()
	yosh = State()
	shahar = State()
	birodar = State()
	tanishuv = State()
	shaharr = State()
	transport = State()
	rang = State()
	qaroqchi = State()
	dedi = State()
	hayvon = State()
