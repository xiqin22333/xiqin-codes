import turtle

turtle.setup(600, 400)

t = turtle.Pen()
t.pensize(3)
t.pencolor("green")

# 绘制第一个圆
t.penup()
t.goto(-50, 50)
t.pendown()
t.circle(50)

# 绘制第二个圆
t.penup()
t.goto(50, 50)
t.pendown()
t.circle(50)

# 绘制第三个圆
t.penup()
t.goto(-50, -50)
t.pendown()
t.circle(50)

# 绘制第四个圆
t.penup()
t.goto(50, -50)
t.pendown()
t.circle(50)

turtle.done()