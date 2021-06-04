def index_value(li):
    for i in range(len(li)):
        if i+1 == li[i]:
            print(i+1)
            break


n = int(input())
li = [int(x) for x in input().split()]
index_value(li)
