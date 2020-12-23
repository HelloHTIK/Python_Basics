# 查找和替换

# 检查字符串是否以指定字符串开头
startswith_str = "Hello Python"
print(startswith_str)
print(startswith_str.startswith("Hello"))

# 检查字符串是否以指定字符串结束
endswith_str = "Hello Python"
print(endswith_str)
print(endswith_str.endswith("on"))

# 检测str是否包含在string中，如果返回开始的索引值，否则返回-1
# 如果start和end指定范围，则检查是否包含在范围内
# index方法同样可以查找指定的字符串在大字符串中的索引
find_str = "Hello Python"
print(find_str)
print(find_str.find("llo"))

# 类似于find（）函数，顺序从右到左
rfind_str = "Hello Python"
print(rfind_str)
print(rfind_str.rfind("ool"))

# 类似于find（）函数，如果str不在string会报错
index_str = "Hello Python"
print(index_str)
print(index_str.index("llo"))

# 类似于index（）方法，从右到左
rindex_str = "Hello Python"
print(rindex_str)
print(rindex_str.rindex("llo"))

# 把string中的 old_str 替换成 new_str， 如果num指定，则替换不超过num次
# replace 方法执行完成之后，会返回一个新的字符串
# 注意： 不会修改原有字符串的内容
replace_str = "Hello Python"
print(replace_str)
print(replace_str.replace("Python", "Work"))
print(replace_str)
