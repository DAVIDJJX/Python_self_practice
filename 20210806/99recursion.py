def func(a,b):
    c=int(a)*int(b)
    print(a,'*',b,'=',c)
    if a==1 and b==1:
        c==1
        retun c
    elif a!=1 and b==1:
        print(end='/n')
        func(a-1,b)
    else:
        func(a,b-1)
    
func(9,9)


