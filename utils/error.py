# __author:EstherWang
# time:25/02/2021
from utils import Logger
from utils.Logger import Log


class PROCESS_ERROR(Exception):
    def __init__(self, message):
        self.message = message
        Log().error(self.message)


'''
如果找不到进程抛出异常
'''
def rasie_error(error_message=None, error_code=0):
    if error_message is None:
        error_message = "不存在这个进程"

    def decorate(func):
        def wrapper(*args, **kwargs):
            ret = func(*args, **kwargs)
            if ret == error_code:
                raise PROCESS_ERROR(error_message)
            else:
                return ret
        return wrapper

    return decorate
