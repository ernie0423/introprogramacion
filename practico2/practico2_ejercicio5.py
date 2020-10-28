def inversa(palabra):
    tam = len(palabra)
    for indice in range(tam -1,-1,-1):
        palabraInv = palabraInv + palabra[indice]
    print(palabraInv)

palabra = input("ingrese una palabra: ")
inversa(palabra)