suminv=int(input("Минимальная сумма инвестиций - "))
summ=int(input("Cколько долларов у Майкла - "))
sumi=int(input("Сколько долларов у Ивана - "))
if (summ >= suminv) and (sumi >= suminv):
   print(2)
elif  (summ <= suminv) and (sumi >= suminv):
   print("Иван")
elif (summ >= suminv) and (sumi <= suminv):
   print("Майкл")
elif (summ <= suminv) and (sumi <= suminv) and ((summ + sumi) >= suminv):
   print(1)
elif (summ <= suminv) and (sumi <= suminv) and ((summ + sumi) <= suminv):
   print(0)
