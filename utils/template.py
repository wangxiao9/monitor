# __author:EstherWang
# time:27/02/2021
import os
import time

import xlwt


class Template:
    NAME = 1
    PID = 2
    TIME = 3
    CPU_TOTAL = 4
    CPU = 5
    MEMORY = 6
    MOMERTY_PRECENT = 7
    IO_READ = 8
    IO_WRITE = 9


    def __init__(self):
        self.filename = "performance" + str(int(time.mktime(time.localtime()))) + ".xls"
        self.workbook = xlwt.Workbook(encoding='utf-8')  # 新建工作簿
        self.sheet1 = self.workbook.add_sheet("performance indicators")  # 新建sheet
        self.touch_template()

    def __str__(self):
        return self.filename

    def touch_template(self):
        self.sheet1.write(0, Template.NAME, "NAME")
        self.sheet1.write(0, Template.PID, "PID")
        self.sheet1.write(0, Template.TIME, "TIME")
        self.sheet1.write(0, Template.CPU_TOTAL, "CPU_TOTAL")
        self.sheet1.write(0, Template.CPU, "CPU")
        self.sheet1.write(0, Template.MEMORY, "MEMORY")
        self.sheet1.write(0, Template.MOMERTY_PRECENT, "MOMERTY_PRECENT")
        self.sheet1.write(0, Template.IO_READ, "IO/READ")
        self.sheet1.write(0, Template.IO_WRITE, "IO/WRITE")
        self.workbook.save(os.path.abspath('.') + "\\files" + self.filename)


if __name__ == '__main__':
    print(os.path.abspath('..'))



