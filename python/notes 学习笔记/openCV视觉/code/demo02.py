# 导入 OpenCV 库
import cv2
import numpy as np
# 读取图像
img = cv2.imread('./image/color.jpg')

# 简单阈值处理
ret, img1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)


 # 获取 ROI
roi = img[50:150, 50:150]  # 获取 (50,50) 到 (150,150) 的区域
# 修改 ROI
img[50:150, 50:150] = [0, 255, 0]  # 将 ROI 区域设置为绿色

# 显示窗口
cv2.imshow('widow', img1)
cv2.imshow("widow2", img)

# 等待用户按键,参数 0 表示无限等待，直到用户按下任意键
cv2.waitKey(0)
# 关闭所有窗口
cv2.destroyAllWindows()