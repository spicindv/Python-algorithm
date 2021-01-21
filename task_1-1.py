numbers = int(input('Введите трехзначное число: '))
a = numbers // 100
b = (numbers % 100) // 10
c = (numbers % 100) % 10

s = a + b + c
m = a * b * c
# вывод времени в формате чч:мм:сс
print(f"{s = }")
print(f"{m = }")
