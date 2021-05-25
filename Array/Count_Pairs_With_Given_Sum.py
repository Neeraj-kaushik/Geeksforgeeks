def pair_with_given_sum(n, x, li):
    count = 0
    for i in range(len(li)-1):

        for j in range(i+1, len(li)):
            sum = li[i]
            sum = sum+li[j]
            if sum == x:
                count += 1
    print(count)


n = int(input())
x = int(input())
li = [int(x) for x in input().split()]
pair_with_given_sum(n, x, li)
