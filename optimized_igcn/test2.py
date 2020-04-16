import numpy as np
from matplotlib import pyplot as plt
plt.style.use('ggplot')#使用‘ggplot风格美化图表’
x = np.linspace(0,1.5,50)
y1=(1-x)
y2= (1-x)**2
y3=(1-x)**3
y4=(1-x)**4
y5=(1.1-x)**2
plt.figure(1)
plt.xlabel("λ̃̃")
plt.ylabel("p(λ̃)")
plt.xlim(0,2)
plt.ylim(-1, 1)
plt.title(r"$p(λ ̃)=(μ-λ ̃)^2$")

#plt.plot(x,y1,label='k=1')
plt.plot(x,y2,label='μ=1')
plt.plot(x,y5,label='μ=1.1')
#plt.plot(x,y3,label='k=3')
#plt.plot(x,y4,label='k=4')
plt.legend()
plt.savefig('function.png', dpi=1200)
plt.rcParams['figure.dpi']=1200
plt.show()