# ejercicios-de-herencias

El enlace al repositorio de GitHub de este proyecto es el siguiente: [GitHub](https://github.com/GonzaloGmv/ejercicios-de-herencias)

Autores:

[Miguel](https://github.com/migueliiin)

[Carlos](https://github.com/carlospuigserver)

[Nacho](https://github.com/Nachopedrero)

[Gonzalo](https://github.com/GonzaloGmv)

[José Zazo](https://github.com/jzazooro)

### Ejercicio a. Herencia simple

El código de este ejercicio es el siguiente:
```
class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def traslacion(self, a, b):
        self.x = self.x + a
        self.y = self.y + b
    def __str__(self):
        return "X: {self.x}; Y: {self.y}".format(self=self)

class Punto3D(Punto2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    def traslacion(self, a, b, c):
        super().traslacion(a, b)
        self.z = self.z + c
    def __str__(self):
        return "X: {self.x}; Y: {self.y}, Z: {self.z}".format(self=self)
```

### Ejercicio b. Puzle

En la salida estandar, este programa muestra:
```
a
a

b
bb
bb
c
cc
c
```
