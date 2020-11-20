import tkinter as libtk
from tkinter import *
def borrarletra():
    letra.set("")

def reiniciar():
    lblIntentos.set(6)
    letra.set("")
    print("Reiniciar")

def buscarLetra():
    coincidencias = 0
    l = letra.get()
    l = l.upper()
    cintentos = int(lblIntentos.get())
    for pos in range(0, tam, 1):
        if (l == vectorPalabraOculta[pos]):
            vectorPalabraGuiones[pos] = l
            coincidencias = coincidencias + 1
    guiones.set(vectorPalabraGuiones)
    if (coincidencias == 0):
        cintentos = cintentos - 1
        lblIntentos.set(cintentos)
        if (cintentos == 0):
            guiones.set("PERDISTE, SE ACABARON LOS INTENTOS")
            print(archivoPalabras)
    borrarletra()

# Definición palabra oculta y los vectores a utilizar
archivoPalabras = open("palabraoculta.txt", "r")
import random
random.choices(archivoPalabras)
lista = archivoPalabras.readlines()
archivoPalabras.close()
intentos = 6
palabraoculta = lista[3]
tam = len(palabraoculta)
vectorPalabraOculta = []
vectorPalabraGuiones = []
for pos in range(0, tam, 1):
    vectorPalabraOculta.append(str(palabraoculta[pos]))
    vectorPalabraGuiones.append("-")
ventana = libtk.Tk()
ventana.config(width=500, height=500)
guiones = StringVar()
etiquetaGuiones = Label(ventana, textvariable=guiones)
etiquetaGuiones.place(x=125, y=50)
guiones.set(vectorPalabraGuiones)
etiquetaIntentosDesc = Label(ventana, text="Intentos: ")
etiquetaIntentosDesc.place(x=250, y=0)
lblIntentos = StringVar()
etiquetaIntentosValor = Label(ventana, textvariable=lblIntentos)
etiquetaIntentosValor.place(x=300, y=0)
lblIntentos.set("6")
letra = StringVar()
entradaLetra = Entry(ventana, textvariable=letra)
entradaLetra.place(x=10, y=100)
botonAdivinar = Button(ventana, text="Adivinar!", command=buscarLetra)
botonAdivinar.place(x=150, y=95)
botonReiniciar = Button(ventana, text="Reiniciar!", command=reiniciar)
botonReiniciar.place(x=150, y=120)
ventana.mainloop()
