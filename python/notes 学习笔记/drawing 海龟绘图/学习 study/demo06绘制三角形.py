import turtle

turtle.setup(600,400)
t = turtle.Pen()    


# t.forward(100)
# t.left(120)
# t.forward(100)
# t.left(120)
# t.forward(100)
# t.left(120)

# 优化代码
for i in range(3):
    t.fd(100)
    t.left(120)

turtle.done()


