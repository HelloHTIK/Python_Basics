def demo01():
    return int(input("输入整数： "))


def demo02():
    return demo01()


# 李勇异常的传递性，在主程序捕获异常
try:
    print(demo02())
except Exception as result:
    print("未知错误 %s" % result)
