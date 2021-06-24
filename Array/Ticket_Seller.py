def ticket_profit(k, li):
    sum = 0
    while k != 0:
        for i in range(len(li)):
            max = 0
            if li[i] > max:
                max = li[i]
                print(max)
                a = i
        li[a] = li[a]-1
        print(li)
        sum = sum+max
        k = k-1
    print(sum)


n = int(input())
k = int(input())
li = [int(x) for x in input().split()]
ticket_profit(k, li)
