#Codigo sacado de http://edupython.blogspot.com.co/2013/07/la-seccion-de-oro.html
from turtle import *

fi = 1.618033988749895

def cuadro(longitud):
    begin_fill()
    for i in range(4):
        fd(longitud)
        lt(90)
    end_fill()

def rectangulo_dorado(n, longitud):
    for i in range(n):
        cuadro(longitud)
        # Mover la tortuga a la esquina contraria y girarla
        # 90 grados a la izquierda.
        fd(longitud)
        lt(90)
        fd(longitud)

        longitud *= fi

def espiral_dorada(n, radio):
    for i in range(n):
        circle(radio, 90)
        radio *= fi

def espiral(n, radio):

    color('White')
    fillcolor('SteelBlue')
    pensize(1)
    rectangulo_dorado(n, radio)
    # Regresa la tortuga al centro de la pantalla pero sin
    # dibujar por su paso.
    penup()
    home()
    pendown()
    color('Gold')
    pensize(4)
    espiral_dorada(n, radio)

hideturtle()
speed('slow')
espiral(11, 2)
done()
