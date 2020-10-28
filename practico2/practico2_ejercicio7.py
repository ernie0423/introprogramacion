def caracteres(numC, caracter):
    carac = (caracter*numC)
    print(carac)

caracter = input("Dame el caracter que quires que se repita: ")
num = int(input("Dame el numeros de veces que quieres que se repita el caracter: "))
caracteres(num, caracter)