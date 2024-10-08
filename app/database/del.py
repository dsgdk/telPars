from models import TelegramMessage, get_engine, get_session

def delete_all_messages():
    # Підключення до бази даних
    engine = get_engine()
    session = get_session(engine)
    
    try:
        # Видаляємо всі записи з таблиці
        session.query(TelegramMessage).delete()
        session.commit()
        print("All records deleted successfully")
    except Exception as e:
        session.rollback()
        print(f"Error occurred during deletion: {e}")
    finally:
        # Закриваємо сесію
        session.close()

# Виклик функції
delete_all_messages()
