def median(li):

    li = sorted(li)
    if len(li) % 2 != 0:
        x = len(li) // 2+1
        print(li[x-1])
    else:
        x = len(li) // 2
        print((li[x-1]+li[x])//2)


li = [int(x) for x in input().split()]
median(li)
