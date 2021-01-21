import random

a = int(input('Введите первое число диапазона: '))
b = int(input('Введите второе число диапазона: '))

print(f'Случайное число из выбранного диапазона = {random.randint(a, b)}')

# случайное вещественное число

a = float(a)
b = float(b)
num = random.uniform(a, b)

print(f"Случайное вещественное число из выбранного диапазона = {format(num, '.3f')}")

# случайный символ

l1 = input('Введите первую букву диапазона (a - z): ')
l2 = input('Введите вторую букву диапазона (a - z): ')

alphabet = ['0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

l1_ind = alphabet.index(l1)
l2_ind = alphabet.index(l2)

rand1 = alphabet[random.randint(l1_ind, l2_ind)]

print(f'Случайная буква из выбранного дипазона: "{rand1}"')
