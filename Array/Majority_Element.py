def majority_element(n,li):
    max=0
    l=len(li)
    for i in range(l-1):
        count=0
        for j in range(l):
            if li[i]==li[j]:
                count+=1
            if count>=max:
                max=count
                a=li[i]
    if max>l//2:
        print(a)
    else:
        print('-1')

n=int(input())
li=[int(x) for x in input().split()]
majority_element(n,li)