# Telegram parser

This application is intended for parsing the specified Telegram channels. Telethon parses messages that are stored in a SQL database. In addition, a separate Telegram bot was created, which allows you to display the last 10 saved messages, displaying the text of the message, ID, first name, last name, nickname, phone number of the sender, as well as the date and time of receiving the message.

telegram_monitoring/
├── app/
│   ├── bot/
│   │   ├── __init__.py
│   │   ├── bot.py
│   │   └── handlers.py
│   ├── parser/
│   │   ├── __init__.py
│   │   └── parser.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── models.py
│   ├── config.py
│   └── main.py
├── migrations/
│   └── ... (файли міграцій)
├── docker/
│   ├── app/
│   │   └── Dockerfile
│   └── bot/
│       └── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .env
