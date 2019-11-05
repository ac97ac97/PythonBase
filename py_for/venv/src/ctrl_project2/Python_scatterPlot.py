import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams['font.family'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 数据传入
n = 1024
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)

plt.scatter(x, y)

plt.title('绘制散点图')

# 以分辨率为72来保存图片
plt.savefig('散点图', dpi=72)
# 显示图形
plt.show()
