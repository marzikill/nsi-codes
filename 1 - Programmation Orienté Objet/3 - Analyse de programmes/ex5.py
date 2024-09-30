class Point:
    def __init__(self, x, y):
        """ Point, int, int -> None """
        self.x = x
        self.y = y
        
    def deplace(self, dx, dy):
        """ Point, int, int -> None """
        self.x = self.x + dx
        self.y = self.y + dy

    def symetrique(self):
        """ Point -> Point """
        return Point(-self.x, -self.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

class Segment:
    def __init__(self, debut:Point, fin:Point) -> None:
        """Crée un segment ?"""
        self.debut = debut
        self.fin = fin

Segment(Point(0, 0), Point(1, 1))


a = Point(2, 4)
# attributs : x, et y
# méthodes : __init__ , deplace, symetrique, __str__

b = Point(1, 2) # représente B(1 ; 2)
print(b)
b.deplace(3, 5)
print(b)
b.symetrique()
print(b)