# 导入 OpenCV 库
import cv2
import numpy as np
# 读取图像
img = cv2.imread('./image/color.jpg')

# 分离通道
b, g, r = cv2.split(img)

# 显示窗口
cv2.imshow("widow", b)
# 等待用户按键,参数 0 表示无限等待，直到用户按下任意键
cv2.waitKey(0)
# 关闭所有窗口
cv2.destroyAllWindows()