n=int(input())
li=[int(x) for x in input().split()]
if n==1:
    print('0')
if li[0]>=li[1]:
    print('0')
if li[n-1]>= li[n-2]:
    print(n-1)
for i in range(1,n-1):
    if (li[i-1]<=li[i]) and (li[i+1]<=li[i]):
        print(i)