from script.main_modul3 import data_info, cache_operation_to_info, cache_operation_from_info, forme_date


def test_data_info():
    """
    :return: проверяем ff вывод отформатированной информации на экран из полученного потока операций
    """
    assert data_info()[1] == {'date': '2019-07-03T18:35:29.512364',
                              'description': 'Перевод организации',
                              'from': 'MasterCard 7158300734726758',
                              'id': 41428829,
                              'operationAmount': {'amount': '8221.37',
                                                  'currency': {'code': 'USD', 'name': 'USD'}},
                              'state': 'EXECUTED',
                              'to': 'Счет 35383033474447895560'}


def test_forme_date():
    """
    :return: проверяем ff вывод даты в заданном формате
    """
    assert forme_date(data_info()[1]) == '03.07.2019'


def test_cache_operation_to_info():
    """
    :return: проверяем ff вывод и формат информации о получателе ДС
    """
    assert cache_operation_to_info(data_info()[1]) == 'Счет **5560'


def test_cache_operation_from_info():
    """
    :return: проверяем ff вывод и формат информации об отправителе ДС
    """
    assert cache_operation_from_info(data_info()[1]) == 'MasterCard 7158 30** **** 6758'
