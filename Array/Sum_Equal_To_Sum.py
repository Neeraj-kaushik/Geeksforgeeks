def sum_equal_sum(li):
    li1 = []
    a = 0
    for i in range(len(li)-1):
        for j in range(i+1, len(li)):
            val = li[i]+li[j]
            if val in li1:
                a = 1
                break
            li1.append(val)
    if a == 1:
        print("1")
    else:
        print("0")


n = int(input())
li = [int(x) for x in input().split()]
sum_equal_sum(li)
