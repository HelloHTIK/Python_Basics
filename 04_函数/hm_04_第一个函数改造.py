name = "小明"
# python 解释器知道下方定义了一个函数
# 函数上下要保留两行空行


def say_hello():
    """函数的注释要加在函数里面"""
    """打招呼"""
    '''你好'''
    print("Hello 1")
    print("Hello 2")
    print("Hello 3")


print(name)

# 只有在程序中主动调用函数,才会让函数执行
say_hello()

print(name)
