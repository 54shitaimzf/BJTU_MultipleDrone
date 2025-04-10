from time import sleep

import airsim
import time
import numpy as np
from PySide6.QtCore import QObject, Slot, Signal, QDir
import json

class MultiDrones(QObject):
    origin_x = None       # 无人机初始位置
    origin_y = None
    client = airsim.MultirotorClient()
    nums = 0
    def __init__(self, parent=None):
        super(MultiDrones, self).__init__(parent)
        file_path = QDir.homePath() + "/Documents/AirSim/settings.json"
        with open(file_path, 'r') as f:
            data = json.load(f)
        vehicles = data['Vehicles']
        self.nums = len(vehicles)
        self.origin_x = [0] * self.nums
        self.origin_y = [0] * self.nums
        self.flying = True
        for i in range(len(vehicles)) :
            self.origin_x[i] = vehicles['UAV' + str(i+1)]['X']
            self.origin_y[i] = vehicles['UAV' + str(i+1)]['Y']

    def get_UAV_pos(self, vehicle_name="SimpleFlight"):
        state = self.client.simGetGroundTruthKinematics(vehicle_name=vehicle_name)
        x = state.position.x_val
        y = state.position.y_val
        i = int(vehicle_name[3])
        x += self.origin_x[i - 1]
        y += self.origin_y[i - 1]
        pos = np.array([[x], [y]])
        return pos

    @Slot()
    def run(self):
        # connect to the AirSim simulator
        for i in range(self.nums):
            name = "UAV" + str(i + 1)
            self.client.enableApiControl(True, name)  # 获取控制权
            self.client.armDisarm(True, name)  # 解锁（螺旋桨开始转动）
            if i != self.nums-1:  # 起飞
                self.client.takeoffAsync(vehicle_name=name)
            else:
                self.client.takeoffAsync(vehicle_name=name).join()

        for i in range(self.nums):  # 全部都飞到同一高度层
            name = "UAV" + str(i + 1)
            if i != self.nums-1:
                self.client.moveToZAsync(-3, 1, vehicle_name=name)
            else:
                self.client.moveToZAsync(-3, 1, vehicle_name=name).join()

        # 参数设置
        v_max = 2  # 无人机最大飞行速度
        r_max = 20  # 邻居选择的半径
        k_sep = 7  # 控制算法系数
        k_coh = 1
        k_mig = 1
        pos_mig = np.array([[25], [0]])  # 目标位置
        v_cmd = np.zeros([2, 9])

        for i in range(500):
            for i in range(self.nums):  # 计算每个无人机的速度指令
                name_i = "UAV" + str(i + 1)
                pos_i = self.get_UAV_pos(vehicle_name=name_i)
                r_mig = pos_mig - pos_i
                v_mig = k_mig * r_mig / np.linalg.norm(r_mig)
                v_sep = np.zeros([2, 1])
                v_coh = np.zeros([2, 1])
                N_i = 0
                for j in range(self.nums):
                    if j != i:
                        N_i += 1
                        name_j = "UAV" + str(j + 1)
                        pos_j = self.get_UAV_pos(vehicle_name=name_j)
                        if np.linalg.norm(pos_j - pos_i) < r_max:
                            r_ij = pos_j - pos_i
                            v_sep += -k_sep * r_ij / np.linalg.norm(r_ij)
                            v_coh += k_coh * r_ij
                v_sep = v_sep / N_i
                v_coh = v_coh / N_i
                v_cmd[:, i:i + 1] = v_sep + v_coh + v_mig

            for i in range(self.nums):  # 每个无人机的速度指令执行
                name_i = "UAV" + str(i + 1)
                self.client.moveByVelocityZAsync(v_cmd[0, i], v_cmd[1, i], -3, 0.1, vehicle_name=name_i)

        # 循环结束
        for i in range(self.nums):
            name = "UAV" + str(i + 1)
            self.client.landAsync(vehicle_name=name)
            self.client.enableApiControl(False, vehicle_name=name)  # 释放控制权
















