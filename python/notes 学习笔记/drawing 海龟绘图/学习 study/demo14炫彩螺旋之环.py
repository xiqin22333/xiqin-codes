import turtle

turtle.setup(600, 400)
t = turtle.Pen()
t.speed(0)
t.pensize(5)

color_value = 1.0
color_step = color_value / 36

for i in range(36):
    color_value -= color_step
    t.color(0.5, 1, color_value)
    for j in range(3):
        t.forward(100)
        t.left(90)
    #     绘制第四条边
    t.forward(100)
    t.left(100)



turtle.done()