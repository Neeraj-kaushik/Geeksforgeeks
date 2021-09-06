from collections import Counter


def find_number(n, li):
    dis = Counter(li)
    res = []
    for i in range(1, n+1):
        if i not in dis:
            res.insert(1, i)
        if dis[i] > 1:
            res.insert(0, i)
    print(res)


n = int(input())
li = [int(x) for x in input().split()]
find_number(n, li)
