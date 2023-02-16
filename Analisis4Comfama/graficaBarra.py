import matplotlib.pyplot as plt

años=[2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
consumidores=[4000,10000,8000,4500,4000,5000,4800,12000,14000,10000]
colores=["#6376EE","#63EE93","#EE63C0","#63ECEE","#63ECEE","#343A76","#92310A","#92900A","#8BA9CA","#D59D2E"]

plt.bar(años,consumidores,color=colores)
plt.xlabel("años")
plt.ylabel("consumidores")
plt.title("consumidores")

plt.show()
