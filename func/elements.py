from random import randint


def element():
    array = []
    for i in range(100):
        a = randint(1, 20)
        array.append(a)
    print(f'Количество {len(array)}: {array}')

    mno = set(array)  # Преобразуем из листа в множество
    array = list(mno)  # Преобразуем из множества в лист
    print(f'Количество {len(array)}: {array}')
