def max_li(li, ind):
    if ind == len(li)-1:
        return li[ind]
    max1 = max_li(li, ind+1)
    if max1 > li[ind]:
        return max1
    else:
        return li[ind]


li = [int(x) for x in input().split()]
print(max_li(li, 0))
