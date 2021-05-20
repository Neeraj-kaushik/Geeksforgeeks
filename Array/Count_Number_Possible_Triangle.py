def no_of_triangle(n,li):
    count=0
    li=sorted(li)
    for i in range(0,n-2):
        k=i+2
        for j in range(i+1,n):
            while k<n and li[i]+li[j]>li[k]:
                k=k+1
            if k>j:
                count=count+k-j-1

    
    print(count)


n=int(input())
li=[int(x) for x in input().split()]
no_of_triangle(n,li)