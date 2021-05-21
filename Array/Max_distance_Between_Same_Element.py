def max_distance(li):
    max=0
    for i in range(len(li)-1):
        for j in range(i+1,len(li)):
            if li[i]==li[j]:
                a=j-i
                if a>max:
                    max=a
    print(max)


n=int(input())
li=[int(x) for x in input().split()]
max_distance(li)