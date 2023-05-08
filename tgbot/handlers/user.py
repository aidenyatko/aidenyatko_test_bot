from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from tgbot.lexicon.lexicon_ua import LEXICON_UA

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message):
    await message.reply(text=LEXICON_UA['/start'])


@user_router.message(Command(commands='help'))
async def user_help(message: Message):
    await message.reply(text=LEXICON_UA['/help'])


@user_router.message()
async def bot_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON_UA['no_echo'])
