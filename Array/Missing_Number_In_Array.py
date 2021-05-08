def missing_number(n,li):
    if n==len(li):
        print('-1')
    elif li[-1]!=n:
        print(n)
    for i in range(len(li)-1):
        if li[i]-li[i+1]!= -1:
            print(li[i]+1)



n=int(input())
li=[int(x) for x in input().split()]
missing_number(n,li)