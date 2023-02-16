from unittest import FunctionTestCase
import pandas as pd

fuenteDatos=pd.read_csv("./empleados(3).csv")
print (fuenteDatos)

#Filtrar empleados que solo sean analistas 1
print("\n")
print("empleados analista1")
analista1=fuenteDatos[fuenteDatos["cargo"]=='analista1']
print(analista1)


#Filtrar empleados que solo sean analistas 2

print("\n")
print("empleados analista2")
analista2=fuenteDatos[fuenteDatos["cargo"]=='analista2']
print(analista2)

#Filtrar empleados en general que tengan menos de 30 años

print("\n")
print("empleados menores de 30 años")
filtroEdad=fuenteDatos[fuenteDatos["edad"]<30]
print (filtroEdad)

#Filtrar empleados en general que tengan mas de 50 años

print("\n")
print("empleados mayores de 50 años")
filtroEdad1=fuenteDatos[fuenteDatos["edad"]>50]
print (filtroEdad1)

