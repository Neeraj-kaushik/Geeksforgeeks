def max_product(li):
    max=0
    for i in range(len(li)-1):
        product=li[i]
        for j in range(i+1,len(li)):
            product=product*li[j]
            if product>max:
                max=product
    print(max)




n=int(input())
li=[int(x) for x in input().split()]
max_product(li)