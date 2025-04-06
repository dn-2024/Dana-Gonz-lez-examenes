
class Persona:
    def __init__(self,nombre,edad,saldo):
        self.nombre = nombre
        self.edad = edad
        self._saldo = saldo
        self.nacionalidad = "peruano"

    def transferencia(self,destinatario,monto=2500):
        if self._saldo < monto:
            return "No puede transferir"
        else:
            self._saldo -= monto
            destinatario._saldo += monto
            return "{} tranfirió S/.{}".format(self.nombre,monto)

    def mostrar_saldo(self):
        if self._saldo == 0:
           return "Saldo insuficiente"
        else:
            return "Puede retirar,saldo actual: {}".format(self._saldo)


class Empleado(Persona):
    def __init__(self,nombre,edad,saldo,aumSueldo):
        super().__init__(nombre, edad,saldo)
        self.sueldo = aumSueldo
    
    def aumentoSueldo(self):
        self.sueldo += self.sueldo


empleado1 = Empleado("Piero",45,14000,1500)
empleado2 = Empleado("Carmen",37,10,1100)

print(empleado1.mostrar_saldo())
print(empleado2.mostrar_saldo())

empleado1.transferencia(empleado2,2000)
print(empleado1.mostrar_saldo())
print(empleado2.mostrar_saldo())

empleado1.aumentoSueldo()
empleado2.aumentoSueldo()
print(f"empleado 1, nuevo sueldo: {empleado1.sueldo}")
print(f"empleado 2, nuevo sueldo: {empleado2.sueldo}")