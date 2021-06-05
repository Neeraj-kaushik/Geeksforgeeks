def convert_array(li):
    
    for i in range(0, len(li)-2, 2):
        if li[i] > li[i+1]:
            li[i], li[i+1] = li[i+1], li[i]
        if li[i+1] < li[i+2]:
            li[i+1], li[i+2] = li[i+2], li[i+1]
    if li[-1]<li[-2]:
        li[-1],li[-2]=li[-2],li[-1]
        

    print(li)


n = int(input())
li = [int(x) for x in input().split()]
convert_array(li)
