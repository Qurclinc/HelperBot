from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="ОАЕ"), KeyboardButton(text="РАЕ")],
    [KeyboardButton(text="Диофантовое уравнение")]
], resize_keyboard=True)