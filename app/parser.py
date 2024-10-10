import os
import asyncio

from dotenv       import load_dotenv
from telethon     import TelegramClient
from database.add import add_new_telegram_message
from database.get import get_last_message_id_from_db

load_dotenv()

# -- Config
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
client = TelegramClient('parser', api_id, api_hash)

# -- Channels that we will monitor
channels = os.getenv('TELEGRAM_CHATS')
channels_list = [channel.strip() for channel in channels.split(",")]

async def check_new_messages(channel):
    last_saved_id = get_last_message_id_from_db()  # -- Отримуємо останній збережений ID з БД
    new_messages = []                                            # -- Список для збереження нових повідомлень
    async for message in client.iter_messages(channel):          # -- Отримання всіх повідомлень з каналу
        if last_saved_id is None or message.id > last_saved_id:  # -- Перевірка на None та ID повідомлення
            sender = await message.get_sender()
            if sender:
                new_messages.append({                       # -- Додаємо нове повідомлення до списку
                    'message_text': message.text or '',     # -- Текст
                    'message_date': message.date or '',     # -- Дата
                    'sender_id': sender.id,                 # -- ID відправника
                    'first_name': sender.first_name or '',  # -- Ім'я
                    'last_name': sender.last_name or '',    # -- Прізвище
                    'username': sender.username or '',      # -- Ім'я користувача
                    'phone_number': sender.phone or '',     # -- Номер телефону
                    'message_id': message.id                # -- ID повідомлення
                })
    for msg in sorted(new_messages, key=lambda m: m['message_id']):
        add_new_telegram_message(**msg)

async def main():
    await client.start()
    for channel in channels_list:
        await check_new_messages(channel)

if __name__ == "__main__":
    asyncio.run(main())
