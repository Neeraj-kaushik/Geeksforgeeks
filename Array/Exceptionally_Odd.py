def odd(li):
    for i in range(len(li)-1):
        count = 1
        for j in range(i+1, len(li)):
            if li[i] == li[j]:
                count += 1
        if count % 2 != 0:
            print(li[i])
            break


n = int(input())
li = [int(x) for x in input().split()]
odd(li)
