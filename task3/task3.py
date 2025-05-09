import json


def get_value_by_id(values: list[dict], id_val: int) -> str | None:
    """
    По идентификатору id_val находит нужное значение в списке values
    в случае его отсутствия возвращает None
    """
    for value in values:
        if value['id'] == id_val:
            return value['value']


def tree_traversal(tests: list[dict], values: list[dict]) -> None:
    """
    Функция, которая рекурсивно обходит список словарей tests и находит по идентификатору 'id' значения из values
    и записывает в словари tests по ключу 'value'
    """
    for test in tests:
        # проверяем наличие ключа 'value'
        if test.get('value') is not None:
            # получаем значение по идентификатору из values
            val = get_value_by_id(values, test['id'])
            # если значение есть, то записываем его
            if val is not None:
                test['value'] = val
        # при наличии у рассматриваемого словаря ключа 'values' рекурсивно вызываем эту функцию
        if 'values' in test.keys():
            tree_traversal(test['values'], values)


if __name__ == '__main__':
    # путь к результатам прохождения теста
    values_way = input()
    # путь к структуре для построения отчета на основе прохождения тестов
    test_way = input()
    # путь для записи результата
    report_way = input()

    with open(values_way) as vf:
        values_data = json.loads(vf.read())
        vf.close()

    with open(test_way) as tf:
        test_data = json.loads(tf.read())
        tf.close()

    # вызываем рекурсивную функцию для модификации данных из файла со структурой для построения отчета
    tree_traversal(test_data['tests'], values_data['values'])

    with open(report_way, 'w') as rf:
        rf.write(json.dumps(test_data, indent=2))
        rf.close()
