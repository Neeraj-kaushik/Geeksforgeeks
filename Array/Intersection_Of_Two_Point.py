def intersection_point(n, m, li, li1):
    count = 0
    for i in range(len(li)):
        if li[i] in li1:
            count = count+1
    print(count)


n = int(input())
m = int(input())
li = [int(x) for x in input().split()]
li1 = [int(x) for x in input().split()]
intersection_point(n, m, li, li1)
