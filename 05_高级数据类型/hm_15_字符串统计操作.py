hello_str = "Hello Python"

# 1. 统计字符串长度
print(len(hello_str))

# 2. 统计某一个小 (子) 字符串出现的次数
print(hello_str.count("o"))
print(hello_str.count("llo"))

# 3. 某一个子字符串出现的位置
print(hello_str.index("llo"))
print(hello_str.index("o"))

# 注意: 如果使用index 方法传递底子字符串不存在, 程序会报错
# print(hello_str.index("abc"))
