import logging
import asyncio
import json
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


import app.algebra as alg
import app.geometry as geo
import app.physics as phy
import app.chemistry as che
import app.informatics as inf


from app.handlers import router


bot = Bot(token='7937156923:AAGz7XBoiUnryy9-yVwsmoWrt0NsKD7iHFc')
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


