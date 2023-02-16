#Construir un programa que reciba el tamaño de una lista  y la llene con múltiplos de 7
import random 

print("============1 Punto=============")

numero= int(input('ingrese un numero: '))

miLista = []

for x in range(0,numero):
    numeroalt = (random.randint(1, 9))*7
    miLista.append(numeroalt)

print(miLista)


### second Construir un programa que reciba el tamaño de una lista y la llene con números entregados por el usuario

print("============2 Punto=============")

numero1= int(input('ingrese un numero para el tamano lista: '))

miLista1 = []

for x in range(0,numero1):
    numero2= int(input('ingrese el numero para agregar a la lista: '))
    miLista1.append(numero2)

print(miLista1)


### third Leer 8 ciudades colombianas, guardarlas en una lista y mostrar en orden inverso los datos ingresados


print("============3 Punto=============")

ciudades = ['medellin','bogota','cali','cartagena','manizales','barranquilla','tolima','quindio']
tamano = len(ciudades)


for x in range(tamano,0,-1):
    print(ciudades[(x-1)])



### 4 Leer 20 números enteros y guardar en una lista, después permitir que el usuario busque un número y si este se encuentra en la lista indicar con un mensaje que el resultado es exitoso



print("============4 Punto=============") 

miLista3 = []
band = False
for x in range(0,20):
    numero3= int(input('ingrese el numero para agregar a la lista: '))
    miLista3.append(numero3)

print(miLista3)

numero4= int(input('ingrese el numero que desea buscar en la lista: '))

for x in miLista3:
    if x == numero4:
        print("El numero si existe")
        band = True
        break
if band == False:
    print("El numero No existe")





