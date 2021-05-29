def upto(sum, li):
    n = 1
    while n != sum:
        if n not in li:
            return n
            break
        n = n+1
    return 0


def not_subset(li):
    for i in range(len(li)-1):
        sum = li[i]
        a = upto(sum, li)
        if a == 0:
            for j in range(i+1, len(li)):
                sum = sum+li[j]
                b = upto(sum, li)
                if b > 0:
                    print(b)
                    break


n = int(input())
li = [int(x) for x in input().split()]
not_subset(li)
