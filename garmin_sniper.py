
import os
import json
import urllib.request
import urllib.parse

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

SEARCH_TERMS = [
    "Garmin LVS32",
    "Garmin LVS34",
    "Garmin GLS 10",
    "Garmin ECHOMAP",
    "Garmin LiveScope",
]

MAX_PRICE = 500

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = urllib.parse.urlencode({
        "chat_id": CHAT_ID,
        "text": message
    }).encode()

    request = urllib.request.Request(url, data=data)

    with urllib.request.urlopen(request, timeout=20) as response:
        return json.loads(response.read())

if __name__ == "__main__":
    message = (
        "🎣 GARMIN DEAL SNIPER IS VERBONDEN!\n\n"
        "Zoektermen:\n"
        + "\n".join("• " + term for term in SEARCH_TERMS)
        + "\n\nMaximale vraagprijs: €500\n"
        + "\nVolgende stap: advertentiebronnen aansluiten."
    )

    send_telegram(message)
    print("Telegram testbericht verzonden.")
