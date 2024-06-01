class Transport:
   def __init__(self, name, max_speed, mileage):
       self.name = name
       self.max_speed = max_speed
       self.mileage = mileage
class Autobus(Transport):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)
        self.max_speed  = max_speed
        self.mileage  = mileage
a1 = Autobus('Renaul Logan', 180, 12)

print(f'Название автомобиля: {a1.name}. Cкорость: {a1.max_speed}. Пробег: {a1.mileage}.')

