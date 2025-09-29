from io import open

# abrir fichero en modo lectura
archivo_texto=open("archivo.txt","r")
# escribir frase
#archivo_texto.write("\nHola Mundo!!!")

# leer fichero
print(archivo_texto.read())
# situar el puntero(cursor) dentro del fichero de texto
archivo_texto.seek(5) 
#s lunes,
#manana martes.
#buenos dias

print(archivo_texto.read())
archivo_texto.close()
