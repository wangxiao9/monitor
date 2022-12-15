# __author:EstherWang
# time:25/02/2021
import psutil


from config import config
from utils.error import PROCESS_ERROR


class BaseMonitor:
    def __init__(self):
        self.pid = config.PID

    def __str__(self):
        p = int(self.pid)
        if psutil.pid_exists(p):
            return str(p)
        raise PROCESS_ERROR("pid does not exist")