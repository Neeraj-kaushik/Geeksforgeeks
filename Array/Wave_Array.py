def wave_array(n,li):
    for i in range(len(li)):
        if i%2!=0:
            if li[i]>li[i-1]:
                li[i],li[i-1]=li[i-1],li[i]
            elif li[i]>li[i+1]:
                li[i],li[i+1]=li[i+1],li[i]
        elif i==0:
            if li[i]<li[i+1]:
                li[i],li[i+1]=li[i+1],li[i]
        elif i==len(li):
            if li[i]<li[i-1]:
                li[i],li[i-1]=li[i-1],li[i]
    print(li)


n=int(input())
li=[int(x) for x in input().split()]
wave_array(n,li)