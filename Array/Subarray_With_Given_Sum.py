n=int(input())
s=int(input())
sum=0
li=[int(x) for x in input().split()]
b=len(li)
for i in range(b):
    sum=li[i]
    for j in range(i+1,b):
        if sum==s:
            print(i,' ',j)
        elif sum>s and j==b:
            break
        sum=sum+li[j]

                        