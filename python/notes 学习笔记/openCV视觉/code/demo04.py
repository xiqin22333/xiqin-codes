import cv2
import numpy as np
# 读取图像
img = cv2.imread('./image/color.jpg')



# 缩放(缩放后的宽高)
new_img = cv2.resize(img, (2560, 1080))

# 旋转（图像中心点坐标（x, y）、旋转角度（degree）、缩放比例（scale））
rotation_matrix = cv2.getRotationMatrix2D((500,1000), 45, 1)
# 选择后的宽高
r_img = cv2.warpAffine(img, rotation_matrix, (2560, 2560))


# 修改

# 显示窗口
cv2.imshow("widow", new_img)
cv2.imshow("widow", r_img)

# 等待用户按键,参数 0 表示无限等待，直到用户按下任意键
cv2.waitKey(0)
# 关闭所有窗口
cv2.destroyAllWindows()