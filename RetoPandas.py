
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

#¿Cuál es el promedio de salario de un analista 1?

print("\n")
print("Promedio salarial analista1")
promedioAnalista1=analista1["salario"].mean()
print(promedioAnalista1)

#¿Cuál es el promedio de salario de un analista 2?

print("\n")
print("Promedio salarial analista2")
promedioAnalista2=analista2["salario"].mean()
print(round(promedioAnalista2,2))


#Filtrar empleados cuto porcentaje de deducción sea mayor al 10%

print("\n")
print("porcentaje mayor al 10%")
porcentajeEmpleados=fuenteDatos[fuenteDatos["porcentajeDeduccion"]>10 ]
print(porcentajeEmpleados)


#Cambiar todos los datos nan por el valor 0

print("\n")
print("cambio de datos nan")
nanRemplazo =fuenteDatos.fillna (0)
print(nanRemplazo)

#Cambiar los nan de nombres por la palabra default, los nan de cargo por el mensaje sin cargo y edad por 0

print("\n")
print("cambio de  nan nombres por default")
cambioNaN=fuenteDatos.fillna({"nombres":"default", "cargo": "sin cargo", "edad":0})
print(cambioNaN)