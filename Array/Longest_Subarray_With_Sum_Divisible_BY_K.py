def maximum_subarray(li, k):
    max = 0
    for i in range(len(li)-1):
        sum = li[i]
        for j in range(i+1, len(li)):
            sum = sum+li[j]

            if sum % k == 0:
                a = j-i+1

                if a > max:
                    max = a
    print(max)


li = [int(x) for x in input().split()]
k = int(input())
maximum_subarray(li, k)
