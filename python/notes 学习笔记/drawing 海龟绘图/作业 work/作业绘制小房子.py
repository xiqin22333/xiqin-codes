import turtle

turtle.setup(600,400)
t = turtle.Pen()


for _ in range(4):
    turtle.forward(100)
    turtle.right(90)
    turtle.end_fill()


for i in range(3):
    t.fd(100)
    t.left(120)

turtle.done()

# 公选一班。龚耀博