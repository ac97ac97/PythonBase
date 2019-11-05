import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.family']=['SimHei']
# 数据传入
x=[5,4,2,1]  #x轴坐标数据
y=[7,8,9,10] #y坐标数据

# 绘制线段
plt.plot(x,y,'y',label='线 1',linewidth=2)

plt.title('绘制折线图')  #添加图标标题

# 添加y轴标题
plt.ylabel('Y轴')
# 添加X轴标题
plt.xlabel('X轴')
# 设置图例
plt.legend()

# 以分辨率为72来保存图片
plt.savefig('折线图',dpi=72)
# 显示图形
plt.show()