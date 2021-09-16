def count_triplet(n, x, li):
    i, count = 0, 0
    j = i+1
    while i <= len(li)-3:
        for k in range(j+1, len(li)):
            if li[i]+li[j]+li[k] < x:
                count += 1
        i += 1
        j += 1
    print(count)


n = int(input())
x = int(input())
li = [int(x) for x in input().split()]
count_triplet(n, x, li)
