# 假设： 一下内容是从网络上抓取的
# 要求： 顺序并且居中对齐输出一下内容
poem = ["\t\n登鹳雀楼",
        "王之涣",
        "白日依山尽\t\n",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]


# 居中对齐
for poem_str in poem:

    # 先使用strip方法去除字符串中的空白字符
    # 再使用 center 方法使文本居中对齐
    print("|%s|" % poem_str.strip().center(20, "　"))

# # 向左对齐
# for poem_str in poem:
#
#     # 先使用strip方法去除字符串中的空白字符
#     # 再使用 ljust 方法使文本居中对齐
#     print("|%s|" % poem_str.ljust(20, "　"))
#
# # 向右对齐
# for poem_str in poem:
#
#     # 先使用strip方法去除字符串中的空白字符
#     # 再使用 rjust 方法使文本居中对齐
#     print("|%s|" % poem_str.rjust(20, "　"))
