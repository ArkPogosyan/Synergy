class Caja:
    summa = 100


    def top_up(self, pocup):
        self.summa += pocup
        return f'в кассе {self.summa} рублей'
    
    def count_1000(self):
        print('в кассе: ', self.summa//1000, 'тыс. рублей') 
    
    def take_awey(self, x):
        if x <= self.summa:
            self.summa -= x
            return f'в кассе: {self.summa} рублей'
        else:
            return f'недостаточно денег'

r = Caja()
print(r.count_1000())

