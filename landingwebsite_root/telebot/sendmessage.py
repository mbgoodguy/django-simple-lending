import requests

token = '6082705720:AAGk9a7b11dge-IN0VLhtZ3irkmoakwnb6s'
chat_id = '-882262196'
text = 'Test2'


def sendtelegram():
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'
    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': text,
    })


sendtelegram()
