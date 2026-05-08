from telegram import Bot

TOKEN = "8382298610:AAEC_wCKFIUZGHSvqBfHMZY4HDUa-_hmPj4"

CHAT_ID = "7366145742"

bot = Bot(token=TOKEN)

async def send_alert(message):

    try:

        await bot.send_message(

            chat_id=CHAT_ID,

            text=message
        )

        print(
            "TELEGRAM ALERT SENT"
        )

    except Exception as e:

        print(
            "TELEGRAM ERROR:",
            e
        )