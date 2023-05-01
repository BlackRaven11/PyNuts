from math import sqrt
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(point: {},{})'.format(self.x, self.y)

    def distance(self, pt):
        return sqrt( (self.x-pt.x)**2 + (self.y-pt.y)**2)      

p1 = Point(1, 1)
p2 = Point(2, 2)

print(p1.distance(p2)) 
