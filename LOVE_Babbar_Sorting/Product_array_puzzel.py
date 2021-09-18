def product_array(li):
    n = len(li)
    l, r = [1]*n, [1]*n
    for i in range(1, n):
        l[i] = l[i-1]*li[i-1]
    print(l)
    for i in range(n-2, -1, -1):
        r[i] = r[i+1]*li[i+1]
    print(r)
    for i in range(len(li)):
        li[i] = l[i]*r[i]
    print(li)


li = [int(x) for x in input().split()]
product_array(li)
