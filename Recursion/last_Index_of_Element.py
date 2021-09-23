def index(li, x):
    if len(li) == 0:
        return -1
    smallli = index(li[1:], x)
    if smallli == -1:
        if li[0] == x:
            return 0
        else:
            return -1
    else:
        return smallli+1


li = [int(x) for x in input().split()]
x = int(input())
print(index(li, x))
