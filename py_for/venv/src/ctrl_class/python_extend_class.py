# 单继承
# class Animal(object):
#     def __init__(self,age,sex=1,weight=0.0):
#         self.age=age
#         self.sex=sex
#         self.weight=weight
#     def eat(self):
#         self.weight +=0.5
#         print('动物吃........')
# class Dog(Animal):
#     def eat(self):
#         self.weight +=0.9
#         print('狗狗吃.......')
# dog=Dog(2,0,10.0)
# dog.eat()
# print('体重:{0:.2f}'.format(dog.weight))
# 多继承
#先去子类找调用方法 若没有再去父类找 多个父类从左往右依次查找
class ParentClass1:
    def run(self):
        print('ParentClass1 run...............')


class ParentClass2:
    def run(self):
        print("ParentClass2  run....................")


class SubClass1(ParentClass1, ParentClass2):
    pass


class SubClass2(ParentClass2, ParentClass1):
    pass


class SubClass3(ParentClass1, ParentClass2):
    def run(self):
        print("subClass3 run....................")


sub1 = SubClass1()
sub1.run()
sub2 = SubClass2()
sub2.run()
sub3 = SubClass3()
sub3.run()
