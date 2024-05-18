sp=input("Введите строку: ")
while "  " in sp:
    sp = sp.replace("  ", " ")
print(sp)
