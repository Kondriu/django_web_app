import requests
from .models import TeleSettings


def setTelegramm(tg_name, tg_phone):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat_id)
        text = str(settings.tg_message)

        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'

        a = text.find('{')  # первое c начала нахождение в корпусе текста символа '{'
        b = text.find('}')  # первое c начала нахождение в корпусе текста символа '}'
        c = text.rfind('{')  # первое c конца нахождение в корпусе текста символа '{'
        d = text.rfind('}')  # первое c конца нахождение в корпусе текста символа '}'

        if a and b and c and d:
            part1 = text[0: a]
            part2 = text[b + 1: c]
            part3 = text[d: -1]
            # text_all = part1 + tg_name + part2 + tg_phone + part3
            text_all = f'{part1}{tg_name}{part2}{tg_phone}{part3}'
        else:
            text_all = text

        try:
            req = requests.post(method, data={
                'chat_id': chat_id,
                'text': text_all
            })

        except:
            pass
        finally:
            if req.status_code != 200:
                print("Ошибка отпарвки")
            elif req.status_code == 500:
                print('ошибко 500')
            else:
                print('все ок, сообщение отправлено')

    else:
        pass
