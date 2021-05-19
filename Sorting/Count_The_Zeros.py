def count(li):
    count=0
    for i in range(n-1,-1,-1):
        if li[i]==0:
            count=count+1
        else:
            break
    print(count)

n=int(input())
li=[int(x) for x in input().split()]
count(li)