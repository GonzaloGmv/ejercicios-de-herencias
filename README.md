# ejercicios-de-herencias

El enlace al repositorio de GitHub de este proyecto es el siguiente: [GitHub](https://github.com/GonzaloGmv/ejercicios-de-herencias)

Autores:

[Miguel](https://github.com/migueliiin)

[Carlos](https://github.com/carlospuigserver)

[Nacho](https://github.com/Nachopedrero)

[Gonzalo](https://github.com/GonzaloGmv)

[José Zazo](https://github.com/jzazooro)

### Ejercicio a. Herencia simple

El UML de este ejercicio es el siguiente:

![ejrA drawio](https://user-images.githubusercontent.com/91721237/159280218-019ddb29-964c-4781-a494-f14e9aa25b10.png)

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

### Ejercicio d. Herencia multiple caso real

El UML de este ejercicio es el siguiente:

![ejrA drawio](https://github.com/GonzaloGmv/ejercicios-de-herencias/blob/main/UML/herenciamultiplecasoreal.drawio.png)

El código de este ejercicio es el siguiente:

```
class pared: 
    def __init__(self, horientacion):
        self.horientacion=horientacion

class ventana(pared): 
    def __init__(self, horientacion, superficie):
        super().__init__(horientacion)
        self.superficie=superficie
        return self.superficie

class casa(ventana):
    def __init__(self, paredes, horientacion, superficie):
        self.paredes=paredes
    def superficieacristalada(self):
        return(self.paredes.superficie)

pared_norte = pared("NORTE") 
pared_oeste = pared("OESTE") 
pared_sur = pared("SUR") 
pared_este = pared("ESTE")
ventana_norte = ventana(pared_norte, 0.5) 
ventana_oeste = ventana(pared_oeste, 1) 
ventana_sur = ventana(pared_sur, 2) 
ventana_este = ventana(pared_este, 1)
casa = casa([pared_norte, pared_oeste, pared_sur, pared_este]) 

print(casa.superficieacristalada())
```
