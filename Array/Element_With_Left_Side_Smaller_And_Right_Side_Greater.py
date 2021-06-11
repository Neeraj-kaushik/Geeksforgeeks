def element_found(li):
    for i in range(1,len(li)-1):
        if li[i]>li[i-1] and li[i]<li[i+1]:
            print(li[i],end=" ")


n=int(input())
li=[int(x) for x in input().split()]
element_found(li)