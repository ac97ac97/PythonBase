#多态（多个子类共同继承同一个父类）
class Figure():
    def draw(self):
        print('绘制 Figure 。。。')


class Ellipse(Figure):
    def draw(self):
        print('绘制 Ellipse 。。。')


class Triangle(Figure):
    def draw(self):
        print('绘制 Triangle 。。。')


f1 = Figure()
f1.draw()
f2 = Ellipse()
f2.draw()
f3 = Triangle()
f3.draw()
#实例化后参数前者是否为后者类的子类
print(isinstance(f1,Figure))
print(isinstance(f2,Triangle))

#前者是否为后者子类
print(issubclass(Triangle,Figure))
print(issubclass(Triangle,Ellipse))