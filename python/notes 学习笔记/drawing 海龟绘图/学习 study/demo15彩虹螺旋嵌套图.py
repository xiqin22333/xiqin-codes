import turtle

turtle.setup(600, 400)
t = turtle.Pen()
t.speed(0)
t.pensize(5)

color_list = ['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'pink']
for i in range(1,9):
    t.color(color_list[i % 8])
    t.forward(100)
    t.left(45)

turtle.done()