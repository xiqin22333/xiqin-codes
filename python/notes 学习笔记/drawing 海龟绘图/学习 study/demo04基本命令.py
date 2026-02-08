import turtle
turtle.setup(800,600)
t = turtle.Pen()

# 1,改变海龟方向不会前进
t.seth(45)
# 2海龟转向
t.right(45)
t.left(90)
# 3海龟移动
t.forward(100)
t.fd(50)
turtle.done()
# 3.2向后
t.backward(100)
t.bk(50)
turtle.done()