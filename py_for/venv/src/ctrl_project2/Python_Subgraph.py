import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams['font.family'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def drowsubbar():
    # 数据传入
    x1 = [1, 3, 5, 7, 9]  # x轴坐标数据
    y1 = [5, 2, 7, 8, 2]  # y坐标数据
    x2 = [2, 4, 6, 8, 10]  # x轴坐标数据
    y2 = [8, 6, 2, 5, 6]  # y坐标数据

    # 绘制线段
    plt.bar(x1, y1, label='柱状图1')
    plt.bar(x2, y2, label='柱状图2')
    plt.title('绘制柱状图')  # 添加图标标题


def drawsubpie():
    activites = ['工作', '睡', '吃', '玩']
    # 各种活动所占时间列表
    slices = [8, 7, 3, 6]
    # 各种活动在饼状图的颜色
    cols = ['r', 'b', 'y', 'c']

    plt.pie(slices, labels=activites, colors=cols, shadow=True, explode=(0, 0.1, 0, 0), autopct='%.1f%%')

    plt.title('绘制饼状图')


def drawsubline():
    # 数据传入
    x = [5, 4, 2, 1]  # x轴坐标数据
    y = [7, 8, 9, 10]  # y坐标数据

    # 绘制线段
    plt.plot(x, y, 'y', label='线 1', linewidth=2)

    plt.title('绘制折线图')  # 添加图标标题

    # 添加y轴标题
    plt.ylabel('Y轴')
    # 添加X轴标题
    plt.xlabel('X轴')
    # 设置图例
    plt.legend()


def drawsubscatter():
    # 设置中文字体
    plt.rcParams['font.family'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    # 数据传入
    n = 1024
    x = np.random.normal(0, 1, n)
    y = np.random.normal(0, 1, n)

    plt.scatter(x, y)

    plt.title('绘制散点图')


plt.subplot(2, 2, 1)
drowsubbar()
plt.subplot(2, 2, 2)
drawsubpie()
plt.subplot(2, 2, 3)
drawsubline()
plt.subplot(2, 2, 4)
drawsubscatter()
# 调整布局
plt.tight_layout()
# 以分辨率为72来保存图片
plt.savefig('子图表', dpi=72)
plt.show()
