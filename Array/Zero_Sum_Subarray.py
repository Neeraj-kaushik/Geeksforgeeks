def zero_sum(li):
    count = 0
    for i in range(len(li)):
        sum = li[i]
        if sum == 0:
            count += 1
        for j in range(i+1, len(li)):
            sum = sum+li[j]
            if sum == 0:
                count += 1
    print(count)


n = int(input())
li = [int(x) for x in input().split()]
zero_sum(li)
