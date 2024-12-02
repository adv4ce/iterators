from FlatIterator import FlatIterator
from flat_generator import flat_generator
import types

def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item, f"Тест 1 не пройден! Ошибка: {flat_iterator_item} != {check_item}"

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None], 'Тест 1 не пройден! Итерация не совпала с ожидаемым результатом'

def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item, f"Тест 2 не пройден! Ошибка: {flat_iterator_item} != {check_item}"

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None], 'Тест 2 не пройден! Итерация не совпала с ожидаемым результатом'

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType), 'Тест 2 не пройден! Не является генератором'

def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item, f"Тест 3 не пройден! Ошибка: {flat_iterator_item} != {check_item}"

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!'], 'Тест 3 не пройден! Итерация не совпала с ожидаемым результатом'

def test_4():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item, f"Тест 4 не пройден! Ошибка: {flat_iterator_item} != {check_item}"

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!'], 'Тест 4 не пройден! Итерация не совпала с ожидаемым результатом'

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType), 'Тест 4 не пройден! Не является генератором'
