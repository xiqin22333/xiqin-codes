import turtle
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(5)
turtle.colormode(255)



# 树干
t.penup()
t.goto(-25, -100)
t.pendown()
t.fillcolor("brown")
t.begin_fill()
for _ in range(4):
    t.forward(50)
    t.right(90)
t.end_fill()

# 1三角
t.penup()
t.goto(-75, -100)
t.pendown()
t.fillcolor(0,100,0)
t.begin_fill()
for _ in range(3):
    t.forward(150)
    t.left(120)
t.end_fill()

# 2三角
t.penup()
t.goto(-50, -50)
t.pendown()
t.fillcolor(0,140,0)
t.begin_fill()
for _ in range(3):
    t.forward(100)
    t.left(120)
t.end_fill()

#3三角
t.penup()
t.goto(-25, 0)
t.pendown()
t.fillcolor(0,180,0)
t.begin_fill()
for _ in range(3):
    t.forward(50)
    t.left(120)
t.end_fill()

# 星星
t.penup()
t.goto(-10, 50)
t.pendown()
t.fillcolor(255,255,0)
t.begin_fill()
for _ in range(5):
    t.forward(20)
    t.right(144)
t.end_fill()




t.hideturtle()
turtle.done()
