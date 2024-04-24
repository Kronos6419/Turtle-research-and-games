from turtle import Turtle, Screen

turtle1 = Turtle()
turtle1.color("#E72929")
turtle1.shape("turtle")

def drawsquare():
    turtle1.forward(100)
    turtle1.left(90)
    turtle1.forward(100)
    turtle1.left(90)
    turtle1.forward(100)
    turtle1.left(90)
    turtle1.forward(100)
    turtle1.color("#2C7865")

drawsquare()
screen = Screen()
print(screen.canvheight)
screen.exitonclick()
