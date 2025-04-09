from SettingWindow import SettingWindow
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication([])
    window = SettingWindow()
    window.show()
    app.exec()
