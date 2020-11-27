print("ingrese un numero de cuatro digitos 1 por 1 para comprobar si es capicua ")
digito1=str(input("ingrese el primer digito: "))
digito2=str(input("ingrese el segundo digito: "))
digito3=str(input("ingrese el tercer digito: "))
digito4=str(input("ingrese el cuarto digito: "))
digito5=str(input("ingrese el quinto digito: "))
vectorcapicua=[digito1,digito2,digito3,digito4,digito5]
print(vectorcapicua)
coincidencias=0
if vectorcapicua[0]==vectorcapicua[4]:
    print("primera coicidencia encontrada!")
    coincidencias=coincidencias+1
    if(vectorcapicua[1] == vectorcapicua[3]):
        print("segunda coicidencia encontrada!")
        coincidencias = coincidencias + 1
    if coincidencias==2:
        print("su numero es capicua! :D")
    else:
        print("su numero no es capicua D:")