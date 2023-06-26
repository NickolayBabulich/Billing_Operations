import json
from datetime import date, datetime


def load_data(filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data


def date_format(date_log):
    date_log = ' '.join(date_log.split('T'))
    formated_date = datetime.strptime(str(date_log), '%Y-%m-%d %H:%M:%S.%f').strftime('%d.%m.%Y')
    return formated_date


def if_executed(data):
    last_operations = []
    for i in data[-6:]:
        if i.get('state') == 'EXECUTED':
            last_operations.append(i)
    return last_operations


def sender_format(account):
    account = ''.join([i for i in account.split() if i.isdigit()])
    res = ''
    format_str = account[:6] + '*' * (len(account) - 10) + account[-4:]
    for i in range(0, len(format_str), 4):
        res += format_str[i:i + 4] + ' '
    if res == '':
        return f'Счет отправителя неизвестен'
    return res


def receiver_format(account):
    return f"{' '.join([i for i in account.split() if i.isalpha()])} **{account[-4:]}"
