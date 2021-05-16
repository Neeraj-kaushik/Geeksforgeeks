def frequency(li,n):
    i=1
    li1=[]
    while i<=n:
        count=0
        for j in range(len(li)):
            if li[j]==i:
                count=count+1
        li1.append(count)
        i=i+1
    for k in range(len(li1)):
        print(li1[k],end=' ')
            

n=int(input())
li=[int(x) for x in input().split()]
frequency(li,n)