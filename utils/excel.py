#coding:utf-8
import os
import xlrd
from paramiko.proxy import subprocess
from xlutils.copy import copy
from utils.template import Template


class ExcelCommon(Template):

    def __init__(self):
        super(ExcelCommon, self).__init__()
        self.wb = xlrd.open_workbook(os.path.abspath('.') + "\\files"+ self.filename)
        #self.wb = xlrd.open_workbook(self.filename)
        self.excel = copy(self.wb)
        self.table = self.get_table()

    def __call__(self, *args, **kwargs):
        self.excel.save(os.path.abspath('.') + "\\files" + self.filename)
        #self.excel.save(self.filename)

    def __str__(self):
        return super(ExcelCommon, self).__str__()

    def write_name(self, row, value):
        self.table.write(row, self.NAME, value)

    def write_pid(self, row, value):
        self.table.write(row, self.PID, value)

    def write_time(self, row, value):
        self.table.write(row, self.TIME, value)

    def write_cpu(self, row, value):
        self.table.write(row, self.CPU, value)

    def write_cpu_total(self, row, value):
        self.table.write(row, self.CPU_TOTAL, value)

    def write_memory(self, row, value):
        self.table.write(row, self.MEMORY, value)

    def write_memory_precent(self, row, value):
        self.table.write(row, self.MOMERTY_PRECENT, value)

    def write_io_read(self, row, value):
        self.table.write(row, self.IO_READ, value)

    def write_io(self, row, value):
        self.table.write(row, self.IO_WRITE, value)

    # 获取有多少张表
    def get_sheets(self):
        return len(self.wb.sheet_names())


    # 获取写入的表(可重新封装)
    def get_table(self):
        write_table = self.excel.get_sheet(0)
        return write_table

    # 获取一共多少条case
    def get_cases_nums(self):
        return self.get_table().nrows

    # 获取列
    def get_cases_col(self):
        return self.get_table().ncols


if __name__ == '__main__':
    pass