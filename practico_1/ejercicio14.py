edad = int(input("ingrese su edad porfavor: "))
peso = int(input("ingrese su peso en kg porfavor: "))
estatura = float(input("ingrese su estatura en metros porfavor: "))
Indice_de_masa_corporal = int(peso / estatura **2)
print(f"su indice de masa corporal es {Indice_de_masa_corporal} ")
if edad < 45:
    if Indice_de_masa_corporal <= 22.0:
        print("su condicion de riesgo en base a su indice de masa corporal es: baja")
    if edad >= 45:
        if Indice_de_masa_corporal < 22.0:
            print("su condicion de riesgo en base a su indice de masa corporal es: media")
        elif Indice_de_masa_corporal >= 22.0:
            print("su condicion de riesgo en base a su indice de masa corporal es: alta")