a = int(input('Введите число А:'))
b = int(input('Введите число B(большее или равное А):'))
for i in range (a, b+1):
    if i % 2 == 0:
        print (i, end=' ')
