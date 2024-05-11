n = int(input('Введите число: '))
m = []
for i in range(n):
    a = int(input())
    m.append(a)
m.reverse()
print(*m)
