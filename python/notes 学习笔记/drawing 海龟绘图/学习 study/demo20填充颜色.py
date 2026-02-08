import turtle
from idlelib.configdialog import font_sample_text

turtle.setup(600,400)
t = turtle.Pen()

t.color('red')
t.pensize(1)

t.fillcolor('green')

t.begin_fill()
t.circle(100,steps=4)
t.end_fill()


t.color('magenta')
t.fillcolor('pink')


t.begin_fill()

for i in range(4):
    t.fd(100)
    t.left(90)
t.goto(0,100)

for i in range(3):
    t.fd(100)
    t.left(120)

t.end_fill()

t.penup()
t.goto(0,200)
t.pendown()
t.write('你好海龟',font=('simHei',18,'bold'))



turtle.done()
