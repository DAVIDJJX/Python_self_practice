import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import polyfit

x = np.arange(4, 12, 1)
y=x*10
plt.figure('pic')
plt.scatter(x, y)  # 每組x和y之間用逗號隔開就行
b,m=polyfit(x,y,1)
plt.plot(x,b+m*x)
plt.title('michael quiz',fontsize=26)
plt.axis([0,150,0,150])
plt.xlabel('n',fontsize=16)
plt.ylabel('t',fontsize=16)
plt.savefig('picf.jpg')
plt.show()
plt.close()