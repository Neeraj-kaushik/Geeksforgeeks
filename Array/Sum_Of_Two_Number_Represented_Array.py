def sum_of_two_number(li, li1):
    a = li[0]
    for i in range(1, len(li)):
        a = a*10+li[i]
    b = li1[0]
    for i in range(1, len(li1)):
        b = b*10+li1[i]
    c = a+b
    n = c

    li2 = []
    while c != 0:
        num = c % 10
        li2.append(num)
        c = c//10
    li2 = li2[::-1]
    print(li2)


n = int(input())
m = int(input())
li = [int(x) for x in input().split()]
li1 = [int(x) for x in input().split()]
sum_of_two_number(li, li1)
