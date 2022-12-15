import time

import psutil

from config import config
from client.cpu import CPUStatus
from client.disk_io import IO
from client.momery import MomeryStatus
from utils.excel import ExcelCommon


class Run:
    i = 1

    def __init__(self):
        super(Run, self).__init__()
        self.cpu = CPUStatus()
        self.memory = MomeryStatus()
        self.io = IO()
        self.e = ExcelCommon()

    def cpu_precent(self):
        precent = self.cpu.process_cpu_precent()
        return precent

    def cpu_total(self):
        return self.cpu.cpu_total()

    def memory_used(self):
        return self.memory.used_momery()

    def memory_precent(self):
        return self.memory.process_precent()

    def io_read(self):
        return self.io.read()

    def io_write(self):
        return self.io.write()

    def current_time(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def main(self):
        # while (Run.i < 10):
        print("-----------------------Start Monitor------------------------")
        while True:
            self.e.write_pid(Run.i, config.PID)
            self.e.write_time(Run.i, self.current_time())
            self.e.write_cpu(Run.i, self.cpu_precent())
            self.e.write_cpu_total(Run.i, self.cpu_total())
            self.e.write_memory(Run.i, self.memory_used())
            self.e.write_memory_precent(Run.i, self.memory_precent())
            self.e.write_io_read(Run.i, self.io_read())
            self.e.write_io(Run.i, self.io_write())
            self.e()
            time.sleep(1)
            Run.i = Run.i + 1
            print("recoder:" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


if __name__ == '__main__':
    r = Run()
    r.main()