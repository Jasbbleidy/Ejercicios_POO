class Animales:
    def __init__(self, nombre, tipo_alimentacion, tamaño_cm):
        self.nombre = nombre
        self.tipo_alimentacion = tipo_alimentacion
        self.tamaño_cm = tamaño_cm 
        self.correr = False
        self.comer = False
        
def comenzar_dormir(self):
    self.correr = True
    print("El animal ha comenzado a dormir.")

def terminar_dormir(self):
    self.correr = True
    print("El animal ha terminado de dormir.")

def comenzar_comer(self):
    self.comer = True
    print("El animal ha comenzado a comer.")

def terminar_comer(self):
    self.comer = True
    print("El animal ha terminado de comer.")

def get_nombre(self):
        return self._nombre
    
def set_nombre(self, nombre):
        self._nombre = nombre
    
def get_tipo_alimentacion(self):
        return self._tipo_alimentacion
    
def set_tipo_alimentacion(self, tipo_alimentacion):
        self._tipo_alimentacion = tipo_alimentacion

def get_tamaño_cm(self):
        return self._tamaño_cm 
    
def set_tamaño_cm(self, tamaño_cm):
        self._tamaño_cm = tamaño_cm
    
def get_comenzar_comer(self):
        return self._comenzar_comer


animal1 = Animales("Jirafa","herbivoro","90")
print(animal1.nombre, animal1.tipo_alimentacion, animal1.tamaño_cm)

animal1.comenzar_dormir()
animal1.terminar_comer()


class Cocodrilos(Animales):
    def __init__(self, nombre, tipo_alimentacion, tamaño_cm, habitad)
        super().__init__(nombre, tipo_alimentacion, tamaño_cm)
        self.habitad = habitad

    def nadar(self):
        print("nadar en el {self.habitad} de los cocodrilos")


class Osos_pardos(Animales):
    def __init__(self, nombre, tipo_alimentacion, tamaño_cm, habitad)
        super().__init__(nombre, tipo_alimentacion, tamaño_cm)
        self.habitad = habitad
    
    def hibernar(self):
        print("el oso hiberna en {self.habitad} en invierno")


cocodrilo1 = Cocodrilos("Marvin", "carnivoro", "600", "humedales")
cocodrilo1.comenzar_comer()
cocodrilo1.nadar()

oso1 = Osos_pardos("Baloo", "carnivoro", "280", "montañas")
oso1.comenzar_dormir()
oso1.hibernar()