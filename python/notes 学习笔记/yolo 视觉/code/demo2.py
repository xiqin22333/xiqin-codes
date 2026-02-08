import cv2
from ultralytics import YOLO

# 加载模型
model = YOLO("yolo11n.pt")

# 摄像头编号
camera_no = 0

# 打开摄像头
cap = cv2.VideoCapture(camera_no)

while cap.isOpened():
    # 获取图像
    res, frame = cap.read()
    # 如果读取成功
    if res:
        # 正向推理 （results结果）
        results = model(frame)

        # 绘制结果
        annotated_frame = results[0].plot()

        # 显示图像（窗口名字）（变量）
        cv2.imshow(winname="windows", mat=annotated_frame)

        # 如果参数为 0，则表示无限期等待。
        # 如果参数大于 0，则表示等待指定的毫秒数后，如果没有按键事件发生，程序将继续执行.
        # 在处理视频时，通常会设置一个大于 0 的延迟时间,从而控制视频播放的速度。
        # 如果等于27（esc）结束代码
        if cv2.waitKey(5) == 27:
            break

    else:
        break

# 释放链接
cap.release()
# 关闭所有窗口
cv2.destroyAllWindows()