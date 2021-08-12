def duplicate(li):
    li1 = []
    for i in li:
        if i not in li1:
            li1.append(i)
        else:
            print(i)


t = int(input())
while t != 0:
    li = [int(x) for x in input().split()]
    duplicate(li)
    t -= 1
