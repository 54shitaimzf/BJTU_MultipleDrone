import threading
import airsim


# AirsimClient单例
class AirsimClient(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        self.client = airsim.MultirotorClient()
        self.client.confirmConnection()

    def __new__(cls, *args, **kwargs):
        if not hasattr(AirsimClient, "_instance"):
            with AirsimClient._instance_lock:
                if not hasattr(AirsimClient, "_instance"):
                    AirsimClient._instance = object.__new__(cls)
        return AirsimClient._instance
