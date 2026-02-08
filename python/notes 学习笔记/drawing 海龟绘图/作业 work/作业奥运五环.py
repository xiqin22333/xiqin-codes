import turtle
# 使用Turtle图形库用虚拟笔绘制形状

turtle.setup(600, 400)
# 用600x400的窗户准备画布

t = turtle.Pen()
# 为环创建绘图笔实例

# 五个奥运五环的颜色和位置
colors = ['red', 'yellow', 'blue', 'green', 'orange']
positions = [(-120, 0), (0, 0), (120, 0), (-60, -60), (60, -60)]

for i in range(5):
    t.penup()  # 举起笔移动，无需画画
    t.goto(positions[i])  # 把笔放在下一个环应该开始的地方
    t.pendown()  # 放下笔开始画画
    t.color(colors[i])  # 使用指定的戒指颜色
    t.circle(60)  # 画一个半径60像素的圆

turtle.done()  #窗口保持开启，直到用户关闭
