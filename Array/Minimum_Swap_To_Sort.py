def min_swaps(li):
    li1=sorted(li)
    count=0
    i=j=0
    while (i<=len(li)-1) and (j<=len(li1)-1):
        if li[i]!=li1[j]:
            count+=1
            i+=1
            j+=1
        else:
            i+=1
            j+=1
    x=count//2
    print(x)

    

li=[int(x) for x in input().split()]
min_swaps(li)