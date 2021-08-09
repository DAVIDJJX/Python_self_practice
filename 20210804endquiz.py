import time
start=time.time()
a=int(input('choose a number:'))
sum=0
for i in range(1,a+1):    
    sum=sum+i
print(sum)
end=time.time()
print('the time com use is',end-start)

import time
start=time.time()
a=int(input('choose a number : '))
print((1+a)*a/2)
end=time.time()
print('the time com use is',end-start)