import turtle

t = turtle.Pen()
t.pensize(1)
t.speed(2)
t.color('green')

for i in range(0,301,10):
    t.penup()
    t.setposition(i,0)
    t.pendown()
    t.setposition(0,300-i)

turtle.done()
