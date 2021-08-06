def move_neg(li):
    start = 0
    for i in range(len(li)):
        if li[i] < 0:
            temp = li[i]
            li[i] = li[start]
            li[start] = temp
            start += 1
    print(li)


t = int(input())
while t != 0:
    li = [int(x) for x in input().split()]
    move_neg(li)
    t -= 1
