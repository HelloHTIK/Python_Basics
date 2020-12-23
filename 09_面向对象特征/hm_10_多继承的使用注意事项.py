class A:

    def test(self):
        print("A --- test 方法")

    def demo(self):
        print("A --- demo 方法")


class B:

    def test(self):
        print("B --- test 方法")

    def demo(self):
        print("B --- demo 方法")


# 避免出现 父类之间 存在 同名方法或属性
class C(A, B):
    """
    多继承可以让子类对象,同时具有多个父类的属性和方法
    """
    pass


# 创建子类对象
c = C()

c.test()
c.demo()

# 确定 C类对象调用方法的顺序
# Python中的 MRO -- 方法搜索顺序
# 针对 类 提供一个内置属性
print(C.__mro__)


