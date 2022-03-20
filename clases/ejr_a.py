class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def traslacion(self, a, b):
        self.x = self.x + a
        self.y = self.y + b
    def __str__(self):
        return "X: {self.x}; Y: {self.y}".format(self=self)

a = Punto2D(1,2)
print("A = {}".format(a))
a.traslacion(-1, -2) 
print("A = {}".format(a))
b = Punto2D(-3, 0) 
b.traslacion(5, -1) 
print("B = {}".format(b))

class Punto3D(Punto2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    def traslacion(self, a, b, c):
        super().traslacion(a, b)
        self.z = self.z + c
    def __str__(self):
        return "X: {self.x}; Y: {self.y}, Z: {self.z}".format(self=self)

c = Punto3D(1,5,-3)
c.traslacion(0, -2, 1)
print("C = {}".format(c)) 