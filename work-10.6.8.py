

N = int(input('Введите число '))
for x in range(N, 0, -1):
    for y in range(N, 0, -1):
        if x - 1 < y:
            print(y, end='')
        else:
            print('.', end='')
    for y in range(1, N + 1):
        if x - 1 < y:
            print(y, end='')
        else:
            print('.', end='')
    print()