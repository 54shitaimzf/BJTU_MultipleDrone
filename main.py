import  json
import math
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QSpinBox
import airsim
import time
import numpy as np

def fix_settings(config):
    #文档入口
    config ["SeeDocsAt"] = "https://github.com/Microsoft/AirSim/blob/main/docs/settings.md"
    config ["SettingVersion"] = 1.2
    config ["SimMode"] = "Multirotor"
    config ["ViewMode"] = "FlyWithMe"

def set_up_vehicles(num, config):
    vehicles = {}
    for i in range(num):
        index = "UAC" + str(i + 1)
        if i + 1 == 1 :
            vehicles[index] = {
                "VehicleType": "SimpleFlight",
                "X": 0, "Y": 0, "Z": 0,
                "Yaw": 0
            }
        else :
            angle = 360 / num * i
            print(angle)
            vehicles[index] = {
                "VehicleType": "SimpleFlight",
                "X": 3 * math.cos(math.radians(angle)), "Y": math.sin(math.radians(angle)), "Z": 0,
                "Yaw": 0
            }
    config ["Vehicles"] = vehicles


def output_settings(num, config):
    config = {}
    fix_settings(config)
    print(config)
    set_up_vehicles(num, config)
    config = json.dumps(config)
    file = open("settings.json", "w")
    tabs = 0
    for char in config:
        if char == "}":
            file.write("\n")
            for i in range(tabs - 1):
                file.write("\t")
        file.write(char)
        if char == "{":
            tabs += 1
            file.write("\n")
            for i in range(tabs):
                file.write("\t")
        if char == "}":
            tabs -= 1
            file.write("\n")
            for i in range(tabs):
                file.write("\t")
        if char == ",":
            file.write("\n")
            for i in range(tabs):
                file.write("\t")
    file.close()

class SettingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AirSim Settings: ")
        self.resize(400, 300)
        btn = QPushButton(self)
        btn.setText("Generate!")
        btn.setGeometry(QtCore.QRect(50, 200, 300, 50))
        self.number = QSpinBox(self)
        self.number.setMaximum(10)
        self.number.setMinimum(1)
        self.number.setGeometry(QtCore.QRect(100, 100, 200, 50))
        btn.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        output_settings(self.number.value(), {})

if __name__ == "__main__":
    app = QApplication([])
    window = SettingWindow()
    window.show()
    app.exec()
