import random
tamañodelvector = int(input("ingrese un tamaño para el vector: "))
vector_1 = [tamañodelvector]
numparacomparar=int(input("ingrese un numero para comparar los ultimos digitos: "))
vectoruwu=[]
for i in range(0, tamañodelvector - 1):
    num = random.randint(0, 300)
    vector_1.append(num)
uwu=sorted(vector_1)
for xd in uwu:
    if xd%10==numparacomparar:
        vectoruwu.append(xd)
print(vector_1)
print(vectoruwu)