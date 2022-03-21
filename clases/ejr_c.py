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