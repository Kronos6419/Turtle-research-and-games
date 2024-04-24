import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Turtle Maze 2")

# Create the maze
class Maze(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)

# Create the player, had to set coords actively like this otherwise it wouldn't work with moving and collision.
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("turtle")
        self.color("blue")
        self.setheading(90)
        self.penup()
        self.speed(0)

    def go_up(self):
        x_cor = self.xcor()
        y_cor = self.ycor() + 24
        if (x_cor, y_cor) not in walls:
            self.goto(x_cor, y_cor)

    def go_down(self):
        x_cor = self.xcor()
        y_cor = self.ycor() - 24
        if (x_cor, y_cor) not in walls:
            self.goto(x_cor, y_cor)

    def go_left(self):
        x_cor = self.xcor() - 24
        y_cor = self.ycor()
        if (x_cor, y_cor) not in walls:
            self.goto(x_cor, y_cor)

    def go_right(self):
        x_cor = self.xcor() + 24
        y_cor = self.ycor()
        if (x_cor, y_cor) not in walls:
            self.goto(x_cor, y_cor)

# Create maze layout, tried it with 1's and 0's before but kept ending up weird, this worked better.
level = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP  XXX              XXXX",
    "X   XXXXXX   XXXXX   XXXX",
    "X       XX   XXXXX   XXXX",
    "X       XX   XX          ",
    "XXXXXX  XX   XX        XX",
    "XXXXXX  XX   XXXXX   XXXX",
    "XXXXXX  XX    XXXX   XXXX",
    "XX  XX  XX    XXXX   XXXX",
    "XX  XX  XXX   XXXX  XXXXX",
    "XX  XX  XXX   XXX      XX",
    "XX            XXX      XX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

# Create maze objects, essential to make collision with walls work, pretty much copy-pasted from reference.
walls = []
for y in range(len(level)):
    for x in range(len(level[y])):
        character = level[y][x]
        screen_x = -288 + (x * 24)
        screen_y = 288 - (y * 24)

        if character == "X":
            maze = Maze()
            maze.goto(screen_x, screen_y)
            walls.append((screen_x, screen_y))

        if character == "P":
            player = Player()
            player.goto(screen_x, screen_y)

# Keyboard bindings, for w_a_s_d instead of arrow keys this time
wn.listen()
wn.onkey(player.go_up, "w")
wn.onkey(player.go_down, "s")
wn.onkey(player.go_left, "a")
wn.onkey(player.go_right, "d")

wn.mainloop()
