def equilibrium_point(n,li):
    l=len(li)
    sum1=0
    sum2=0
    for i in range(l):
        if l==1:
            print('1')
        elif i==l:
            print('-1')
        else:
            sum1=0
            sum2=0
            for j in range(i):
                sum1=sum1+li[j]
            for k in range(i+1,l):
                sum2=sum2+li[k]
            if sum1==sum2:
                print(i+1)
                break
                
        

n=int(input())
li=[int(x) for x in input().split()]
equilibrium_point(n,li)