def min_jumps(li):
    steps, max1, curr_pos = 0, 0, 0
    if li[0] == 0:
        return -1
    for i in range(len(li)):
        max1 = max(max1, i+li[i])
        if max1 >= len(li):
            steps += 1
            print('jump of max')
            return steps
        if i == curr_pos:
            curr_pos = max
            steps += 1
            print('jump of halt')
    if curr_pos >= len(li):
        return steps
    return -1


t = int(input())
while t != 0:
    li = [int(x) for x in input().split()]
    print(min_jumps(li))
    t -= 1
