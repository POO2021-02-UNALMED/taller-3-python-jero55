class Control:
    
    def __init__(self,tv):
        self.tv = None
    
    def turnOn(self):
        self.tv.turnOn()
    
    def turOf(self):
        self.tv.turnOf()

    def canalUp(self):
        self.tv.canalUp()
    
    def canalDown(self):
        self.tv.canalDown()

    def volumenUp(self):
        self.tv.volumenUp()
    
    def volumenDown(self):
        self.tv.volumenDown()
    
    def setCanal(self,canal):
        self.tv.setCanal(canal)

    def enlazar(self,tv):
        self.tv = tv
        tv.setControl(self)
    
    def getTv(self):
        return self.tv

    def setTv(self,tv):
        self.enlazar(tv)    