import numpy as np
import matplotlib.pyplot as plt
def fit(fit_x,fit_y,fit_num = 7):#fit_num表示自由度为7进行拟合数据
    fit_x = np.array(fit_x)
    fit_y = np.array(fit_y)
    f1 = np.polyfit(fit_x, fit_y, fit_num)
    p1 = np.poly1d(f1)#p1为生成的拟合多项式
    print(p1)
    return p1
#NELL
x=[0.7,0.71,0.73,0.75,0.8,0.85,0.9,1,1.05,1.1,1.15,1.2,1.25,1.3]
y=[0.66770,0.66357,0.65428,0.65428,0.62436,0.58101,0.53354,0.45820,0.36945,0.36017,0.36429,0.36326,0.26832,0.17141]

#Cora
# x=[0.7,0.75,0.8,0.85,0.9,0.95,1,1.05,1.1,1.15,1.2,1.25,1.3]
# y=[0.782,0.795,0.808,0.813,0.812,0.811,0.811,0.814,0.820,0.817,0.813,0.811,0.811]

#Citeseer
# x=[0.7,0.75,0.8,0.85,0.9,0.95,1,1.05,1.1,1.15,1.2,1.25,1.3]
# y=[0.718,0.718,0.727,0.731,0.723,0.724,0.717,0.715,0.713,0.709,0.707,0.709,0.705]

#Pubmed
# x=[0.7,0.75,0.8,0.85,0.9,0.95,1,1.05,1.1,1.15,1.2,1.25,1.3]
# y=[0.769,0.776,0.776,0.780,0.785,0.789,0.790,0.793,0.800,0.794,0.789,0.787,0.785]

figure, ax = plt.subplots()
fit(x,y)
fitx = []
iu = 0.7
while iu <= 1.3:
    iu += 0.01
    fitx.append(iu)
font1 = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 15
}
plt.title(r"$G=(μ-L)^2$",fontdict={'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 15})

plt.ylim(0.100,0.750)
plt.xlabel('μ',fontdict={'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 20})
plt.ylabel('accuracy',fontdict={'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 23})
plt.plot(x,y,label='NELL')
plt.vlines(1, 0.100, 0.750, colors = "gray", linestyles="dashed")
plt.legend(prop=font1)     #添加图例
plt.tick_params(labelsize=15)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
plt.savefig('NELL.png', dpi=600)
plt.rcParams['figure.dpi']=600
plt.show()

