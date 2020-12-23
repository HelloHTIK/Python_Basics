name_list = ["张三", "李四", "王五", "王二小"]

# 使用迭代遍历列表(迭代iteration遍历)
# 迭代遍历就是重复遍历
"""
# 顺序的从列表中依次获取数据, 每一次循环过程中, 数据都会保存在my_name 这个变量中
# 在循环体内部可以访问到当前这一次获取到的数据 
# 使用 for 可以实现迭代遍历

for my_name in 列表变量:

    print("我的名字叫 %s " % my_name)
"""

for my_name in name_list:

    print("我的名字叫 %s " % my_name)
