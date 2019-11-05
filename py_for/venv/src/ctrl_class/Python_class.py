# class Animal(object):
#     """定义动物类"""
#
#     def __init__(self, age, sex, weight):
#         self.sex = sex
#         self.age = age
#         self.weight = weight
#
#
# animal = Animal(12, 1, 66)
#
# print('年龄：{0}'.format(animal.age))
# print('性别:{0}'.format('雌性' if animal.sex == 0 else '雄性'))
# print('体重 ：{0}'.format(animal.weight))


# class Account(object):
#     """定义银行账户"""
#     lilv=0.618
#     def __init__(self,owner,amount):
#         self.owner=owner
#         self.amount=amount
# account=Account('Jerry',1000000) #实例化对象
# print('用户:{0}'.format(account.owner))
# print('余额：{0}'.format(account.amount))
# print('利率:{0}'.format(Account.lilv))
# #print('利率:{0}'.format(account.lilv)) 也能正常运行出结果但是不符合规则
# #类里面的构造函数里面的形参可看做一个字典 有键值 和 值 可通过字典添加方式来增添属性
# print('account的所有实例变量{0}'.format(account.__dict__))
# account.lilv1=0.7777
# account.lilv2=0.2222
# print('account的所有实例变量{0}'.format(account.__dict__))

# 实例方法
# 在定义变量时候若加上_例如:self.weight变成 self._weight 则该变量变为私有变量只可以在在类内所属作用域内访问 超出访问出错
# 在定义类内方法时 若在方法名字前加上_例如run() 变成_run() 则该方法变成 私有方法 只可以在类内进行访问 在类外进行访问则会报错
# class Animal(object):
#     """定义动物类"""
#
#     # 实例方法
#     def __init__(self, age, sex, weight):
#         self.sex = sex
#         self.age = age
#         self.weight = weight
#     def run(self):
#         self.weight += 0.05
#         print('run----------')
#     def eat(self):
#         self.weight += 0.1
#         print('eat---------')
#
#
# animal = Animal(12, 1, 66)
#
# print('体重 ：{0:.2f}'.format(animal.weight))
# animal.eat()
# print('体重 ：{0:.2f}'.format(animal.weight))
# animal.run()
# print('体重 ：{0:.2f}'.format(animal.weight))

# 类方法
# class Account(object):
#     """定义银行账户"""
#     lilv = 0.618
#
#     def __init__(self, owner, amount):
#         self.owner = owner
#         self.amount = amount
#
#     # 类方法
#     @classmethod
#     def lilv_by(cls, amt):
#         return cls.lilv * amt
#
#
# lilvsum = Account.lilv_by(12_000.0)
# print('计算利率: {0:.4f}'.format(lilvsum))

# 类方法
# class Account(object):
#     """定义银行账户"""
#     lilv = 0.618
#
#     def __init__(self, owner, amount):
#         self.owner = owner
#         self.amount = amount
#
#     # 类方法
#     @classmethod
#     def lilv_by(cls, amt):
#         return cls.lilv * amt
#
#     #静态方法
#     @staticmethod
#     def lilv_with(amt):
#         return Account.lilv_by(amt)
#
# lilvsum1 = Account.lilv_by(12_000.0)
# print('计算利率: {0:.4f}'.format(lilvsum1))
#
# lilvsum2 = Account.lilv_with(12_000.0)
# print('计算利率: {0:.4f}'.format(lilvsum2))

# 定义属性 setter和getter方法
# 1 手动写入 属性的setter和getter方法
# class Animal(object):
#     """定义动物类"""
#
#     # 实例方法
#     def __init__(self, age, sex=1, weight=0.0):
#         self.sex = sex
#         self.age = age
#         self._weight = weight
#
#     def set_weight(self,weight):  #设置属性的setter方法
#         self._weight=weight
#
#     def get_weight(self):        #设置属性的getter方法
#         return self._weight
#
#
# a1 = Animal(2, 0, 10.0)
# print('a1的体重:{0:.2f}'.format(a1.get_weight()))  #调用a1实例化animal的getter方法
#
# a2 = a1.set_weight(111.0)                         #调用a1实例化animal的setter方法
# print('a2的体重:{0:.2f}'.format(a1.get_weight()))  #调用a1实例化animal的getter方法

# 2 通过访问器
class Animal(object):
    """定义动物类"""

    # 实例方法
    def __init__(self, age, sex=1, weight=0.0):
        self.sex = sex
        self.age = age
        self._weight = weight

    @property
    def weight(self):  # 替代get_weight
        return self._weight

    @weight.setter
    def weight(self, weight):  # 替代 set_weight(self,weight)
        self._weight = weight


a1 = Animal(2, 0, 10.0)
print('a1的体重:{0:.2f}'.format(a1.weight))  # 调用a1实例化animal的getter方法

a1.weight = 111.99  # 调用a1实例化animal的setter方法
print('a2的体重:{0:.2f}'.format(a1.weight))  # 调用a1实例化animal的getter方法
