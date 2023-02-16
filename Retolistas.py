#Convertir la tupla=(50,45,20,30,40,87) en una lista que solo contenga números >40 
listanumeros = []
numeros= (50,45,20,30,40,87)

for x in numeros:
    if x >40:
     listanumeros.append(x)

print(listanumeros)
    

#Convertir la tupla=(50,45,20,30,40,87) en una lista que solo contenga números  PARES

listanumeros1 = []

for x in numeros:
    if x%2 ==0:
     listanumeros1.append(x)

print(listanumeros1)








