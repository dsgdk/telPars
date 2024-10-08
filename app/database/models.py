import os
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from sqlalchemy import Column, Integer, BigInteger, String, Numeric, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
load_dotenv()

class TelegramMessage(Base):
    __tablename__ = 'telegram_messages'
    
    id           = Column(Integer, nullable=False, primary_key=True )
    message_text = Column(String,  nullable=False)
    message_date = Column(String,  nullable=False)
    sender_id    = Column(Numeric, nullable=False)
    first_name   = Column(String,  nullable=False)
    last_name    = Column(String,  nullable=False)
    username     = Column(String,  nullable=False)
    phone_number = Column(String,  nullable=False)
    message_id   = Column(Numeric, nullable=False, unique=True)

    def __repr__(self):
        return f"<TelegramMessage(id={self.id}, message_text='{self.message_text}', message_date='{self.message_date}', " \
            f"sender_id={self.sender_id}, first_name='{self.first_name}', last_name='{self.last_name}', " \
            f"username='{self.username}', phone_number='{self.phone_number}', message_id={self.message_id})>"

# -- Creating an engine for PostgreSQL
def get_engine():
    user     = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host     = os.getenv('DB_HOST')
    port     = os.getenv('DB_PORT')
    dbname   = os.getenv('DB_NAME')

    if None in [user, password, host, port, dbname]:
        raise ValueError(f"One or more environment variables are missing: user={user}, password={password}, host={host}, port={port}, dbname={dbname}")

    connection_string = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'
    return create_engine(connection_string)

def create_tables(engine):
    Base.metadata.create_all(engine)

def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()
