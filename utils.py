import json
from datetime import datetime


def load_data(filename):
    """
    функция получает данные из json
    :param filename: имя json файла
    :return: возвращаем массив данных
    """
    with open(filename, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data


def date_format(date_log):
    """
    функция форматирует дату до вида согласно ТЗ
    :param date_log: преобразуем строку для форматирования даты
    :return: возвращаем сформатированную дату
    """
    date_log = ' '.join(date_log.split('T'))
    formatted_date = datetime.strptime(date_log, '%Y-%m-%d %H:%M:%S.%f').strftime('%d.%m.%Y')
    return formatted_date


def if_executed(data, operations_amount):
    """
    функция выводит лог успешных операций
    :param data: данные операций
    :param operations_amount: параметр задает необходимое количество операций для отображения
    :return: возвращает список только успешных и отсортированных операций от самой последней в заданном количестве
    """
    executed_operations = [operation for operation in data if operation.get('state') == 'EXECUTED']
    sorted_last_operations = sorted(executed_operations, key=lambda x: x.get('date'), reverse=True)
    return sorted_last_operations[:operations_amount]


def sender_format(sender_account):
    """
    функция форматирует отображение счета отправителя согласно ТЗ
    :param sender_account: получаем данные по счету отправителя
    :return: возвращаем отформатированную строку
    """
    account = ''.join([i for i in sender_account.split() if i.isdigit()])
    card_name = ' '.join([i for i in sender_account.split() if i.isalpha()])
    formatted_sender_account = ''
    format_str = account[:6] + '*' * (len(account) - 10) + account[-4:]
    for i in range(0, len(format_str), 4):
        formatted_sender_account += format_str[i:i + 4] + ' '
    if formatted_sender_account == '':
        return f'Счет отправителя неизвестен'
    return f'{card_name} {formatted_sender_account.strip()}'


def receiver_format(receiver_account):
    """
    функция форматирует отображение счета получателя согласно ТЗ
    :param receiver_account: олучаем данные по счету получателя
    :return: возвращаем отформатированную строку
    """
    return f"{' '.join([i for i in receiver_account.split() if i.isalpha()])} **{receiver_account[-4:]}"
