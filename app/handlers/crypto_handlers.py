from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from html import escape

from app.backend.Euclid import find_values, do_PAE, do_OAE
from app.backend.Diophantine import solve_diophantine_equation
import app.keyboards as kb

router = Router()

class OAE(StatesGroup):
    numbers = State()

class PAE(StatesGroup):
    numbers = State()

class Diophantine(StatesGroup):
    coefficients = State()

###############
### OAE alg ###
###############
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
    await message.answer(f"<pre>{safe}</pre>", parse_mode="HTML", reply_markup=kb.main_kb)

###############
### PAE alg ###
###############

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

    safe = escape(text)
    await state.clear()
    await message.answer(f"<pre>{safe}</pre>", parse_mode="HTML", reply_markup=kb.main_kb)

#######################
### Diophantine alg ###
#######################

@router.message(F.text == "Диофантовое уравнение")
async def message_Diophantine(message: types.Message, state: FSMContext):
    await message.answer("Введите числа разделённые пробелами соответствующие коэффициентам\n``` ax + by = c```\nСоответствующие коэффициентам a, b и c соответственно.\n\nНапример: `439 118 3` для уравнения 439x + 118y = 3", parse_mode="Markdown")
    await state.set_state(Diophantine.coefficients)
    
@router.message(Diophantine.coefficients)
async def make_Diophantine(message: types.Message, state: FSMContext):
    # ожидаем три числа: a, b и c
    try:
        a, b, c = map(int, message.text.split())
    except ValueError:
        await message.answer("Неверный ввод. Введите три целых числа через пробел, например: `439 118 3`", parse_mode="Markdown")
        return
    result = solve_diophantine_equation(a, b, c)
    text = f"{a}x + {b}y = {c}\n\n"
    try:
        if result["result"] == "Нет решений":
            message.answer(result["answer"])
            return
    except KeyError:
        pass
    text += f"({a}, {b}) = {result["gcd"]}\n"
    text += f"{c} ⫶ {result["gcd"]} => ∃ решение\n\n"
    text += do_PAE(result["table"])
    text += f"\n\nНОД({a}, {b}) = {result["gcd"]} = {a} * {result["k1"]} + {b} * {result["k2"]}\n"
    x0, y0 = result["part_solution"]
    if result["multiplicated"]:
        text += f"{a} * {result["k1"]} + {b} * {result["k2"]} = {result["gcd"]} | {result["gcd"]}\n"
        text += f"{a // result["gcd"]} * {result["k1"]} + {b // result["gcd"]} * {result["k2"]} = {result["gcd"]} | * {c} : {result["gcd"]}\n"
    text += f"{a // result["gcd"]} * {x0} + {b // result["gcd"]} * {y0} = {c // result["gcd"]}\n\n"
    text += f"Частное решение:\nX̄ = {x0}\nɏ = {y0}\n\n"
    sol = result["common_solution"]
    text += f"Общее решение:\nx = {sol["x"][0]} + {sol["x"][1]}t\ny = {sol["y"][0]} - {sol["y"][1]}t\nt ∈ Z\n"

    safe = escape(text)
    await state.clear()
    await message.answer(f"<pre>{safe}</pre>", parse_mode="HTML", reply_markup=kb.main_kb)
