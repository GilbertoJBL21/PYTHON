from shutil import copyfile

source = 'C:\\Users\\javie\\OneDrive\\Escritorio\\PYTHON\\Archivos\\lenguaje.txt'

#source2 = r'C:\Users\javie\OneDrive\Escritorio\PYTHON\Archivos\lenguaje_2.txt'

archivo =open(source, 'r')

#print(archivo.read())
#print(archivo.readline())
#print(archivo.readlines())

#archivo.close

"""contenido='C#,PHP,C,C+,TypeScript'
archivo = open('source2', 'r+') # w: write , r: read

archivo.write(contenido)
archivo.seek(0)
#print(archivo.read())

for linea in archivo.readlines():
    print(linea)

archivo.close()"""



#destination = r'C:\Users\javie\OneDrive\Escritorio\PYTHON\Archivos\lenguaje_3.txt'

#copyfile(source,destination)

def establecer_archivo(ruta,permiso):
    archivo = open(ruta, "r+")
    return archivo

def leer_archivo(archivo):
    contenido = archivo.read()
    return contenido

def escribir_archivo(archivo,texto):
    archivo.write(texto)

arch = establecer_archivo(r'C:\Users\javie\OneDrive\Escritorio\PYTHON\Archivos\lenguaje.txt', 'r+')
print(leer_archivo(arch))
escribir_archivo(arch,"MI CODIGO")
arch.seek(0)
print(leer_archivo(arch))