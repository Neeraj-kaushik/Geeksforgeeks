def largest_number_formed(li):
    li1 = []
    for i in range(len(li)):
        a = li[i]
        while a != 0:
            num = a % 10
            li1.append(num)
            a = a//10
    li1 = sorted(li1)
    for i in range(len(li1)-1, -1, -1):
        print(li1[i], end="")


n = int(input())
li = [int(x) for x in input().split()]
largest_number_formed(li)
