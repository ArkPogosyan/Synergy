class Tortuga:

    def __init__(self, x, y, s):
        self.x = x
        self.y = y 
        self.s = s
    
    def go_up(self):
        self.y += self.s
        return self.y
    
    def go_down(self):
        self.y -= self.s
        return self.y
    
    def go_left(self):
        self.x  -= self.s
        return self.x
    
    def go_right(self):
        self.x += self.s
        return self.x
    
    def degrade(self):
        self.s  -= 1
        return self.s

    def evolve(self):
        self.s += 1
        return self.s
    
    def count_moves(self, x2, y2):
        return self.x - x2, self.y - y2

r = Tortuga(4, 6, 12)

print(r.go_up(), r.go_down(), r.go_left(), r.go_right(), r.degrade(), r.evolve(), r.count_moves(2, 3))


    