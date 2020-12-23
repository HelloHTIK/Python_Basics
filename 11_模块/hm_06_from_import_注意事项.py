# from hm_01_测试模块1 import say_hello
from hm_02_测试模块2 import say_hello as module2_say_hello
from hm_01_测试模块1 import say_hello

# 如果两个模块，字在同名的函数，那么后导入模块的函数，会覆盖掉先导入的函数

say_hello()
module2_say_hello()
