from sqlalchemy.orm import sessionmaker
from .models import TelegramMessage, get_engine

# -- Функція для отримання останнього message_id з бази даних
def get_last_message_id_from_db():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        last_message = session.query(TelegramMessage).order_by(TelegramMessage.message_id.desc()).first()
        if last_message:
            # print(f"Останній ID: {last_message.message_id}")
            return last_message.message_id
        else:
            # print("Повідомлень немає.")
            return None
    except Exception as e:
        # print(f"Помилка під час отримання останнього message_id: {e}")
        return None
    finally:
        session.close()

get_last_message_id_from_db()
