def rotation(li):
    min = 1000
    for i in range(len(li)):
        if li[i] < min:
            min = li[i]
            loc = i

    print("The array is rotated ", loc, "Times")


n = int(input())
li = [int(x) for x in input().split()]
rotation(li)
