def sort012(n,li):
    l=len(li)
    for i in range(l-1):
        for j in range(i+1,l):
            if li[i]>li[j]:
                li[i],li[j]=li[j],li[i]
    print(li)
    

n=int(input())
li=[int(x) for x in input().split()]
sort012(n,li)