n = int(input('Введите целое число: '))
sp = []
print('Введите',n,'чисел через пробел: ')
sp = list(map(int,input().split()))
sp.insert(0,sp.pop())
print(*sp)
