import logging
import os
import time

from utils.common import CommonHelper

'''
根据创建的log，进入对应的log的写入log
'''
class Log:
    def __init__(self):
        self.com = CommonHelper()
        # log日志命令
        # self.logname = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + '.log'
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')

    def create_log_dir(self):
        path = self.com.create_dir('logs')
        os.chdir(path)
        self.logname = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + '.log'
        return self.logname

    def __console(self, level, message):
        # 添加到文件里
        fileHandler = logging.FileHandler(self.create_log_dir(), 'a', encoding='utf-8')
        fileHandler.setLevel(logging.DEBUG)
        fileHandler.setFormatter(self.formatter)

        # 输出控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        # 写入文件
        self.logger.addHandler(fileHandler)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
            # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fileHandler)
        # 关闭打开的文件
        fileHandler.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)


if __name__ == '__main__':
    for i in range(0, 10):
        Log().info(i)