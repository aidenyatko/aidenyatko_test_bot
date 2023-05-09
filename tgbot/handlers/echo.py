from aiogram import Router
from aiogram.types import Message
from tgbot.lexicon.lexicon_ua import LEXICON_UA

echo_router: Router = Router()


# Хэндлер для сообщений, которые не попали в другие хэндлеры
@echo_router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON_UA['other_answer'])
