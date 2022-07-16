import dotenv
import os
import requests

dotenv.load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN', '0')


def test_bot_valid():
    if BOT_TOKEN == '0':
        raise Exception('Invalid token')

    res = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getMe")
    assert res.ok == True
