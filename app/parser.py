import os
from dotenv import load_dotenv
from telethon import TelegramClient, events
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

@client.on(events.NewMessage(chats=channels_list))
async def new_message_handler(event):
    message = event.message
    sender = await message.get_sender()
    last_id = get_last_message_id_from_db()
    print("last id:", last_id)

    if sender:
        print("message id: ", message.id)
        add_new_telegram_message(
            message_text=message.text or '',
            message_date=message.date or '',
            sender_id=sender.id,
            first_name=sender.first_name or '',
            last_name=sender.last_name or '',
            username=sender.username or '',
            phone_number=sender.phone or '',
            message_id=message.id
        )

if __name__ == "__main__":
    client.start()
    print("Listening for new messages...")
    client.run_until_disconnected()
