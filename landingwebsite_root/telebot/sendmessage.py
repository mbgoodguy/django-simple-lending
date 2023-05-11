import requests
from .models import TeleSettings


def sendtelegram(tg_name, tg_phone):
    settings = TeleSettings.objects.get(pk=1)
    token = str(settings.tg_token)
    chat_id = str(settings.tg_chat)
    text = str(settings.tg_message)
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'

    part1 = text[0:text.find('{')]
    part2 = text[text.find('}')+1:text.rfind('{')]
    part3 = text[text.rfind('}'):-1]

    text_slice = part1 + tg_name + part2 + tg_phone + part3

    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': text_slice,
    })
