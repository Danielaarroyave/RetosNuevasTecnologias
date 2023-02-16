#importando libreria

import matplotlib.pyplot as plt

#1 tener una fuente de datos
barrios=["Calasanz", "Laureles", "Castilla", "Belen", "Robledo", "Boston", "Buenos aires", "Manrique", "Estadio", "Blanquizal"]
poblacion=[12000, 25000, 40000, 100000, 200000, 50000, 60000, 250000, 10000, 5000]

barrios3=["Calasanz", "Laureles", "Castilla", "Belen", "Robledo", "Boston", "Buenos aires", "Manrique", "Estadio", "Blanquizal"]
poblacion3=[1000, 25000, 41000, 110000, 100000, 5000, 63000, 220000, 11000, 3000] 


barriosBello=["La Cumbre", "Santa Ana", "Niquia", "Bella Vista", "Paris", "Camacol", "Cabañas", "Barrio Obrero", "Navarra", "Pacheli"]
poblacionBello=[30000, 12000, 100000, 50000, 25000,3000, 5500,4850,10000,5000]

#2 PROCEDO A UTILIZAR EL MATPLOTLIB PARA GENERAR LA GRAFICA

#3 MODIFICAMOS LA GRAFICA

plt.plot(barrios, poblacion, marker="o", linestyle="-.", color="g")
plt.plot(barrios3, poblacion3, marker="4", linestyle="--", color="b")
plt.xlabel("Barrios de Medellin")
plt.ylabel("poblacion")
plt.title("Densidad de población Medellin 2023")


plt.savefig("linea.png")
plt.show()

