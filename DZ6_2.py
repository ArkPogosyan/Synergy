x = int(input('Введите натуральное число: '))
a = 0 # счетчик натуральных деелителей
for i in range (1, x+1):
    if x % i == 0:
        a = a+1
print ('Количество натуральных делителей числа',x,'-',a)
