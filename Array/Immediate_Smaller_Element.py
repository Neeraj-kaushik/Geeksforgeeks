def smaller(li):
    for i in range(len(li)-1):
        if li[i] > li[i+1]:
            li[i] = li[i+1]
        elif li[i] < li[i+1]:
            li[i] = -1
    li[-1] = -1
    print(li)


n = int(input())
li = [int(x) for x in input().split()]
smaller(li)
