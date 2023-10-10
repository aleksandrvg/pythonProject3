from square import circle
import random

print(circle(10))

array = []
for i in range(100):
    a = random.randint(1, 20)
    array.append(a)
print(f'Количество {len(array)}: {array}')

mno = set(array)
array = list(mno)
print(f'Количество {len(array)}: {array}')
