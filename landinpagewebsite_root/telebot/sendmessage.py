import requests
from .models import TeleSettings


def setTelegramm(tg_name, tg_phone):
    settings = TeleSettings.objects.get(pk=1)
    token = str(settings.tg_token)
    chat_id = str(settings.tg_chat_id)
    text = str(settings.tg_message)

    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'

    a = text.find('{')
    b = text.find('}')
    c = text.rfind('{')
    d = text.rfind('}')

    part1 = text[0: a]
    part2 = text[b + 1: c]
    part3 = text[d: -1]

    # text_all = part1 + tg_name + part2 + tg_phone + part3
    text_all = f'{part1}{tg_name}{part2}{tg_phone}{part3}'

    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': text_all
    })

