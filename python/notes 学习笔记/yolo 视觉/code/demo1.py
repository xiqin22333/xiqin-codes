# 导入三方库
from ultralytics import YOLO

# 加载训练模型
a1 = YOLO("yolo11n.pt")

# show显示检测结果，save保存检测结果
a1('images/3.jpg' , show=True , save=True)
