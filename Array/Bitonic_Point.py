def max_element(n,li):
    a=n//2
    max=0
    if li[a]>li[a+1]:
        for i in range(0,a+1):
            if li[i]>max:
                max=li[i]
        print(max)
    else:
        for i in range(a+1,len(li)):
            if li[i]>max:
                max=li[i]
        print(max)


n=int(input())
li=[int(x) for x in input().split()]
max_element(n,li)