import requests


BOT_TOKEN = '7207909276:AAEJOmg8pSHheVu24sucKppmQBbxQRc_IVw'


API_METHOD = 'setWebhook'
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/{API_METHOD}"

request_data = {
    'url': 'https://functions.yandexcloud.net/d4ekn1jt6cm57uldng78'
}

response_data = requests.post(API_URL, request_data)

print(response_data.json())
