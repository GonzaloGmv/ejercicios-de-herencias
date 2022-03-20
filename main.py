from clases.ejr_a import *

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
