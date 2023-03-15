# Задание №3
for i in range(20):
    for j in range(20):
        if j == 0 or j == 19:
            print('|', end='')
        elif i == 0 or i == 19:
            print('-', end='')
        else:
            print(' ', end='')
    print()