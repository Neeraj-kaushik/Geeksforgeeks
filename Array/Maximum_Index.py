def max_index(li):
    max=0
    for i in range(len(li)-1):
        a=0
        for j in range(len(li)):
            if li[i]<=li[j]:
                a=j-i
        if max<a:
            max=a
    print(max)    

n=int(input())
li=[int(x) for x in input().split()]
max_index(li)