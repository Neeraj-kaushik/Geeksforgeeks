def product_array_puzzle(li):
    for i in range(len(li)):
        a = 1
        sum = 0
        for j in range(0, i):
            a = a*li[j]
        b = 1
        for k in range(i+1, len(li)):
            b = b*li[k]
        sum = a*b
        print(sum, end=' ')


n = int(input())
li = [int(x) for x in input().split()]
product_array_puzzle(li)
