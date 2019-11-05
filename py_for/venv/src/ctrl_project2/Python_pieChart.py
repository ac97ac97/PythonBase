import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.family']=['SimHei']
# 各种活动标题列标
activites=['工作','睡','吃','玩']
# 各种活动所占时间列表
slices=[8,7,3,6]
# 各种活动在饼状图的颜色
cols=['r','b','y','c']

plt.pie(slices,labels=activites,colors=cols,shadow=True,explode=(0,0.1,0,0),autopct='%.1f%%')

plt.title('绘制饼状图')
# 以分辨率为72来保存图片
plt.savefig('饼状图',dpi=72)
# 显示图形
plt.show()