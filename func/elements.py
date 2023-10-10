from random import randint


def element():
    array = []
    for i in range(100):
        a = randint(1, 20)
        array.append(a)
    print(f'Количество {len(array)}: {array}')

    mno = set(array)
    array = list(mno)
    print(f'Количество {len(array)}: {array}')
