def sum_number(num):

    print(num)
    # 递归的出口:当参数满足某个条件时,不再执行函数
    # 没有递归出口会出现死循环
    if num == 1:
        return

    # 递归函数:函数内部自己调用自己
    sum_number(num - 1)


sum_number(5)
