
class Empleado:
    def __init__(self,nombre,edad,saldo,aumSueldo):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo
        self.sueldo = aumSueldo
        self.nacionalidad = "peruano"
    
    def preguntar_nombre(self):
        return self.nombre
    
    def preguntar_edad(self):
        return self.edad
    
    def cumpleanios(self):
        self.edad += 1
        print("Ahora tienes {} años".format(self.edad))

    def aumentoSueldo(self):
        self.sueldo += (self.sueldo* 0.30)

    def mensaje(self,año=2025):
        print("En el año {} tendrá {} años".format(año,self.edad))

empleado1 = Empleado("Piero",45,14000,1500)

print("La edad del 1er empleado es: {}".format(empleado1.edad))
print("El sueldo del 1er empleado es: {}".format(empleado1.sueldo))

empleado1.aumentoSueldo()
empleado1.aumentoSueldo()
print("El sueldo del 1er empleado es: {}".format(empleado1.sueldo))

empleado1.cumpleanios()
empleado1.mensaje()