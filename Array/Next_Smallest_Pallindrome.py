def next_pallindrome(li):
    if len(li) % 2 != 0:
        a = (len(li)//2)+1
    else:
        a = len(li)//2
    li1 = []
    for i in range(0, a):
        li1.append(li[i])
    li1[-1] = li1[-1]+1
    if li1[-1] > 9:
        li1[-1] = 0
        li1[-2] = li1[-2]+1
    li2 = li1[::-1]
    print(li1, end=" ")
    print(li2, end=" ")


n = int(input())
li = [int(x) for x in input().split()]
next_pallindrome(li)
