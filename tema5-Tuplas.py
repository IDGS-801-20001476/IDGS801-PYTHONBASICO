
#Las tuplas no admiten cambios, una vez definidas no podemos reemplazar

tupla=(1,2,3)
print(tupla)
#indica el tipo de dato: lista, dicionario o tupla
print(type(tupla))

tupla2=(7,"Roberto",True, 23.8, 16+7j)
print(tupla2)
#imprimir dependiendo del indice que tiene
print(tupla2[1])
#se pueden recorrer 
print(tupla2[4])
print(tupla2[-1])
#se puede seccionar lo que quieras imprimir
print(tupla2[0:3])
print(tupla2[:3])
print(tupla2[3:])

a,b,c =tupla
print(a)
print(c)

tuplaN=tupla+tupla2
print(tuplaN)
print(tupla.count(2))

#marca error puesto que no se puede editar 
tupla[2]=23



