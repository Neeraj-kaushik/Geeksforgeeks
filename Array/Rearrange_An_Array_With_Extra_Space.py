def rearrange(li):
    li1=[]
    for i in range(len(li)):
        a=li[li[i]]
        print(a,end=' ')

n=int(input())
li=[int(x) for x in input().split()]
rearrange(li)