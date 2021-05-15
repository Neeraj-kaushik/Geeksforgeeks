def smallest_element(li,k):
    for i in range(len(li)-1):
        for j in range(i+1,len(li)):
            if li[i]>li[j]:
                li[i],li[j]=li[j],li[i]
    print(li[k-1])




n=int(input())
li=[int(x) for x in input().split()]
k=int(input())
smallest_element(li,k)