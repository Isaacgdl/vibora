"""
Equipo 3:
Andrea Catalina Fernández Mena          A01197705
Roberto Abraham Pérez Iga               A01384237
Alan Isaac Garcia De Leon               A01383111
"""


from turtle import *
from random import randrange
from freegames import square, vector

#Radomizar los colores de comida y serpiente
import random as rd
#se inicializan todos los objetos que se encontraran dentro del juego
colores=["yellow","blue","green","orange","purple"]
colores2=["brown","cyan","gray","pink","gold"]
color = rd.choice(colores)
color2 = rd.choice(colores2)
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

#Funcion para cambiar la direccino en la que se mueve la vibora.
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

#crear una lista para los movimientos 
movement = [vector(0,10),vector(0,-10),vector(10,0),vector(-10,0)]

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)
    
   # def moveFood():
    #"Move food forward one segment."
    #food = snake[-1].copy()

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, color)

    square(food.x, food.y, 9, color2)

    #Movilizar la comida
    if not inside(food):
        square(food.x, food.y, 9, color2)
    else: 
        food.move(rd.sample(movement,1)[0])

    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()