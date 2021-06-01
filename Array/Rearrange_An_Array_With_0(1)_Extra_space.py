def rearrange_array(li):
    li1 = []
    for i in range(len(li)):
        a = li[li[i]]
        li1.append(a)
    print(li1)


n = int(input())
li = [int(x) for x in input().split()]
rearrange_array(li)
