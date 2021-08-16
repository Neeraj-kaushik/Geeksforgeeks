def max_product(li):
    max1, min1, res = li[0], li[0], li[0]
    for i in range(1, len(li)):
        if li[i] == 0:
            max1 = 1
            min1 = 1
        temp = li[i]*max1
        temp1 = li[i]*min1
        max1 = max(temp1, temp)
        max1 = max(max1, li[i])
        min1 = min(temp1, temp)
        min1 = min(min1, li[i])
        res = max(max1, min1, res)
    print(res)


li = [int(x) for x in input().split()]
max_product(li)
