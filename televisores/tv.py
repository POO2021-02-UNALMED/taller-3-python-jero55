class TV:
    numTV=0
    def __init__(self,marca,estado):
        self.marca = marca
        self.canal = 1
        self.precio = 500
        self.estado = estado
        self.volumen = 1
        self.control = None
        TV.numTV += 1

    def setMarca(self,marca):
        self.marca = marca
    
    def getMarca(self):
        return self.marca
    
    def setControl(self,control):
        self.control = control
    
    def getControl(self):
        return self.control
    
    def setPrecio(self,precio):
        self.precio = precio
    
    def getPrecio(self):
        return self.precio
    
    def setVolumen(self,volumen):
        if volumen > 7 or volumen < 0 or self.estado == False:
            return
        self.volumen = volumen
    
    def getVolumen(self):
        return self.volumen

    def setCanal(self,canal):
        if canal > 120 or canal < 1 or self.estado == False:
            return
        self.canal = canal

    def getCanal(self):
        return self.canal

    @staticmethod
    def getNumTV():
        return TV.numTV

    @classmethod
    def setNumTV(cls,numTV):
        cls.numTV = numTV

    def turnOn(self):
        self.estado = True
    
    def turnOff(self):
        self.estado = False

    def canalUp(self):
        if self.canal +1 >120 or self.estado == False:
            return
        self.canal += 1
    
    def canalDown(self):
        if self.canal-1 < 1 or self.estado == False:
            return
        self.canal -= 1
    
    def volumenUp(self):
        if self.volumen + 1 > 7 or self.estado == False:
            return
        self.volumen += 1
    
    def volumenDown(self):
        if self.volumen - 1 < 0 or self.estado == False:
            return
        self.volumen -= 1 

     