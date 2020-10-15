from time import localtime
fecha_actual = localtime()
print(fecha_actual)
dia = int(input("ingrese su fecha de nacimiento (día): "))
mes = int(input("ingrese su fecha de nacimiento (mes): "))
año = int(input("ingrese su fecha de nacimiento (año): "))
años = fecha_actual.tm_year - año
meses = fecha_actual.tm_mon - mes
dias = fecha_actual.tm_mday - dia
if meses < 0 or dias < 0:
    año = años - 1
    print(f"usted tiene {años} años.")
if meses < 0:
    print(f"faltan {meses * -1} meses para su cumpleaños.")
if dias < 0:
    print(f"faltan {dias * -1} dias para su cumpleaños")
