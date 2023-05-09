from aiogram import Router
from aiogram.filters import CommandStart, Command, Text
from aiogram.types import Message
from tgbot.keyboards.keyboards import game_kb, yes_no_kb
from tgbot.lexicon.lexicon_ua import LEXICON_UA
from tgbot.services.services import get_bot_choice, get_winner

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message):
    await message.reply(text=LEXICON_UA['/start'], reply_markup=yes_no_kb)


@user_router.message(Command(commands=['help']))
async def user_help(message: Message):
    await message.reply(text=LEXICON_UA['/help'])


@user_router.message(Text(text=LEXICON_UA['no_button']))
async def user_no_answer(message: Message):
    await message.reply(text=LEXICON_UA['no'])


@user_router.message(Text(text=LEXICON_UA['yes_button']))
async def user_yes_answer(message: Message):
    await message.reply(text=LEXICON_UA['yes'], reply_markup=game_kb)


@user_router.message(Text(text=[LEXICON_UA['rock'],
                           LEXICON_UA['paper'],
                           LEXICON_UA['scissors']]))
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_UA["bot_choice"]} '
                              f'- {LEXICON_UA[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON_UA[winner], reply_markup=yes_no_kb)