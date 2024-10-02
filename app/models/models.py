from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TelegramMessage(Base):
    __tablename__ = 'telegram_messages'
    
    id           = Column(Integer, nullable=False, primary_key=True )
    message_text = Column(String,  nullable=False, primary_key=False)
    message_date = Column(String,  nullable=False, primary_key=False)
    sender_id    = Column(Integer, nullable=False, primary_key=False)
    first_name   = Column(String,  nullable=False, primary_key=False)
    last_name    = Column(String,  nullable=False, primary_key=False)
    username     = Column(String,  nullable=False, primary_key=False)
    phone_number = Column(String,  nullable=False, primary_key=False)

    def __repr__(self):
        return f"<TelegramMessage(id={self.id}, message_text='{self.message_text}', message_date='{self.message_date}', sender_id={self.sender_id}, first_name='{self.first_name}', last_name='{self.last_name}', username='{self.username}', phone_number='{self.phone_number}')>"

