def maximum_product(li):
    li = sorted(li)
    product = li[-1]*li[-2]
    print(product)


n = int(input())
li = [int(x) for x in input().split()]
maximum_product(li)
