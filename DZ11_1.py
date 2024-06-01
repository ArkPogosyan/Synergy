def factorial(n):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
number = int(input("Введите число: "))
s = factorial(number)
spisok = []
for i in range(s ,0, -1):
    spisok.append(factorial(i))
print(spisok)
