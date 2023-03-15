#Задание №4

n = int(input("Количество чисел в последовательности: "))
cipher_count = 0
k = 0
for _ in range(n):
    new_number = int(input("Введите число: "))
    for i in range(2, new_number // 2 + 1):
        if (new_number % i == 0):
            k = k + 1
    if (k <= 0):
        cipher_count += 1

print('Количество простых чисел в последовательности:', cipher_count)