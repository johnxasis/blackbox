# telegram_webhook.py
from flask import Flask, request
import requests

app = Flask(__name__)
BOT_TOKEN = '7647588745:AAEaiVLS_9x03LR1OP_sPVtFxQBQhEgb6LY'
OWNER_ID = 2106538137

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def telegram_webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        if text == "/believe":
            reply = "The prophecy has been acknowledged."
            requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", json={"chat_id": chat_id, "text": reply})
    return "OK"

if __name__ == '__main__':
    app.run(debug=True)