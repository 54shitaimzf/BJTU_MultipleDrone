import os
import threading
import cv2

from airsim_client.SharedMemory import SharedMemory

class video_thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        SM = SharedMemory()
        while True:
            SM.GetSharedMemoryData()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
