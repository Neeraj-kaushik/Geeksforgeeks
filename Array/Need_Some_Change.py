def changes(li):
    k=2
    while k<=len(li):
        for i in range(len(li)-2):

            li[i],li[i+2]=li[i+2],li[i]
            k=k+2
    print(li)


n=int(input())
li=[int(x) for x in input().split()]
changes(li)