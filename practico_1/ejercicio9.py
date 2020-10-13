num1 = float(input("ingrese un numero: "))
num2 = float(input("ingrese un segundo numero: "))
operador = input("ingrese el operador que desee: ")
if operador == "+":
    conclucion= num1 + num2
    print(f"{num1}+{num2}={conclucion}")
elif operador == "-":
    conclucion= num1 - num2
    print(f"{num1}-{num2}={conclucion}")
elif operador == "*" :
    conclucion = num1 * num2
    print(f"{num1}*{num2}={conclucion}")
elif operador == "/" :
    conclucion = num1/num2
    print(f"{num1}/{num2}={conclucion}")
elif operador == "**":
    conclucion = num1**num2
    print(f"{num1}**{num2}={conclucion}")
else:
    print("syntax error.")