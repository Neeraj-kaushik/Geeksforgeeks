def max_sum(li):
    max = 0
    for i in range(len(li)):
        sum = 0
        for j in range(i, len(li)):
            sum = sum+li[j]
            if max < sum:
                max = sum
        for k in range(0, i):
            sum = sum+li[k]
            if sum > max:
                max = sum
    print(max)


n = int(input())
li = [int(x) for x in input().split()]
max_sum(li)
