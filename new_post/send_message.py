import requests

def send(token, chat_id, text):
    requests.get(
        "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
        .format(token, chat_id, text))