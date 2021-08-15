def sub_sum(li):
    a = set()
    sum = 0
    for i in range(len(li)):
        a.add(sum)
        sum += li[i]
        if sum in a:
            print("Yes")


li = [int(x) for x in input().split()]
sub_sum(li)
