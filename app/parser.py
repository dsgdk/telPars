import os
from dotenv   import load_dotenv
from telethon import TelegramClient, sync, events

from database.add import add_new_telegram_message

load_dotenv()

# -- Config
api_id   = os.getenv('API_ID')   # -- Api id
api_hash = os.getenv('API_HASH') # -- Api hash
client   = TelegramClient('parser', api_id, api_hash)

# -- Channels that we will monitor
channels      = os.getenv('TELEGRAM_CHATS')
channels_list = channels.split(",")

# -- Debug
debug = 0 # -- if 1: on, else: off

@client.on(events.NewMessage(chats=channels_list))
async def handler(event):
    
    if debug == 0:
        sender = await event.get_sender()
        add_new_telegram_message(
            message_text    =event.message.message,
            message_date    =event.message.date,
            sender_id       =event.sender_id,
            first_name      =sender.first_name or '',
            last_name       =sender.last_name  or '',
            username        =sender.username   or '',
            phone_number    =sender.phone      or ''
        )

    if debug == 1: # -- Debug
        sender       = await event.get_sender()
        print(f"Text:          {event.message.message  }"  ) # -- Message
        print(f"Date and time: {event.message.date     }"  ) # -- Date
        print(f"Sender id:     {event.sender_id        }"  ) # -- Sender id
        print(f"First name:    {sender.first_name or ''}"  ) # -- First name
        print(f"Last name:     {sender.last_name  or ''}"  ) # -- Last name
        print(f"Username:      {sender.username   or ''}"  ) # -- Username
        print(f"Phone number:  {sender.phone      or ''}"  ) # -- Phone number
        print("-" * 65)

client.start()
client.run_until_disconnected()
