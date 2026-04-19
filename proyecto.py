from abc import ABC, abstractmethod


class Persona(ABC):
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    @abstractmethod
    def mostrar_rol(self):
        pass



class Veterinario(Persona):
    def __init__(self, nombre, documento, especialidad):
        super().__init__(nombre, documento)
        self.especialidad = especialidad

    def mostrar_rol(self):
        return f"Veterinario en {self.especialidad}"

    def atender_mascota(self, mascota):
        print(f"{self.nombre} atiende a {mascota.nombre}")


class Recepcionista(Persona):
    def mostrar_rol(self):
        return "Recepcionista"

    def registrar_cliente(self, cliente):
        print(f"Cliente {cliente.nombre} registrado")


class Cliente(Persona):
    def __init__(self, nombre, documento, telefono):
        super().__init__(nombre, documento)
        self.telefono = telefono
        self.mascotas = []

    def mostrar_rol(self):
        return "Cliente"

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def mostrar_mascotas(self):
        for m in self.mascotas:
            print(f"{m.nombre} - {m.especie}")



class Mascota:
    def __init__(self, nombre, especie, edad, peso):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso



class Tratamiento:
    def __init__(self, nombre, costo, duracion):
        self.nombre = nombre
        self.costo = costo
        self.duracion = duracion


class Consulta:
    def __init__(self, mascota, veterinario, motivo, diagnostico):
        self.mascota = mascota
        self.veterinario = veterinario
        self.motivo = motivo
        self.diagnostico = diagnostico
        self.tratamientos = []

    def crear_tratamiento(self, nombre, costo, duracion):
        t = Tratamiento(nombre, costo, duracion)
        self.tratamientos.append(t)

    def calcular_costo_consulta(self):
        return sum(t.costo for t in self.tratamientos)

    def mostrar_resumen(self):
        print(f"\nMascota: {self.mascota.nombre}")
        print(f"Veterinario: {self.veterinario.nombre}")
        print(f"Diagnóstico: {self.diagnostico}")
        print("Tratamientos:")
        for t in self.tratamientos:
            print(f"- {t.nombre}: ${t.costo}")



class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto):
        pass


class PagoEfectivo(MetodoPago):
    def procesar_pago(self, monto):
        print(f"Pagado en efectivo: ${monto}")


class PagoTarjeta(MetodoPago):
    def procesar_pago(self, monto):
        print(f"Pagado con tarjeta: ${monto}")


class PagoTransferencia(MetodoPago):
    def procesar_pago(self, monto):
        print(f"Pagado por transferencia: ${monto}")


class Factura:
    def __init__(self, consulta):
        self.consulta = consulta
        self.subtotal = consulta.calcular_costo_consulta()
        self.impuesto = self.subtotal * 0.19

    def calcular_total(self):
        return self.subtotal + self.impuesto

    def pagar(self, metodo_pago):
        total = self.calcular_total()
        metodo_pago.procesar_pago(total)

print("===================================")
print("    HOSPITAL VETERINARIO HOVET")
print("===================================")
print("Hola, bienvenido al sistema")
print("===================================")

print("========================================")
print(" Sistema de Diagnóstico Veterinario")
print("========================================")


def main():
    cliente = Cliente("Juan", "123", "300")

    m1 = Mascota("Firulais", "Perro", 3, 10)
    m2 = Mascota("Michi", "Gato", 2, 5)

    cliente.agregar_mascota(m1)
    cliente.agregar_mascota(m2)

    vet = Veterinario("Carlos", "999", "General")

    consulta = Consulta(m1, vet, "Dolor", "Infección")

    consulta.crear_tratamiento("Antibiótico", 50000, 5)
    consulta.crear_tratamiento("Vitaminas", 30000, 3)

    consulta.mostrar_resumen()

    factura = Factura(consulta)

    print("========================================")
    print("FACTURA")
    print("========================================")
    
    print("\nPago 1:")
    factura.pagar(PagoEfectivo())
    
    print("!Pago procesado correctamente!  ")
    print("\n")
   

if __name__ == "__main__":
    main()


print("===================================")
print("    HOSPITAL VETERINARIO HOVET")
print("===================================")
print("Gracias por usar nuestro sistema :)")
print("===================================")
print("\n")




