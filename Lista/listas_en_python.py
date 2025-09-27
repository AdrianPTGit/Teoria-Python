# LISTA EN PYTHON

#sintaxis:
#
#   nombreLista = [elem1, elem2, elem3.....]

miLista=["Maria","Pepe","Marta","antonio"]

# imprimir lista con print().

# toda la lista.

print(miLista[:]) #El operador [:] crea una copia superficial de la lista antes de imprimirla.
# El resultado visual es el mismo.

#Imprime la referencia original de la lista. Normalmente verás el contenido entre corchetes.
print(miLista)

# un solo elemento de la lista utilizando el indice.
print(miLista[3])

# imprimir indice -1.

print(miLista[-2])

# imprime elementos del indice 0 al 2.
print(miLista[0:3])
# igual
print(miLista[:2])

# agregar elemento a la lista con metodo append().

miLista.append("Sandra") # al final de la lista.
miLista.insert(2, "adrian")# agrega en elemento en la posicion 2 del inidice de la lista.
print(miLista[:])

#para agregar varios elemento a lavez usar metodo extend()

miLista.extend(["Carlos","Ana","antonio"])
print(miLista[:])

# como saber el indice de un elemento. Util en listas grandes con metodo index()

print(miLista.index("Ana"))

# existe un elemento en la lista con in

print("Pepe" in miLista)

# una lista puede almacenar diferentes tipos de datos.

lista = [1, 12.2, True, 's', "hola"]
print(lista[:])

# eliminar elementos con metodo remove()

lista.remove('s')
print(lista[:])

# eliminar ultimo elemento de la lista

print(miLista.pop())
print(miLista[:])

# con el operador + podemos unir (concatenar) listas diferentes

milista3 = miLista + lista

print(milista3[:])

# con el operador * repite el contenido de una lista

print(lista*3)