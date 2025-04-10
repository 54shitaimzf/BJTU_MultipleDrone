import json
import math
from PySide6.QtCore import QDir, QThread
from PySide6.QtWidgets import QMainWindow
from ui.Ui_ControlWindow import Ui_ControlWindow
from utils.MultipleDrones import MultiDrones as Md

class ControlWindow(QMainWindow, Ui_ControlWindow):
    controller = None
    thread = None
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.generateSettingButton.clicked.connect(self.gen_btn_clicked)
        self.startFlightButton.clicked.connect(self.ctrl_btn_clicked)
        self.stopFlightButton.clicked.connect(self.stop_btn_clicked)

    def gen_btn_clicked(self):
        output_settings(self.numDroneBox.value(),{})

    def ctrl_btn_clicked(self):
        self.thread = QThread()
        self.controller = Md()
        self.controller.moveToThread(self.thread)
        self.thread.started.connect(self.controller.run)
        self.thread.start()

    def stop_btn_clicked(self):
        temp = 0


def fix_settings(config):
    #文档入口
    config ["SeeDocsAt"] = "https://github.com/Microsoft/AirSim/blob/main/docs/settings.md"
    config ["SettingVersion"] = 1.2
    config ["SimMode"] = "Multirotor"
    config ["ViewMode"] = "FlyWithMe"

def set_up_vehicles(num, config):
    vehicles = {}
    for i in range(num):
        index = "UAV" + str(i + 1)
        if i + 1 == 1 :
            vehicles[index] = {
                "VehicleType": "SimpleFlight",
                "X": 0, "Y": 0, "Z": 0,
                "Yaw": 0
            }
        else :
            angle = 360 / (num - 1) * i
            print(angle)
            vehicles[index] = {
                "VehicleType": "SimpleFlight",
                "X": 3 * math.cos(math.radians(angle)), "Y":3 * math.sin(math.radians(angle)), "Z": 0,
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