import requests



token = '5755566044:AAE0-yfTrhqMlVnbUGAfVyyy2ixuG7SIEuM'
chat_id = '-938549786'
text = "Дивно святкувати День Конституції в країні, президент якої, почав порушувати з першого дня своєї коденції"


def setTelegramm():

    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'
    # method = api + token + '/sendMessage?chat_id=' + chat_id + '&text=' + text

    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': text
    })

setTelegramm()