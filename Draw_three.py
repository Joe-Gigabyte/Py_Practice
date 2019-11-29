import os
os.system('clear')

# import turtle library
import turtle 
i = 0
my_pen = turtle.Turtle()
my_pen.speed(100)
if(i <= 16):   
    for i in range(16):
        my_pen.color("blue")
        my_pen.pensize(10)
        my_pen.forward(100)
        my_pen.pensize(2)
        my_pen.right(90)
        my_pen.right(45)
        my_pen.right(22.5)
        for i in range(16):
            my_pen.color("yellow")
            my_pen.forward(50)
            my_pen.right(90)
            my_pen.right(45)
           # my_pen.right(135)
      


turtle.done()    