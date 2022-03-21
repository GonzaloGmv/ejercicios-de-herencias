#CLASE BASE
class A:
    def __init__(self,a):
        self.a=a
        a=A

#CLASE DERIVADA DE LA CLASE A
class B(A):
    def __init__(self,a,b):
        self.b=b
        self.a=a

#CLASE DERIVADA DE LA CLASE A
class C(A):
    def __init__(self,a,c):
        self.c=c
        self.a=a

#CLASE DERIVADA DE LA CLASE A
class D(B,C):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

d = D(1,2,3)

print("Pertenece el elemento d a la clase A?: {}\nPertenece el elemento d a la clase B?: {}\nPertenece el elemento d a la clase C?: {}".format(isinstance(d,A),isinstance(d,B),isinstance(d,C)))

print("a(A)={} \nb(B)={} \nc(C)={} \n".format(str(d.a),str(d.b),str(d.c)))