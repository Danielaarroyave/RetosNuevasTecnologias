import matplotlib.pyplot as pyplot

dias=['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
ventas=[150000, 440000, 90000, 420000, 610000, 790000, 770000]
colores=["#6376EE","#63EE93","#EE63C0","#63ECEE","#63ECEE","#343A76","#92310A"]


pyplot.bar(dias,ventas, color=colores )
pyplot.xlabel("dias")
pyplot.ylabel("ventas")
pyplot.title("Ventas de Cremas")

pyplot.show()