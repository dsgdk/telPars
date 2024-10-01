import os
from dotenv   import load_dotenv
from telethon import TelegramClient, sync, events
load_dotenv()

# -- Config
api_id   = os.getenv('API_ID')          # -- Api id
api_hash = os.getenv('API_HASH')        # -- Api hash
client   = TelegramClient('parser', api_id, api_hash)

# -- Channels that we will monitor
channels      = os.getenv('TELEGRAM_CHATS')
channels_list = channels.split(",")

# -- Debug
debug = 1 # -- if 1: on, else: off

@client.on(events.NewMessage(chats=channels_list))
async def handler(event):
    
    message_text = event.message.message    # -- Message
    message_date = event.message.date       # -- Date
    sender_id    = event.sender_id          # -- Sender id
    
    sender       = await event.get_sender()

    first_name   = sender.first_name or ''  # -- First name
    last_name    = sender.last_name or ''   # -- Last name
    username     = sender.username or ''    # -- Username
    phone_number = sender.phone or ''       # -- Phone number

    if debug == 1:                          # -- Debug
        print(f"Text:               {message_text}")
        print(f"Date and time:      {message_date}")
        print(f"Sender id:          {sender_id}"   )
        print(f"First name:         {first_name}"  )
        print(f"Last name:          {last_name}"   )
        print(f"Username:           {username}"    )
        print(f"Phone number:       {phone_number}")

client.start()
client.run_until_disconnected()
