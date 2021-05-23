def stickler_thief(li):
    a = li[0]
    b = 0
    for i in range(1, len(li)):
        c = max(a, b)
        a = b+li[i]
        b = c
    print(max(a, b))


n = int(input())
li = [int(x) for x in input().split()]
stickler_thief(li)
