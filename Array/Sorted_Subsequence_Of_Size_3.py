def find_3_number(li):
    count=0
    for i in range(len(li)-2):
        for j in range(len(li)-1):
            for k in range(len(li)):
                if li[i]<li[j]<li[k] and i<j<k:
                    count+=1
    if count!=0:
        print('1')
    else:
        print('0')            




n=int(input())
li=[int(x) for x in input().split()]
find_3_number(li)