def smallest_subarray(li, x):
    i, j = 0, 1
    sum = li[0]
    result = 100000
    if sum > x:
        return 1
    if j < len(li):
        sum += li[j]
    while i < len(li) and j < len(li):
        if sum > x:
            result = min(result, j-i+1)
            sum -= li[i]
            i += 1
        else:
            j += 1
            if j < len(li):
                sum += li[j]
    print(result)


li = [int(x) for x in input().split()]
x = int(input())
smallest_subarray(li, x)
