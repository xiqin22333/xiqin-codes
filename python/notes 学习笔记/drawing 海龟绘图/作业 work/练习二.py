import turtle

turtle.setup(600,400)
t =  turtle.Pen()
t.pencolor('purple')
t.speed(0)

for i in range(10,101,5):
    t.penup()
    t.setposition(0,-100)
    t.setheading(0)
    t.pendown()


    t.circle(i,60+i*2)


turtle.done()