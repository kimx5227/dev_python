import turtle, random

def drawShapes():
    s = int(input("Enter seed: "))
    random.seed(s)
    x = random.randint(5,10)
    for i in range(x):
        t = turtle.Turtle()
        t.hideturtle()
        for i in range(8):
            t.forward(50)
            t.right(45)
        t.penup()
        t.setpos(t.pos()[0] + 10, t.pos()[1])
        t.pendown()

drawShapes()
