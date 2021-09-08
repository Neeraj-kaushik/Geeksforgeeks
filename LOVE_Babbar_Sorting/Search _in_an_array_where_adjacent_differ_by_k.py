def search(li, k, x):
    for i in range(len(li)):
        if li[i] == x:
            print(i)
            break


li = [int(x) for x in input().split()]
k = int(input())
x = int(input())
search(li, k, x)
