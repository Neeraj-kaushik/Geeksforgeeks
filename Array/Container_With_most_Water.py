def container(li):
    max = 0
    for i in range(len(li)-1):
        for j in range(i+1, len(li)):
            a = j-i
            b = min(li[i], li[j])
            c = a*b
            if max < c:
                max = c
    print(max)


n = int(input())
li = [int(x) for x in input().split()]
container(li)
