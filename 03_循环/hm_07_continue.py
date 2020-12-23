i = 0

while i < 10:

    # 当某个条件满足时,不执行后续重复的代码
    # i == 3

    if i == 3:
        # 注意在循环中使用 continue 这个关键字
        # 在使用关键字之前,需要确认循环的计数是否修改
        # 否则可能会导致死循环
        i += 1

        continue

    print(i)

    i += 1

print("continue循环over")
