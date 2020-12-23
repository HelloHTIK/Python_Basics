# 定义布尔型变量 has_ticket 表示是否有车票
has_ticket = True

# 定义整型变量 knife_length 表示刀的长度,CM
knife_length = 20

# 首先检查是否有车票,如果有才允许进行安检
if has_ticket:
    print("车票检查通过,准备开始安检")

# 安检时,需要检查大的长度,p判断是否超过20CM

    # 如果超过20CM,提示刀的长度,不允许上车
    if knife_length > 20:
        print("你携带的刀长度有 %d 公分长,不能上车" % knife_length)

    # 如果不超过20CM,安检通过
    else:
        print("安检通过,允许上车")
        print("祝你旅途愉快!")

# 如果没有车票,不允许进门
else:
    print("你没有车票,不能进门!")
