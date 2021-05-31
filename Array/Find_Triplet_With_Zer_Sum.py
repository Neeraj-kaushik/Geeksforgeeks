def find_triplet(li, n):
    count = 0
    for i in range(len(li)-2):
        for j in range(i+1, len(li)-1):
            for k in range(j+1, len(li)):
                if li[i]+li[j]+li[k] == 0:
                    count += 1

    print(count)


n = int(input())
li = [int(x) for x in input().split()]
find_triplet(li, n)
