def bubble_sort(n,li):
    l=len(li)
    for i in range(l-1):
            if li[i]>li[i+1]:
                li[i],li[i+1]=li[i+1],li[i]
    print(li)


n=int(input())
li=[int(x) for x in input().split()]
bubble_sort(n,li)