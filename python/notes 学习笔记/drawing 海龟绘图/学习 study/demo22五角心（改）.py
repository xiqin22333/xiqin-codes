import turtle

# 绘制背景
def draw_rectangle(t, width, height):
    t.penup()
    t.goto(-width/2, height/2)
    t.pendown()
    t.color("red")
    t.begin_fill()
    for i in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()
    t.penup()

# 绘制五角星 - 修正版本（100%有效）
def draw_star(t, size):
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.right(144)
        t.forward(size)
        t.left(72)  # 关键修复：形成闭合路径
    t.end_fill()

# 其他函数保持不变...
def draw_5_stat(t, width, height):
    t.color("yellow")
    t.penup()
    t.goto(-width/2 + width*1/6, height/2 - height*1/6)
    t.setheading(-72)
    t.pendown()
    draw_star(t, height*1/6)

    smaller_star_size = height*1/18
    # 第一颗小星星
    t.penup()
    t.goto(-width/2 + width*1/3, height/2 - height*1/10)
    t.setheading(-18)
    t.pendown()
    draw_star(t, smaller_star_size)
    # 第二颗小星星
    t.penup()
    t.goto(-width / 2 + width * 1 / 3, height / 2 - height * 1 / 4)
    t.setheading(0)
    t.pendown()
    draw_star(t, smaller_star_size)
    # 第三颗小星星
    t.penup()
    t.goto(-width / 2 + width * 1 / 3.5, height / 2 - height * 1 / 3)
    t.setheading(18)
    t.pendown()
    draw_star(t, smaller_star_size)
    # 第四颗小星星
    t.penup()
    t.goto(-width / 2 + width * 1 / 4.5, height / 2 - height * 1 / 2.2)
    t.setheading(54)
    t.pendown()
    draw_star(t, smaller_star_size)

# 主程序
if __name__ == "__main__":
    t = turtle.Pen()
    t.speed(5)
    width, height = 600, 400
    screen = turtle.Screen()
    screen.title("国旗")
    screen.setup(width + 50, height + 50)

    draw_rectangle(t, width, height)
    draw_5_stat(t, width, height)
    turtle.done()