from sqlalchemy.orm import sessionmaker
from .models import TelegramMessage, get_engine

# -- Функція для додавання нового повідомлення в базу даних
def add_new_telegram_message(message_text, message_date, sender_id, first_name, last_name, username, phone_number):
    # -- Створюємо сесію
    engine  = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # -- Створюємо нове повідомлення
        new_message = TelegramMessage (
            message_text    =message_text,
            message_date    =message_date,
            sender_id       =sender_id,
            first_name      =first_name,
            last_name       =last_name,
            username        =username,
            phone_number    =phone_number
        )

        session.add(new_message)

        session.commit()
        print("Повідомлення успішно додано в базу даних")

    except Exception as e:
        # -- If error - rollback
        session.rollback()
        print(f"Помилка під час додавання повідомлення: {e}")

    finally:
        # -- Close session
        session.close()
