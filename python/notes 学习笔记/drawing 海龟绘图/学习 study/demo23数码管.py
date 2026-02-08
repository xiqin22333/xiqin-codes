#1，画一条线  2，花一串数字 3，读取系统时间，显示当前时间
import turtle
import time

# 绘制线条
def drawline(draw):
    if draw:
        turtle.pendown()
    else:
        turtle.penup()
    turtle.fd(40)
    turtle.right(90)

# 绘制数字8
def eight():
    drawline(True)
    drawline(True)
    drawline(True)
    drawline(True)
    turtle.left(90)
    drawline(True)
    drawline(True)
    drawline(True)

# 绘制0-9
def drawDigits(d):
    drawline(True) if d in [2,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if d in [0,1,3,4,5,6,7,9] else drawline(False)
    drawline(True) if d in [0,2,3,5,6,7,9] else drawline(False)
    drawline(True) if d in [0,2,6,8] else drawline(False)
    turtle.left(90)
    drawline(True) if d in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if d in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if d in [0,1,2,3,4,7,8,9] else drawline(False)
    turtle.penup()
    turtle.left(180)
    turtle.fd(20)


# 绘制时间
def drawDate(date):
    for i in date:
        drawDigits(eval(i))

# 主函数
def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    turtle.pencolor('blue')
    drawDate(time.strftime('%Y%m%d',time.gmtime()))
    turtle.done()



main()