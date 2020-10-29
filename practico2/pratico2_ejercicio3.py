def contador(lista):
    contador = 0
    for i in lista:
        contador = contador + 1
    return contador


palabra = input("ingrese la palabra: ")
res = contador(palabra)
print(res)