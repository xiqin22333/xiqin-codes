import turtle   # 导入 turtle 图形库，用来画图
import random   # 导入 random 库，用来随机选择颜色

t = turtle.Pen()   # 创建一支画笔对象

t.pensize(1)   # 设置画笔粗细
t.speed(0)     # 设置绘制速度，0 表示最快

color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'cyan', 'violet']
# 定义颜色列表

for i in range(0, 300, 10):   # 循环变量 i，从 0 到 300，每次增加 10
    t.color(random.choice(color_list))   # 随机选择一种颜色
    t.setposition(i, 0)                 # 移动到右边
    t.setposition(0, 300 - i)           # 移动到上方
    t.setposition(-i, 0)                # 移动到左边
    t.setposition(0, i - 300)           # 移动到下方
    t.setposition(i, 0)                 # 回到右边起点，形成星芒效果


turtle.done()   # 保持窗口打开
# 一班 龚耀博