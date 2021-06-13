def pairs(li, k):
    count = 0
    for i in range(len(li)-1):
        for j in range(i+1, len(li)):
            if li[i]-li[j] == k or li[j]-li[i] == k:
                count += 1
    print(count)


n = int(input())
li = [int(x) for x in input().split()]
k = int(input())
pairs(li, k)
