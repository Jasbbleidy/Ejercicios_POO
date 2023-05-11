class Bebidas:
    def __init__(self, nombre, color, sabor):
        self.nombre = nombre
        self.color = color
        self.sabor = sabor
        self.tomar = False
        self.regar = False
        
def comenzar_tomar(self):
    self.tomar = True
    print("La bebida se ha terminado.")

def comenzar_regar(self):
    self.regar = True
    print("La bebida se ha regado.")

def get_nombre(self):
        return self._nombre
    
def set_nombre(self, nombre):
        self._nombre = nombre
    
def get_color(self):
        return self._color
    
def set_color(self, color):
        self._tamaño = color

def get_sabor(self):
        return self._sabor 
    
def set_sabor(self, sabor):
        self._sabor = sabor
    
def get_comenzar_tomar(self):
        return self._comenzar_tomar


bebida1 = Bebidas("Gaseosa","rojo","dulce")
print(bebida1.nombre, bebida1.color, bebida1.sabor)

bebida1.comenzar_tomar()
bebida1.tomar()


class Alcohol(Bebidas):
    def __init__(self, nombre, color, sabor, contiene_alcohol)
        super().__init__(nombre, color, sabor)
        self.ontiene_alcohol = contiene_alcohol

class Gaseosa(Bebidas):
    def __init__(self, nombre, color, sabor, contiene_alcohol)
        super().__init__(nombre, color, sabor)
        self.ontiene_alcohol = contiene_alcohol


bebida1 = Alcohol("Aguardiente", "transparente", "picante", "si")
bebida1.comenzar_tomar()
bebida1.tomar()

bebida2 =Gaseosa("Pepsi", "cafe", "dulce", "no")
bebida2.comenzar_tomar()
bebida2.tomar()