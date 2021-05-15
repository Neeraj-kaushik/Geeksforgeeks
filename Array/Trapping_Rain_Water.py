def rain_water(li,n):
    max=0
    for i in range(len(li)):
        if li[i]>max:
            max=li[i]
        

n=int(input())
li=[int(x) for x in input().split()]
rain_water(li,n)