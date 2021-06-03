def three_sum_closest(t, li):
    min = 1000
    for i in range(len(li)-2):
        sum = li[i]
        for j in range(i+1, len(li)-1):
            sum = sum+li[j]
            for k in range(j+1, len(li)):
                sum = sum+li[k]
                if sum-t <= min:
                    value = sum
                    min = sum-t
    print(value)


n = int(input())
t = int(input())
li = [int(x) for x in input().split()]
three_sum_closest(t, li)
