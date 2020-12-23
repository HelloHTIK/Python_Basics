# 1. 提示用户输入苹果的单价
price = float(input("苹果的单价："))

# 2. 提示用户输入苹果的重量
weight: float = float(input("苹果的重量："))

# 3. 计算金额
money = price * weight

# 4.格式化字符串
print("苹果的单价是 %.2f" % price)
print("苹果的重量是 %.2f" % weight)
print("苹果总价钱是 %.2f" % money)

print("苹果单价 %.2f 元/斤, 购买了 %.2f 斤, 需要支付 %.2f 元" % (price, weight, money))

scale = 0.25
print("数据比例是 %.2f%%" % (scale * 100))
