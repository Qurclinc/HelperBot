import os
from aiogram import Dispatcher, Bot
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher()