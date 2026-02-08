import turtle
turtle.setup(600,400)
t = turtle.Pen()

t.color('red')
t.pensize(1)

# t.circle(100,360,3)
t.penup()
t.setposition(-200,0)

for edges in range(3,13):
    t.pendown()
    t.circle(30,steps=edges)
    t.penup()
    t.forward(100)


turtle.done()