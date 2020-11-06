#si un cliente del banco deposita 100bs en enero y el banco le paga un 2% del total ahorrado
#por mes cuanto recogera el cliente durante o pasados 12 meses

monto=int(input("ingrese un monto: "))
cantidad_de_meses=int(input("ingrese una cantidad de meses: "))
meses=1
interes=int(input("ingrese el interes: "))
intereses=interes/100
while (meses<=cantidad_de_meses):
    interesganado=(monto*interes)
    monto=monto+interesganado
    print("pasado: ",meses,"mes", "monto actual: ",monto)
    meses=meses+1