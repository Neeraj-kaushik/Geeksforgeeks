def stock_buy_sell(li,n):
    min=10000
    max=-10000
    for i in range(len(li)):
        for j in range(len(li)):
            if li[i]<min:
                min=li[i]
                a=i
            elif li[j]>max:
                max=li[j]
                b=j
    print(a,' ',b)    


n=int(input())
li=[int(x) for x in input().split()]
stock_buy_sell(li,n)