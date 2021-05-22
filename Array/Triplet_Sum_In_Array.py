def triplet_sum(li,x):
    for i in range(len(li)-2):
        sum=li[i]
        for j in range(i+1,len(li)-1):
            for k in range(j+1,len(li)):
                if sum+li[j]+li[k]==x:
                    return 1
    return -1



n=int(input())
x=int(input())
li=[int(x) for x in input().split()]
print(triplet_sum(li,x))