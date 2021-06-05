def max_subarray(li):
    i = 0
    max = 0
    a = 0
    b = 0
    while i <= len(li)-1:

        for j in range(i+1, len(li)):
            sum = li[i]
            if li[j] >= 0:
                sum = sum+li[j]
                if sum > max:
                    sum = max
                    a = i-1
                    b = j

            if li[j] < 0:
                i = j+1
        i = i+1
    print(sum)
    print(a, b)


n = int(input())
li = [int(x) for x in input().split()]
max_subarray(li)
