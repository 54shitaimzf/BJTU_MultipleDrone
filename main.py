from ui.ControlWindow import ControlWindow
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication([])
    window = ControlWindow()
    window.show()
    app.exec()
