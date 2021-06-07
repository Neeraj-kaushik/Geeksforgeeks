def smallest_subarray(li, x):
    a = 1000

    for i in range(len(li)-1):
        sum = li[i]
        li1 = []
        li1.append(li[i])
        for j in range(i+1, len(li)):
            sum = sum+li[j]
            li1.append(li[j])

            if sum > x:

                if a > len(li1):
                    b = len(li1)
                    a = len(li1)

    print(b)


li = [int(x) for x in input().split()]
x = int(input())
smallest_subarray(li, x)
