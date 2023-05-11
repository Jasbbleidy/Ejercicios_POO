class Cuerpos_celestes:
    def __init__(self, nombre, tamaño, material_compuesto):
        self.nombre = nombre
        self.tamaño = tamaño
        self.material_compuesto= material_compuesto 
        self.brillar = False
        self.girar = False
        
def comenzar_brillar(self):
    self.brillar = True
    print("El cuerpo celeste ha comenzado a brillar.")

def comenzar_girar(self):
    self.girar = True
    print("El cuerpo celeste ha girado.")

def get_nombre(self):
        return self._nombre
    
def set_nombre(self, nombre):
        self._nombre = nombre
    
def get_tamaño(self):
        return self._tamaño
    
def set_tamaño(self, tamaño):
        self._tamaño = tamaño

def get_material_compuesto(self):
        return self._material_compuesto 
    
def set_material_compuesto(self, material_compuesto):
        self._material_compuesto = material_compuesto
    
def get_comenzar_brillar(self):
        return self._comenzar_brillar


cuerpo_celeste1 = Cuerpos_celestes("Luna","3474.8 km","oxigeno")
print(cuerpo_celeste1.nombre, cuerpo_celeste1.tamaño, cuerpo_celeste1.material_compuesto)

cuerpo_celeste1.comenzar_brillar()
cuerpo_celeste1.girar()


class Planetas(Cuerpos_celestes):
    def __init__(self, nombre, tamaño, material_compuesto, periodo_orbital)
        super().__init__(nombre, tamaño, material_compuesto)
        self.periodo_orbital = periodo_orbital

    def orbitar(self):
        print("orbitar en un {self.periodo_orbital} de 365 dias")


class Planetas(Cuerpos_celestes):
    def __init__(self, nombre, tamaño, material_compuesto, periodo orbital)
        super().__init__(nombre, tamaño, material_compuesto)
        self.periodo_orbital = periodo_orbital
    
    def orbitar(self):
        print("el oso hiberna en {self.periodo_orbital} en invierno")


planeta1 = Planetas("Tierra", "6.371 km", "agua", "365 dias")
planeta1.comenzar_comer()
planeta1.nadar()

planeta2 = Planetas("Mercurio", "2.439,7 km", "metal", "88 dias")
planeta2.comenzar_girar()
planeta2.orbitar()