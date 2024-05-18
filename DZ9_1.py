n = int(input('Введите количество элементов списка: '))
sp = list(map(int, input('введите числа через пробел: ').split()))[:n]
s = set(sp)
print(len(s))

#n=int(input("Введите количество элементов списка "))

#spisok = list(map(int, input().split()))[:n]

#e=set(spisok)

#print(len(e))