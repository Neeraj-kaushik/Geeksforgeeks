def minimum_swaps(li, k):
    f, nf, count = 0, 0, 100000000
    for i in range(len(li)):
        if li[i] <= k:
            f += 1
    for i in range(0, f):
        if li[i] > k:
            nf += 1
    l = 0
    e = f-1
    while e < len(li):
        count = min(count, nf)
        e += 1
        if e < len(li) and li[e] > k:
            nf += 1
        if l < len(li) and li[l] > k:
            nf -= 1
        l += 1
    print(count)


li = [int(x) for x in input().split()]
k = int(input())
minimum_swaps(li, k)
