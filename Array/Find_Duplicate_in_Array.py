n=int(input())
a=[]
li=[int(x) for x in input().split()]
for i in range(len(li)-1):
    for j in range(i+1,len(li)):
        if li[i]==li[j]:
            print(li[i],end=' ')


