def inrotated(li, t):
    for i in range(len(li)):
        if li[i] == t:
            print(i)


li = [int(x) for x in input().split()]
t = int(input())
inrotated(li, t)
