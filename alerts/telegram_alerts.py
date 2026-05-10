import requests

from config.settings import (
    TELEGRAM_BOT_TOKEN,
    TELEGRAM_CHAT_ID,
    TELEGRAM_ENABLED
)


def validate_telegram_config():

    if not TELEGRAM_ENABLED:
        print("TELEGRAM DISABLED")
        return False

    missing = []

    if not TELEGRAM_BOT_TOKEN:
        missing.append("TELEGRAM_BOT_TOKEN")

    if not TELEGRAM_CHAT_ID:
        missing.append("TELEGRAM_CHAT_ID")

    if missing:
        print(
            "TELEGRAM NOT CONFIGURED: set "
            + ", ".join(missing)
            + " in Railway variables"
        )
        return False

    return True


def _redact_token(text):

    if not TELEGRAM_BOT_TOKEN:
        return text

    return text.replace(
        TELEGRAM_BOT_TOKEN,
        "<redacted>"
    )


def send_alert(message):

    if not validate_telegram_config():
        return False

    try:

        response = requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
            json={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": message,
                "disable_web_page_preview": True
            },
            timeout=10
        )

        if not response.ok:
            try:
                error = response.json().get(
                    "description",
                    response.text
                )
            except ValueError:
                error = response.text

            print(
                f"TELEGRAM ERROR ({response.status_code}): {error}"
            )
            return False

        print(
            "TELEGRAM ALERT SENT"
        )

        return True

    except requests.RequestException as e:

        print(
            "TELEGRAM REQUEST ERROR:",
            _redact_token(str(e))
        )

        return False
