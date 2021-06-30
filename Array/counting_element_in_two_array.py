def counting_element(li, li1):
    li3 = []
    for i in range(len(li)):
        count = 0
        for j in range(len(li1)):
            if li[i] >= li1[j]:
                count = count+1
        li3.append(count)
    print(li3)


n = int(input())
m = int(input())
li = [int(x) for x in input().split()]
li1 = [int(x) for x in input().split()]
counting_element(li, li1)
