def rearrange(n,li):
    max=n-1
    min=0
    li1=[0]*n
    for i in range(len(li)):
        if i%2==0:
            li1[i]=li[max]
            max=max-1
        else:
            li1[i]=li[min]
            min=min+1
    print(li1)
    


    

n=int(input())
li=[int(x) for x in input().split()]
rearrange(n,li)