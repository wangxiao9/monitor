# __author:EstherWang
# time:25/02/2021
import psutil

from client.base import BaseMonitor


class MomeryStatus(BaseMonitor):
    def process(self):
        pid_process = psutil.Process(int(self.__str__()))
        return pid_process

    # 获取当前pid使用的内存单位MB
    def used_momery(self):
        # total = psutil.virtual_memory()
        rss = self.process().memory_info().rss
        return format(float(rss / 1024 / 1024), '.1f') + 'MB'

    # 内存使用率
    def total_precent(self):
        return psutil.virtual_memory().percent

    # 得到内存占比
    def process_precent(self):
        precent = self.process().memory_percent()
        return format(precent, '.1f') + '%'

if __name__ == '__main__':
    print(MomeryStatus().used_momery())