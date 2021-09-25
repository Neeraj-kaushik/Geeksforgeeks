def parray(li):
    if len(li) == 0:
        return
    print(li[0], end=" ")
    return parray(li[1:])


li = [int(x) for x in input().split()]
parray(li)
