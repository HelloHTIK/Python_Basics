# 注意: 再开发时,应该吧模块中索要的全局变量
# 定义再所有函数上方,就可以保证所有的函数
# 就能够正常的访问到每一个全局变量
num = 10
# 再定义一个全局变量
title = "Python程序员"

# 再定义一个全局变量
name = "小明"


def demo():

    print("%d" % num)
    print("%s" % title)
    print("%s" % name)


# 再定义一个全局变量
# title = "Python程序员"

# 再定义一个全局变量
# name = "小明"


demo()
