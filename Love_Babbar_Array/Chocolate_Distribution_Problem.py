def chocolate(li, m):
    i = 0
    li = sorted(li)
    min1 = 100000
    while i+m-1 < len(li):
        min1 = min(min1, li[i+m-1]-li[i])
        i += 1
    print(min1)


li = [int(x) for x in input().split()]
m = int(input())
chocolate(li, m)
