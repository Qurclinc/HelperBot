from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from html import escape

from app.logic import find_values, do_PAE, do_OAE
import app.keyboards as kb

router = Router()

class OAE(StatesGroup):
    numbers = State()

class PAE(StatesGroup):
    numbers = State()

@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer("aboba", reply_markup=kb.main_kb)

@router.message(F.text == "ОАЕ")
async def message_OAE(message: types.Message, state: FSMContext):
    await message.answer("Введите числа разделённые пробелами")
    await state.set_state(OAE.numbers)

@router.message(OAE.numbers)
async def make_OAE(message: types.Message, state: FSMContext):
    try:
        numbers = list(map(int, message.text.split()))
    except ValueError:
        await message.answer("Неверный формат. Введите целые числа, разделённые пробелами.")
        return

    text = do_OAE(numbers)
    from html import escape
    safe = escape(text)

    await state.clear()
    await message.answer(f"<pre>{safe}</pre>", parse_mode="HTML")


@router.message(F.text == "РАЕ")
async def message_PAE(message: types.Message, state: FSMContext):
    await message.answer("Введите числа разделённые пробелами")
    await state.set_state(PAE.numbers)
    
@router.message(PAE.numbers)
async def make_PAE(message: types.Message, state: FSMContext):
    # ожидаем два числа: a b
    try:
        a, b = map(int, message.text.split())
    except ValueError:
        await message.answer("Неверный ввод. Введите два целых числа через пробел, например: `119 34`", parse_mode="Markdown")
        return

    values = find_values(a, b)
    text = do_PAE(values)

    # Экранируем для HTML и отправляем в <pre> чтобы сохранить моноширинность и выравнивание
    safe = escape(text)
    await state.clear()
    await message.answer(f"<pre>{safe}</pre>", parse_mode="HTML")
