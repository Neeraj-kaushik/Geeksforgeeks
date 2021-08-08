def array_max_sum(li):
    max = -1000
    sum = 0
    for i in range(len(li)):
        sum = sum+li[i]
        if sum > max:
            max = sum
        if sum < 0:
            sum = 0
    print(max)


t = int(input())
while t != 0:
    li = [int(x) for x in input().split()]
    array_max_sum(li)
    t -= 1
