def product_pair(x, li):
    a = 0
    for i in range(len(li)-1):

        for j in range(i+1, len(li)):
            product = li[i] * li[j]
            if product == x:
                a = x
    if a == x:
        print('Yes')
    else:
        print('No')


n = int(input())
x = int(input())
li = [int(x) for x in input().split()]
product_pair(x, li)
