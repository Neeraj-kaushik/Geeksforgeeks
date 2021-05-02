n=int(input())
k=int(input())
li=[int(x) for x in input().split()]
for i in range(len(li)):
    if li[i]-k<=0:
        li[i]=li[i]+k
    else:
        li[i]=li[i]-k
# to find min and max i am using direct function of python
a=min(li)
b=max(li)
c=b-a
print(c)