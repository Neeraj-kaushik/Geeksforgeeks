def min_distance(li, x, y):
    min = 10000
    if x not in li or y not in li:
        print(-1)
    else:
        for i in range(len(li)):
            for j in range(i+1, len(li)):
                if li[i] == x and li[j] == y:
                    a = j-i
                    if a < min:
                        min = a
        print(min)


n = int(input())
li = [int(x) for x in input().split()]
x = int(input())
y = int(input())
min_distance(li, x, y)
