# 先导入 random 模块 import random
# random.randint(a,b),返回[a,b]之间的整数,包含 a 和 b
# 在导入工具包的时候,应该把导入的语句放在文件顶部
# 因为这样可以方便下方的代码,在任何需要的时候,使用工具包中的工具
import random

# 从控制台输入要出的拳--石头(1),剪刀(2),布(3)
player = int(input("请输入你要出的拳-石头(1)/剪刀(2)/布(3)"))

# 电脑随机出拳--先假设电脑只会出剪刀,完成整体代码功能
# 导入了随机数工具包 random 实现电脑随机出拳
computer = random.randint(1, 3)

print("玩家选择的拳头是 %d - 电脑出的拳是 %d" % (player, computer))

# 比较胜负

# 比较胜负
# 1石头胜剪刀
# 2.剪刀胜布
# 3布胜街头

# if (()  #八个空格缩进
#        or ()
#        or ()):
# 用括号使or连接在一起
# 用 and 连接,表示两个条件都要成立
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    # 玩家胜利(空行间距,条理清晰)
    print("欧耶,电脑弱爆了")

# 平局(平局更容易编写)先处理平局情况
elif player == computer:
    print("真是心有灵犀哦,再来一盘!")

# 其他情况就是电脑获胜 else
else:
    print("不服气,决战到天明!")
