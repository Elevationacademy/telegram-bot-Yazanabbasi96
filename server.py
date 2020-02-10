from flask import Flask, Response, request
import requests
import functions
import commands_handler

app = Flask(__name__)


@app.route('/sanity')
def sanity(): return "Server is running"


TOKEN = '916747867:AAHDM_t5-RguFh5GtMzSmQySEJNogH-ayjg'


def send_domain():
    TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url=https://9a612240.ngrok.io/message'.format(
        TOKEN)
    requests.get(TELEGRAM_INIT_WEBHOOK_URL)


@app.route('/message', methods=["POST"])
def handle_message():
    req = request.get_json()
    chat_id = req['message']['chat']['id']
    message = req["message"]["text"]
    checker = commands_handler.command_parser(message)
    res = requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'"
                       .format(TOKEN, chat_id, checker))
    return Response("success")


send_domain()
if __name__ == '__main__':
    app.run(port=5002)
