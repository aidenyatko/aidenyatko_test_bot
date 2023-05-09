from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from tgbot.lexicon.lexicon_ua import LEXICON_UA

button_yes: KeyboardButton = KeyboardButton(text=LEXICON_UA['yes_button'])
button_no: KeyboardButton = KeyboardButton(text=LEXICON_UA['no_button'])

yes_no_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

yes_no_kb_builder.row(button_yes, button_no, width=2)

yes_no_kb = yes_no_kb_builder.as_markup(one_time_keyboard=True, resize_keyboard=True)

button_rock: KeyboardButton = KeyboardButton(text=LEXICON_UA['rock'])
button_paper: KeyboardButton = KeyboardButton(text=LEXICON_UA['paper'])
button_scissors: KeyboardButton = KeyboardButton(text=LEXICON_UA['scissors'])

game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_rock], [button_paper], [button_scissors]],
                                                   resize_keyboard=True)
