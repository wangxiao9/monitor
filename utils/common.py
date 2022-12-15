import os
import time


class CommonHelper:
    def __init__(self):
        self.path = os.path.abspath(os.path.dirname(os.getcwd()))
        # self.dirname = time.strftime('%Y-%m-%d', time.localtime(time.time()))


    # 创建文件目录
    def create_dir(self, dirname):
        dir = os.path.join(self.path, dirname)
        if not os.path.exists(dir):
            os.mkdir(dir)
        return dir

    # 创建文件
    def create_file(self, filename, log):
        os.chdir(self.create_dir())
        with open(filename + '.log', 'w') as f:
            f.write(log)

    def run(self):
        dir = os.path.join(self.path, self.dirname)
        print(dir)


if __name__ == '__main__':
    # print(CommonHelper().create_dir())
    CommonHelper().create_file()