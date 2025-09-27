# tuplas en python

# crear tupla con ()

mitupla = ("Juan", 23, 1, 1990)

mitupla2 = 2,3,"hola" # tupla sin parentesis (Empaquetado de tupla)

# desempaquetado de tupla. Esto asigna a variables cada elemento de una tupla

nombre,dia,mes,ano = mitupla

print(ano)
print(dia)
print(nombre)
print(mes)


# mostrar un elemento de una tupla
print(mitupla[0])

#convertir tupla en lista
miLista = list(mitupla)

print(type(miLista))
print(type(mitupla))

print(miLista[:])
print(mitupla[:])

# convertir tupla en lista
mitupla = tuple(miLista)

print(mitupla)

# cuenta cuantas veces se repite un elemento dentro de una tupla metodo count()
repetido = mitupla.count(True)
print(repetido)

# ver longitud de una tupla devuelve el numero de elementos no el indice

longiud = len(mitupla)
indice = longiud - 1
print("la tupla tiene un tamano de :  {}  y un indice de : {}".format(longiud,indice))