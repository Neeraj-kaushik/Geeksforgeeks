def mountain(start, end, li):
    li1 = []
    for i in range(start, end):
        li1.apppend(li[i])
    li2 = sorted(li1)
    if li1 == li2:
        return True


n = int(input())
li = [int(x) for x in input().split()]
q = int(input())
while q != 0:
    start = int(input())
    end = int(input())
    mountain(start, end, li)
