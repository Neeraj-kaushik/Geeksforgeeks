def max_zeros(li):
    max = 0
    for i in range(len(li)):
        a = li[i]
        count = 0
        while a != 0:
            rev = a % 10
            if rev == 0:
                count += 1
            a = a//10

        if count > max:
            max = count

            value = li[i]
    print(value)


n = int(input())
li = [int(x) for x in input().split()]
max_zeros(li)
