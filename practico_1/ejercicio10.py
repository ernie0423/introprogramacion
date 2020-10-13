duracion_de_tramo = int(input("ingrese la duracion: "))
suma = 0
while duracion_de_tramo > 0:
    suma = suma + duracion_de_tramo
    duracion_de_tramo = int(input("ingrese la duracion: "))
tiempo = suma/60
print(f"el tiempo de duracion total del viaje es de {round(tiempo, 2)} horas.")