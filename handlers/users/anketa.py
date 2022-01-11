from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.tayorkey import menuStart
from aiogram.dispatcher.filters import Command

from keyboards.inline.inlinket import categoryMenu
from aiogram.types import Message, CallbackQuery
from loader import dp
from states.personalData import PersonalData


# /form komandasi uchun handler yaratamiz. Bu yerda foydalanuvchi hech qanday holatda emas, state=None
@dp.message_handler()
async def enter_test(message: types.Message):
    text = message.text
    if text == "👤Tayyorman✅":
    	await message.answer("<b>ismingiz nima?</b>",reply_markup=ReplyKeyboardRemove())
    	await PersonalData.ism.set()


@dp.message_handler(state=PersonalData.ism)
async def answer_ism(message: types.Message, state: FSMContext):
    ism = message.text
    await state.update_data(
        {"ism": ism}
    )

    await message.answer("<b>Familiyangiz nima?</b>")

    # await PersonalData.email.set()
    await PersonalData.next()

@dp.message_handler(state=PersonalData.familya)
async def answer_familya(message: types.Message, state: FSMContext):
     familya = message.text
     await state.update_data(
        {"familya": familya}
     )
     await message.answer("<b>Yoshingiz nechada?</b>")
     await PersonalData.next()


@dp.message_handler(state=PersonalData.yosh)
async def answer_yosh(message: types.Message, state: FSMContext):
	yosh = message.text
	await state.update_data(
        {"yosh": yosh}
    )
	await message.answer("<b>Qaysi shaharda yashaysiz?</b>")
	await PersonalData.next()


@dp.message_handler(state=PersonalData.shahar)
async def answer_shahar(message: types.Message, state: FSMContext):
	shahar = message.text
	await state.update_data(
        {"shahar": shahar}
    )
	await message.answer("<b>Sizning eng yaqin birodaringiz kim ismini yozing?</b>")
	await PersonalData.next()


@dp.message_handler(state=PersonalData.birodar)
async def answer_birodar(message: types.Message, state: FSMContext):
	birodar = message.text
	await state.update_data(
        {"birodar": birodar}
    )
	await message.answer("<b>O'sha do'stingiz bilan qayerda tanishgansiz?</b>")
	await PersonalData.next()

@dp.message_handler(state=PersonalData.tanishuv)
async def answer_tanishuv(message: types.Message, state: FSMContext):
	tanishuv  = message.text
	await state.update_data(
        {"tanishuv": tanishuv}
    )
	await message.answer("<b>Oxirgi marta qaysi shaharga bordingiz?</b>")
	await PersonalData.next()
	

@dp.message_handler(state=PersonalData.shaharr)
async def answer_shaharr(message: types.Message, state: FSMContext):
	shaharr = message.text
	await state.update_data(
        {"shaharr": shaharr}
    )
	await message.answer("<b>O'sha shaharga qaysi transportda bordingiz?</b>")
	await PersonalData.next()


@dp.message_handler(state=PersonalData.transport)
async def answer_transport(message: types.Message, state: FSMContext):
    transport = message.text

    await state.update_data(
        {"transport": transport}
    )
    
    await message.answer("<b>O'sha transportning rangi taxminan qanday edi?</b>")

    await PersonalData.next()


@dp.message_handler(state=PersonalData.rang)
async def answer_rang(message: types.Message, state: FSMContext):
    rang = message.text

    await state.update_data(
        {"rang": rang}
    )
    
    await message.answer("<b>Yo'lda kimni uchratgan edingiz, uning ismi nima edi?</b>")

    await PersonalData.next()


@dp.message_handler(state=PersonalData.qaroqchi)
async def answer_qaroqchi(message: types.Message, state: FSMContext):
    qaroqchi = message.text

    await state.update_data(
        {"qaroqchi": qaroqchi}
    )
    
    await message.answer("<b>Siz o'sha uchratgan odamingizga nima dedingiz?</b>")

    await PersonalData.next()


@dp.message_handler(state=PersonalData.dedi)
async def answer_dedi(message: types.Message, state: FSMContext):
    dedi = message.text

    await state.update_data(
        {"dedi": dedi}
    )
    
    await message.answer("<b>Yo'lda qaysi hayvonga duch kelgan edingiz?</b>")

    await PersonalData.next()


@dp.message_handler(state=PersonalData.hayvon)
async def answer_hayvon(message: types.Message, state: FSMContext):
    hayvon = message.text

    await state.update_data(
        {"hayvon": hayvon}
    )
    
    
    # Ma`lumotlarni qayta o'qiymiz
    data = await state.get_data()
    ism = data.get("ism")
    familya = data.get("familya")
    yosh = data.get("yosh")
    shahar = data.get("shahar")
    birodar = data.get("birodar")
    tanishuv = data.get("tanishuv")
    shaharr = data.get("shaharr")
    transport = data.get("transport")
    rang = data.get("rang")
    qaroqchi = data.get("qaroqchi")
    dedi = data.get("dedi")
    hayvon = data.get("hayvon")
    
    msg = f"<b>Bir bor ekan bir yo'q ekan, Hozirgi {shahar} degan shaharda {ism} degan odam bor ekan. Uning familiyasi {familya} ekan. Aytishlaricha hozir uning yoshi {yosh} da ekan. Kunlardan bir kuni {ism} {tanishuv} degan joyda {birodar} bilan tanishibdi. {ism} va {birodar} do'st bo'lishibdi. Bir kuni {ism} bilan {birodar} birgalikda {shaharr} ga borishga qaror qilishibdi. Ular {rang} {transport} ga minib yo'lga chiqibdi. Uzoq yo'l bosibdi. Yo'lda {transport} buzilibdi. Shu payt {ism} va {birodar} oldiga baland bo'yli {qaroqchi} paydo bo'lib Ularning yo'lini to'sibdi. Aslida {qaroqchi} qaroqchilik qilar ekan. Shunda {ism} {qaroqchi} ga qarab {dedi} - debdi. Buni eshitgan qaroqchi - {qaroqchi} ning g'azabi kelib {ism} ga qilich ko'taribdi. Shu payt {ism} ning baxtiga uzoqdan bahaybat yirtqich {hayvon} paydo bo'ldi va u yugurib {qaroqchi} oldiga keldi. Keyin esa {qaroqchi} ni g'ajib tashlab o'ljaga aylantiribdi. Buni ko'rgan {ism} va {birodar} xursand bo'ldilar. Chunki {hayvon} ularni {qaroqchi} dan xalos etgandi. Shunday qilib har ikki do'st: {familya} {ism} va {birodar} murodu maqsadiga yetgan ekan...</b>"
    await message.answer(msg,reply_markup=categoryMenu)
    await state.finish()


@dp.callback_query_handler(text="courses")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("<b>🔄Qaytadan Boshlash Uchun 🤖Botga /boshlash Tugmasini Bosing✅\n/boshlash /boshlash /boshlash\n/boshlash /boshlash /boshlash\n/boshlash /boshlash /boshlash</b>")
    # 2-variant
    # await state.reset_state()

    # 3-variant. Ma`lumotlarni saqlab qolgan holda
    # await state.reset_state(with_data=False)
