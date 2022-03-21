from clases.ejr_a import *
from clases.ejr_c import *
from clases.herenciamultiplecasoreal import *

if __name__ == "__main__":
    while True:
        ejr = input("Escriba el numero del ejercicio que desea iniciar, a, c o d: ")
        try:
            ejr == 'a' or ejr == 'b' or  ejr == 'c'
        except:
            pass
        else:
            break
    if ejr == 'a':
        a = Punto2D(1,2)
        print("A = {}".format(a))
        a.traslacion(-1, -2) 
        print("A = {}".format(a))
        b = Punto2D(-3, 0) 
        b.traslacion(5, -1) 
        print("B = {}".format(b))
        c = Punto3D(1,5,-3)
        c.traslacion(0, -2, 1)
        print("C = {}".format(c)) 
    if (ejr =='c' or ejr =='C') :
        d = D(1,2,3)
        c = C(7,8)
        print("Pertenece el elemento d a la clase A?: {}\nPertenece el elemento d a la clase B?: {}\nPertenece el elemento d a la clase C?: {}".format(isinstance(d,A),isinstance(d,B),isinstance(d,C)))
        print("Pertenece el elemento c a la clase D?:"+str(isinstance(c,D)))
        print("a(A)={} \nb(B)={} \nc(C)={} \n".format(str(d.a),str(d.b),str(d.c)))
    if ejr =='d':
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
