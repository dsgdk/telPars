from models import TelegramMessage, get_engine, get_session

def delete_last_message():
    
    engine = get_engine()
    session = get_session(engine)
    
    # Отримуємо останній запис у таблиці за його id
    last_message = session.query(TelegramMessage).order_by(TelegramMessage.id.desc()).first()
    
    # Якщо запис існує, видаляємо його
    if last_message:
        session.delete(last_message)
        session.commit()
        print(f"Record with id={last_message.id} deleted successfully")
    else:
        print("There are no entries to delete")

    # Закриваємо сесію
    session.close()

# Виклик функції
delete_last_message()
