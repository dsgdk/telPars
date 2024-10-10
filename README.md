# Telegram parser

This application is intended for parsing the specified Telegram channels. Telethon parses messages that are stored in a SQL database. In addition, a separate Telegram bot was created, which allows you to display the last 10 saved messages, displaying the text of the message, ID, first name, last name, nickname, phone number of the sender, as well as the date and time of receiving the message.

## Project Structure

```
telPars/
├── app/
│   ├── database/
│   │   ├── add.py
│   │   ├── del.py
│   │   ├── get.py
│   │   ├── models.py
│   │   └── print.py
│   ├── parser.py
│   └── tg_bot.py
├── .env
├── LICENCE
├── README
└── requirements.txt
```

## Використання

1. Клонуйте репозиторій 
```
git clone https://github.com/dsgdk/telPars.git
```
2. Відкрийте папку з проєктом
```
cd telPars
```
3. Створіть .env файл і заповніть його (приклад нижче)
```
nano .env
```
4. Запустіть parser.py, або додайте його в Crontab файл (інструкція нижче)
```
python3 parser.py
```
5. Запустіть tg_bot.py
```
python3 tg_bot.py
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

## Background Parsing Using Crontab 
### 1. First, you need to manually run the script to create the session file for Telegram authentication:
```
python3 /home/path/to/your/parser.py
```
### 2. Next, open the crontab file:
```
crontab -e
```
### 3. At the end of the file, add the following line to run the parser every 30 minutes and save logs:
```
*/30 * * * * /usr/bin/python3 /home/path/to/your/parser.py >> /path/to/logfile.log 2>&1
```

This command will run the parser every 30 minutes. The results (both output and errors) will be saved in the log file at /path/to/logfile.log. The 2>&1 part ensures that both standard output and errors are redirected to the same log file.
