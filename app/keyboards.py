from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="ОАЕ"), KeyboardButton(text="РАЕ")],
    [KeyboardButton(text="Диофантовое уравнение"), KeyboardButton(text="Мультипликативное обратное")]
], resize_keyboard=True)