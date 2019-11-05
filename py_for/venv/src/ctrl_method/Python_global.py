x=20
def print_value():
    global x
    x=10
    print("函数中x = {0}".format(x))
print_value()
print("全局变量{0}".format(x))