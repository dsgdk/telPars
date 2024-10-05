from models import TelegramMessage, get_engine, get_session

def delete_last_message():
    # Отримуємо engine та сесію
    engine = get_engine()
    session = get_session(engine)
    
    # Отримуємо останній запис у таблиці за його id
    last_message = session.query(TelegramMessage).order_by(TelegramMessage.id.desc()).first()
    
    # Якщо запис існує, видаляємо його
    if last_message:
        session.delete(last_message)
        session.commit()
        print(f"Запис з id={last_message.id} успішно видалено")
    else:
        print("Немає записів для видалення")

    # Закриваємо сесію
    session.close()

# Виклик функції
delete_last_message()
