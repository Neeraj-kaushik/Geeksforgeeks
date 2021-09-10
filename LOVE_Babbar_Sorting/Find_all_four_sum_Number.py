def sum_number(n, x, li):
    i = 0
    j = 1
    k = 2
    li1, li2 = [], []
    while i <= len(li)-4:
        for l in range(k+1, len(li)):
            if li[i]+li[j]+li[k]+li[l] == x:
                li1.append(li[i])
                li1.append(li[j])
                li1.append(li[k])
                li1.append(li[l])
                li1 = sorted(li1)
        li2.append(li1)
        i += 1
        j += 1
        k += 1
    print(li2)


n = int(input())
k = int(input())
li = [int(x) for x in input().split()]
sum_number(n, k, li)
