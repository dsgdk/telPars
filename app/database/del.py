from models import TelegramMessage, get_engine, get_session
from sqlalchemy import text

def delete_all_messages():
    engine = get_engine()
    session = get_session(engine)
    
    try:
        session.query(TelegramMessage).delete()
        session.commit()

        sequence_name_query = "SELECT pg_get_serial_sequence('telegram_messages', 'id')"
        result = session.execute(text(sequence_name_query)).fetchone()

        if result:
            sequence_name = result[0]
            session.execute(text(f"ALTER SEQUENCE {sequence_name} RESTART WITH 1"))
            session.commit()

        print("All records deleted successfully, ID sequence reset")
    except Exception as e:
        session.rollback()
        print(f"Error occurred during deletion: {e}")
    finally:
        session.close()

delete_all_messages()