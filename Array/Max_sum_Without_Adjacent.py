def max_sum(li):
    inc = li[0]
    exc = 0
    for i in range(1, len(li)):
        excn = max(inc, exc)
        inc = exc+li[i]
        exc = excn
    print(max(inc, exc))


n = int(input())
li = [int(x) for x in input().split()]
max_sum(li)
