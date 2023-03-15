n = int(input('Введите количество уровней пирамиды: '))
number = 1

for i in range(1, n+1):
    print('\t' * (n - i), end = '')
    for j in range(i):
        print(number, end = '')
        number += 2
        print('\t'* 2, end = '')
    print()