from tkinter import *
from turtle import *
import turtle
import math

def dibujarTriangulo():
    size = float(input("Ingrese el tamaño de un lado: "))
    if size <= 500:
        setup(640,480)
        cursor = turtle.Pen()
        cursor.pencolor('white')
        cursor.setx(300)
        cursor.sety(-200)
        cursor.pencolor('black')
        angulo = (360/3)
        for x in range (1, 4):
            cursor.left(angulo)
            cursor.forward(size)
        print("Perimetro es igual: "+str(size*3))
        altura = ((math.tan(60))*(size/2))
        print("El area es igual a: "+str((size * altura)/2))
    else:
        print("Fuera de Rango")
def dibujarCuadrado():
    size = float(input("Ingrese el tamaño de un lado: "))
    if size <= 500:
        setup(640,480)
        cursor = turtle.Pen()
        cursor.pencolor('white')
        cursor.setx(300)
        cursor.sety(-200)
        cursor.pencolor('black')
        angulo = (360/4)
        for x in range (1, 5):
            cursor.left(angulo)
            cursor.forward(size)
        print("Perimetro es igual: "+str(size*4))
        print("El area es igual a: "+str(size**2))
    else:
        print("Fuera de Rango")

def dibujarRectangulo():
    size1 = float(input("Ingrese el tamaño de un lado: "))
    size2 = float(input("Ingrese el tamaño del otro lado: "))
    setup(640,480)
    cursor = turtle.Pen()
    cursor.pencolor('white')
    cursor.setx(300)
    cursor.sety(-200)
    cursor.pencolor('black')
    cursor.left(90)
    cursor.forward(size1)
    cursor.left(90)
    cursor.forward(size2)
    cursor.left(90)
    cursor.forward(size1)
    cursor.left(90)
    cursor.forward(size2)

    print("Perimetro es igual: "+str(size1*2+size2*2))
    print("El area es igual a: "+str(size1*size2))

def dibujarPoligono():
    size = float(input("Ingrese el tamaño de un lado: "))
    setup(640,480)
    cursor = turtle.Pen()
    cursor.pencolor('white')
    cursor.setx(200)
    cursor.sety(-200)
    cursor.pencolor('black')
    angulo = (360/5)
    for x in range (1, 6):
        cursor.left(angulo)
        cursor.forward(size)
root = Tk()
ejercici1 = Button(root, text = 'Triangulo', bd = 5, command = dibujarTriangulo)
ejercici1.pack()
ejercici2 = Button(root, text = 'Cuadrado', bd = 5, command = dibujarCuadrado)
ejercici2.pack()
ejercici3 = Button(root, text = 'Rectangulo', bd = 5, command = dibujarRectangulo)
ejercici3.pack()
ejercici4 = Button(root, text = 'Pentagono', bd = 5,command =dibujarPoligono)
ejercici4.pack()


root.title("Examen")
root.mainloop()
