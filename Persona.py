class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
        self.saludar = False
        self.presentarse = False
        
def comenzar_saludar(self):
    self.saludar = True
    print("Hola, mucho gusto.")

def comenzar_presentarse(self):
    self.presentarse = True
    print("Mi nombre es Manuel, tengo 28 años y soy policia.")

 def get_nombre(self):
        return self._nombre
    
def set_nombre(self, nombre):
        self._nombre = nombre
    
def get_edad(self):
        return self._edad
    
def set_edad(self, edad):
        self._edad = edad
    
def get_comenzar_saludar(self):
        return self._comenzar_saludar


persona1 = Persona("Manuel","28","Police")
print(persona1.nombre, persona1.edad, persona1.profesion)

persona1.comenzar_saludar()
persona1.comenzar_presentarse()


class Estudiante(Persona):
    def __init__(self, nombre, edad, profesion, materia_favorita)
        super().__init__(nombre, edad, profesion)
        self.materia_favorita = materia_favorita

    def escribir(self):
        print("escribir la {self.materia_favorita} de la persona")


class Arquitecto(Persona):
    def __init__(self, nombre, edad, profesion, casas_construidas)
        super().__init__(nombre, edad, profesion)
        self.casas_construidas = casas_construidas
    
    def diseñar(self):
        print("dibujar un plano para el proyecto de {self.casas_construidas}")


estudiante1 = Estudiante("Luis", "15", "estudiante", "quimica")
estudiante1.comenzar_saludar()
estudiante1.escribir()

arquitecto1 = Arquitecto("Alenxandra", "32", "arquitecta", "7")
arquitecto1.comenzar_presentarse()
arquitecto1.diseñar()


        
