from sqldata import *
from matplotlib import *
from numpy import *
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
def add0_1(y):
    a = array(y)
    z = a + 0.1
    return z

mpl.rcParams['xtick.labelsize'] = 10
mpl.rcParams['ytick.labelsize'] = 10


x1,y1 = getlvl('UserInfo2018')
x2,y2 = getlvl('UserInfo')
y21 = add0_1(y2)
fig = plt.figure('等级与UID的关系散点图')
plt.plot(x2, y21, '.b',label="UserInfo")
plt.plot(x1, y1, '.r',label="UserInfo2018")
plt.legend(loc='upper right', frameon=False)

sex1 = getsex('UserInfo2018')
sex2 = getsex('UserInfo')
fig = plt.figure('性别(除去保密)饼状图',figsize=(6,3))
ax1 = fig.add_subplot(121)
ax1.set_title('UserInfo2018')
ax2 = fig.add_subplot(122)
ax2.set_title('UserInfo')
ax1.pie(sex1,colors = ('#00FFCC','#66ccff'),labels = ('男','女'),autopct = '%3.1f%%')
ax2.pie(sex2,colors = ('#00FFCC','#66ccff'),labels = ('男','女'),autopct = '%3.1f%%')

type1 = getVIPtype('UserInfo2018')
type2 = getVIPtype('UserInfo')
types = array([type1[1],type1[2],type2[1],type2[2]])
types *= 50000
fig1 = plt.figure('VIP用户直方图',figsize=(6,3))
plt.bar(['18年VIP','18年年费VIP','17年冬VIP','17年秋年费VIP'],types)



x1,y1 = getVIPAndLvl('UserInfo2018')
x2,y2 = getVIPAndLvl('UserInfo')
y21 = add0_1(y2)
fig = plt.figure('VIP用户的等级与UID的关系散点图')
plt.plot(x2, y21, '.b',label="UserInfo")
plt.plot(x1, y1, '.r',label="UserInfo2018")
plt.legend(loc='upper right', frameon=False)


plt.show()
