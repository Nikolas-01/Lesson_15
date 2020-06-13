import requests
import time
import pprint
TOKEN = '1168070893:AAF0Woq78-CKmpbR2s9ZynPU21fUMikbG6U'
BOT_URL = f'https://api.telegram.org/bot{TOKEN}'
proxies = {
    'http': 'http://51.158.98.121:8811',
    'https': 'http://51.158.98.121:8811',
}
url = f'{BOT_URL}/getMe'
result = requests.get(url, proxies = proxies)
#print(result.status_code)
url = f'{BOT_URL}/getUpdates'
while True:
    time.sleep(3)
    result = requests.get(url, proxies=proxies)
    pprint.pprint(result.json())
    messages = result.json()['result']
    for message in messages:
        chat_id = message['message']['chat']['id']
        url_send = f'{BOT_URL}/sendMessage'
        params = {
                'chat_id': chat_id,
                'text': 'Добрый день!'
                  }
        answer = requests.post(url_send, params = params, proxies = proxies)