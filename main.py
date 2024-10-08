import random
import uuid

from telebot import TeleBot
from telebot.types import Message

import pyjokes

from dotenv import dotenv_values

from help import help_text

CONFIG = dotenv_values('.env')
bot = TeleBot(CONFIG['TOKEN'])


@bot.message_handler(commands=['start'])
def command_start(message: Message):
    username = message.chat.username
    bot.send_message(chat_id=message.chat.id, text=f'Привет, {username}!')


@bot.message_handler(commands=['help'])
def command_help(message: Message):
    bot.reply_to(message=message, text=help_text)


@bot.message_handler(commands=['random'])
def command_random_number(message: Message):
    bot.reply_to(message=message, text=random.randrange(0, 1_000_000))


@bot.message_handler(commands=['joke'])
def command_random_joke(message: Message):
    joke = pyjokes.get_joke(language='ru')
    bot.reply_to(message=message, text=joke)


@bot.message_handler(commands=['uuid'])
def command_random_uuid(message: Message):
    bot.reply_to(message=message, text=uuid.uuid4())


bot.infinity_polling()
