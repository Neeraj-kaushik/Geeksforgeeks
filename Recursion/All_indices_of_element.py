def index(li, x, ind, fsf):
    if ind == len(li):
        return [0]*fsf

    if li[ind] == x:
        li1 = index(li, x, ind+1, fsf+1)
        li1[fsf] = ind
        return li1
    else:
        li1 = index(li, x, ind+1, fsf)
        return li1


li = [int(x) for x in input().split()]
x = int(input())
print(index(li, x, 0, 0))
