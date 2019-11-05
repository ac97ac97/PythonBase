#相同方法或性质的归结到1类 鸭子类型
class Animal:
    def run(self):
        print('动物跑--------')


class Dog(Animal):
    def run(self):
        print('狗跑----------')


class Car:
    def run(self):
        print('汽车跑---------')


def go(animal):
    animal.run()


go(Animal())
go(Dog())
go(Car())
