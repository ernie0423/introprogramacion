numero = int(input("ingrese un numero: "))
contador = 0
divisor = 0
for divisor in range(1,numero+1):
    if numero % divisor == 0:
        print(divisor)
        contador += 1