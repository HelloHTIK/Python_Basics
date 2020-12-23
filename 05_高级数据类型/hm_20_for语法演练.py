# 完整的for循环

for num in [1, 2, 3]:

    print(num)

    # 使用break退出循环
    if num == 3:
        break
else:
    # 如果循环体内部使用break退出循环
    # else 下方的代码就不会被执行
    print("会执行吗?")

print("循环结束")