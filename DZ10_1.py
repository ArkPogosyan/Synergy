mascote = {}
while True:
    nombrem  = input('введите имя питомца (выход enter) :')
    if nombrem == '':
        break
    else:
        vid = input('введите вид питомца: ')
        ano = int(input('введите возраст питомца:'))
        finpalabra = ''
        if ano % 10 == 1 and ano != 11 and ano % 100 != 11:
            finpalabra = 'год'
        elif 1 < ano % 10 <= 4 and ano % 100 != 12 and ano != 13 and ano != 14:
            finpalabra = 'года'
        else:
            finpalabra = 'лет'
        nombreh = input('введите имя хозяина: ')
        mascote[nombrem] = {'Вид питомца: ': vid, 'Возраст питомца: ': ano, 'Имя хозяина: ': nombreh}
for key in mascote.keys():
    print("Это", mascote[key]['Вид питомца: '], "по кличке", key,". Возраст питомца:", mascote[key]['Возраст питомца: '], finpalabra, "Имя хозяина:", mascote[key]['Имя хозяина: '])
