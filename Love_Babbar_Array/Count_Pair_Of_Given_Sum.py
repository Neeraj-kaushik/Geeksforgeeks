def sum_pair(k, li):
    count = 0
    for i in range(len(li)-1):
        for j in range(i+1, len(li)):
            if li[i]+li[j] == k:
                count += 1
    print(count)


k = int(input())
li = [int(x) for x in input().split()]
sum_pair(k, li)
