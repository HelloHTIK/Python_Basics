# 参数前面加一个'*'可以储存元组
# 参数前面加两个'*'可以储存字典


def demo(num, *args, **kwargs):

    print(num)
    print(args)
    print(kwargs)


# demo(1)
demo(1, 2, 3, 4, 5, name="小明", age=18)
# demo(1, 2, 3, 4, 5, name="小明", age=18, gender=True)
