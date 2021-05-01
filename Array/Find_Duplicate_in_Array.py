n=int(input())
a=[]
li=[int(x) for x in input().split()]
for i in range(len(li)-1):
    for j in range(i+1,len(li)):
        if i==j:
            a.append(li[i])
x=len(a)
for i in a:
    if x==0:
        print('-1')
    else:
        print(i,end=' ')

