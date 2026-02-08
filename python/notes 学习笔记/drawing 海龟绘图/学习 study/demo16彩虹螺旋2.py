import turtle

turtle.setup(600, 400)
t = turtle.Pen()
t.speed(0)
width = 1

color_list = ['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'pink']
for i in range(1,9):
    width +=i * 0.05
    t.pensize(width)
    t.color(color_list[i % 8])
    t.forward(2+ i*5)
    t.left(45)

turtle.done()