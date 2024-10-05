from sqlalchemy.orm import sessionmaker
from models import TelegramMessage, get_engine

# Функція для додавання нового повідомлення в базу даних
def add_new_telegram_message(message_text, message_date, sender_id, first_name, last_name, username, phone_number):
    # Створюємо сесію
    engine  = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Створюємо нове повідомлення
        new_message = TelegramMessage (

            message_text    =message_text,
            message_date    =message_date,
            sender_id       =sender_id,
            first_name      =first_name,
            last_name       =last_name,
            username        =username,
            phone_number    =phone_number
        
        )

        # Додаємо повідомлення до сесії
        session.add(new_message)

        # Фіксуємо зміни (зберігаємо в базу даних)
        session.commit()
        print("Повідомлення успішно додано в базу даних")

    except Exception as e:
        # Якщо сталася помилка, робимо rollback
        session.rollback()
        print(f"Помилка під час додавання повідомлення: {e}")

    finally:
        # Закриваємо сесію
        session.close()

# Приклад виклику функції
add_new_telegram_message(
    message_text="Це тестове повідомлення",
    message_date="15",
    sender_id=12345,
    first_name="John",
    last_name="Doe",
    username="johndoe",
    phone_number="+123456789"
)
