def kadane_algorithm(li,n):
    max=-10000
    for i in range(len(li)-1):
        sum=li[i]
        for j in range(i+1,len(li)):
            sum=sum+li[j]
            if sum>max:
                max=sum
    print(max)


n=int(input())
li=[int(x) for x in input().split()]
kadane_algorithm(li,n)