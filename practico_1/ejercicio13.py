numero_de_terminos = int(input("n:"))
suma = 0
for numero_de_termino_actual in range(1, numero_de_terminos):
    if numero_de_termino_actual % 2 == 0:
            signo = -1
    else:
            signo = 1
    valor_termino_actual = signo / (1 + 2*(numero_de_termino_actual-1))
    suma = suma + valor_termino_actual
pi = 4 * suma
print(pi)