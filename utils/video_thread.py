import os
import threading

import airsim
import numpy as np
import cv2

class video_thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        client = airsim.MultirotorClient()
        client.confirmConnection()

        while True:
            try:
                # 获取图像响应
                responses = client.simGetImages([
                    airsim.ImageRequest("1", airsim.ImageType.Scene, False, False)
                ])

                if responses:
                    img_data = responses[0].image_data_uint8
                    if not img_data:
                        print("图像数据为空")
                        continue

                    # 将字节数据转换为 numpy 数组
                    img1d = np.frombuffer(img_data, dtype=np.uint8)
                    # 调整数组形状以匹配图像尺寸
                    frame = img1d.reshape(responses[0].height, responses[0].width, 3)

                    # 显示帧
                    cv2.imshow('AirSim Video', frame)

                    # 按 'q' 键退出循环
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    print("未获取到图像响应")

            except Exception as e:
                print(f"视频流错误: {e}")

        # 关闭所有 OpenCV 窗口
        cv2.destroyAllWindows()
