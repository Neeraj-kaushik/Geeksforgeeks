def subarray(n,li):
    l=len(li)
    max=0
    sum=0
    for i in range(l):
        sum=li[i]
        for j in range(i+1,l):
            if sum==0:
                print(i,j)
                a=j-i
                if a>max:
                    max=a
            elif sum!=0 and j==l:
                break
            sum=sum+li[j]
    print(max)

n=int(input())
li=[int(x) for x in input().split()]
subarray(n,li)