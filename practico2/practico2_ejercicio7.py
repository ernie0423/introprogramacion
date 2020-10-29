def caracteres(numC, caracter):
    carac = (caracter*numC)
    print(carac)

caracter = input("ingrese el caracter que quiera que se repita: ")
num = int(input("ingrese el numeros de veces que quiera que se repita el caracter: "))
caracteres(num, caracter)