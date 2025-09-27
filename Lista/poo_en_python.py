# POO en Python.
# crear clase:

class Coche():
    # crear constructor
    
    def __init__(self):
    
        # propiedades de la clase coche.
        self.__largoChasis=250 
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enMarcha=False
    
    # crear metodo.
    
    def arrancar(self,arrancamos):
        self.__enMarcha=arrancamos
        if(self.__enMarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"

        #pass  aparece por defecto. Al crear el metodo borrar.
        
    def estado(self): 
        print("El coche tiene: ",self.__ruedas, 
            " ruedas. Un ancho de: ",self.__anchoChasis,
            " Y un largo de: ", self.__largoChasis)
# instanciar objeto coche.
miCoche = Coche()
# indicar una propiedad de un objeto.
print(miCoche.arrancar(True))
miCoche.estado()

# instancia de otro objeto coche
print("-------------------------instancia de micoche2------------------------------------")
miCoche2 = Coche()
print(miCoche2.arrancar(True))

miCoche2.ruedas=2 # variable encapsulada no es accesible desde fuera de la clase

miCoche2.estado()
