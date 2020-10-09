num1 = int(input("ingrese un numero entero: "))
num2 = int(input("ingrese otro numero entero: "))
cociente = num1 // num2
resto = num1 % num2
if resto == 0 :
    print("la division es exacta")
else :
    print("la division no es exacta")
print(f"cociente: {cociente}")
print(f"resto: {resto}")