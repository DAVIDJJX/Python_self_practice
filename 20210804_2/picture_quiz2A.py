import matplotlib.pyplot as plt
import numpy as np
## 1

xpt=[1,3,5,9]
ypt=[1,3,5,9]
plt.scatter(xpt,ypt)
plt.title("michael's quiz",fontsize=26)
plt.xlabel('n',fontsize=16)
plt.ylabel('t',fontsize=16)
plt.savefig('pic3.jpg')
plt.show()