import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.family']=['SimHei']
# 数据传入
x1=[1,3,5,7,9]  #x轴坐标数据
y1=[5,2,7,8,2] #y坐标数据
x2=[2,4,6,8,10]  #x轴坐标数据
y2=[8,6,2,5,6] #y坐标数据

# 绘制线段
plt.bar(x1,y1,label='柱状图1')
plt.bar(x2,y2,label='柱状图2')

plt.title('绘制柱状图')  #添加图标标题

# 添加y轴标题
plt.ylabel('Y轴')
# 添加X轴标题
plt.xlabel('X轴')
# 设置图例
plt.legend()

# 以分辨率为72来保存图片
plt.savefig('柱状图',dpi=72)
# 显示图形
plt.show()