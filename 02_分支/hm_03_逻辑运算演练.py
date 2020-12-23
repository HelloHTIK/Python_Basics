# 定义一个整形变量age
age = 10

# 要求年龄在0-120岁之间
"""
0 <= age <= 120
and 并且连接
age >= 0 and age <= 120
"""

if 0 <= age <= 120:
    print("年龄正确")
else:
    print("年龄不正确")