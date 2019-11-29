import os
os.system('clear')

# import turtle library
import turtle 
i = 0
my_pen = turtle.Turtle()


if(i <= 16):   
    for i in range(16):
        my_pen.penup()
        my_pen.goto(25, 50)
        my_pen.pendown()
        my_pen.color("dark green")
        my_pen.forward(100)
        my_pen.right(90)
        my_pen.right(45)
        my_pen.right(22.5)
       
        for i in range(16):
            my_pen.penup()
            my_pen.goto(25, 50)
            my_pen.pendown()
            my_pen.color("blue")
            my_pen.forward(100)
            my_pen.right(90)
            my_pen.right(45)
            my_pen.right(22.5)
           
        
    
    

turtle.done()                               