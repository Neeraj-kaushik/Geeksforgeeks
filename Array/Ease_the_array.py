def ease_array(li):
    li1 = []
    for i in range(len(li)-1):
        if li[i] == li[i+1] and li[i+1] != 0 and li[i] != 0:
            li[i] = li[i]*2
            li[i+1] = 0
    a = 0
    for i in li:
        if i == 0:
            a += 1
        else:
            li1.append(i)

    for i in range(a):
        li1.append(0)
    print(li1)


li = [int(x) for x in input().split()]
ease_array(li)
