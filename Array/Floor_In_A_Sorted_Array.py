def find_floor(x,li):
    a=-1
    for i in range(len(li)):
        if li[i]>x:
            a=i-1
            break
    if a==-1:
        print(-1)
    else:
        print(a)
    



n=int(input())
x=int(input())
li=[int(x) for x in input().split()]
find_floor(x,li)