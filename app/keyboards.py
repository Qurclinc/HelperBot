from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="ОАЕ"), KeyboardButton(text="РАЕ")]
], resize_keyboard=True)