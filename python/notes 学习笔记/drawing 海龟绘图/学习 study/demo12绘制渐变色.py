import turtle

turtle.setup(600,400)
t = turtle.Pen()

t.pensize(5)

color_value = 1.0
color_step = color_value/10

for i in range(4):
    color_value -= color_step
    t.color(0.5,1,color_value)
    t.forward(100)
    t.left(90)

turtle.done()