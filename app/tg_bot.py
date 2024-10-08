from dotenv         import load_dotenv
from database.print import get_messages

import telebot
import os

load_dotenv()
token = os.getenv('BT_TOKEN')

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Hello! Type "/last_messages" to get the last 10 messages.')

@bot.message_handler(commands=['last_messages'])
def send_last_messages(message):
    last_messages = get_messages()                    # -- Отримуємо останні повідомлення
    bot.send_message(message.chat.id, last_messages)  # -- Надсилаємо їх у Telegram

bot.polling(none_stop=True)
