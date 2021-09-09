def pairs(l, n, li):
    count = 0
    x = set()
    for i in range(len(li)):
        if li[i] in x:
            print("True")
        else:
            x.add(li[i]-n)
            x.add(n+li[i])
        print(x)


l = int(input())
n = int(input())
li = [int(x) for x in input().split()]
pairs(l, n, li)
