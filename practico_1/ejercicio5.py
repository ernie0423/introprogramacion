palabra_1 = str(input("ingrese una palabra: "))
palabra_2 = str(input("ingrese una segunda palabra: "))
long1 = len(palabra_1)
long2 = len(palabra_2)
if long1 > long2:
    print(f"{palabra_1} tiene {long1 - long2} letras mas que {palabra_2}")
elif long1 == long2:
    print(f"{palabra_1} tiene las mismas letras que {palabra_2}")
else:
    print(f"{palabra_2} tiene las mismas letras que {palabra_1} .")