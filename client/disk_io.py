# __author:EstherWang
# time:25/02/2021
import psutil

from client.base import BaseMonitor


class IO(BaseMonitor):
    def process(self):
        pid_process = psutil.Process(int(self.__str__()))
        return pid_process

    # 获取当前pid io 读写
    def io(self):
        io = self.process().io_counters().read_count
        return io

    # 内存使用率
    def read(self):
        read = self.process().io_counters().read_count
        return read

    # 得到内存占比
    def write(self):
        write = self.process().io_counters().write_count
        return write

if __name__ == '__main__':
    print(IO().read())