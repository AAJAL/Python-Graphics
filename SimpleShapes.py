import turtle

def triangle():
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(-200, -50)
    turtle.pendown()
    turtle.circle(40, steps=3)

def square():
    turtle.penup()
    turtle.goto(-100, -50)
    turtle.pendown()
    turtle.circle(40, steps=4)

def pentagon():
    turtle.penup()
    turtle.goto(0, -50)
    turtle.pendown()
    turtle.circle(40, steps=5)

def hexagon():
    turtle.penup()
    turtle.goto(100, -50)
    turtle.pendown()
    turtle.circle(40, steps=6)

def circle():
    turtle.penup()
    turtle.goto(200, -50)
    turtle.pendown()
    turtle.circle(40)
    turtle.done()

triangle()
square()
pentagon()
hexagon()
circle()
