from collections import Counter


def majority_element(n, li):
    x = Counter(li)
    a = n//2
    for key, value in x.items():
        if value > a:
            print(key)


n = int(input())
li = [int(x) for x in input().split()]
majority_element(n, li)
