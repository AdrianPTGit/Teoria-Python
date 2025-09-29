# manejo de arcchivos en Python

from io import open # abre un archivo 

archivo_texto = open("archivo.txt","w") # open() --> crea el fichero 
#con parametros: nombre de fichero y modo escritura "w"

frase = "Hoy es lunes, \n manana martes."

# escribir en el fichero
archivo_texto.write(frase)


#cerrar fichero
archivo_texto.close()

# leer fichero

archivo_texto = open("archivo.txt","r") # open() --> crea el fichero 
#con parametros: nombre de fichero y modo lectura "r"

texto = archivo_texto.read() # leer fichero
print(texto)



# metodo readlines() --> lee el fichero por lineas y las almacena en una lista

lineas_texto = archivo_texto.readlines()


print(lineas_texto)
print(type(lineas_texto))

# sobreescribit fichero
archivo_texto = open("archivo.txt","a") # open() --> crea el fichero 
#con parametros: nombre de fichero y modo sobreescritura "a"
texto2 = "\nbuenos dias"
archivo_texto.write(texto2)

archivo_texto.close()