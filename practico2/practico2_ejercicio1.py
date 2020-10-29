def numeroMax(num1,num2):
    if num1 > num2:
        print(num1, "es mayor que", num2)
    else:
        print(num2, "es mayor que ", num1)

num1 = int(input("ingresa el primer numero: "))
num2 = int(input("ingresa el segundo numero: "))
numeroMax(num1,num2)