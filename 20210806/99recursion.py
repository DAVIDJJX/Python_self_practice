## 99乘法表
def func(a:int,b:int):
    c=int(a)*int(b)
    print(a,'*',b,'=',c)
    if a==1 and b==1:
        return c
    elif a!=1 and b==1:
        print(end='\n')
        func(a-1,9)
    else:
        func(a,b-1)
        
func(9,9)


