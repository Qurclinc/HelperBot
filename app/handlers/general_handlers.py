from aiogram import Router, F, types
from aiogram.filters import Command
import app.keyboards as kb

router = Router()

@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Бот помогающий решать задачи для криптографии (опционально)\n`/help` для помощи.", reply_markup=kb.main_kb, parse_mode="Markdown")

@router.message(Command("help"))
async def get_help(message: types.Message):
    await message.answer("""Продукт предоставляется "как есть" (так называемый AS IS).
Создатели не несут ответственности за допущенные ошибки и погрешности. Это вы недостаточно протестировали средство. Shame on you.

Посмотреть исходный код можно на [github](https://github.com/Qurclinc/HelperBot)""", parse_mode="Markdown", reply_markup=kb.main_kb)