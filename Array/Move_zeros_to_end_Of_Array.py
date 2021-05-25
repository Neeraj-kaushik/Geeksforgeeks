def zero_to_end(li):
    li1 = []
    a = 0
    for i in range(len(li)):
        if li[i] == 0:
            a = a+1
        else:
            li1.append(li[i])
    for i in range(a):
        li1.append(0)
    print(li1)


n = int(input())
li = [int(x) for x in input().split()]
zero_to_end(li)
