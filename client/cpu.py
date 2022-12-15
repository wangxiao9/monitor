# __author:EstherWang
# time:25/02/2021
import psutil

from config import config
from client.base import BaseMonitor


class CPUStatus(BaseMonitor):


    def process(self):
        pid_process = psutil.Process(int(self.__str__()))
        return pid_process

    """
    当前系统几核
    """
    def cpu_count(self):
        return psutil.cpu_count()


    """
    当前系统，cpu占用率
    """
    def cpu_total(self):
        cpu_total_precent = psutil.cpu_percent(interval=config.IN)
        return format(cpu_total_precent, '.1f') + '%'


    """
    当前pid 占内存比例
    """
    def process_cpu_precent(self):
        cpu_precent = self.process().cpu_percent(interval=config.IN) / self.cpu_count()
        return format(cpu_precent, '.1f') + '%'


if __name__ == '__main__':
    print(psutil.cpu_times())

