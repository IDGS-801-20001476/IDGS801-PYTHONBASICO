
#es un tipo de datoq ue nos permite almacenar diferentes tipos de datos através de un Key valor

miDiccionario={"Matricula":12345, "Nombre":"Dario","edad":23}

print(type(miDiccionario))
print(miDiccionario)
"cambiar valor del nombre"
miDiccionario["Nombre"]="Panfilo"
print(miDiccionario)
#imprimir un dato especifico
print(miDiccionario["edad"])
#imprimir los valores
print(miDiccionario.values())
#imprimir el nombre de que son 
print(miDiccionario.keys())
