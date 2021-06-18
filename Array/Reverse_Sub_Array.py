def reverse_subarray(li, l, r):
    li1 = []
    for i in range(len(li)):
        if i >= l-1 and i <= r-1:
            li1.append(li[i])
    li1 = li1[::-1]
    li2 = []
    for i in range(0, l-1):
        li2.append(li[i])
    for i in range(len(li1)):
        li2.append(li1[i])
    for i in range(r, len(li)):
        li2.append(li[i])
    print(li2)


n = int(input())
li = [int(x) for x in input().split()]
l = int(input())
r = int(input())
reverse_subarray(li, l, r)
