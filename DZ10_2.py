nuevo_dict = {}
primero_numero = int(input('Введите число начала: '))
segundo_numero = int(input('введите стмло конца: '))
if primero_numero > segundo_numero:
    for i in range(primero_numero, segundo_numero - 1, -1):
        nuevo_dict[i] = i ** i
for i in range(primero_numero, segundo_numero + 1):
        nuevo_dict[i] = i ** i
print(nuevo_dict)
