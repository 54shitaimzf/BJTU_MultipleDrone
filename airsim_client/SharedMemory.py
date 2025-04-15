import ctypes
from ctypes import wintypes
import cv2
import numpy as np
import time
import threading

# 常量
INVALID_HANDLE_VALUE = ctypes.c_void_p(-1).value
PAGE_READWRITE = 0x04
FILE_MAP_READ = 0x0004
WAIT_OBJECT_0 = 0x00000000
WAIT_TIMEOUT = 0x00000102
INFINITE = 0xFFFFFFFF
MUTEX_WAIT_TIME_MS = 5000


# 加载 kernel32.dll
kernel32 = ctypes.windll.kernel32

# 定义所需 WinAPI 函数
OpenFileMapping = kernel32.OpenFileMappingW
OpenFileMapping.restype = wintypes.HANDLE
OpenFileMapping.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.LPCWSTR]

MapViewOfFile = kernel32.MapViewOfFile
MapViewOfFile.restype = ctypes.c_void_p
MapViewOfFile.argtypes = [wintypes.HANDLE, wintypes.DWORD, wintypes.DWORD, wintypes.DWORD, ctypes.c_size_t]

UnmapViewOfFile = kernel32.UnmapViewOfFile
UnmapViewOfFile.restype = wintypes.BOOL
UnmapViewOfFile.argtypes = [ctypes.c_void_p]

CloseHandle = kernel32.CloseHandle
CloseHandle.restype = wintypes.BOOL
CloseHandle.argtypes = [wintypes.HANDLE]

OpenMutex = kernel32.OpenMutexW
OpenMutex.restype = wintypes.HANDLE
OpenMutex.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.LPCWSTR]

WaitForSingleObject = kernel32.WaitForSingleObject
WaitForSingleObject.restype = wintypes.DWORD
WaitForSingleObject.argtypes = [wintypes.HANDLE, wintypes.DWORD]

ReleaseMutex = kernel32.ReleaseMutex
ReleaseMutex.restype = wintypes.BOOL
ReleaseMutex.argtypes = [wintypes.HANDLE]

class SharedMemory(object):
    _instance_lock = threading.Lock()

    def __init__(self, DroneName: str="UAV1", imageSizeWidth: int=1280, imageSizeHeight: int=720):
        self.SHARED_MEMORY_NAME = DroneName
        self.MUTEX_NAME=DroneName+"Mutex"
        self.image_width = imageSizeWidth
        self.image_height = imageSizeHeight
        self.SHARED_MEMORY_SIZE = imageSizeWidth * imageSizeHeight * 4
        self.image_array = np.zeros((self.image_height, self.image_width, 4), dtype=np.uint8)
        # 打开互斥量（必须与 C++ 端互斥量名一致）
        self.hMutex = OpenMutex(0x00100000 | 0x0001, False, self.MUTEX_NAME)  # SYNCHRONIZE | MUTEX_MODIFY_STATE
        if not self.hMutex:
            raise RuntimeError("无法打开互斥锁")
        # 打开共享内存
        self.hMapFile = OpenFileMapping(FILE_MAP_READ, False, self.SHARED_MEMORY_NAME)
        if not self.hMapFile:
            CloseHandle(self.hMutex)
            raise RuntimeError("无法打开共享内存")
        # 映射视图
        self.pBuf = MapViewOfFile(self.hMapFile, FILE_MAP_READ, 0, 0, self.SHARED_MEMORY_SIZE)
        if not self.pBuf:
            CloseHandle(self.hMapFile)
            CloseHandle(self.hMutex)
            raise RuntimeError("无法映射共享内存")

    def GetSharedMemoryData(self):
        result = WaitForSingleObject(self.hMutex, MUTEX_WAIT_TIME_MS)
        if result == WAIT_OBJECT_0:
            try:
                # 读取共享内存数据
                ctypes.memmove(self.image_array.ctypes.data, self.pBuf, self.SHARED_MEMORY_SIZE)

                image_bgr = cv2.cvtColor(self.image_array, cv2.COLOR_BGRA2BGR)

                # return image_bgr

                cv2.imshow('AirSim Video', image_bgr)

                #
                # cv2.imshow('AirSim Video', image_bgr)
                # 提高亮度，这里将亮度增加 50，可根据需要调整该值
                # brightness_increase = 50
                # image_bgr = np.clip(image_bgr.astype(np.int32) + brightness_increase, 0, 255).astype(np.uint8)

                # cv2.imshow('AirSim Video', image_bgr)
                # cv2.imshow('AirSim Video', image_bgr)
            finally:
                ReleaseMutex(self.hMutex)  # 必须释放
        elif result == WAIT_TIMEOUT:
            print("等待共享内存超时...")
            time.sleep(0.01)
            return
        else:
            print("等待互斥量失败！")
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

    def __del__(self):
        UnmapViewOfFile(self.pBuf)
        CloseHandle(self.hMapFile)
        CloseHandle(self.hMutex)










