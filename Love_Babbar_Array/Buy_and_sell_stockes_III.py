def buy_sell(li, n):
    lmin = li[0]
    rmax = li[n-1]
    larr, rarr = [0]*n, [0]*n
    # left array
    for i in range(1, len(li)):
        larr[i] = max(larr[i-1], li[i]-lmin)
        lmin = min(lmin, li[i])
    # right array
    i = n-2
    while i >= 0:
        rarr[i] = max(rmax-li[i], rarr[i+1])
        rmax = max(rmax, li[i])
        i -= 1
    profit = rarr[0]
    for j in range(1, n):
        profit = max(profit, rarr[j]+larr[j-1])
    print(profit)


n = int(input())
li = [int(x) for x in input().split()]
buy_sell(li, n)
