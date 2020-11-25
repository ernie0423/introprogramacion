suma=0
vectorsuma=[]
vector_1=[]
vector_2=[]

numeros_1=0
for i in range(0,5):
    agregado=int(input("ingrese cinco numeros: "))
    numeros_1=numeros_1+agregado
    vector_1.append(numeros_1)

numeros_2=0
for i in range(0,5):
    agregado2=int(input("ingrese cinco numeros más: "))
    numeros_2=numeros_2+agregado2
    vector_2.append(numeros_2)


for num in range(0,5):
    suma = vector_1[num] + vector_2[num]
    vectorsuma.append(suma)
print(vectorsuma)
