import asyncio
from config import bot, dp
from app.handlers.crypto_handlers import router as crypto_router

async def main():
    dp.include_router(crypto_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())