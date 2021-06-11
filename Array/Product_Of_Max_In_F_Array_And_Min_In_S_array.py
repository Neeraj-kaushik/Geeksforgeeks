def product_of_element(li, li1):
    li = sorted(li)
    li1 = sorted(li1)
    a = li[-1]*li1[0]
    print(a)


li = [int(x) for x in input().split()]
li1 = [int(x) for x in input().split()]
product_of_element(li, li1)
