slovo = input('Введите слово латиницей с гласными буквами: ')
esumm=slovo.count('e') # считает количество гласных e
asumm=slovo.count('a') # считает количество гласных a
isumm=slovo.count('i') # считает количество гласных i
usumm=slovo.count('u') # считает количество гласных u
osumm=slovo.count('o') # считает количество гласных o
summglas=esumm+asumm+isumm+usumm+osumm # суммирует гласные
print("всего гласных",summglas) #выводит количество гласных
print("всего согласных",len(slovo)-summglas)
if (esumm==0):
    print ("гласной e в слове False")
else:
    print ('e=',esumm)
if (usumm==0):
    print ("гласной u в слове False")
else:
    print ('u=', usumm)
if (osumm==0):
    print ("гласной o в слове False")
else:
    print("o=",osumm)
if (asumm==0):
    print ("гласной a в слове False")
else:
    print("a=",asumm)
if (isumm==0):
    print ("гласной i в слове False")
else:
    print("i=",isumm)
