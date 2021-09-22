def index(li, x):
    if len(li) == 0:
        return -1
    if li[0] == x:
        return 0
    smalla = index(li[1:], x)
    if smalla == -1:
        return-1
    else:
        return smalla+1


li = [int(x) for x in input().split()]
x = int(input())
print(index(li, x))
