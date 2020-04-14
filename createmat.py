import numpy
from matplotlib import pyplot as plt
print('\n\n\n')	
################### 样本数据初始化
#A类数据
xcord_a=[2.2,2.4,1.1]#x轴坐标
ycord_a=[1.4,2.3,3.4]#y轴坐标
#B类数据
xcord_b=[8.3,9.2,10.2,11.2]
ycord_b=[7.3,8.3,11.1,9.3]
#待测试样本
xcord_x=[4.6]
ycord_x=[3.4]
 
#################### 显示数据
fig = plt.figure()
ax = fig.add_subplot(111)
#ax.scatter(xcord,ycord, c=colors, s=markers)
type1 = ax.scatter(xcord_a, ycord_a, s=20, c='red')#s=后面的数值是这个点的大小，c=表示颜色
type2 = ax.scatter(xcord_b, ycord_b, s=20, c='green')
type3 = ax.scatter(xcord_x, ycord_x, s=20, c='blue')
ax.legend([type1, type2, type3], ["A", "B", "x"], loc=2) #loc是从右上角开始数值为1的逆时针4个角的位置，范围1~4
ax.axis([1,12,1,12])#坐标范围，前2个数值是x坐标的范围，后2个是y轴坐标范围
plt.xlabel('x cord')
plt.ylabel('y cord')
plt.show()
 
print('\n\n\n')
#################### 计算待测试对象和样本数据间的差值
#取待测试数据的坐标值
x = xcord_x[0]
y = ycord_x[0]
print('待测试对象坐标x=%f，y=%f'%(x,y))
#计算和A类样本的距离值
dista = []#保存和A类样本的距离值
ind = 0
for xa in xcord_a:
	ya = ycord_a[ind]#取对应y点坐标
	dist = ((x-xa)**2 + (y-ya)**2)**0.5#计算待测试数据与当前样本坐标的距离
	print('A:ind=%d,cord:(%f,%f),dist=%f'%(ind,xa,ya,dist))
	dista.append(dist)
	ind += 1
#计算和B类样本的距离值	
distb = []#保存和B类样本的距离值
ind = 0
for xb in xcord_b:
	yb = ycord_b[ind]#取对应y点坐标
	dist = ((x-xb)**2 + (y-yb)**2)**0.5#计算待测试数据与当前样本坐标的距离
	print('B:ind=%d,cord:(%f,%f),dist=%f'%(ind,xb,yb,dist))
	distb.append(dist)
	ind += 1
	
	
print('\n\n\n')
