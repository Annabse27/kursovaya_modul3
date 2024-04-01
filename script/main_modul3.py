#обращаемся к необходимым для реализации проекта библиотекам
import json
from datetime import datetime as dt


def data_info():
    """
    вызываем список из джейсон файла, извлекаем данные для проекта
    :return: list[]
    """
    with open('operation.json') as file:
        line_json = file.read()
    all_strings = json.loads(line_json)
    return all_strings


def organisation_operation(operation_data):
    """

    :param operation_data: list[] который мы получаем из ff data_info(), его мы и будем передавать.
    Назовем operationХХХ по аналогии с полученным для выполнения курсовой файла джейсон
    :return: list[] организованный по ключу "EXECUTED" список
    """
    list_operation = []
    for operation in operation_data:
        if operation.get('state') == "EXECUTED":
            list_operation.append(operation)
    return list_operation



def chronologie_operation(operation_data: list[dict]) -> list[dict]:
    """

    :param operation_data: list[] организованный по ключу "EXECUTED"
    :return: list[] представлен в хронологическом порядке, по дате
    """
    sorted_list = sorted(operation_data, key=lambda x: x['date'], reverse=True)
    return sorted_list


def forme_date(operation):
    """

    :param operation: list[] организованный по ключу "EXECUTED" и дате
    :return: str : дата в формате 'дд.ММ.ГГ'
    """
    date = operation['date']
    dt_time = dt.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return dt_time.strftime('%d.%m.%Y')


def cache_operation_from_info(operation):
    """

    :param operation: list[] организованный по ключу "EXECUTED" и дате
    :return: str : "данные по исходящей операции откуда перечислены ДС"

    Номер карты и номер счета замаскирован и не отображается целиком
    (для карты видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных пробелом;
    видны только последние 4 цифры номера счета).
    """
    operation_from = operation.get('from')

    if operation_from:
        part = operation_from.split(' ')
        numbers = part[-1]
        if len(numbers) == 16:
            masked_numbers = f"{numbers[:4]} {numbers[4:6]}** **** {numbers[-4:]}"
            return (" ".join(part[:-1]) + " " + masked_numbers)
        else:
            return (f"Счет **{numbers[-4:]}")


def cache_operation_to_info(operation):
    """

        :param operation: list[] организованный по ключу "EXECUTED" и дате
        :return: str : "данные по исходящей операции куда перечислены ДС"

        Номер карты и номер счета замаскирован и не отображается целиком
        (для карты видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных пробелом;
        видны только последние 4 цифры номера счета).
        """
    operation_to = operation.get('to')
    if operation_to:
        part_2 = operation_to.split(' ')
        numbers_2 = part_2[-1]
        if len(numbers_2) == 16:
            masked_numbers = f"{numbers_2[:4]} {numbers_2[4:6]}** **** {numbers_2[-4:]}"
            return (" ".join(part_2[:-1]) + " " + masked_numbers)
        else:
            return (f"Счет **{numbers_2[-4:]}")


#вывод на экран
data = data_info()
operation = organisation_operation(data)
#выводим последние пять операций по заданию
operation = chronologie_operation(operation)[:5]
for i in operation:
    print(f"{forme_date(i)} {i['description']}")
    print(f"{cache_operation_from_info(i)} {'-'}{'>'} {cache_operation_to_info(i)}")
    print(f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
    print()
