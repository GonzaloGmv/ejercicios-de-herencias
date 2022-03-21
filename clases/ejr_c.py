#CLASE BASE
class A:
    def __init__(self,a):
        self.a=a

#CLASE DERIVADA DE LA CLASE A
class B(A):
    def __init__(self,b):
        self.b=b

#CLASE DERIVADA DE LA CLASE A
class C(A):
    def __init__(self,c):
        self.c=c

class D(B,C):
    def __init__(self,d):
        self.d=d

d = D(1,2,3)

print("Pertenece el elemento d a la clase A?: {}\nPertenece el elemento d a la clase B?: {}\nPertenece el elemento d a la clase C?: {}".format(isinstance(d,A),isinstance(d,B),isinstance(d,C)))