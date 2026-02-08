import turtle

turtle.setup(600,400)
t = turtle.Pen()
# 绘制速度
t.speed(1)
t.color('yellow')

t.begin_fill()
for i in range(5):
    t.fd(100)
    t.left(144)
    t.fd(100)
    t.left(72)
t.end_fill()
turtle.done()
