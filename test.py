from flask import Flask, request
import requests

app = Flask(__name__)


def send_message(chat_id, text):
    method = "sendMessage"
    token = "1872273294:AAFE2PGjCEIo28bh6UowoELtmJ7Qal3VxG0"
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)


@app.route("/", methods=["POST"])
def receive_update():
    chat_id = request.json["message"]["chat"]["id"]
    send_message(chat_id, "Hello!")
    return "ok"


if __name__ == "__main__":
    app.run()
