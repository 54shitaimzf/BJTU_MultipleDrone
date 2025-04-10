from PySide6.QtGui import QSurfaceFormat

from ui.ControlWindow import ControlWindow
from utils.video_thread import video_thread
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    # t = video_thread()
    # t.start()
    app = QApplication([])
    window = ControlWindow()
    window.show()
    app.exec()
