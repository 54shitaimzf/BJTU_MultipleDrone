import cv2

from airsim_client.SharedMemory import SharedMemory

SM = SharedMemory()

while True:
    SM.GetSharedMemoryData()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break