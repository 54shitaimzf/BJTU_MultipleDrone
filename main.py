from PySide6.QtGui import QSurfaceFormat

from ui.ControlWindow import ControlWindow
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication([])

    # 设置 OpenGL 格式
    fmt = QSurfaceFormat()
    fmt.setVersion(3, 3)
    fmt.setProfile(QSurfaceFormat.CoreProfile)
    QSurfaceFormat.setDefaultFormat(fmt)

    window = ControlWindow()
    window.show()
    app.exec()
