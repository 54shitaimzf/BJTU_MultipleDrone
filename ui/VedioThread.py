import cv2
import numpy as np
from PySide6.QtCore import QThread, Signal, Qt, QSize
from PySide6.QtGui import QImage, QSurfaceFormat
from OpenGL import GL
from PySide6.QtOpenGLWidgets import QOpenGLWidget

from airsim_client.client import AirsimClient


# ==================== 自定义 OpenGL 视频控件 ====================
class OpenGLVideoWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.frame = None
        self.texture_id = None

        # 配置 OpenGL 格式
        fmt = QSurfaceFormat()
        fmt.setSwapInterval(1)  # 启用垂直同步
        self.setFormat(fmt)

    def initializeGL(self):
        GL.glEnable(GL.GL_TEXTURE_2D)
        self.texture_id = GL.glGenTextures(1)
        GL.glBindTexture(GL.GL_TEXTURE_2D, self.texture_id)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_LINEAR)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_LINEAR)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_S, GL.GL_CLAMP_TO_EDGE)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_T, GL.GL_CLAMP_TO_EDGE)

    def paintGL(self):
        print("paintGL")
        if self.frame is not None:
            GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
            GL.glBindTexture(GL.GL_TEXTURE_2D, self.texture_id)

            # 更新纹理数据
            h, w, _ = self.frame.shape
            GL.glTexImage2D(
                GL.GL_TEXTURE_2D, 0, GL.GL_RGB,
                w, h, 0, GL.GL_RGB, GL.GL_UNSIGNED_BYTE,
                self.frame.data
            )

            # 渲染纹理到四边形
            GL.glBegin(GL.GL_QUADS)
            GL.glTexCoord2f(0, 1)
            GL.glVertex2f(-1, -1)
            GL.glTexCoord2f(1, 1)
            GL.glVertex2f(1, -1)
            GL.glTexCoord2f(1, 0)
            GL.glVertex2f(1, 1)
            GL.glTexCoord2f(0, 0)
            GL.glVertex2f(-1, 1)
            GL.glEnd()

    def update_frame(self, frame):
        # 转换颜色空间 BGR→RGB
        self.frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.update()  # 触发重绘


# ==================== 视频获取线程 ====================
class VideoThread(QThread):
    frame_signal = Signal(np.ndarray)

    def __init__(self, drone_num=1):
        super().__init__()
        self.drone_num = drone_num
        self.running = True

    def run(self):
        import airsim
        client = AirsimClient().client
        client.confirmConnection()
        # print("线程运行中")

        while self.running:
            try:
                # print("接受视频帧")
                responses = client.simGetImages([
                    airsim.ImageRequest("1", airsim.ImageType.Scene, False, False)
                ])

                if responses:
                    img_data = responses[0].image_data_uint8
                    if not img_data:
                        # print("图像数据为空")
                        continue

                    img1d = np.frombuffer(img_data, dtype=np.uint8)
                    frame = img1d.reshape(responses[0].height, responses[0].width, 3)

                    if frame is not None:
                        self.frame_signal.emit(frame)

                else:
                    print("未获取到图像响应")


            except Exception as e:
                print(f"视频流错误: {e}")

            self.msleep(20)  # 约50 FPS

    def stop(self):
        self.running = False
        self.wait()
