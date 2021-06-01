def key_pair(x, li):
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            sum = li[i]
            sum = sum+li[j]
            if sum == x:
                return('Yes')
    return('No')


n = int(input())
x = int(input())
li = [int(x) for x in input().split()]
value = key_pair(x, li)
print(value)
