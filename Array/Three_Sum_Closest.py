def three_sum_closest(t, li):
    min = 1000
    for i in range(len(li)-2):
        for j in range(i+1, len(li)-1):
            for k in range(len(li)):
                sum = li[i]+li[j]+li[k]
                if sum == t:
                    min = t
                    break
                else:
                    sum = abs(sum)
                    a = abs(sum-t)
                    if a < min:
                        min = a
                        b = sum
    print(b)


n = int(input())
t = int(input())
li = [int(x) for x in input().split()]
three_sum_closest(t, li)
