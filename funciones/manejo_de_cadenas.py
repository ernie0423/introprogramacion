#manejo de cadenas/strings

palabra = input("ingrese una frase: ")

print(palabra)

tamaño = len(palabra)
tamaño= tamaño-1
print(f"tamaño de la frase: ", tamaño)

palabra_invertida = ""
for indice in range(tamaño, -1, -1):
    palabra_invertida = palabra_invertida + palabra[indice]

print(palabra_invertida)