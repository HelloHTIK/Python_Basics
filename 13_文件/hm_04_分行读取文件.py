# 打开文件
file = open("README")
while True:
    # 读取一行内容
    text = file.readline()

    # 判断是否读取到内容
    if not text:
        break

    # 每读取一行的末尾已经有一个'\n'
    print(text, end="")

# 关闭文件
file.close()
