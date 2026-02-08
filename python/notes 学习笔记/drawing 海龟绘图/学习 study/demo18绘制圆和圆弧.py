import turtle
turtle.setup(600,400)
t = turtle.Pen()


# 绘制圆半径正数，逆时针
t.circle(50)
# 绘制圆半径负数，顺时针
t.circle(-50)


# 绘制圆弧
t.penup()
t.setposition(100,0)
t.pendown()
# 顺时针，90度
t.circle(-100, 90)


turtle.done()
