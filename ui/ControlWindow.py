import json
import math
from PySide6 import QtCore
from PySide6.QtCore import QDir
from PySide6.QtWidgets import QMainWindow, QPushButton, QSpinBox

from ui.Ui_ControlWindow import Ui_ControlWindow

class ControlWindow(QMainWindow, Ui_ControlWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.generateSettingButton.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        output_settings(self.numDroneBox.value(), {})

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
    file_path = QDir.homePath() + "/Documents/AirSim/settings.json"
    file = open(file_path, "w")
    file.truncate()
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