class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):  
        self.enMarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print(
            "Marca:", self.marca,
            "\nModelo:", self.modelo,
            "\nEn marcha:", self.enMarcha,
            "\nAcelerando:", self.acelera,
            "\nFrenando:", self.frena
        )

class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado = cargar
        if self.cargado:
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"

class Moto(Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.hCaballito = ""

    def caballito(self):
        self.hCaballito = "Voy haciendo el caballito."

    def estado(self):
        super().estado()
        print(self.hCaballito)


class VElectricos():
    def __init__(self):
        self.autonomia=100
    def cargarEnergia(self):
        self.cargando=True
# Pruebas
print("----------------------------------MOTO----------------------------------------")
miMoto = Moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado()
print("----------------------------------FURGONETA-----------------------------------")
miFurgoneta = Furgoneta("Renault", "Kangoo")
print(miFurgoneta.carga(True))
miFurgoneta.estado()


class BicicletaElectrica(Vehiculos, VElectricos): # herencia multiple.
    pass
print("----------------------------------BICLICLETA ELECTRICA-----------------------------------")

miBici = BicicletaElectrica("orbea", "HC130")
# IMPORTANTE:
# en la herencia multiple se da preferencia al constructor que pasamos como primera clase heredada. 

