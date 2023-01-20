
nombres=["Juan", "Mario","Laura"]
numeros=[1,2,3,4,5]
datos=[1,2.5,"Mario",True]

nombres[0]="Roberto"

print(nombres[:])
print(nombres[2])
print(nombres[:3])
print(nombres[1:])
#agregar a la lista
nombres.append("Dario")
print(nombres)
#reemplazar
nombres.insert(2,"Maria")
print(nombres)


nombres.extend(["chencha",2,23,5])
print(nombres)
#elimina el parametro que le dieron
nombres.remove("chencha")
print(nombres)
#elimina el último elemento
nombres.pop()
print(nombres)

n=["Juan"]
n2=n*5
print(n2)
print(nombres)
#elimina el n elemento de la lista
del nombres[2]
print(nombres)

