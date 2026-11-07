import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
fig,ax=plt.subplots()
x=[1,2,3,4,5,6,7,8,9,10]
y1=[2,4,1,5,3,7,5,8,7,9]
y2=[2,1,2,3,4,2,3,5,6,9]
ax.plot(x,y1,color="pink",marker="*",label="游惑")
ax.plot(x,y2,color="blue",marker="*",label="秦究")
ax.set_title("喜爱值")
ax.set_xlabel("时间")
ax.set_ylabel("数值")
ax.legend()
plt.show()
