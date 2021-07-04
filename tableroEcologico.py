# Escriba un programa que permita imprimir un tablero Ecológico (verde y blanco) de acuerdo al tamaño indicado. Por ejemplo el gráfico a la izquierda es el resultado de un tamaño: 8x6



import turtle as t
import time

def es_par(numero):
    if numero%2 == 0:
        return True
    else: return False



def cuadrado(ancho, alto=1):
    t.penup()
    t.speed(100)
    t.setheading(270)
    t.forward(150)
    t.setheading(180)
    t.forward(300)
    t.pendown()
    
    
    for j in range(alto):
        bandera = 0
        for i in range(ancho):
            if es_par(j):
                if es_par(i):
                    bandera = 1
                else: bandera = 0
            

            if bandera == 0:
                t.begin_fill()
                t.fillcolor('white')
                for i in range(4):
                    t.forward(50)
                    t.left(90)
                t.end_fill()
                t.penup()
                t.setheading(180)
                t.backward(50)
                t.pendown()
                bandera = 1
                
            else:
                t.begin_fill()
                t.fillcolor('green')
                for i in range(4):
                    t.forward(50)
                    t.left(90)
                t.end_fill()
                t.penup()
                t.setheading(180)
                t.backward(50)
                t.pendown()
                bandera = 0

        t.penup()
        t.forward(50*(ancho))
        t.right(90)
        t.forward(50)
        t.left(90)
        t.pendown()
    
    nombre = t.textinput("Nombre", "¿Cuál es su nombre?")
    t.write(f'            {nombre} ejecutaste un programa hecho por ANDRES RODRIGUEZ')
    
    
    

def fuente_roja(texto):
    red = "\033[31m" + texto + "\033[0m"
    return red


def opciones(si_o_no):
    while not si_o_no.upper() in ['SI', 'NO']:
        
        si_o_no = t.textinput('INGRESE UNA OPCION VALIDA', 'Ingrese nuevamente la opción (SI o NO): ')
    return si_o_no.upper()

def devuelve_num_entero(numero):
    while not numero.isdigit():
        numero = t.textinput('INGRESE UNA OPCION VALIDA', 'Ingrese un numero: ')
    return int(numero)




while True:
    
    
    t.setup(800, 800, 300, 150)
    t.title('tablero Ecológico (verde y blanco)')
    flecha = t.Turtle()
    
    t.screensize(300, 150)

    
    opcion = opciones(t.textinput('Quiere crear una cuadro ecologico??', '¿Quiere crear un cuadro ecologico? Elija una opción (Si o No)'))

    if opcion == 'NO':
        break

    ancho = devuelve_num_entero(t.textinput('Ancho del cuadro','Ingrese el ancho del cuadro: '))
    alto = devuelve_num_entero(t.textinput('Alto del cuadro', 'Ingrese el ato del cuadro: '))

    if alto == 0:
        alto = 1

    cuadrado(ancho, alto)
    
    time.sleep(5)
    t.clearscreen()




