def buy_sell_stock(li):
    max_profit = 0
    min_val = li[0]
    if len(li) <= 0:
        return 0
    for i in range(1, len(li)):
        if li[i] < min_val:
            min_val = li[i]
        else:
            if li[i]-min_val > max_profit:
                max_profit = li[i]-min_val
    return max_profit


li = [int(x) for x in input().split()]
val = buy_sell_stock(li)
print(val)
