def element(n, k, li):
    x = n//k
    li = sorted(li)
    li1 = []
    i, k, count = 0, 1, 1
    while i <= len(li) and k <= len(li)-1:
        if li[k]-li[i] == 0:
            count += 1
            if count > x:
                li1.append(li[i])
            k += 1
            i += 1
        else:
            i += 1
            k += 1
            count = 1
    if len(li1) == 0:
        print('0')
    else:
        print(li1)


n = int(input())
k = int(input())
li = [int(x) for x in input().split()]
element(n, k, li)
