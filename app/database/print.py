from sqlalchemy.orm import sessionmaker
from .models import TelegramMessage, get_engine

engine  = get_engine()
Session = sessionmaker(bind=engine)
session = Session()

def get_messages():
    last_10_messages = session.query(TelegramMessage).order_by(TelegramMessage.id.desc()).limit(10).all()
    last_10_messages.sort(key=lambda message: message.id)
    
    # -- print 
    # for message in last_10_messages:
    #     print(f"    id:           {message.id}")
    #     print(f"    message_text: {message.message_text}")
    #     print(f"    message_date: {message.message_date}")
    #     print(f"    sender_id:    {message.sender_id}")
    #     print(f"    first_name:   {message.first_name}")
    #     print(f"    last_name:    {message.last_name}")
    #     print(f"    username:     {message.username}")
    #     print(f"    phone_number: {message.phone_number}")
    #     print("-" * 65)

    # Форматування повідомлення
    message_text = ""
    for message in last_10_messages:
        message_text += (
            f"id: {message.id}\n"
            f"message_text: {message.message_text}\n"
            f"message_date: {message.message_date}\n"
            f"sender_id: {message.sender_id}\n"
            f"first_name: {message.first_name}\n"
            f"last_name: {message.last_name}\n"
            f"username: {message.username}\n"
            f"phone_number: {message.phone_number}\n"
            f"{'-' * 65}\n"
        )

    session.close()  # Закрийте сесію
    return message_text