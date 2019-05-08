class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self):

        self.x = 0
        self.y = 0

p = Point()         # instancia um objeto do tipo Point
q = Point()

p.x=1
p.y=4

q.x=5
q.y=6

print(p.x)
print(p.y)

print(q.x)
print(q.y)

print(p is q)       # o operador 'is' retorna false o que significa que eles são objetos diferentes
