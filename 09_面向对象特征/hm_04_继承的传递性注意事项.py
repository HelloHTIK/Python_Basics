class Animal:

    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


class Dog(Animal):

    # 子类拥有父类的所有属性和方法
    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):

    # 子类的子类同样继承父类
    def fly(self):
        print("我会飞")




class Cat(Animal):

    def catch(self):
        print("抓老鼠")

# 创建一个哮天犬对象
xtq = XiaoTianQuan()

xtq.bark()
xtq.eat()
xtq.drink()
xtq.run()
xtq.fly()


