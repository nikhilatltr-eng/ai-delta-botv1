# Railway Setup

Set these variables in the Railway service:

```text
DELTA_API_KEY
DELTA_API_SECRET
BASE_URL
WS_URL
SYMBOL
TELEGRAM_BOT_TOKEN
TELEGRAM_CHAT_ID
TELEGRAM_ENABLED=true
```

Use this start command for the trading alert worker:

```text
python main.py
```

To test only Telegram delivery from Railway, temporarily set the start
command to:

```text
python tools/test_telegram_alert.py
```

After the test alert arrives, switch the start command back to `python main.py`.
