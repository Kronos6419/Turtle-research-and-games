import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Turtle Maze")
screen.setup(600, 600)

# Create the maze walls
def draw_maze():
    walls = turtle.Turtle()
    walls.color("black")
    walls.width(2)
    walls.penup()
    walls.goto(-250, 250) #turtle.position() / pos()
    walls.pendown()
    for _ in range(4):
        walls.forward(500)
        walls.right(90)
    walls.penup()
    walls.goto(-150, 250)
    walls.pendown()
    walls.right(90)
    walls.forward(400)
    walls.left(90)
    walls.forward(50)
    walls.left(90)
    walls.forward(300)
    walls.right(90)
    walls.forward(50)
    walls.right(90)
    walls.forward(350)
    walls.left(90)
    walls.forward(250)
    walls.left(90)
    walls.forward(50)
    walls.left(90)
    walls.forward(150)
    walls.right(90)
    walls.forward(150)
    walls.left(90)
    walls.forward(50)
    walls.left(90)
    walls.forward(150)
    walls.back(150)
    walls.left(90)
    walls.left(90)  
    walls.forward(200)
    walls.right(90)
    walls.forward(200)
    walls.right(90)
    walls.forward(300) 
    walls.right(90)
    walls.forward(50)
    walls.right(90)
    walls.forward(250)
    walls.left(90)
    walls.forward(50)
    walls.left(90)
    walls.forward(200)               
    walls.hideturtle()

# Keyboard functions, a complicated to figure out, might be easier with certain imports I saw 
def go_up():
    player.setheading(90)
    player.forward(10)

def go_down():
    player.setheading(270)
    player.forward(10)

def go_left():
    player.setheading(180)
    player.forward(10)

def go_right():
    player.setheading(0)
    player.forward(10)

# Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.penup()
player.speed(0)
player.goto(-200, 200)

# Keyboard bindings
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# Draw the maze
draw_maze()

# Main loop
screen.mainloop()
