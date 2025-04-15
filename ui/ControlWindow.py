import json
import math
from PySide6.QtCore import QDir, QThread, Signal, Slot
from PySide6.QtWidgets import QMainWindow, QMessageBox
from ui.Ui_ControlWindow import Ui_ControlWindow
from utils.MultipleDrones import MultiDrones as Md

class ControlWindow(QMainWindow, Ui_ControlWindow):
    controller = Md()
    thread = QThread()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.generateSettingButton.clicked.connect(self.gen_btn_clicked)
        self.startFlightButton.clicked.connect(self.ctrl_btn_clicked)
        self.stopFlightButton.clicked.connect(self.stop_btn_clicked)
        self.testControlButton.clicked.connect(self.test_connection)

    def gen_btn_clicked(self):
        output_settings(self.typeComboBox.currentIndex(), self.numDroneBox.value(), {})

    def ctrl_btn_clicked(self):
        self.controller.set_target(self.targetXBox.value(), self.targetYBox.value())
        self.controller.moveToThread(self.thread)
        self.thread.started.connect(self.controller.run)
        self.thread.start()
        self.controller.finished.connect(self.ctrl_thread_stopped)

    def stop_btn_clicked(self):
        self.controller.stopping()
        self.controller.finished.disconnect(self.ctrl_thread_stopped)

    @Slot()
    def ctrl_thread_stopped(self):
        self.thread.quit()
        self.thread.deleteLater()

    def closeEvent(self, event):
        self.stop_btn_clicked()
        event.accept()

    def test_connection(self):
        QMessageBox.information(self, "Connection Failed", "TODO")


def fix_settings(config):
    #文档入口
    config ["SeeDocsAt"] = "https://github.com/Microsoft/AirSim/blob/main/docs/settings.md"
    config ["SettingVersion"] = 1.2
    config ["SimMode"] = "Multirotor"
    config ["ViewMode"] = "FlyWithMe"

def set_up_vehicles_circ(num, config):
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

def set_up_vehicles_rect(num, config):
    vehicles = {}
    for i in range(num):
        index = "UAV" + str(i + 1)
        if i + 1 == 1:
            vehicles[index] = {
                "VehicleType": "SimpleFlight",
                "X": 0, "Y": 0, "Z": 0,
                "Yaw": 0
            }
        else:
            temp_length = 5
            vehicles[index] = {
                "VehicleType": "SimpleFlight",
                "X": math.floor((i-1)/4+1) * temp_length if i % 4 == 1 or i % 4 == 3 else -math.floor((i-1)/4+1) * temp_length,
                "Y": math.floor((i-1)/4+1) * temp_length if i % 4 == 1 or i % 4 == 2 else -math.floor((i-1)/4+1) * temp_length,
                "Z": 0,
                "Yaw": 0
            }
    config["Vehicles"] = vehicles

def set_up_vehicles_line(num, config):
    vehicles = {}
    for i in range(num):
        index = "UAV" + str(i + 1)
        if i + 1 == 1:
            vehicles[index] = {
                "VehicleType": "SimpleFlight",
                "X": 0, "Y": 0, "Z": 0,
                "Yaw": 0
            }
        else:
            vehicles[index] = {
                "VehicleType": "SimpleFlight",
                "X": 0, "Y": 3 * math.floor((i+1)/2) if i % 2 == 0 else 3 * -math.floor((i+1)/2), "Z": 0,
                "Yaw": 0
            }
    config["Vehicles"] = vehicles

def output_settings(type, num, config):
    config = {}
    fix_settings(config)
    print(config)
    match type:
        case 0:
            set_up_vehicles_circ(num, config)
        case 1:
            if (num-1) % 4 != 0:
                QMessageBox.critical(None, "错误", "无人机数目非法，应为4n+1")
                return
            set_up_vehicles_rect(num, config)
        case 2:
            set_up_vehicles_line(num, config)
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
    QMessageBox.information(None,"信息", "成功生成配置！")