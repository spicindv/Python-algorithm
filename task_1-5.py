import random

l1 = input('Введите первую букву диапазона (a - z): ')
l2 = input('Введите вторую букву диапазона (a - z): ')

alphabet = ['0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

l1_ind = alphabet.index(l1)
l2_ind = alphabet.index(l2)

rand1 = alphabet[random.randint(l1_ind, l2_ind)]

print(f'Выбранные буквы имеют порядковые номера: {l1} = {l1_ind}, {l2} = {l2_ind},'
      f' и между ними находятся {l2_ind - l1_ind - 1} букв(ы)')
