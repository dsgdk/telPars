# Telegram parser

This application is intended for parsing the specified Telegram channels. Telethon parses messages that are stored in a SQL database. In addition, a separate Telegram bot was created, which allows you to display the last 10 saved messages, displaying the text of the message, ID, first name, last name, nickname, phone number of the sender, as well as the date and time of receiving the message.

# Project Structure

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
├── docker-compose.yml
├── LICENCE
└── requirements.txt
```