def count_inversion(li):
    count=0
    for i in range(len(li)-1):
        for j in range(len(li)):
            if li[i]>li[j] and i<j:
                count=count+1
                li[i],li[j]=li[j],li[i]
    print(count)
            

n=int(input())
li=[int(x) for x in input().split()]
count_inversion(li)
