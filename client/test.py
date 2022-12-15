# __author:EstherWang
# time:27/02/2021


def a_new_decorator(func):
    def wrapTheFunction():
        print("111")
        func()
        print("2222")
    return wrapTheFunction


@a_new_decorator
def func2():
    print("333")

func2()