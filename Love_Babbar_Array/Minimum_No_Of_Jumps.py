def min_jumps(li):
    steps, max1, curr_pos = 0, 0, 0
    if li[0] == 0:
        return -1
    for i in range(len(li)-1):
        max1 = max(max1, i+li[i])
        if max1 >= len(li)-1:
            steps += 1
            return steps
        if i == curr_pos:
            curr_pos = max1
            steps += 1
    if curr_pos >= len(li)-1:
        return steps
    return -1


t = int(input())
while t != 0:
    li = [int(x) for x in input().split()]
    print(min_jumps(li))
    t -= 1
