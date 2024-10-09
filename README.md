# Telegram parser

This application is intended for parsing the specified Telegram channels. Telethon parses messages that are stored in a SQL database. In addition, a separate Telegram bot was created, which allows you to display the last 10 saved messages, displaying the text of the message, ID, first name, last name, nickname, phone number of the sender, as well as the date and time of receiving the message.

## Project Structure

```
telPars/
├── app/
│   ├── alembic/
│   │   ├── versions/
│   │   │   └── ...
│   │   ├── env.py
│   │   └── README
│   ├── database/
│   │   ├── add.py
│   │   ├── del.py
│   │   ├── get.py
│   │   ├── models.py
│   │   ├── print.py
│   │   └── README
│   ├── parser.py
│   └── tg_dot.py
├── docker/
│   └── ...
├── .env
├── docker-compose.yml
├── LICENCE
└── requirements.txt
```

## .env example

```
# -- Telethon
API_ID=id
API_HASH=hash

# -- Telegram
BT_TOKEN=token


# -- Chats
TELEGRAM_CHATS=chat_1,chat_2,chat_3

# -- PostgreSQL
DB_USER=username
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=database_name
```

## Парсинг в фоновому режимі 
Фоновий парсинг можна оформити за допомогою crontab. 

### 1. Перед тим, як додати код в автозапуск потрібно запустити його вручну ось так:
```
python3 /home/path/to/your/parser.py
```
### 2. Далі, відкрити crontab файл:
```
crontab -e
```
### 3. В кінці файлу додати це:
```
*/30 * * * * /usr/bin/python3 /home/path/to/your/parser.py >> /path/to/logfile.log 2>&1
```

Парсинг буде відбуватися кожні 30 хвилин.