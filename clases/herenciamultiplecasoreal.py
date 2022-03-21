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