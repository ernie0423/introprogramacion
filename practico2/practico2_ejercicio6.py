def palindromo(palabra):
    tam = len(palabra)
    tam = tam - 1
    palabraInv = ""
    for indice in range(tam,-1,-1):
        palabraInv = palabraInv + palabra[indice]

    if palabraInv == palabra:
        print(palabra, " = TRUE")
    else:
        print(palabra, " = FALSE")

palabra = input("ingrese una frase: ")
palindromo(palabra)