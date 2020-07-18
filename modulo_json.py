""" Probar la libreria json de forma basica"""

import json

#json= string (cadena de caracteres). a continuacion se crea una variable tipo json con f (fstring)
#f (fstring)= tipo de codificacion de python que permite meter variables dentro de cadenas de strings se ponen
#tres comillas para indicar que se debe hacer salto de linea.
variable_json ="""{"Carolina":"Velez", "Terry":"Rojas", "Juan Jose":"Rojas"}"""

diccionario_json=json.loads(variable_json,) #transformar el string variable_json en un diccionario

print(diccionario_json)

#Para traer o cargar a python un archivo json 
with open('archivo.json','r') as f:  #with = keyword para generar un entorno de ejecucion (scopes o ambitos) dentro 
    animales = json.load(f)          #de mi codigo para ejecutar funciones o acciones que deban ser cerradas justo despues de terminar su
                                     #ejecucion (se usa cuando la ejecucion representa una alta carga computacional)
                                     
                                     #open('archivo','r') funcion para abrir archivos. el argumento 'r' indica que 
                                     #solo se leera el archivo.
                                     # as f indica que el archivo se guardara en una variable f
                                     #json.load(f) convierte el archivo json en un objeto de python tipo diccionario
print(animales)
print(type(animales))

diccionario={'Carolina':'Velez', 'Terry':'Rojas', 'Juan Jose':'Rojas'}
print(json.dumps(diccionario)) # el metodo dumps convierte objetos tipo diccionario de python a formato json 

#Para crear archivos en formato json 
with open('D:/D/DEVNET ASSOCIATE/Practicas Juanjo/diccionario.json','w') as a: # open('ruta_archivonuevo','w') funcion  
                                     #para crear un archivo .json. el argumento 'w' indica que se escribira sobre el
                                     # nuevo archivo.
    json.dump(diccionario,a)         #tomar el diccionario, transformarlo en json y meterlo en un archivo