lista = []
numero = int(input("ingrese el numero de palabras: "))
i = 1
while(numero > 1):
    palabra = input("ingrese una palabra: ")
    lista.append(palabra)
    i = i + 1
    numero = numero + 1
    print(lista)
corta = min(lista)
larga = max(lista)
for i in range(0, numero):
    if len(corta) < len(numero[i]):
        corta = numero[i]
    elif len(larga) > len(numero[i]):
        larga = numero[i]
        print(f"la palabra mas larga es {larga}.")
        print(f"la palabra mas corta es {corta}.")