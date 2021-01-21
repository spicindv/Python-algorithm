y1 = float(input('Введите y1: '))
x1 = float(input('Введите x1: '))
y2 = float(input('Введите y2: '))
x2 = float(input('Введите x2: '))
m = x2 - x1
if x1 != 0:
    if m != 0:
        k = (y2 - y1) / (x2 - x1)
        b = y1 - k / x1
        print(f"y = {k} * x + {b}")
    else:
        print("решений нет")
else:
    print("решений нет")
